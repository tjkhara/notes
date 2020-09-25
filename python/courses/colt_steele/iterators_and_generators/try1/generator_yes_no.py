def yes_or_no():
	answer = "yes"
	while True:
		yield answer
		answer = "no" if answer == "yes" else "yes"

answer = yes_or_no()

print(next(answer))
print(next(answer))
print(next(answer))