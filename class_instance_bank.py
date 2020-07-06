import sys
class Bank(object):
    """Bank vali class hai ye"""

    def __init__(self, name, balance=0.0):
            self.name=name
            self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print('Balance amount is less, so no withdrawl')
        else:
            self.balance-=amount
            return self.balance
name=input('Your name please: ')
b=Bank(name)
while(True):
    print('D- deposit, W- withdraw, e or E - exit')
    choice=input('your choice: ')
    if choice=='e' or choice=='E':
        sys.exit()
    amt=float(input('Enter amount: '))

    if choice=='d' or choice=='D':
        print('Balance after deposit ',b.deposit(amt))
    if choice=='w' or choice =='W':
        print('Balance after deposit ',b.withdraw(amt))
