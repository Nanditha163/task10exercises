#Program to search number(0-9) of length between 1 to 3 in given string
import re
result=re.finditer(r"([0-9]{1,3})","Numbers are 16,3,21,82 and 590 are included")
print("Number of length 1 to 3")
for n in result:
    print(n.group(0))


    OUTPUT:
    Number of length 1 to 3
    16
    3
    21
    82
    590
