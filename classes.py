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
    def __init__(self, owner, balance, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111, 999999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        # self.balance -= amount if self.has_overdraft == True else "Sorry Withdrawal is more than current balance"
        return self.balance - amount if amount <= self.balance or self.has_overdraft else "Sorry, withdrawal amount exceeds current balance."


    def __str__(self):
        return f'Account {self.account_no} / Balance: {self.balance}'
    

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        BankAccount.__init__(self, owner, balance)

    def withdraw(self, amount = None):
        return "No Withdrawals permitted"
    
chase = BankAccount('John Michael', 40000)

print(chase)

print(chase.owner, chase.balance, chase.account_no)

print(chase.withdraw(500000))





