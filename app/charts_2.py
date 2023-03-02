from read_csv import *
from charts import *
import json

path = './app/data.csv'
data = read_csv(path)

country = data[-7]
print(json.dumps(country, sort_keys = False, indent = 4), end = '\n\n')
info = list(country.items())
print(info)
info = info[5:13]
print(info)
info = dict(info)
print(json.dumps(info, sort_keys = False, indent = 4), end = '\n\n')

labels = [labels for labels in info.keys()]
print('labels => ', labels)
values = [int(value) for value in info.values()]
print('values => ', values)

generate_bar_chart(labels, values)