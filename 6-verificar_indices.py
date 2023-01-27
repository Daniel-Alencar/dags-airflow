import util

from MongoDBWeb import MongoDBWeb
from settings import verbose, number_of_computers, vehicles_to_search_path

vehicles_to_search = util.read_json(vehicles_to_search_path)

bd = MongoDBWeb()

for id in range(number_of_computers):
  indices_de_busca = bd.get_indexes(id)

  if verbose:
    print(indices_de_busca)
    if indices_de_busca["modelo_especifico"] != None:
      print(
        vehicles_to_search
          [indices_de_busca["marca"]]["modelos_base"]
          [indices_de_busca["modelo_base"]]
          [indices_de_busca["modelo_especifico"]]
      )
    print("")

