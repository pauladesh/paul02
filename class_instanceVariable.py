class Sample:
    def __init__(self):
        self.x=11



    def modify(self):
        self.x+=1






s1=Sample()
s2=Sample()
print('x in s1 =',s1.x)
print('x in s2 =',s2.x)
s1.modify()
print('x in s1 =',s1.x)
print('x in s2 =',s2.x)
