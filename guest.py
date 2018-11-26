filename = 'guest.txt'

with open(filename,'a') as file_object:
    while True:
        guest = input("type your name:")
        print("Welcom " + guest)
        guest += '\n'
        file_object.write(guest)

