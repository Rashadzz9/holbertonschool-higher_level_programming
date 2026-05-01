#!/usr/bin/python3
"""This code defines width and height"""

class Rectangle:
    """Defines a  this file is a class"""

    def __init__(self, width=0, height=0):
       """Define edirik hight ve width onlari tanidirig"""
       self.width = width
       sefl.height = height

    @property
    def width(self):
        """width deyerini __ olarag retireve"""
        return self.__width

    @width.setter
    def width(self, value):
        """errorlari basa salacayig ki bunu ver"""
        if not isinstance(value, int):
           raise TypeError("width must be an integer")
        if value < 0:
           raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """eyni qayda ile height edirik"""
        return self.__height

    @height.setter
    def height(self, value):
        """burada ise errorlari veririk"""
        if not isinstance(value, int):
           raise TypeError("height must be an integer")
        if value < 0:
           raise ValueError("height must be >= 0")
           self.height = value
