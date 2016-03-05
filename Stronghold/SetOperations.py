import BioLib
def readSet(string):
    newset = set()
    for x in string:
      if(x != "{" or x != "}" or x != " " or x != ","):
        newset.add(x)
    return newset

file = BioLib.getFile("seto")
n = int(file.readline())
a = readSet(file.readline())
b = readSet(file.readline())
print a
print b
        
