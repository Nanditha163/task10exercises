#Program that matches a word containing 'ab'
import re
def wordab(word):
    pattern='\w*ab.\w*'
    if re.search(pattern,word):
        return "Match found!"
    else:
        return "Match not found!"
print(wordab("The girl is absent for today class"))
print(wordab("Be positive!"))
print(wordab("abstraction is hiding internal details !"))


OUTPUT:
Match found!
Match not found!
Match found!
