class Customer:
    _instances = []
    def __init__(self, given_name=None, family_name=None):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        Customer._instances.append(self)
        
        
    def get_given_name(self):
        return self._given_name
        
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            print(f"Setting given name to: {first_name}")
            self._given_name = first_name
            self._full_name = f"{first_name} {self._family_name}"
        else:
            print('Given name must be a string.')
    
    given_name = property(get_given_name, set_given_name)
    
    def get_family_name(self):
        return self._family_name
        
    def set_family_name(self, last_name):
        if isinstance(last_name, str):
            print(f"Setting family name to: {last_name}")
            self._family_name = last_name
            self._full_name = f"{self._given_name} {last_name}"
        else:
            print('Family name must be a string.')

    family_name = property(get_family_name, set_family_name)
    
    def full_name(self):
        return self._full_name
    @classmethod
    def all(cls):
        return cls._instances


# Example usage
Joy = Customer("Joy", "Anyango")
print(Joy.given_name)  


Joy.given_name = 'Olive'
print(Joy.given_name) 

Joy.given_name = False  

print(Joy.full_name()) 


print(Joy.family_name) 

Joy.family_name = 'Otieno'
print(Joy.family_name) 

Joy.family_name = 10  


Charity=Customer("Charity",'Wambui')
Patience=Customer('Patience',"Muraguri")
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())