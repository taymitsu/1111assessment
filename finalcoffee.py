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

#Challenge 5 & 13:
class CoffeeBar:
  def __init__(self, name, barista):
    self.name = name
    self.barista = barista
    self.orders_list = []

  def place_order(self, current_order):
    self.orders_list.append(current_order)

  def process_orders(self):
   for order in self.orders_list:
     print(f"{self.barista.greeting} {order.to_string()}")

#Challenge 9:
class Barista(Person):
  def __init__(self, name, greeting):
    super().__init__(name, favorite_drink="")
    self.greeting = greeting 
#Challenge 10:
#barista1 = Barista("Kevin", "Hey Dude!")

#############################################
#person1 = Person("Tay", "sugar cookie latte")
#order1 = person1.my_order()
#print(order1.to_string())
#############################################

#Challenge 4
#Amy = Person("Amy", "Coffee")
#Bob = Person("Bob", "Tea")
#Cat = Person("Cat", "Milk")

#order_Amy = Amy.my_order()
#order_Bob = Bob.my_order()
#order_Cat = Cat.my_order()

#print(order_Amy.to_string())
#print(order_Bob.to_string())
#print(order_Cat.to_string())

#Challenge 6 & 7
#test (create instance of CoffeeBar)
#Challenge 11 & 12:
barista1 = Barista("Kevin", "Hey Dude!")
coffee_bar = CoffeeBar("Temple Coffee Roasters", barista1)

Amy = Person("Amy", "Dirty Chai")
Bob = Person("Bob", "Espresso shot")
Cat = Person("Cat", "Iced Matcha Latte with Cold Foam")

order_Amy = Amy.my_order()
order_Bob = Bob.my_order()
order_Cat = Cat.my_order()

coffee_bar.place_order(order_Amy)
coffee_bar.place_order(order_Bob)
coffee_bar.place_order(order_Cat)

#Challenege 8
coffee_bar.process_orders()