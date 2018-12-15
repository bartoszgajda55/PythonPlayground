# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "John"
age = 37

# Concatenate
print("My name is " + name + ", age is " + str(age))

# String Formatting

# Arguments by position
print("My name is {name}, age is {age}".format(name=name, age=age))

# F-Strings (3.6+)
print(f"My name is {name}, age is {age}")

# String Methods
s = "hello world"

# Capitalize string
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
