# FizzBuzz Challenge

def fizzbuzz(n, limit):
    for i in range(limit + 1):
        if i % n == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

##fizzbuzz(5, 100)  # Call the function with n=5 and limit=100

# Anagrama

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if str1 == str2:
        return False
    
    return sorted(str1) == sorted(str2)

##print(is_anagram("amor", "roma"))

# Fibonacci Sequence

def fibonacci(position: int):
    a,b = 0, 1
    for i in range(1,position+1):
        print(f"Position {i} number {a}")
        a, b = b, a + b

##fibonacci(50)

# Prime Numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

##print(is_prime(17))

# Invert a String

def invert_string(string: str):
    inverted = ""
    for char in string:
        inverted = char + inverted
    return inverted

##print(invert_string("Hello World!"))