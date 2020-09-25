'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
    new_word = word[0].upper() + word[1:]
    return new_word

print(capitalize("tim"))