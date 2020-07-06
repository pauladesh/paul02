#A python program to create a Dob class within a person class.
class Baap:
    def __init__(self):
        self.name='Adesh'
        self.db=self.Dob()
    def display(self):
        print('Aur {} bhai kya haal hai?'.format(self.name))
    class Dob:
        def __init__(self):
            self.dd=22
            self.mm='Aug'
            self.yy=1994
        def display(self):
            print('Teri date of birth hai {}-{}-{}'.format(self.dd,self.mm,self.yy))
s=Baap()
s.display()
b=s.db
b.display()
a
