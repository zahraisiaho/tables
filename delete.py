import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully connected to the database")
conn.execute('DELETE from Company1 where ID=4')
conn.commit()
data=conn.execute("SELECT*FROM Company1")
for rows in data:
    print("ID:", rows[0])
    print("Firstname:", rows[1])
    print("Lastname:", rows[2])
    print("Age:", rows[3])
    print("Salary:", rows[4])
    print("Task:", rows[5])

print("successfully removed 1 row")
conn.close()