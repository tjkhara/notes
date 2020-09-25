import sqlite3
from employee import Employee

# This method creates the file if it does not exist
# if it exists then it just connects
conn = sqlite3.connect('employee.db')

# create a curson
c = conn.cursor()

# create an employee table
# Need to run this only once
# c.execute("""CREATE TABLE employees(
# 		first text,
# 		last text,
# 		pay integer
# 		)""")

emp_1 = Employee("John","Doe",80000)
emp_2 = Employee("Jane","Doe",90000)



# insert
# c.execute("INSERT INTO employees VALUES ('Corey','Shafer',50000)")
# c.execute("INSERT INTO employees VALUES ('Mary','Shafer',70000)")

# first proper way
# c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))

# commits the current transaction
# conn.commit()

# second proper way
# c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# commits the current transaction
# conn.commit()

# select
# first approach
c.execute("SELECT * FROM employees WHERE last=?", ('Shafer',))

print(c.fetchall())

# second approach
c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})

print(c.fetchall())

# commits the current transaction
conn.commit()

# close the connection
conn.close()