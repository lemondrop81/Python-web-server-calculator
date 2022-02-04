"""
    Assignment WebApp
    Date: Febuary 2 2022
    Description: A simple MyMath program
"""

import app


class MyMath():
    """Contains math functions"""

    def __init__(self, number):
        """Class constructor"""
        self.number = number

    def standard_deviation(self, number):
        """Returns the standard deviation of a list of numbers."""
        suma = 0
        for counter in number:
            suma += ((counter - sum(number) / len(number)) ** 2)
        return (suma/(len(number) - 1)) ** 0.5

    def largest(self, number):
        """Returns the largest number in the list."""
        largest = max(number)
        return largest

    def avg(self, number):
        """Returns the average of a list of numbers."""
        suma = 0
        for num in number:
            suma += num
        avg = suma / len(number)
        return avg

    def print(self, nums):
        """Prints the results."""
        print(f"Standard deviation of nums: {math.standard_deviation(nums)}, " +
              f"the average of nums: {math.avg(nums)}")

NUMBER = 0
NUMS = []


math = MyMath(1)
