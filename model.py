##function take a string, return the string but reversed
def flipit(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring

print(flipit("hello"))

##function takes a string, returns all caps version
def shout(string):
    return string.upper()
