#To access the base class constructor from sub class
class Father:
    def __init__(self):
        self.pro=80000
    def display(self):
        print('Father\'s property is {}'.format(self.pro))
class Son(Father):
    pass
s=Son()
s.display()
