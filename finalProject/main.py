import sqlite3

conn = sqlite3.connect('todolist.db')
curser = conn.cursor()
curser.execute(""" 
                create table if not exists tasktable (
                   id integer primary key autoincrement,
                   taskname text not null,
                   iscomplete integer default 0)
                    """)
print("Table created successfully")

def addTask(task):
    curser.execute('insert into tasktable (taskname) values (?)', (task,))
    conn.commit()
    print("Task added successfully")

def showTasks():
    rows = curser.execute('select * from tasktable')
    for row in rows:
        status = 'Complete' if row[2] else 'notComplete' 
        print(f'{row[0]}.   {row[1]}  [{status}]')
    
def menu():
    while(True):
        print('📋 To-Do List Menu:')
        print('1. Add Task')
        print('2. View Tasks')
        print('10. Exit')

        choice = input('Enter Choice : ')
        if choice == '1':
            t = input("Enter task name : ")
            addTask(t)
        elif choice == '2':
            showTasks()
        else:
            print('👋 Goodbye!')
            break
menu()

conn.close()



