def sum(a, b, fsum):
    return fsum(a + b)

def sum_1(a):
    return a + 1

def sum_2(a):
    return a + 2

print(sum(5, 3, sum_2))  # Use a function as an argument
print(sum(5, 3, sum_1))  # Use another function as an argument

# Closure example

def sum_10():
    def add(a):
        return a + 10
    return add

sum_value = sum_10()  # Create a closure that adds 10 to its argument
print(sum_value(5))  # Call the closure with an argument

print(sum_10()(5))  # Call the closure function with an argument

def rest_10(b):
    def rest(a):
        return a - 10 - b
    return rest

print(rest_10(5))
print(rest_10(5)(20))  # Call the closure with an argument

# Built-in higher orden functions

# Map example

numbers = [1, 2, 3, 4, 5]

new_numbers = list(map(lambda a: a*2 ,numbers)) # Use map to double each number in the list

print(new_numbers)  

def transformation(a):
    return a / 5

new_numbers = list(map(transformation, numbers))  # Use a function
print(new_numbers)

# Filter example

def filter_greater_than_2(a):
    return a > 2

new_numbers = list(filter(filter_greater_than_2, numbers))  # Use filter to get numbers greater than 2
print(new_numbers)

new_numbers = list(filter(lambda a: a > 2, numbers))  # Use a lambda function
print(new_numbers)

# Reduce example

from functools import reduce

def sum_numbers(a, b):
    return a + b

new_numbers = reduce(sum_numbers, numbers)  # Use reduce to sum all numbers in the list
print(new_numbers)

new_numbers = reduce(lambda a, b: a + b * 2, numbers)  # Use a lambda function