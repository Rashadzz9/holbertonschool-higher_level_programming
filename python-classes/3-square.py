#!/usr/bin/python3
class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initializes a new  suqare with arrow"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
