class Task:
    def __init__(self,other):
        other=other.split(', ')
        self.task_id=other[0]
        self.title=other[1]
        self.description=other[2]
        self.due_date=other[3]
        self.status=other[4]
    def __str__(self,):
        return f'{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}'
class TaskManager:
    def __init__(self):
        self.f_name='task.txt'
    def add(self):
        with open(self.f_name,'a') as file:
            self.task_id=input('Enter Task ID: ')
            self.title=input('Enter Title: ')
            self.description=input('Enter Description: ')
            self.due_date=input('Enter Due Date (YYYY-MM-DD): ')
            self.status=input('Enter Status (Pending/In Progress/Completed): ')
            print('Task added successfully!\n')
            other=f'{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}'
            file.write(str(Task(other))+'\n')
    def view(self):
        with open(self.f_name) as file:
            print('Tasks:')
            print(file.read())
        return
    def update(self):
        new_id=input('Enter Task ID to change: ')
        f=1
        with open(self.f_name) as file:
            records=file.readlines()
        ne_title=input('Enter new title:')
        ne_description=input('Enter new description:')
        ne_due_date=input('Enter new due date:')
        ne_status=input('Enter new status: ')
        with open(self.f_name,'w') as file:
            for i in records:
                det=Task(i)
                if det.task_id==new_id:
                    print('Task\'s informations successfully updated\n')
                    file.write(f'{new_id}, {ne_title}, {ne_description}, {ne_due_date}, {ne_status}\n')
                    f=0
                else:
                    file.write(i)
        if f:
            print('Task Not Found\n')
    def delete(self):
        re_id=input('Enter Task ID to delete: ')
        with open(self.f_name) as file:
            records=file.readlines()
        with open(self.f_name,'w') as file:
            for i in records:
                det=Task(i)
                if det.task_id!=re_id:
                    file.write(i)
        print()
        return 
    def filter(self):
        with open(self.f_name) as file:
            ta=file.readlines()
        sta=['In Progress\n','Completed\n']
        ta.sort(key=lambda x:sta.index(Task(x).status))
        for i in ta:print(i)
        return
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
manag=TaskManager()
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