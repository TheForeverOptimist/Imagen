# class Dog():
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f'{self.name} says woof!')

#     def __str__(self):
#         return f'Dog named {self.name} is {self.age} years old'
    




# spot = Dog('Spot', 8)

# print(spot)

# print(spot.name, spot.age)

# spot.bark()


# lassie = Dog('Lassie')

# print(lassie.name, lassie.age)

class Vehicle():
    def __init__(self, make, model, running=False):
        self.make = make
        self.model = model
        self.running= running

    def start(self):
        running = True
        print('running...')

    def stop(self):
        running = False
        print('stopped...')

    def __str__(self):
        return f'Vehicle is a {self.make} model {self.model}'
    

car = Vehicle('Audi', 'Q7')

print(car)

print(car.make, car.model)

car.start()

car.stop()
