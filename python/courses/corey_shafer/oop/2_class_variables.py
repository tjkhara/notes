class Employee(object):
	
	num_of_emps = 0

	# class variable
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
		Employee.num_of_emps += 1

	def __repr__(self):
		return f"First: {self.first} Last: {self.last} Pay: {self.pay} Email: {self.email}"

	def full_name(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee(first="TJ", last="Khara", pay=50000)
emp_2 = Employee(first="Miles", last="Khara", pay=60000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# printing out namespace

# print(emp_1.__dict__)
# print(Employee.__dict__)

print(Employee.num_of_emps)