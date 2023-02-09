import util
from MongoDBWeb import MongoDBWeb

bd = MongoDBWeb()

completos = util.read_json("json/completos.json")
bd.persistent(completos)