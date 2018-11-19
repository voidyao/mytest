cities = {
    'wujiang': {
        'country': 'china',
        'population': 22,
        'fact': 'nice',
    },
    'newyork': {
        'country': 'usa',
        'population': 2,
        'fact': 'bad'
    },
}

for cityname, city_infor in cities.items():
    print("The city: " + cityname)
    countryname = city_infor['country']
    countrypop = city_infor['population']
    countryfact = city_infor['fact']

    print("\t Country: " + countryname)
    print("\t Population: " + str(countrypop))
    print("\t fact: " + countryfact)

