favorite_laguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# if 'erin' not in favorite_laguages.keys():
#     print("Erin,please take out poll!")
#
# for name in sorted(favorite_laguages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
# for language in favorite_laguages.values():
#     print(language.title())

for language in set(favorite_laguages.values()):
    print(language.title())