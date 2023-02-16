import unittest
import json
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base
import os


class test_rectangle(unittest.TestCase):

    def test_rectangle_instance(self):
        """Test if rectangle instance is created successfully"""
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Base)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, rect._Base__nb_objects)

    def test_rectangle_str_width(self):
        """Test that passing a string as width raises a TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_Rectangle_negative_or_zero_args(self):
        """
        Test if creating Rectangle instance with negative
        or zero args raises ValueError
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        """Test that the area method exists"""
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_str_output(self):
        """Test that str method returns the expected string representation"""
        r = Rectangle(3, 4, 2, 1, 10)
        expected_output = "[Rectangle] (10) 2/1 - 3/4"
        self.assertEqual(str(r), expected_output)

    def test_display_without_x_y(self):
        """
        Test that the display method outputs the correct
        representation of a rectangle
        """
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_display(self):
        """Test rectangle display exists"""
        r = Rectangle(2, 2, 2, 2)
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            self.assertEqual(buffer.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """Test Rectangle to_dictionary"""
        r = Rectangle(2, 5, 4, 1, 7)
        expected_output = {'id': 7, 'width': 2, 'height': 5, 'x': 4, 'y': 1}
        self.assertDictEqual(r.to_dictionary(), expected_output)

    def test_update(self):
        """ Test update method with arbitrary number of arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_args_1(self):
        """ Test update method with one argument """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args_2(self):
        """ Test update method with two arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_args_3(self):
        """ Test update method with three arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_args_4(self):
        """ Test update method with four arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args_5(self):
        """ Test update method with five arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_create(self):
        rect = Rectangle(10, 9, 8, 7, 6)
        rect_dictionary = rect.to_dictionary()
        second_rect = Rectangle.create(**rect_dictionary)
        self.assertEqual(second_rect.id, 6)

    def test_save_to_file_None(self):
        """Test Rectangle save_to_file method with None as argument"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file(self):
        """ test save file """
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_save_to_file_empty(self):
        """ save empty file """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_load_from_file_no_file(self):
        """ Try to load unexistented file """
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """ Checks load file """
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect2 = Rectangle(6, 7, 8, 9, 10)
        li = [rect1, rect2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1 = lo[0]
        r2 = lo[1]
        self.assertTrue(type(r1) is Rectangle)
        self.assertTrue(type(r2) is Rectangle)
        self.assertEqual(str(rect1), str(r1))
        self.assertEqual(str(rect2), str(r2))
        self.assertIsNot(rect1, r1)
        self.assertIsNot(rect2, r2)
        self.assertNotEqual(rect1, r1)
        self.assertNotEqual(rect2, r2)