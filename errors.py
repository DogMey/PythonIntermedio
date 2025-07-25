# SyntaxError

try:
    eval("x === 10")
except SyntaxError as e:
    print(f"SyntaxError: {e}")

# NameError

try:
    print(x)
except NameError as e:
    print(f"NameError: {e}")

# IndexError

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError: {e}")

# ModuleNotFoundError

try:
    import module
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")

# AttributeError

try:
    my_list = [1, 2, 3]
    my_list.append(4)
    my_list.non_existent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# KeyError

try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

# TypeError

try:
    result = "string" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# ZeroDivisionError

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# ImportError

try:
    from math import non_existent_function
except ImportError as e:
    print(f"ImportError: {e}")

# ValueError

try:
    int("Hi")
except ValueError as e:
    print(f"ValueError: {e}")

# FileNotFoundError

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")