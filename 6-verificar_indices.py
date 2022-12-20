from MongoDBWeb import MongoDBWeb
from settings import computer_id, verbose

bd = MongoDBWeb()
indices_de_busca = bd.get_indexes(computer_id)

if verbose:
  print(indices_de_busca)