class Father:
    def __init__(self):
        self.property=80000
    def display(self):
        print('Father\'s property is {}'.format(self.property))
class Son(Father):
    def __init__(self):
        self.property=20000
    def display(self):
        print('Son\'s property is {}'.format(self.property))
s=Son()
s.display()
