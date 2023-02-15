#!:/usr/bin/python3

from .test_base import TestBase
from models.rectangle import Rectangle


class TestRectangle(TestBase):
    @classmethod
    def setUpClass(self, class_name=Rectangle):
        return super().setUpClass(class_name)