#!/usr/bin/python3

def print_last_digit(number):
    """Prints and returns the last digit of a number."""
    # Calculate the last digit by taking the absolute value first
    last_digit = abs(number) % 10
    # Print the digit using string format, no newline
    print("{}".format(last_digit), end="")
    # Return the value of the last digit
    return last_digit
