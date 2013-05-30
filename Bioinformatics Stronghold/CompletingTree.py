import BioLib

file = BioLib.getFile("tree")
n = int(file.readline())
edges = 0
for x in file.readlines():
    edges+=len(x.split())-1
print n-edges-1
    
    
