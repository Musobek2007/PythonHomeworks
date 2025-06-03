def ad(a):
    with open('employees.txt','a') as txt:
        txt.write(a)
        txt.write('\n')

def vi():
    txt=open('employees.txt')
    print(txt.read())

def se(e_id):
    txt=open('employees.txt')
    employees=txt.readlines()
    g='There is not an employee with this ID '+ e_id
    for i in employees:
        details=i.split()
        if details[0]==e_id:
            g=str(i)
            break
    txt.close()
    return g

def edit(e_id,re):
    t=se(e_id)
    with open('employees.txt') as txt:
        p=txt.read()
        p=p.replace(t[:-1],' '.join(re),1)
    with open('employees.txt','w') as txt:
        txt.write(p)

ID=[]
with open('employees.txt') as lis:
    for i in lis:
        de=i.split()
        if len(de)>0:
            ID.append(de[0])
while True:
    print('''1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit''')
    a=input('Enter the number you want to choose: ')
    if a=='1':
        print('Enter new employee record like this')
        print('Employee ID, Name, Position, Salary')
        record=input().split(', ')
        if record[0] not in ID:
            ID.append(record[0])
            ad(' '.join(record))
        else:
            print('Enter new employee with different ID that is not included in this list')
            print(*ID)
            record=input().split(', ')
            ad(' '.join(record))
    elif a=='2':
        print()
        vi()
    elif a=='3':
        e_id=input('Enter employee ID you want to see: ')
        print()
        print(se(e_id))
    elif a=='4':
        n_id=input('Enter employee ID you want to change: ')
        print('Enter new employee record like this')
        print('Employee ID, Name, Position, Salary')
        re=input().split(', ')
        edit(n_id,re)
    elif a=='5':
        d_id=input('Enter employee ID that you want to delete: ')
        edit(d_id,'')
    elif a=='6':
        exit()
    else:
        print('hatolik yuz berdi')
    with open('employees.txt','r') as file:
        li=file.readlines()

    l=[i for i in li if i.strip()!='']
    with open('employees.txt','w') as file:
        file.writelines(l)