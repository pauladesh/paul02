#A python program to create Emp class and make all the members of the Emp class available to another class, i.e. Myclass 
class Emp:
    def __init__(self, id,name, salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print('ID=> ',self.id)
        print('Name => ',self.name)
        print('salary => ',self.salary)

class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()
e=Emp(10,'Adesh',12000)
Myclass.mymethod(e)
