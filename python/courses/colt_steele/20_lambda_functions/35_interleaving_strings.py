def interleave(s1,s2):
	l1 = list(s1)
	l2 = list(s2)
	zip_list = list(zip(l1,l2))
	word = ""
	for part in zip_list:
		word += "".join(part)
	# part1 = "".join(zip_list[0])
	# part2 = "".join(zip_list[1])
	# word = part1 + part2
	return word

print(interleave("lzr", "iad"))

