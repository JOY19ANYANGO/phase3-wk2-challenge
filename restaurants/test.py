import unittest
from restaurant import Restaurant  # Import the Restaurant class
from customer import Customer  # Import the Customer class
from review import Review  # Import the Review class

class TestRestaurantReviewSystem(unittest.TestCase):

    def setUp(self):
        self.restaurant = Restaurant('Galitos')
        self.customer1 = Customer("Joy", "Anyango")
        self.customer2 = Customer("Natasha", "Wanjira")
        self.review1 = Review(self.customer1.full_name(), self.restaurant.name(), 9)
        self.review2 = Review(self.customer2.full_name(), self.restaurant.name(), 5)

    # Test Customer class methods
    def test_customer_initialization(self):
        self.assertEqual(self.customer1.given_name, "Joy")
        self.assertEqual(self.customer1.family_name, "Anyango")
        self.assertEqual(self.customer2.given_name, "Natasha")
        self.assertEqual(self.customer2.family_name, "Wanjira")

    def test_customer_full_name(self):
        self.assertEqual(self.customer1.full_name(), "Joy Anyango")
        self.assertEqual(self.customer2.full_name(), "Natasha Wanjira")

  

   
    # Test Review class methods
    def test_review_rating(self):
        self.assertEqual(self.review1.rating(), 9)
        self.assertEqual(self.review2.rating(), 5)

    def test_review_customer(self):
        self.assertEqual(self.review1.customer(), self.customer1.full_name())
        self.assertEqual(self.review2.customer(), self.customer2.full_name())

    def test_review_restaurant(self):
        self.assertEqual(self.review1.restaurant(), self.restaurant.name())
        self.assertEqual(self.review2.restaurant(), self.restaurant.name())

    # Add more test cases for other Review methods...

if __name__ == '__main__':
    unittest.main()
