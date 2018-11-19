dinner = ["zou", "ken" , "ivy"]
print(dinner)

canthere = 'zou'
dinner.remove(canthere)
dinner.insert(0,"void")
print(dinner)

print("The person " + canthere + " cant come.")
print(len(dinner))
print("welcom to dinner" +"\n"+ dinner[0] + "\n" +dinner[1] +"\n" +dinner[2])

print("The table is big, add person")

dinner.insert(0,"oasis")
dinner.insert(2,"shelf")
dinner.append("lary")
print("weclom to dinner")
print(dinner)

print("The food is not enough")

person = dinner.pop(0)
print(person + " leave")

person = dinner.pop(0)
print(person + " leave")

person = dinner.pop(0)
print(person + " leave")

person = dinner.pop(0)
print(person + " leave")

print(dinner[0] +"\tand\t" +dinner[1] + " is here.")

del dinner[0]
print(dinner)
del dinner[0]
print(dinner)





