from review import Review  # Import the Review class

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
    
    def reviews(self):
        restaurant_reviews = []
        for review in Review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews
    
    def customers(self):
        reviewed_customers = []
        for review in Review.all():
            if review.restaurant() == self:
                reviewed_customers.append(review.customer())
        return list(set(reviewed_customers))

#example usage
kfc=Restaurant('KFC')
print(kfc.name()) 
galitos=Restaurant('Galitos')
print(galitos.name())
cjs=Restaurant("CJ'S") 
print(cjs.name())
non_string_restaurant = Restaurant(123)