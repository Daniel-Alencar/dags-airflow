import util
from MongoDBWeb import MongoDBWeb

from settings import number_of_computers, verbose
from settings import incomplete_to_search_path

vehicles_to_search = util.read_json(incomplete_to_search_path)
length = len(vehicles_to_search)

bd = MongoDBWeb(
  vehicles_to_search_length=length,
  number_of_computers=number_of_computers
)
bd.add_indexes()
