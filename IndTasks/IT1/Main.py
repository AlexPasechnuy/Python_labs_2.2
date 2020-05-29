import csv
import ast
from IndTasks.IT1.Country import Country

def csv_dict_reader(path):
    with open(path, 'r') as f_obj:
        countries = list()
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            ctr = Country(line["country_name"])
            ctr.addCities(ast.literal_eval(line["cities"]))
            countries.append(ctr)
        return countries

def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["country_name","cities"],
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        writer.writerows(data)

def create_csv_data(crt_list):
    data = []
    for ctr in countries:
        data.append({
            'country_name': ctr.name,
            'cities': ctr.createCityDict(),
        })
    return data

countries = list()

countries = csv_dict_reader("source.csv")

write_csv("dest.csv",create_csv_data(countries))