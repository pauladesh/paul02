from teacher import Teacher
class Student(Teacher):
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
s=Student()
s.setid(10325)
s.setname('Adesh')
s.setaddress('325/6, street number 65, Hari Nagar, New Delhi - 10065')
s.setmarks(400)

print('Your ID is, ',s.getid())
print('Hi, ',s.getname())
print('You stay at ',s.getaddress())
print('Your marks are ',s.getmarks())
