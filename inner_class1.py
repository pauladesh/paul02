class Person:
    def __init__(self):
        self.name='Paul'
    def display(self):
        print('Hi, ',self.name)
    class Dob:
        def __init__(self):
            self.dd=29
            self.mm='Sep'
            self.yy=1995
        def display(self):
            print('Your D.o.B is {}-{}-{}'.format(self.dd,self.mm,self.yy))
s=Person()
s.display()
b=Person().Dob()
b.display()
