import json

def read_json(path):
  with open(path) as jsonFile:
    json_object = json.load(jsonFile)
  return json_object

def print_formatted_json(jsonObject):
  print(json.dumps(jsonObject, indent=2))

def clear_json(jsonPath):
  with open(jsonPath, "w") as jsonFile:
    json.dump([], jsonFile)
