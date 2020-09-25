from termcolor import colored

# print(dir(termcolor))

# help(termcolor)

text = colored("Hi there", color="yellow", on_color="on_magenta", attrs=["blink"])

print(text)