# def combine_words(word, **kwargs):
# 	if kwargs == {}:
# 		return word
# 	if kwargs.get("prefix"):
# 		return kwargs["prefix"] + word
# 	if kwargs.get("suffix"):
# 		return word + kwargs["suffix"]

# print(combine_words("child"))
# print(combine_words("child", prefix="man"))
# print(combine_words("child", suffix="ish"))

# another solution

def combine_words(word, **kwargs):
	if 'prefix' in kwargs:
		return kwargs['prefix'] + word
	if 'suffix' in kwargs:
		return word + kwargs['suffix'] 
	else:
		return word


print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))