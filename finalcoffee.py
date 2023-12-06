class Person: 
  def __init__(self, name, favorite_drink, my_order):
    self.name = name
    self.favorite_drink = favorite_drink
    #self.my_order = 

    #def my_order(self):

class Order: 
  def __init__(self, drink_type, person):
    self.type = drink_type
    self.person = person

    def to_string(self):
      print(f"{self.person.name} ordered: {self.drink_type}")


person1 = Person("Tay", "sugar cookie latte")
order1 = person1.my_order()

print(order1.to_string())