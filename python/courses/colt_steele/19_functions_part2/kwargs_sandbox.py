def combine_words(word, **kwargs):
	if kwargs.get("prefix"):
		return kwargs.get("prefix") + word

	if kwargs.get("suffix"):
		return word + kwargs.get("suffix")

print(combine_words("child", suffix="ish"))
print(combine_words("child", prefix="man"))