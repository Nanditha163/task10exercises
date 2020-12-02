#program to match a string that contains only uppercase letters
import re
def uppermatch(string):
    pattern = re.compile(r".*[A-Z]$")
    if re.match(pattern,string):
        return "Match found!String is in uppercase"
    else:
        return"Match not found"
print(uppermatch("HELLO WORLD"))
print(uppermatch("new123@#python"))

OUTPUT:
C:\Users\Dell\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/Dell/PycharmProjects/pythonProject/task10ex5.py
Match found!String is in uppercase
Match not found
