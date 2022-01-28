import app

class MyMath():
    """Contains math functions"""

    def __init__(self, number):
        """Class constructor"""
        self.number = number

    def standardDeviation(self, number):
        """Returns the standard deviation of a list of numbers."""
        suma = 0
        for x in number:
            suma += ((x - sum(number)/len(number))**2)
        return (suma/(len(number)-1)) **0.5

    def avg(self, number):
        """Returns the average of a list of numbers."""
        sum = 0
        for num in number:
            sum += num
        avg = sum / len(number)
        
        return avg

    def print(self, nums):
        print(f"Standard deviation of nums: {math.standardDeviation(nums)}, the average of nums: {math.avg(nums)}")

number = 0
nums = []


math = MyMath(1)



