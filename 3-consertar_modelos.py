import util
from Vehicle_Search import Vehicle_Search

marca = "Chevrolet"
modelo_base = "Classic"

mes_busca = "janeiro"
ano_busca = 2015

vs = Vehicle_Search()
vs.setup()
vehicle_json = {}

vs.marca = marca
vs.modelo_base = modelo_base
vs.mes_busca = mes_busca
vs.ano_busca = ano_busca

vehicle_names = vs.get_models_from_model_base(marca, modelo_base, mes_busca, ano_busca)
vs.close()

util.print_formatted_json(vehicle_names)