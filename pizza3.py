prompt = "\nPlease enter some of pizza:"
prompt += "\n(Enter 'quit' to exit.) "

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print("give u" + pizza + "!")
