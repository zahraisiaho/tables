import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully connected to the database")

conn.execute("update Company1 set salary=50000.00 where ID=1")
conn.commit()
data = conn.execute("SELECT*FROM Company1")
for rows in data:
    print("ID:", rows[0])
    print("firstname:", rows[1])
    print("Lastname:", rows[2])
    print("Age:", rows[3])
    print("Salary:", rows[4])
    print("Task:", rows[5])
conn.close()


