import sqlite3

conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company1(ID, firstname, Lastname, Age, Salary, Task)\
            VALUES(1, 'Zahra', 'Isiaho', 25, 300000.00, 'Ass. Manager')");
conn.execute("INSERT INTO Company1(ID, firstname, Lastname, Age, Salary, Task)\
              VALUES(2, 'Andrew', 'Ouma', 27, 500000.00, 'Accountant')");
conn.execute("INSERT INTO Company1(ID, firstname, Lastname, Age, Salary, Task)\
             VALUES(3, 'Nicole', 'Korir', 24, 250000.00, 'Engineer')");
conn.execute("INSERT INTO Company1(ID, firstname, Lastname, Age, Salary, Task)\
              VALUES(4, 'Michelle', 'Chebet', 29, 600000.00, 'Manager')");

conn.commit()
print("Successfully inserted values in Company1 table")

conn.close()