from MongoDBWeb import MongoDBWeb

bd = MongoDBWeb()
bd.update_indexes(0,0,0)
indices = bd.get_indexes()

print(indices)