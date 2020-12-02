#To check for a number at end of word/sentence:
import re
def numend(string):
    pattern=re.compile(r".*[0-9]$")
    if pattern.match(string):
        return "Number found at end!"
    else:
        return "Number not found at end!"
print(numend("abcd123"))
print(numend("Meet at 12"))
print(numend("The climate is cold"))

OUTPUT:
Number found at end!
Number found at end!
Number not found at end!
