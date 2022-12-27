import pandas
import util

from pymongo import MongoClient
from settings import structure_columns, verbose

class MongoDBWeb:
  def __init__(self, vehicles_to_search_length=[], number_of_computers=0):
    self.password = "20deAbril%5Cn"
    self.user = "Gking"
    self.cluster = "ic-cluster"
    self.codigo = "lcpuy5t"
    
    self.client = MongoClient(
      f"mongodb+srv://{self.user}:{self.password}@{self.cluster}.{self.codigo}.mongodb.net"
    )
    self.database = self.client["veiculos"]
    self.collection = self.database["carros"]

    self.vehicles_to_search_length = vehicles_to_search_length
    self.number_of_computers = number_of_computers

  def add_indexes(self):
    indices = []
    number_of_indexes = int(self.vehicles_to_search_length / self.number_of_computers)

    for computer_id in range(self.number_of_computers):
      indices.append({
        "id": computer_id,
        "marca": computer_id * number_of_indexes,
        "modelo_base": 0,
        "modelo_especifico": 0
      })
    
    self.collection.insert_many(indices)
    
  def update_indexes(self, computer_id, indices_de_busca):
    self.collection.update_one(
      { "id": computer_id },
      { '$set': indices_de_busca }
    )

  def get_indexes(self, computer_id):
    value = self.collection.find_one({"id": computer_id})
    value.pop('_id')
    return value
    
  def persistent(self, jsonObject_list):
    self.collection.update_one(
      { "site": "Fipe" },
      { 
        "$push": { 
          "vehicles": {
            "$each": jsonObject_list
          }
        }
      },
      upsert=True
    )

  def print_all(self):
    documents_list = self.collection.find({})
    for document in documents_list:
      document.pop('_id')
      if verbose:
        util.print_formatted_json(document)

  def delete_all(self):
    self.collection.delete_many({})
      
  def generate_csv(self):
    value = self.collection.find_one({"site": "Fipe"})
    value.pop('_id')
    value.pop('site')

    structure = pandas.DataFrame(columns = structure_columns)
    
    for vehicle in value['vehicles']:
      data = [vehicle['marca'], vehicle['modelo']]
      for year in vehicle['anos_modelo'].keys():
        data.append(year)
        for month in vehicle['anos_modelo'][year]:
          price = list(month.values())
          data.append(price[0])

        new = pandas.DataFrame([data], columns = structure_columns)
        structure = pandas.concat([structure, new])

        structure.fillna(value = "NULL", axis = 1, inplace = True)
        del data[2 : ]
    
    structure.to_csv("data.csv", index = False, header = True)