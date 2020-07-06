class Myclass:
    n=0
    def __init__(self):
        Myclass.n=Myclass.n+1

    @staticmethod
    def noObject():
        print('Number of instances are ',Myclass.n)

obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
askjdfh=Myclass()
Myclass.noObject()
