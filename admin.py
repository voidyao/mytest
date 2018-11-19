accounts = []

if accounts:

    for account in accounts:
        if account == 'admin':
            print(account + ",would you like to see a status report?")
        else:
            print("Hello " +account+ ",thank you for logging in again")
else:
    print("We need to find some users!")