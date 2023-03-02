#Import pkg
import charts
import read_csv
import utils
import json

def run():
    #get date from csv file by region
    data = read_csv.read_csv('./data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries, percentage = utils.world_population_percentage(data)
    print(countries, percentage)

    #get pie chart from data
    charts.generate_pie_chart(countries, percentage)

    #get country from promp
    country = input('Type Country!.. ')

    #get informstion country
    infomartion_country = utils.population_by_country(data, country)
    print(json.dumps(infomartion_country, sort_keys = False, indent = 4), end = '\n\n')

    if len(infomartion_country) > 0:
        infomartion_country = infomartion_country[0]

        #get population countri
        population_country = utils.get_population(infomartion_country)

        print(json.dumps(population_country, sort_keys = True, indent = 4))

        #get labels and values for charts
        labels = list(population_country.keys())
        print(labels)
        values = [int(population_country[key]) for key in labels]
        print(values)

        #get bar charts from data
        charts.generate_bar_chart(country, labels, values)


    

if __name__ == '__main__':
    run()