import pandas
from settings import data_path

data = pandas.read_csv(data_path, encoding = 'utf-8', delimiter = ',')

data = data.drop_duplicates()
data.fillna(value = "NULL", axis = 1, inplace = True)

data.to_csv(data_path, index = False, header = True)
