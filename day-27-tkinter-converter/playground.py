# def add(*num):
#     print(num[len(num) - 1])
#     result = sum([i for i in num])
#     print(result)
#
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Here kwargs become an dictionary
# def calculate(n, **kwargs):
#     # for key, value in kwargs.items():
#     #     print(f"key: {key}\nvalue: {value}")
#     # print()
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(1, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # Using get, we ca make an argument optional,
        self.color = kwargs.get("color")  # without value it will return None
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(f"Model: {my_car.model}\nCar mark: {my_car.make}")
