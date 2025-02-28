class Item:
    def calculate_total_cost(self,x,y):
          return x*y
          pass 
item1=Item()
item1.price=100
item1.name="Phone"
item1.quantity=24
print(item1.calculate_total_cost(item1.price,item1.quantity))


item2=Item()
item2.price=10000
item2.name="i pad"
item2.quantity=20
print(item2.calculate_total_cost(item2.price,item2.quantity))

print(type(item1))
print(type(item1.price))
print(type(item1.name))
print(type(item1.quantity))

#random_var="puneeth"
#print(random_var.upper())
#print(random_var.lower())

