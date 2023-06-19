# def fahr_to_celsius(temp):
#     return((temp - 32) * (5/9))

# print(fahr_to_celsius(50))


# def first_function():
#   pass

# result = first_function()
# print(result)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

math_operations = {
    '+': add,
    '-': subtract
}

selected_operation = '+'

print(math_operations[selected_operation](2,4))

