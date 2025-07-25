my_original_list = [1, 2, 3, 4, 5]

my_list = [i for i in my_original_list]

print(my_list)  # Output: [1, 2, 3, 4, 5]

my_range = range(11)  # Create a range object from 0 to 10
print(my_range)  # Output: range(0, 11)

my_list = [i for i in range(11)]
print(my_list)

my_list = [i for i in range(11) if i % 2 == 0]  # List comprehension with a condition
print(my_list)  # Output: [0, 2, 4, 6, 8, 10]

my_list = [i+1 for i in range(11)] 
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def trasnfer_function(i):
    return (i + 20)/30

my_list = [trasnfer_function(i) for i in range(61) if i % 30 == 0]
print(my_list)

my_list = [i*0 for i in range(11)]  # List comprehension with a multiplication by 0
print(my_list)