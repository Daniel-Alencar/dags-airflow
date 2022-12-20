import util
from MongoDBWeb import MongoDBWeb

from settings import number_of_computers, verbose
from settings import vehicles_to_search_path

vehicles_to_search = util.read_json(vehicles_to_search_path)
length = len(vehicles_to_search)

bd = MongoDBWeb(
  vehicles_to_search_length=length,
  number_of_computers=number_of_computers
)
bd.delete_all()
bd.add_indexes()

if verbose:
  bd.print_all()