import re

def check_input(input_string):

    # does the string have an upper case letter?

    pattern_upper = re.compile(r'[A-Z]')
    matches_upper = pattern_upper.finditer(input_string)
    
    isupper = False

    for match_upper in matches_upper:
        print(match_upper)
        isupper = True
    print("Is there an upper case letter?")
    print(isupper)

    # does the string have a lower case letter?

    pattern = re.compile(r'[a-z]')
    matches = pattern.finditer(input_string)

    islower = False

    for match in matches:
        print(match)
        islower = True
    print("Is there a lower case letter?")
    print(islower)

    # does the string end in a number? 

    pattern_num = re.compile(r'[0-9]$')
    matches_endnum = pattern_num.finditer(input_string)

    endnum = False

    for match_endnum in matches_endnum:
        print(match_endnum)
        endnum = True
    print("Does the string end with a number?")
    print(endnum)

    if isupper and islower and endnum:
        return True
    else:
        return False


print("Checking overall result")
result = check_input("tkhara123")
print(result)
print('\n\n')
