
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartLimit(unittest.TestCase):
    def test_add_dvd_full(self):
        cart = Cart()

        for i in range(20):
            self.assertTrue(
                cart.add_dvd(DigitalVideoDisc(f"DVD {i}"))
            )

        self.assertFalse(
            cart.add_dvd(DigitalVideoDisc("DVD 21"))
        )


class TestCartDiscount(unittest.TestCase):
    def test_discount_calculation(self):
        cart = Cart()
        dvd = DigitalVideoDisc("The Lion King")
        dvd.cost = 100.0

        cart.add_dvd(dvd)

        self.assertAlmostEqual(
            cart.total_cost_with_discount(20), 80.0
        )

    def test_invalid_discount_percent(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
