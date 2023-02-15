#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
   def test_instance(self):
        """ Test instantiation """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(89).id, 89)
        self.assertEqual(Base('a').id, 'a')
        #self.assertEqual(Base("abc".id, "abc"))
        #self.assertEqual(Base(None).id, None)
        

if __name__ == '__main__':
    unittest.main()
