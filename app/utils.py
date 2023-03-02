import re


def get_population(country_data):
  population_history = [[key, country_data[key]] for key in country_data.keys() if re.search('^[1-3]', key)]
  population_history = {key: value for key, value in population_history}
  
  return population_history

def population_by_country(data, country):
  result = list(filter(lambda items: items['Country'] == country, data))
  return result

def world_population_percentage(data):
  countries = list(map(lambda x: x['Country'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  return countries, percentage