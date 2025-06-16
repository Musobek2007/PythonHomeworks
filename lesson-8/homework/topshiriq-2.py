class Account:
    def __init__(self,other):
        other=other.split(', ')
        self.number=other[0]
        self.name=other[1]
        self.balance=int(other[2])
    def __str__(self,):
        return f'{self.number}, {self.name}, {self.balance}'
class Bank:
    def __init__(self):
        self.f_name='accounts.txt'
        with open(self.f_name) as file:
            self.ac_nu=Account(file.readlines()[-1]).number
    def create_account(self):
        with open(self.f_name,'a') as file:
            self.name=input('Enter your name: ')
            self.initial=input('Enter initial_deposit: ')
            self.ac_nu+=1
            print(f'Your account number is: {self.ac_nu}')
            other=f'{self.ac_nu}, {self.name}, {self.initial}'
            file.write(str(Account(other))+'\n')
    def view_account(self):
        emp_id=input('Enter account number to view: ')
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
            for i in records:
                emp=Account(i)
                if emp.number==emp_id:
                    print('Account Found:')
                    print(emp)
                    f=0
                    break
        if f:
            print('Account Not Found\n')
        return 
    def deposit(self):
        new_id=input('Enter account_number to deposit: ')
        new_de=int(input('Enter money how much you want to deposit: '))
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
        with open(self.f_name,'w') as file:
            for i in records:
                det=Account(i)
                if det.number==new_id:
                    ne_balance=det.balance+new_de
                    file.write(f'{new_id}, {det.name}, {ne_balance}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Account Not Found\n')
    def withdraw(self):
        new_id=input('Enter account_number to deposit: ')
        new_de=int(input('Enter money how much you want to withdraw: '))
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
        with open(self.f_name,'w') as file:
            for i in records:
                det=Account(i)
                if det.number==new_id:
                    ne_balance=max(0,det.balance-new_de)
                    file.write(f'{new_id}, {det.name}, {ne_balance}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Account Not Found\n')
    def exi(self):
        exit(print('Goodbye!\n'))
print('''1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit\n''')
manag=Bank()
while True:
    cho=input('Enter your choice: ')
    if cho=='1':
        manag.add()
    elif cho=='2':
        manag.view()
    elif cho=='3':
     manag.update()
    elif cho=='4':
        manag.delete()
    elif cho=='5':
        manag.filter()
    elif cho=='6':
        print('Tasks saved')
    elif cho=='7':
        print('Tasks loaded')
    elif cho=='8':
        manag.exi()