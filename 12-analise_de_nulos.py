import pandas
from settings import data_without_null_path, data_path

data = pandas.read_csv(data_path, encoding = 'utf-8', delimiter = ',')

clean_data = data.drop(["Marca", "Modelo", "Ano-modelo"], axis = 1, inplace = False)

cols_to_check = clean_data.columns
clean_data['is_na'] = clean_data[cols_to_check].isnull().apply(lambda x: all(x), axis = 1) 

print(f"Quantidade de linhas nulas: {clean_data['is_na'].sum()}")

list_data = list(clean_data['is_na'])

for index in range(len(list_data)):
  if(list_data[index]):
    data.drop(index, axis = 0, inplace = True)

data.fillna(value = "NaN", axis = 1, inplace = True)
data.to_csv(data_without_null_path, index = False, header = True)