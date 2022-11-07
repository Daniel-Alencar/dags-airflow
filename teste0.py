# Faz a execução do Web Scrapping de acordo com o que desejamos
def execution(self):
  print(self.indices_de_busca)

  self.setup()
  while util.check_indexes(self.vehicles_to_search, self.indices_de_busca):
    vehicle_information = self.get_vehicle_information(
      
      # marca
      self.vehicles_to_search
        [indices_de_busca["marca"]]["marca"],
      
      # modelo
      self.vehicles_to_search
        [indices_de_busca["marca"]]["modelos_base"]
        [indices_de_busca["modelo_base"]]
        [indices_de_busca["modelo_especifico"]]
    )

    vehicle_information_formatted = json.dumps(vehicle_information, indent=2)
    print(vehicle_information_formatted)

    self.vehicles_with_price.append(vehicle_information)
    with open("json/vehicles_with_price.json", "w") as jsonFile:
      json.dump(self.vehicles_with_price, jsonFile, indent=2)
    print("\n=======================\n")

    if util.update_indexes(self.vehicles_to_search, indices_de_busca) == False:
      break
    indices_de_busca = util.read_json("json/indices_de_busca.json")

  # Fechamento de execução do web_scrapping
  self.driver.quit()
