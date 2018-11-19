user_1 = {
    'name': 'void',
    'age': 11,
    'city': 'wj',
}
user_2 = {
    'name': 'amy',
    'age': 7,
    'city': 'bj'
}

users = [user_1, user_2]

for user in users:
    # print(user)
    print("The " + user['name'].title() + " has " + str(user['age']) + " years old " +
          "live in " + user['city'])
