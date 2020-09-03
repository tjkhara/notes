import re

username = 'tkhara123'

pattern = re.compile(r'[a-z]')

matches = pattern.search(username)

print(matches)