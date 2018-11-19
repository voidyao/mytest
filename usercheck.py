current_users = ['void', 'ken', 'shelf', 'sky', 'lb']

new_users = ['vOId', 'david', 'KEn', 'lily', 'rock']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please type an another account!")
    else:
        print("This account is not inuse.")
