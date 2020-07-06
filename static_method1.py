class Myclass:
    @staticmethod
    def mymethod(x,n):
        result=x**n
        print('{} raised to power {} is {}'.format(x,n,result))
Myclass.mymethod(4,1)
Myclass.mymethod(2,1)
