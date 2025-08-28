import sqlite3
# print(sqlite3.version_info)

print(sqlite3.sqlite_version)
try:
    conn = sqlite3.connect('studentInfo.db')

    cursor = conn.cursor() # connection execute

    print('Database connected !!!')

    cursor.execute("""
        create table if not exists students (
               id integer primary key autoincrement,
               name text not null,
               age integer,
               grade text 
               )    
    """)
    print('student table created !!!')

#   cursor.execute("""
#             insert into students(name,age,grade) 
#                    values ('Aditya', 21, 'B+')
#                    """)

# to avoid sql injection 

    cursor.execute("insert into students (name,age,grade) values (?,?,?)",('Ram', 24,'C+'))

    conn.commit()
    print('Data added successfully')

#   cursor.execute('update students set name= ? where id=?',('AdityaG', 3))

#   conn.commit()


    cursor.execute('delete from students where id=?',(3,))
    conn.commit()

    cursor.execute("""
               select * from students
               """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as err:
    print("database error",err)
    
finally:
    conn.close()


