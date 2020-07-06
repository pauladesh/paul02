class Student:
    def __init__(self,n=' ',m=0):
        self.name=n
        self.marks=m

    def display(self):
        print('Hi, ',self.name)
        print('Your marks are ',self.marks)







s = Student()
s.display()
print('_________________________')





s1 = Student('Lakshmi Ray',800)
s1.display()
