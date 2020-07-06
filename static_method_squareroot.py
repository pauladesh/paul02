#A python program to create a static method that caculates the square root value of a given number.
import math
class Src:
    """Src stands for square root class"""
    @staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result

num=float(input('Enter the number: '))
rel=Src.calculate(num)
print('The square root of {} is {:.2f}'.format(num,rel))
