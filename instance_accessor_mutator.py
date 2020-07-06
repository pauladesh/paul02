#A python program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.
class Student:
    def setName(self,name):   #mutator method
        self.name=name

    def getName(self):    #accessor method
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks
n=int(input('How many students: '))
i=0

while i<n:
    s=Student()
    name=input('Enter your name: ')
    s.setName(name)
    marks=int(input('Enter your marks: '))
    s.setMarks(marks)
    print('Hi, ',s.getName())
    print('your marks are: ',s.getMarks())

    i+=1
    print('-----------------------------')
