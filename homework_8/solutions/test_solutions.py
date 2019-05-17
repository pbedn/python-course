import unittest


from .solutions import *


class TestCase(unittest.TestCase):
    def test_h1(self):
        self.assertEqual(h1().Albania.name, 'Albania')
        self.assertEqual(h1().Albania.value, 355)
        with self.assertRaises(AttributeError):
            h1().Poland

    def test_h2(self):
        expected = [("Afghanistan", 93),
                    ("Albania", 355),
                    ("Algeria", 213),
                    ("Andorra", 376),
                    ("Angola", 244),
                    ("Antarctica", 672)]
        for i, (name, value) in enumerate(h2()):
            self.assertEqual((name, value), expected[i])

    def test_h3(self):
        expected = [
                    "Afghanistan",
                    "Algeria",
                    "Angola",
                    "Albania",
                    "Andorra",
                    "Antarctica"]
        for i, name in enumerate(h3()):
            self.assertEqual(name, expected[i])

    def test_h4(self):
        expected = [93, 355, 213, 376, 244, 672]
        for i, value in enumerate(h4()):
            self.assertEqual(value, expected[i])

    def test_h5(self):
        test_input = [
           'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
           'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
           'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
           'white', 'orange', "orange", 'red'
        ]
        expected = [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]

        self.assertEqual(h5(test_input), expected)

    def test_h6(self):
        test_input = (
            ('V', 1),
            ('VI', 1),
            ('V', 2),
            ('VI', 2),
            ('VI', 3),
            ('VII', 1),
        )
        expected = {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]}
        self.assertEqual(h6(test_input), expected)

    def test_h7(self):
        test_input = (
            ('V', 1),
            ('VI', 1),
            ('V', 2),
            ('VI', 2),
            ('VI', 3),
            ('VII', 1),
        )
        expected = {'VI': 3, 'V': 2, 'VII': 1}
        self.assertEqual(h7(test_input), expected)

    def test_h8(self):
        expected = [("Afghanistan", 93),
                    ("Albania", 355),
                    ("Algeria", 213),
                    ("Andorra", 376),
                    ("Angola", 244)]
        for i, (name, value) in enumerate(h8()):
            self.assertEqual((name, value), expected[i])

    def test_h9(self):
        test_input = {'Afghanistan': 93,
                      'Albania': 355,
                      'Algeria': 213,
                      'Andorra': 376,
                      'Angola': 244}
        expected = [("Afghanistan", 93),
                    ("Albania", 355),
                    ("Algeria", 213),
                    ("Andorra", 376),
                    ("Angola", 244)]
        expected_rev = [("Angola", 244),
                        ("Andorra", 376),
                        ("Algeria", 213),
                        ("Albania", 355),
                        ("Afghanistan", 93)]
        for i, val in enumerate(h9(test_input)):
            self.assertEqual(val, expected[i])
        for i, val in enumerate(h9(test_input, reverse=True)):
            self.assertEqual(val, expected_rev[i])

    def test_h10(self):
        test_input = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
        expected = [('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
        self.assertEqual(h10(test_input), expected)

    def test_h11(self):
        test_input = ([2, 1, 3, 4, 5], [2, 1, 3, 5, 4])
        expected = False
        self.assertEqual(h11(*test_input), expected)

    def test_h12(self):
        test_input = [10, 20, 30, 40, 50]
        expected = [10, 20, 30, 40, 50]
        for i, val in enumerate(h12(test_input)):
            self.assertEqual(val, expected[i])

    def test_h13(self):
        test_input = (12.236, 36.36)
        expected = 4
        self.assertEqual(h13(test_input), expected)
        test_input = (12, 25)
        expected = 4
        self.assertEqual(h13(test_input), expected)

    def test_h14(self):
        test_input = (12, 25)
        expected = 2
        self.assertEqual(len(h14(test_input)), expected)

    def test_h15(self):
        test_input = [10, 20, 30, 40, 50]
        expected = 5
        self.assertEqual(h15(test_input), expected)

    def test_h16(self):
        test_input = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(h16(test_input), expected)

    def test_h17(self):
        test_input = [1, 2, 3, 4, 5, 6]
        expected = b'010000000200000003000000040000000500000006000000'
        self.assertEqual(h17(test_input), expected)

    def test_h18(self):
        test_input = [7, 8, 9, 10]
        expected = ["array1: array('i', [7, 8, 9, 10])",
                    "Bytes: b'0700000008000000090000000a000000'",
                    "array2: array('i', [7, 8, 9, 10])"]
        self.assertEqual(h18(test_input), expected)

    def test_h19(self):
        test_input = (('V', 1),
                      ('V', 3),
                      ('V', 2))
        expected = [('V', 1),
                    ('V', 3),
                    ('V', 2)]
        self.assertEqual(h19(test_input), expected)

    def test_h20(self):
        test_input = (('V', 1),
                      ('V', 3),
                      ('V', 2))
        expected = [('V', 2),
                    ('V', 3)]
        self.assertEqual(h20(test_input), expected)

    def test_h21(self):
        test_input = (('V', 1),
                      ('V', 3),
                      ('V', 2))
        expected = [('V', 2),
                    ('V', 3),
                    ('V', 6)]
        self.assertEqual(h21(test_input), expected)

    def test_h22(self):
        test_input = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
        expected = [10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
        self.assertEqual(h22(test_input), expected)

    def test_h23(self):
        test_input = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
        expected = [100, 90], [10, 20, 20]
        self.assertEqual(h23(test_input), expected)

    def test_h24(self):
        test_input = [1, 2, 4, 5], 6
        expected = 4
        self.assertEqual(h24(*test_input), expected)
        test_input = [1, 2, 4, 5], 3
        expected = 2
        self.assertEqual(h24(*test_input), expected)

    def test_h25(self):
        test_input = [1, 2, 4, 7], 6
        expected = 3
        self.assertEqual(h25(*test_input), expected)
        test_input = [1, 2, 4, 7], 3
        expected = 2
        self.assertEqual(h25(*test_input), expected)

    def test_h26(self):
        test_input = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
        expected = [14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
        self.assertEqual(h26(test_input), expected)

    def test_h27(self):
        test_input = 4
        expected = [0, 1, 2, 3], 4
        self.assertEqual(h27(test_input), expected)

    def test_h28(self):
        test_input = 4
        expected = True, False
        self.assertEqual(h28(test_input), expected)

    def test_h29(self):
        test_input = 4
        expected = ['0', '1', '2', '3']
        self.assertEqual(h29(test_input), expected)

    def test_h30(self):
        test_input = 4
        expected = ['3', '2', '1', '0']
        self.assertEqual(h30(test_input), expected)


if __name__ == '__main__':
    unittest.main()
