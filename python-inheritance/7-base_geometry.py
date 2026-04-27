#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry
"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        - name is always a string
        - if value is not an integer: raise a TypeError
        - if value is less or equal to 0: raise a ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
