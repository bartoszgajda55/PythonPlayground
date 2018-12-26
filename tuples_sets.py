# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value tuple (needs trailing comma)
fruits2 = ("Apples",)

# Can't change a value
# fruits[0] = "Pears"

# Delete tuple
del fruits2

# Get length
len(fruits)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {"Apples", "Oranges", "Mango"}

# Chech if something is in set
"Apples" in fruits_set

# Add to set
fruits_set.add("Grape")

# Remove
fruits_set.remove("Grape")

# Clear set
fruits_set.clear()
