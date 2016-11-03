import unittest
from basket import Basket
import numbers

class BasketTests(unittest.TestCase):
    
    # setup method to create objects
    def setUp(self):
        print("setting up")
        self.keijon_ostoskori = Basket("Keijo", ["kissa", "koira"], 20)
    
    # tear down method
    def tearDown(self):
        print("Tearing down")
        del self.keijon_ostoskori

    # test if variable customer is a string
    def test_customer_is_string(self):
        self.assertIsInstance(self.keijon_ostoskori.customer, list, "variable customer is not a string")

    # test if variable contents is a list
    def test_contents_are_list(self):
        self.assertIsInstance(self.keijon_ostoskori.contents, list, "variable content is not a list")

    # test if variable price is a number
    def test_price_is_number(self):
        self.assertIsInstance(self.keijon_ostoskori.price, numbers.Number, "variable price is not a number")

    # test if add_product method adds a product to the list
    def test_can_add_product(self):
        self.keijon_ostoskori.add_product("kala", 5)
        self.assertIn("kala", self.keijon_ostoskori.contents, "add_product did not add new item")

    # test of delete_product method deletes a product
    def test_can_delete_product(self):
        self.keijon_ostoskori.delete_product("koira", 20)
        self.assertNotIn("Pasi", self.keijon_ostoskori.contents, "delete_product did not delete item")

if __name__ == '__main__':
    unittest.main()
