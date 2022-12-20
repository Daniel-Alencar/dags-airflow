from MongoDBWeb import MongoDBWeb
from settings import verbose

bd = MongoDBWeb()

if verbose:
  bd.print_all()