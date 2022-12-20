import util
from settings import vehicles_to_search_path

anos = [ 2015, 2022 ]

vehicles_to_search = util.read_json(f"json/vehicles_to_search_{anos[0]}.json")
vehicles_to_search_2022 = util.read_json(f"json/vehicles_to_search_{anos[1]}.json")

for vehicle_2022 in vehicles_to_search_2022:
  occurances = vehicles_to_search.count(vehicle_2022)
  if occurances == 0:
    vehicles_to_search.append(vehicle_2022)

util.update_json(vehicles_to_search_path, vehicles_to_search)
print("Redundância retirada!")

# Contagem da quantidade de modelos para busca
modelos_base_count = 0
for vehicle in vehicles_to_search:
  for modelo_base in vehicle["modelos_base"]:
      modelos_base_count += len(modelo_base)

print(f"Teremos a busca de {modelos_base_count} modelos diferentes!")