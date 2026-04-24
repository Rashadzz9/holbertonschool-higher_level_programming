#!/usr/bin/python3
"""burada 4 deded diyes print"""


def print_square(size):
    """funksiya yaziyoruze"""
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
