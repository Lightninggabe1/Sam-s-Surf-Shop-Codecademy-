import unittest
import surfshop
import datetime

class SurfShopTests(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    # old version without parameterization
    # def test_add_surfboards(self):
    #     message = self.cart.add_surfboards(2)
    #     self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
    #     self.cart = surfshop.ShoppingCart()

    @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    # commented out - test should not fail at the end of project
    #@unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

   

unittest.main()
