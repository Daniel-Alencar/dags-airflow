from MongoDBWeb import MongoDBWeb
from settings import verbose, number_of_computers, computer_id

bd = MongoDBWeb()

for id in range(number_of_computers):
  indices_de_busca = bd.get_indexes(id)

  if verbose:
    print(indices_de_busca)
