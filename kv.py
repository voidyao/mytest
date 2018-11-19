# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

favorite_laguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# for name, language in favorite_laguages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")

# for name in favorite_laguages.keys():
#     print(name.title())

friends = ['phil', 'sarah']
for name in favorite_laguages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite laguage is " +
              favorite_laguages[name].title() + "!")

