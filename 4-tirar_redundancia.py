import util
from settings import vehicles_to_search_path, vehicles_only_from_year_path

anos = [ 2021, 2022 ]

vehicles_to_search0 = util.read_json(f"json/vehicles_to_search_{anos[0]}.json")
vehicles_to_search1 = util.read_json(f"json/union.json")

union_vehicles = vehicles_to_search0.copy()
subtraction_vehicles = vehicles_to_search0.copy()

for vehicle1 in vehicles_to_search1:
  occurances = vehicles_to_search0.count(vehicle1)
  if occurances == 0:
    union_vehicles.append(vehicle1)
  else:
    subtraction_vehicles.remove(vehicle1)



util.update_json(f"json/union.json", union_vehicles)
util.update_json(f"json/subtraction.json", subtraction_vehicles)