import re

def check_input(input_string):

    # does the string have a lower case letter?

    pattern = re.compile(r'[a-z]')
    matches = pattern.finditer(input_string)




