#Program to check string contains certain set of characters
import re
def checkstr(string):
    charre=re.compile(r'[^a-zA-Z0-9.]')
    string=charre.search(string)
    return not bool(string)
print(checkstr("ABCDEFabcdef123450"))
print(checkstr("*&%@#!}{"))


OUTPUT:
True
False