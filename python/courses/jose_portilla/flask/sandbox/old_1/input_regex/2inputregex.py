import re

def check_input(input_string):

    # does the string have an upper case letter?

    pattern_upper = re.compile(r'[A-Z]')
    matches_upper = pattern_upper.finditer(input_string)
    
    isupper = False

    for match_upper in matches_upper:
        isupper = True

    # does the string have a lower case letter?

    pattern = re.compile(r'[a-z]')
    matches = pattern.finditer(input_string)

    islower = False

    for match in matches:
        islower = True

    # does the string end in a number? 

    pattern_num = re.compile(r'[0-9]$')
    matches_endnum = pattern_num.finditer(input_string)

    endnum = False

    for match_endnum in matches_endnum:
        endnum = True

    if isupper and islower and endnum:
        return True
    else:
        return False


print("Checking overall result")
result = check_input("H123")
print(result)
print('\n\n')
