reviers = {
    'nile': 'egypt',
    'changjiang': 'jiangsu',
    'huanghe': 'suzhou',
    }

for revier in reviers.keys():
    print("The " + revier.title() + " runs throuth " + reviers[revier].title() + ".")

for i in reviers.keys():
    print(i.title())
for country in reviers.values():
    print(country.title())


