class Restaurant:
    def __init__(self,name):
        self._name=name
    def name(self):
        return self._name    


#example usage
kfc=Restaurant('KFC')
print(kfc.name()) 
galitos=Restaurant('Galitos')
print(galitos.name())
cjs=Restaurant("CJ'S") 
print(cjs.name())