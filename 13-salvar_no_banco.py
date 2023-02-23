import util
from MongoDBWeb import MongoDBWeb

bd = MongoDBWeb()

completos = util.read_json("json/vehicles_with_price.json")
bd.persistent(completos)