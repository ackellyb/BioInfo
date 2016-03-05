import BioLib
import math
import itertools

file = BioLib.getFile("prob")
dna = file.readline()
cglist = map(lambda x: float(x), file.readline().split())
problist = list()
for x in cglist:
    CG = math.log10(x/2)
    AT = math.log10((1-x)/2)
    prob = 0
    for y in dna:
        if(y=="C" or y=="G"): prob+=CG
        elif(y=="A" or y=="T"): prob+=AT
    problist.append(prob)
s = reduce(lambda x,y: str(x)+" "+str(y), problist)
print s
