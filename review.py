class Review:
    # keeps track of customers reviews
    reviews=[]
    # initialises  review with customer,restaurant,rating
    def __init__(self,customer,restaurant,rating=0):
        self._customer=customer
        self._restaurant=restaurant
        Review.reviews.append(self)# adds review to the list
        # ensures that the rating is a number
        if isinstance(rating,(int ,float)):
          self._rating=rating
        else:
            print("ratng must be a number") 
            
    #  returns rating        
    def rating(self):
        return self._rating
    
    # returns customer
    def customer(self):
        return self._customer
    
    # returns restaurant
    def restaurant(self):
        return self._restaurant
    
    # returns a list of all reviews 
    @classmethod
    def all(cls):
        return cls.reviews    
    def __repr__(self):
        return f"customer:{self._customer} restaurant:{self._restaurant} rating:{self._rating}"
    
#print("REVIEWS")
#good=Review("Joy Anyango","Kfc",9)
bad=Review("Natasha Wanjira","Galitos",5)
better=Review("Joy ","Java",7)
# print(bad.customer())
nice=Review("Joy Anyango","Galitos",9)
bad=Review("Joy Anyango","Galitos",16)
    