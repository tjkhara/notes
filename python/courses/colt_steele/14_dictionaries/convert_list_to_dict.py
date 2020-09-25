 
# first method

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

# second method

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}

# third method

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = dict(person)