d = {"name" : "Ricky"}

# This gives key error
# d["city"]

def get(d,k):
	try:
		return d[k]
	except KeyError:
		return None


print(get(d,"name")) # Ricky

print(get(d,"age")) 

