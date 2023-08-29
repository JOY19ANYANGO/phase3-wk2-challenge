from review import Review
from restaurant import Restaurant
from  customer import Customer

print("RESTAURANTS")
kfc=Restaurant('Kfc')
print(kfc.name())

galitos=Restaurant('Galitos')
print(galitos.name())
print(galitos.customers())

java=Restaurant('Java')
print(java.name())


print("CUSTOMERS")
joy=Customer("Joy","Anyango")
print(joy.full_name())
natasha=Customer("Natasha","Wanjira")
print(natasha.full_name())

print("REVIEWS")
good=Review("Joy Anyango","Kfc",9)
bad=Review("Natasha Wanjira","Galitos",5)
better=Review("Joy Anyango","Java",7)
print(bad.customer())
nice=Review("Natasha Wanjira","Galitos",9)



