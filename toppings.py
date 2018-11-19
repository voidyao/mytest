# requested_toppings = ['mushrooms', 'green pepers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green pepers':
#         print("Sorry,we are out of green peppers right now.")
#     else:
#         print("Adding "+ requested_topping + ".")
#
# print("\nFinished making your pizza")


# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding "+ requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'qreen pepers','pepernoi', 'pineapple', 'extra cheese']

request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in available_toppings:
        print("Adding "+ request_topping + ".")
    else:
        print("Sorry,we don't have" + request_topping + ".")

print("\nFinished making your pizza")