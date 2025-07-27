import re

my_string = "Hello, World! 123"
my_other_string = "Hello, World! 456"

# Match

print(re.match(r"Hello", my_string)) # Match object

print(re.match(r"123", my_string)) # None

match = re.match(r"Hello", my_other_string, re.I) # re.I is for case-insensitive matching, but this will still return None
print(f"Match {match}")
start, end = (match.span())
print(my_other_string[start:end]) # This will raise an error since match is None

match = re.match(r"123", my_string, re.I)
if match == None:
    print("No match found")
else:
    print(f"Match {match}")
    start, end = (match.span())
    print(my_other_string[start:end])

# Search

search = re.search("World", my_string, re.I) # Search object only the first occurrence
print(search)
start, end = (search.span())
print(my_string[start:end]) # This will print "World"

# Findall

my_string = "Hi and repet Hi and repet Hi" 
findall = re.findall(r"Hi", my_string) # This will return a list of all occurrences of "Hi"
print(findall)

# Split

split = re.split(r"\s", my_string) # This will split the string by 
print(split) # This will print a list of words in the string

# Sub

sub = re.sub(r"Hi", "Hello", my_string) # This will replace all occurrences of "Hi" with "Hello"
print(sub) # This will print "Hello and repet Hello and repet Hello"

sub = re.sub(r"Hi|and", "Hello", my_string) # This will replace all occurrences of "Hi" and "and" with "Hello"
print(sub)

# Patterns

pattern = r"Hello"
string = "This is a example string with Hello in it, but not at the start. Hello again! Hello123"
print(re.findall(pattern, string))

pattern = r"Hello.*?Hello"  # Non-greedy match
print(re.findall(pattern, string))

pattern = r"[a-z]"
print(re.findall(pattern, string))
print(re.match(pattern, string))  # This will return None since the first character is uppercase 'T'
pattern = r"[A-Z]"
print(re.match(pattern, string))  # This will return a list of all uppercase letters in the string

pattern = r"\d"  # This will return a list of all digits in the string
print(re.findall(pattern, string))

pattern = r"\D"  # Non-digit characters
print(re.findall(pattern, string))

pattern = r"..l.."  # This will return a list of all characters that have 'l' in the third position
print(re.findall(pattern, string))

pattern = r".{3}"  # This will return a list of all characters that have 3 characters in the string
print(re.findall(pattern, string))

# Email validation

email = "kevinsantiagoram25@gmail.com"
notemail = "kevinsantiagoram25@gmailcom"

def is_a_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) != None

def validation_email(email):
    if is_a_email(email):
        print(f"{email} is a valid email")
    else:
        print(f"{email} is not a valid email")

validation_email(email)
validation_email(notemail)