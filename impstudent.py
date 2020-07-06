from Student import Student

s=Student()
s.setid(10)
s.setname('Paul')
s.setaddress('478/5, street number 46, Sadh Nagar, New Delhi - 10045')
s.setmarks(900)

print('Your ID is, ',s.getid())
print('Hi, ',s.getname())
print('You stay at ',s.getaddress())
print('Your marks are ',s.getmarks())
