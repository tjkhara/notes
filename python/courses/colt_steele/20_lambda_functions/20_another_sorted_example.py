# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# sorting by playcount
y = sorted(songs, key=lambda song:song["playcount"])

# print(y)

# for reverse we could do

z = sorted(songs, key=lambda song:song["playcount"], reverse=True)

print(z)