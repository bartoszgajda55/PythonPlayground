# A List is a collection which is ordered and changeable. Allows duplicate members.

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use constructor
numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a value
fruits[1]

# Get length
len(fruits)

# Append to list
fruits.append("Bananas")

# Remove
fruits.remove("Grapes")

# Insert into position
fruits.insert(2, "Strawberries")

# Removie with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort

# Reverse list
fruits.sort(reverse=True)
