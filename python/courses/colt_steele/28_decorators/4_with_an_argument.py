from random import choice

def laugh_at(person):
	def get_laugh():
		l = choice(('HAHAHAH', 'lol', 'tehehe'))
		return f"{l} {person}"
	return get_laugh

laugh = laugh_at("Mike")
laugh2 = laugh_at("Narinder")

print(laugh())
print(laugh2())

