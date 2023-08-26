class Restaurant:
    # intialises restaurant with name
    def __init__(self,name):
         if isinstance(name, str):
            self._name = name
         else:
            print("Name must be a string")
    # returns restaurant's name    
    def name(self):
        return self._name    


#example usage
kfc=Restaurant('KFC')
print(kfc.name()) 
galitos=Restaurant('Galitos')
print(galitos.name())
cjs=Restaurant("CJ'S") 
print(cjs.name())
non_string_restaurant = Restaurant(123)