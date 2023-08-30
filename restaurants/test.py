import unittest
from restaurant import Restaurant  # Replace with the actual import path to your Restaurant class
from review import Review  # Replace with the actual import path to your Review class
from customer import Customer
class TestRestaurantMethods(unittest.TestCase):

    def setUp(self):
        self.galitos = Restaurant('Galitos')

    def test_name(self):
        self.assertEqual(self.galitos.name(), 'Galitos')


    def test_average_star_rating_with_reviews(self):
        # Create some review instances
        Review.reviews = []  # Clear existing reviews
        
        good_review = Review("Joy Anyango", "Galitos", 9)
        bad_review = Review("Natasha Wanjira", "Galitos", 5)
        
        self.assertEqual(self.galitos.average_star_rating(), (9 + 5) / 2)
    
    def test_customers_with_reviews(self):
        Review.reviews = []  # Clear existing reviews
        
        good_review = Review("Joy Anyango", "Galitos", 9)
        bad_review = Review("Natasha Wanjira", "Galitos", 5)
        
        expected_customers = {"Joy Anyango", "Natasha Wanjira"}
        self.assertEqual(self.galitos.customers(), expected_customers)
    def test_reviews_with_matching_restaurant(self):
        # Create some review instances
        Review.reviews = []  # Clear existing reviews
        
        good_review = Review("Joy Anyango", "Galitos", 9)
        bad_review = Review("Natasha Wanjira", "Galitos", 5)
        other_review = Review("Some Customer", "KFC", 8)
        
        self.assertEqual(self.galitos.reviews(), [good_review, bad_review])

    def test_reviews_with_non_matching_restaurant(self):
        # Create some review instances
        Review.reviews = []  # Clear existing reviews
        
        good_review = Review("Joy Anyango", "KFC", 9)
        bad_review = Review("Natasha Wanjira", "KFC", 5)
        
        self.assertEqual(self.galitos.reviews(), [])
        
class TestCustomerMethods(unittest.TestCase):

    def setUp(self):
        self.joy = Customer("Joy", "Anyango")
        self.natasha = Customer("Natasha", "Wanjira")
        self.joy2 = Customer("Joy", "Anyango")
     
        
    def test_given_name(self):
        self.assertEqual(self.joy.given_name, "Joy")
        self.joy.given_name = "NewJoy"
        self.assertEqual(self.joy.given_name, "NewJoy")

    def test_family_name(self):
        self.assertEqual(self.joy.family_name, "Anyango")
        self.joy.family_name = "NewAnyango"
        self.assertEqual(self.joy.family_name, "NewAnyango")

    def test_full_name(self):
        self.assertEqual(self.joy.full_name(), "Joy Anyango")

    def test_find_all_by_given_name(self):
        # Test finding all customers by a given name
        all_joys = Customer.find_all_by_given_name("Joy")
        self.assertEqual(len(all_joys), 11)
        for customer in all_joys:
            self.assertEqual(customer.given_name, "Joy")

    
    def test_add_review(self):
        Review.reviews = []  # Clear existing reviews
        
        self.joy.add_review("KFC", 7)
        self.assertEqual(self.joy.num_reviews(), 1)
        self.assertEqual(len(Review.all()), 1)

    def test_find_by_name_existing(self):
        self.assertEqual(Customer.find_by_name("Joy Anyango"), self.joy)

    def test_find_by_name_non_existing(self):
        self.assertIsNone(Customer.find_by_name("John Doe"))

   
    def test_find_by_name_existing(self):
        found_customer = Customer.find_by_name("Joy Anyango")
        self.assertEqual(found_customer.given_name, "Joy")
        self.assertEqual(found_customer.family_name, "Anyango")
        
    def test_all_customers(self):
        # Create some customer instances
        customer1 = Customer("Alice", "Smith")
        customer2 = Customer("Bob", "Johnson")
        customer3 = Customer("Eve", "Brown")
        
        # Call the all class method
        all_customers = Customer.all()
        
        # Verify that all created customers are in the list
        self.assertIn(customer1, all_customers)
        self.assertIn(customer2, all_customers)
        self.assertIn(customer3, all_customers)    
        
class TestReviewMethods(unittest.TestCase):

    def setUp(self):
        self.good_review = Review("Joy Anyango", "Kfc", 9)
        self.bad_review = Review("Natasha Wanjira", "Galitos", 5)
        self.better_review = Review("Joy", "Java", 7)
        self.nice_review = Review("Joy Anyango", "Galitos", 9)
        self.invalid_rating_review = Review("Joy Anyango", "Galitos", "not_a_number")

    def test_rating(self):
        self.assertEqual(self.good_review.rating(), 9)
        self.assertEqual(self.bad_review.rating(), 5)
        self.assertEqual(self.better_review.rating(), 7)
        self.assertEqual(self.nice_review.rating(), 9)

    def test_customer(self):
        self.assertEqual(self.good_review.customer(), "Joy Anyango")
        self.assertEqual(self.bad_review.customer(), "Natasha Wanjira")
        self.assertEqual(self.better_review.customer(), "Joy")

    def test_restaurant(self):
        self.assertEqual(self.good_review.restaurant(), "Kfc")
        self.assertEqual(self.bad_review.restaurant(), "Galitos")
        self.assertEqual(self.better_review.restaurant(), "Java")

    def test_all(self):
        all_reviews = Review.all()
        self.assertIn(self.good_review, all_reviews)
        self.assertIn(self.bad_review, all_reviews)
        self.assertIn(self.better_review, all_reviews)
        self.assertIn(self.nice_review, all_reviews)

    # Add more test cases here for other methods if needed



if __name__ == '__main__':
    unittest.main()
