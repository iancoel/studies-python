# Kind of a template for a type of object
# __init__ is a method/function that is going to be called everytime that someone tries to create a new point. It takes a couple of arguments (all functions that operate on objects themselves (methods) are going to take the first argument called self that represents the object in question)

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(2, 8)
# print(p)
# print(p.x)
# print(p.y)

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True

  def open_seats(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hemione", "Ginny"]
for person in people:
  success = flight.add_passenger(person)
  if success:
    print(f"Added {person} to flight successfully.")