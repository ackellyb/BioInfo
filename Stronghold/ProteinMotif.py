import re
import urllib
import BioLib
import os

def motifToRegex(motif):
    regex = str()
    i = 0
    while i < len(motif):
        if(motif[i]=="{"):
            regex+="[^"+motif[i+1]+"]"
            i+=3
        elif(motif[i]=="["):
            regex+="("+motif[i+1]+"|"+motif[i+2]+")"
            i+=4
        else:
            regex+=motif[i]
            i+=1
    return re.compile(regex)

s = motifToRegex("N{P}[ST]{P}")
proteins = BioLib.getFile("mprt").read().split()
for x in proteins:
    urllib.urlretrieve("http://www.uniprot.org/uniprot/"+x+".fasta",x)
    file = open(x,"r")
    file.readline()
    protein = file.read().replace("\n","")
    match = s.search(protein)
    matches = list()
    if match:
        print x
    while match:
        i = match.start()+1
        matches.append(str(i))
        match = s.search(protein, i)
    print " ".join(matches)

