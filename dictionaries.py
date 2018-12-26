# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

# Use a constructor
person2 = dict(first_name="Sara", last_name="Williams")

# Get a value
person["first_name"]
person.get("last_name")

# Add value
person["phone"] = "555-555-5555"

# Get all keys
person.keys()

# Get items
person.items()

# Copy dictionary
person3 = person.copy()

print(person)
