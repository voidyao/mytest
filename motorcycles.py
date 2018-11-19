# motorcycles = ["honda" , "yamaha" , "suzuki"]
# print(motorcycles)
#
# motorcycles[0] = 'ducati'
# print(motorcycles)
#
# motorcycles.append('wuyang')
# print(motorcycles)
#
# motorcycles.insert(0, 'jiuzhou')
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)
#
# del motorcycles[1]
# print(motorcycles)
#
# popped_motorcycels = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycels)
#
# print("The last motorcycle I owned was a " + popped_motorcycels + ".")
#
# fist_moto = motorcycles.pop(0)
# print("The first moto I owned was a " + fist_moto + ".")
#
# print(motorcycles)

motorcycles = ["honda" , "yamaha" , "suzuki" , "ducati"]
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")