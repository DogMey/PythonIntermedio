sum = lambda a, b: a + b
print(sum(5, 3))  # Example usage of the lambda function

print((lambda a, b: (a * b) + 3)(5, 3))  # Example usage of the lambda function with an expression

def sum_values(x):
    return lambda a, b: a + b + x

print(sum_values(5)(3, 2))  # Example usage of the nested lambda function