# import pyfiglet module 
from pyfiglet import figlet_format
from termcolor import colored



var1 = input("What word do you want to print?")

def print_ascii(text, color="blue"):
	print((colored(figlet_format(var1), color=color)))

print_ascii(var1, "cyan")	

# result = pyfiglet.figlet_format(var1) 

# text = colored(result, color="yellow", on_color="on_magenta", attrs=["blink"])

# print(result) 
