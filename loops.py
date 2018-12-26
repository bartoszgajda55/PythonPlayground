# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Paul", "Sara", "Susan"]

# For loop
for person in people:
  print(f"Person - {person}")

# Break
for person in people:
  if person == "Sara":
    break
  print(f"Person - {person}")
  
# Continue
for person in people:
  if person == "Sara":
    continue
  print(f"Person - {person}")

# range
for i in range(len(people)):
  print(people[i])

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
  print(f"Count: {count}")
  count += 1