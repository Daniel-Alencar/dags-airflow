from MongoDBWeb import MongoDBWeb
from settings import computer_id, verbose

bd = MongoDBWeb()

indices_de_busca = {
  'marca': 0, 
  'modelo_base': 0, 
  'modelo_especifico': 0
}
bd.update_indexes(computer_id, indices_de_busca)

indices_de_busca = bd.get_indexes(computer_id)
if verbose:
  print(indices_de_busca)