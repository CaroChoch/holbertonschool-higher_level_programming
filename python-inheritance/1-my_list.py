#!/usr/bin/python3
""" MyList Class that inherits from list """


class MyList(list):
    """
    MyList Class that inherits from list:
    - ``print_sorted(self)``: Prints the list, but sorted (ascending sort).
    """
    def print_sorted(self):
        """
        public instance method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
