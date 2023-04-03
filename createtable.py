import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully opened database")

conn.execute("""CREATE TABLE Company1(
ID int primary key not null,
firstname text not null,
Lastname text not null,
Age int,
Salary real,
Task text char(20))""")

print("Successfully created Company1 table")
conn.close()