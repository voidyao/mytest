from car import Car
"""让Python打开模块car，并导入其中的car类"""

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()