class Account:
    def __init__(self,other):
        other=other.split(', ')
        self.number=int(other[0])
        self.name=other[1]
        self.balance=int(other[2])
    def __str__(self,):
        return f'{self.number}, {self.name}, {self.balance}'
class Bank:
    def __init__(self):
        self.f_name='accounts.txt'
        try:
            with open(self.f_name) as file:
                self.ac_nu=Account(file.readlines()[-1]).number
        except:self.ac_nu=0
    def create_account(self,name,initial_deposit):
        if not isinstance(initial_deposit,int) or initial_deposit<0:
                    raise ValueError('Enter only digits and higher than 0')
        with open(self.f_name,'a') as file:
            self.ac_nu+=1
            print(f'Your account number is: {self.ac_nu}')
            other=f'{self.ac_nu}, {name}, {initial_deposit}'
            file.write(str(Account(other))+'\n')
    def view_account(self,account_number):
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
            for i in records:
                emp=Account(i)
                if emp.number==account_number:
                    print('Account Found:')
                    print(emp)
                    f=0
                    break
        if f:
            print('Account Not Found\n')
        return 
    def deposit(self,account_number: str,amount: int):
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
        with open(self.f_name,'w') as file:
            for i in records:
                det=Account(i)
                if not isinstance(amount,int) or amount<0:
                    raise ValueError('Enter only digits and higher than 0')
                if det.number==account_number:
                    ne_balance=det.balance+amount
                    file.write(f'{account_number}, {det.name}, {ne_balance}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Account Not Found\n')
    def withdraw(self,account_number,amount):
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
        with open(self.f_name,'w') as file:
            for i in records:
                det=Account(i)
                if not isinstance(amount,int) or amount>det.balance:
                    raise ValueError('Enter only digits and enough money to withdraw')
                if det.number==account_number:
                    ne_balance=max(0,det.balance-amount)
                    file.write(f'{account_number}, {det.name}, {ne_balance}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Account Not Found\n')


