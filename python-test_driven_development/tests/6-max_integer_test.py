""" Unittest for ``max_integer`` function """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_int(self):
        self.assertEquals(max_integer([1, 3, 9]), 9)
        self.assertEquals(max_integer([23, 2, 0]), 23)
        self.assertEquals(max_integer([23, 56, 10]), 56)

    def test_negative(self):
        self.assertEquals(max_integer([-6, -3, -1]), -1)
        self.assertEquals(max_integer([-6, -3, 0]), 0)
        self.assertEquals(max_integer([-6, 10, -1]), 10)

    def test_float(self):
        self.assertEquals(max_integer([-6, -3.7, 14.8, 14.9, 14.1982]), 14.9)

    def test_char(self):
        self.assertEquals(max_integer(["b", "n", "z", "a"]), "z")

    def test_mix_types(self):
        with self.assertRaises(TypeError):
            max_integer([-6, -3, "g"])

    def test_one_element(self):
        self.assertEquals(max_integer([19]), 19)

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
