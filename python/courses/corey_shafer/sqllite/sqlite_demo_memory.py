# This is the version with the in-memory database and you can use this for testing
# it starts fresh everytime

import sqlite3
from employee import Employee

# This method creates the file if it does not exist
# if it exists then it just connects
conn = sqlite3.connect(':memory:')

# create a curson
c = conn.cursor()

# create an employee table
# Need to run this only once
c.execute("""CREATE TABLE employees(
		first text,
		last text,
		pay integer
		)""")

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
	return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

emp_1 = Employee("John","Doe",80000)
emp_2 = Employee("Jane","Doe",90000)

insert_emp(emp_1)
insert_emp(emp_2)

employees = get_emps_by_name('Doe')
print(employees)

update_pay(emp_2,95000)

remove_emp(emp_1)

employees = get_emps_by_name('Doe')
print(employees)

# close the connection
conn.close()