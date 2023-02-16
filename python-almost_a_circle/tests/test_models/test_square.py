import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 4, 3, 8)
        expected_output = {'id': 8, 'size': 5, 'x': 4, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_output)

        """s = Square(5, 0, 0, 8)
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


"""