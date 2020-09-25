import string

username = ""


# test for empty string
if username == "":
	print("username is empty")


# lower case letter check
contains_lower_case_letter = False

lower_case_letters = string.ascii_lowercase
for c in username:
	if c in lower_case_letters:
		contains_lower_case_letter = True
		break

print(contains_lower_case_letter)


# upper case letter check
contains_upper_case_letter = False

upper_case_letters = string.ascii_uppercase

for u in username:
	if u in upper_case_letters:
		contains_upper_case_letter = True
		break

print(contains_upper_case_letter)


# username must end in a number
ends_in_number = False

numbers_list = list(range(0,10))

last_char = username[-1]

if last_char.isnumeric():
	ends_in_number = True

if contains_lower_case_letter and contains_upper_case_letter and ends_in_number:
	print("All conditions are met")
else:
	print("All conditions are not met")


