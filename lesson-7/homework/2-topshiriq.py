class Employee:
    def __init__(self,other):
        other=other.split(', ')
        self.employee_id=other[0]
        self.name=other[1]
        self.position=other[2]
        self.salary=other[3]
    def __str__(self,):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'
class EmployeeManager:
    def add(self):
        with open('employees.txt','a') as file:
            self.employee_id=input('Enter Employee ID: ')
            self.name=input('Enter Name: ')
            self.position=input('Enter Position: ')
            self.salary=input('Enter Salary: ')
            print('Employee added successfully!\n')
            other=f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'
            file.write(str(Employee(other))+'\n')
    def view(self):
        with open('employees.txt') as file:
            records=file.read()
            print('Employee Records:')
            print(records)
        return
    def search(self):
        emp_id=input('Enter Employee ID to search: ')
        f=1
        with open('employees.txt') as file:
            records=file.readlines()
            for i in records:
                emp=Employee(i)
                if emp.employee_id==emp_id:
                    print('Employee Found:')
                    print(emp)
                    f=0
                    break
        if f:
            print('Employee Not Found\n')
        return 
    def update(self):
        new_id=input('Enter Employee ID to change: ')
        f=1
        with open('employees.txt') as file:
            records=file.readlines()
        new_rec=[]
        ne_name=input('Enter new name:')
        ne_position=input('Enter new position:')
        ne_salary=input('Enter new salary:')
        with open('employees.txt','w') as file:
            for i in records:
                det=Employee(i)
                if det.employee_id==new_id:
                    print('Employee\'s informations successfully updated\n')
                    file.write(f'{new_id}, {ne_name}, {ne_position}, {ne_salary}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Employee Not Found\n')
    def delete(self):
        re_id=input('Enter Employee ID to delete: ')
        with open('employees.txt') as file:
            records=file.readlines()
        with open('employees.txt','w') as file:
            for i in records:
                det=Employee(i)
                if det.employee_id!=re_id:
                    file.write(i)
        print()
        return 
    def exi(self):
        exit(print('Goodbye!\n'))
print('''Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit\n''')
manag=EmployeeManager()
while True:
    cho=input('Enter your choice: ')
    if cho=='1':
        manag.add()
    elif cho=='2':
        manag.view()
    elif cho=='3':
        manag.search()
    elif cho=='4':
        manag.update()
    elif cho=='5':
        manag.delete()
    elif cho=='6':
        manag.exi()