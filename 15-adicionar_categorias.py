import pandas as pd
import util

def category_of_model(model):

  for ano_considerado in range(2015, 2023):
    vehicles = util.read_json(f"json/vehicles_{ano_considerado}.json")

    categories_names = [
      category_name

      for category_DICTIONARY in vehicles["vehicles"] 
        for category_name in category_DICTIONARY
    ]

    for i, category in enumerate(vehicles["vehicles"]):
      list_vehicles = category[categories_names[i]]

      for vehicle in list_vehicles:
        modelo = vehicle["modelo"]

        if(str(modelo).upper() == str(model).upper()):
          return categories_names[i]
        
  return None


data = pd.read_csv("csv/Dados com Depreciação.csv")
categories_names = []

# Percorrer o Dataframe
for i, item in data.iterrows():
  modelo = item["Modelo"]

  splitted_modelo = str(modelo).split()
  final_value = 4

  for index in range(0, final_value):
    modelo = splitted_modelo[index]

    category_name = category_of_model(modelo)
    if(category_name != None or index == (final_value - 1)):
      categories_names.append(category_name)
      print(category_name)

      break


data["Categoria"] = categories_names
print(len(categories_names))

data.to_csv("csv/Completed_data.csv", index=False, na_rep='NaN')
