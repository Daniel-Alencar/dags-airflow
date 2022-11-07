import json

def read_json(path):
  with open(path) as jsonFile:
    json_object = json.load(jsonFile)
  return json_object

def print_formatted_json(jsonObject):
  print(json.dumps(jsonObject, indent=2))





def check_indexes(vehicles_to_search, indices_de_busca):
  try:
    print(
      vehicles_to_search
        [indices_de_busca["marca"]]["modelos_base"]
        [indices_de_busca["modelo_base"]]
        [indices_de_busca["modelo_especifico"]]
    )
  except:
    return False
  return True

def update_indexes(vehicles_to_search, indices_de_busca):
  indices_de_busca["modelo_especifico"] += 1
  indexes_OK = check_indexes(vehicles_to_search, indices_de_busca)

  if indexes_OK == False:
    indices_de_busca["modelo_base"] += 1
    indices_de_busca["modelo_especifico"] = 0
    indexes_OK = check_indexes(vehicles_to_search, indices_de_busca)

    if indexes_OK == False:
      indices_de_busca["marca"] += 1
      indices_de_busca["modelo_base"] = 0
      indices_de_busca["modelo_especifico"] = 0
      indexes_OK = check_indexes(vehicles_to_search, indices_de_busca)

      if indexes_OK == False:
        indices_de_busca["marca"] = None
        indices_de_busca["modelo_base"] = None
        indices_de_busca["modelo_especifico"] = None

  print(indices_de_busca)
  with open("json/indices_de_busca.json", "w") as jsonFile:
    json.dump(indices_de_busca, jsonFile)
  return indexes_OK
