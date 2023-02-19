import util
from settings import vehicles_to_search_path, vehicles_only_from_year_path

anos = [ 2016, 2022 ]

vehicles_to_search0 = util.read_json(f"json/vehicles_to_search_{anos[0]}.json")
vehicles_to_search1 = util.read_json(f"json/vehicles_to_search_{anos[1]}.json")

union_vehicles = vehicles_to_search0.copy()
subtraction_vehicles = vehicles_to_search0.copy()

for vehicle1 in vehicles_to_search1:
  occurances = vehicles_to_search0.count(vehicle1)
  if occurances == 0:
    union_vehicles.append(vehicle1)
  else:
    subtraction_vehicles.remove(vehicle1)

util.update_json(vehicles_to_search_path, union_vehicles)
print("Redundância retirada!")

util.update_json(f"{vehicles_only_from_year_path}_{anos[0]}.json", subtraction_vehicles)

# Contagem da quantidade de modelos para busca
modelos_base_count = 0
for vehicle in union_vehicles:
  for modelo_base in vehicle["modelos_base"]:
      modelos_base_count += len(modelo_base)

print(f"Teremos a busca de {modelos_base_count} modelos diferentes!")