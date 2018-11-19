# itemslist = ['bord', 'computer', 'cpu', 'memory', 'ip']
# print("The first there iteams in the list are: ")
# print(itemslist[:3])
# print("\nThere items from the middle of the list are: ")
# print(itemslist[1:4])
# print("\nThe last there items in the list are: ")
# print(itemslist[2:5])

mypizzas = ['bishenke', 'kfc', 'hh']
myfriendpizzas = mypizzas[:]
myfriendpizzas.append("zz")

print("My favorite pizzas are: ")
for pizza1 in mypizzas:
    print(pizza1)
print("My friends favorite pizzas are: ")
for pizza in myfriendpizzas:
    print(pizza)
