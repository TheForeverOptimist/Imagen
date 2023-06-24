class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')




spot = Dog('Spot', 8)

print(spot)

print(spot.name, spot.age)

spot.bark()


lassie = Dog('Lassie')

print(lassie.name, lassie.age)