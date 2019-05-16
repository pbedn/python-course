import unittest


from .solutions import *


class TestCase(unittest.TestCase):
    def test_h1(self):
        self.assertEqual(h1().Albania.name, 'Albania')
        self.assertEqual(h1().Albania.value, 355)
        with self.assertRaises(AttributeError):
            h1().Poland

    def test_h2(self):
        test_data = [("Afghanistan", 93),
                                ("Albania", 355),
                                ("Algeria", 213),
                                ("Andorra", 376),
                                ("Angola", 244),
                                ("Antarctica", 672)]
        for test_input, expected in test_data:
            self.assertEqual(h2(), expected)


if __name__ == '__main__':
    unittest.main()
