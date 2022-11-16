from pymongo import MongoClient
import json

class MongoDBWeb:
  def __init__(self):
    self.password = "20deAbril%5Cn"
    self.user = "Gking"
    self.cluster = "ic-cluster"
    self.codigo = "lcpuy5t"
    
    self.client = MongoClient(
      f"mongodb+srv://{self.user}:{self.password}@{self.cluster}.{self.codigo}.mongodb.net"
    )
    self.database = self.client["veiculos"]
    self.collection = self.database["carros"]

  def add_indexes(self):
    self.collection.insert_one(
      {
        "id": 1,
        "marca": 0,
        "modelo_base": 0,
        "modelo_especifico": 0
      }
    )
    
  def update_indexes(self, marca, modelo_base, modelo_especifico):
    self.collection.update_one({"id": 1}, {'$set': {
          "marca": marca,
          "modelo_base": modelo_base,
          "modelo_especifico": modelo_especifico
        }
      }
    )

  def get_indexes(self):
    value = self.collection.find_one({"id": 1})
    value.pop('_id')
    return value
    
  def persistent(self, filePath):
    with open(filePath) as file:
      fileData = json.load(file)
    self.collection.insert_one(fileData)

