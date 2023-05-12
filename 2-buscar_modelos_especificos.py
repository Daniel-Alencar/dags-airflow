from Vehicle_Search import Vehicle_Search
import util

from settings import verbose

ano_considerado = 2015

mes_busca = "janeiro"
ano_busca = 2015

vehicles = util.read_json(f"json/vehicles_{ano_considerado}.json")

categories_names = [
  category_name

  for category_DICTIONARY in vehicles["vehicles"] 
    for category_name in category_DICTIONARY
]

try:
  vehicles_to_search = util.read_json(f"json/vehicles_to_search_{ano_considerado}.json")
except:
  vehicles_to_search = []

vehicles_discarded_count = 0
vehicles_count = 0
for i, category in enumerate(vehicles["vehicles"]):
  list_vehicles = category[categories_names[i]]

  vs = Vehicle_Search()
  vs.setup()
  for vehicle in list_vehicles:
    vehicle_json = {}

    vs.marca = vehicle["marca"]
    vs.modelo_base = vehicle["modelo"]
    vs.mes_busca = mes_busca
    vs.ano_busca = ano_busca

    if verbose:
      print("="*20)
      print(vs.modelo_base)
      print("="*20)

    vehicle_names = vs.execution()

    if len(vehicle_names) > 0:
      vehicle_json["marca"] = vehicle["marca"]
      vehicle_json["modelos_base"] = []
      vehicle_json["modelos_base"].append(vehicle_names)

      vehicles_to_search.append(vehicle_json)

      if verbose:
        util.print_formatted_json(vehicle_json)

      util.update_json(f"json/vehicles_to_search_{ano_considerado}.json", vehicles_to_search)

      vehicles_count += len(vehicle_names)
    else:
      if verbose:
        print("Veiculo descartado:")
        print(f'{vehicle["marca"]}/{vehicle["modelo"]}')
      vehicles_discarded_count += 1

      try:
        modelos_descartados = util.read_json(f"json/modelos_descartados_{ano_considerado}.json")
      except:
        modelos_descartados = []

      modelo_descartado = {
        "marca": vehicle["marca"],
        "modelo": vehicle["modelo"]
      }
      modelos_descartados.append(modelo_descartado)
      
      util.update_json(f"json/modelos_descartados_{ano_considerado}.json", modelos_descartados)
  
  if verbose:
    print("Modelos considerados:", vehicles_count)
    print("Modelos_base descartados:", vehicles_discarded_count)
  vs.close()