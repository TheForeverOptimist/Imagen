import random

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

# class Vehicle():
#     next_id = 1

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.running= False
#         self.id = Vehicle.next_id
#         Vehicle.next_id += 1

#     def start(self):
#         running = True
#         print('running...')

#     def stop(self):
#         running = False
#         print('stopped...')

#     def __str__(self):
#         return f'Vehicle is a {self.make} model {self.model}'
    
#     @classmethod
#     def get_total_cars(cls):
#         return cls.next_id - 1
    

# car1 = Vehicle('Audi', 'Q7')
# car2 = Vehicle('Toyota', 'Camry')
# car3 = Vehicle('Chevy', 'Cruze')

# #call the class method to get the total number of cars

# # total_cars = Vehicle.get_total_cars()
# print(f'Total number of cars is {Vehicle.get_total_cars()}')

# print(car)

# print(car.make, car.model)

# car.start()

# car.stop()

# print(car.id)

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111, 999999)

    def deposit(amount):
        balance += amount

    def withdraw(amount):
        balance -= amount

    def __str__(self):
        return f'The Bank {self.account_no} is owned by {self.owner} has a balance of {self.balance}'
    
chase = BankAccount('John Michael', 40000)

print(chase)

print(chase.owner, chase.balance, chase.account_no)



