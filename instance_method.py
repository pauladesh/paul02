class Student:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    def display(self):
        print('Hi, ',self.name)
        print('Your marks are ',self.marks)
    def calculate(self):
        if self.marks>=800:
            print('First division')
        elif self.marks>=600:
            print('Second division')
        elif self.marks>=400:
            print('Third division')
        else:
            print('Fail')

i=0
n=int(input('Enter the number of students: '))
while i<n:
    name=input('Name: ')
    marks=int(input('Your marks:'))
    s=Student(name, marks)
    s.display()
    s.calculate()
    print('-----------------------')
    i+=1
