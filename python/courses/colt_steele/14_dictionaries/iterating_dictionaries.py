instructor = {
	"name" : "Colt",
	"owns_dogs" : True,
	"num_courses" : 4,
	"favorite_language" : "Python",
	"is_hilarious" : False,
	44 : "my favirite number"
}

# for v in instructor.values():
# 	print(v)

# for k in instructor.keys():
# 	print(k)

# how to do both

for k,v in instructor.items():
	print(f"{k} : {v}")