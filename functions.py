# def fahr_to_celsius(temp):
#     return((temp - 32) * (5/9))

# print(fahr_to_celsius(50))


# def first_function():
#   pass

# result = first_function()
# print(result)

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# math_operations = {
#     '+': add,
#     '-': subtract
# }

# selected_operation = '+'

# print(math_operations[selected_operation](2,4))


# nums = [1, 3, 2, 6, 5]
# odds = list( filter(lambda num: num % 2, nums) )

# print(odds)


# def fn(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)

# fn(1, 2, 'SEI')

# def dev_skills(dev_name, **kwargs):
#     dev = {'name': dev_name, 'skills': kwargs}
#     return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))


# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
	
# 	For example:

# 	```python
# 	sum_to(6)  # returns 21
# 	sum_to(10) # returns 55
# 	```

def sum_to(n):
    Total = 0
    for num in range(1, n + 1):
        Total += num
    return Total

print(sum_to(10))


# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.

# 	For example:
	
# 	```python
# 	largest([1, 2, 3, 4, 0])  # returns 4
# 	largest([10, 4, 2, 231, 91, 54])  # returns 231