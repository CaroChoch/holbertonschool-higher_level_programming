import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 4, 3, 8)
        expected_output = {'id': 8, 'size': 5, 'x': 4, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_output)

        s = Square(5, 0, 0, 8)
        expected_output = {'id': 8, 'size': 5, 'x': 0, 'y': 0}
        self.assertDictEqual(s.to_dictionary(), expected_output)

        s = Square(7, 7, 7, 7)
        expected_output = {'id': 7, 'size': 7, 'x': 7, 'y': 7}
        self.assertDictEqual(s.to_dictionary(), expected_output)

    def test_getter(self):
        s = Square(9)
        self.assertEqual(s.size, 9)
    
    def test_setter(self):
        s = Square(9)
        s.size = 10
        self.assertEqual(s.size, 10)
    
    def test_str(self):
        s = Square(4)
        with self.assertRaises(TypeError):
            s.size = "Caro"

    def test_zero(self):
        s = Square(4)
        with self.assertRaises(ValueError):
            s.size = 0

    def test_zero(self):
        s = Square(4)
        with self.assertRaises(TypeError):
            s.size = 2.5

    def test_neg(self):
        s = Square(4)
        with self.assertRaises(ValueError):
            s.size = -3
            
