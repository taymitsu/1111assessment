#Challenge 1
class Person:
  def __init__(self, name, favorite_drink):
    self.name = name
    self.favorite_drink = favorite_drink

  #Challenge 3
  def my_order(self):
    return Order(self.favorite_drink, self)

#Challenge 2
class Order:
  def __init__(self, drink_type, person):
    self.drink_type = drink_type
    self.person = person

  def to_string(self):
    return f"{self.person.name} ordered: {self.drink_type}"

person1 = Person("Tay", "sugar cookie latte")
order1 = person1.my_order()
print(order1.to_string())
