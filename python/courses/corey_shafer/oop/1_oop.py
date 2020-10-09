class Employee(object):
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"

	def __repr__(self):
		return f"First: {self.first} Last: {self.last} Pay: {self.pay} Email: {self.email}"

	def full_name(self):
		return f"{self.first} {self.last}"

emp_1 = Employee(first="TJ", last="Khara", pay=50000)
emp_2 = Employee(first="Miles", last="Khara", pay=60000)

# print(emp_1.full_name())

# print(emp_2)


# These three below are the same
print(emp_1.full_name())
print(Employee.full_name(emp_1))



		