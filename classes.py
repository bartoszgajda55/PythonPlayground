# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f"My name is {self.name}"

# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def setBalance(self, balance):
    self.balance = balance

# Initialize User object
brad = User("Brad", "test@test.com", 30)