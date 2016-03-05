import BioLib
import itertools

file = BioLib.getFile("lexf")
alphabet = file.readline().split()
#n = int(file.readline())
lists = list()
n = 4
for x in itertools.product("TACG",repeat=n):
    kmer = str()
    for y in x:
        kmer+=y
    lists.append(kmer)
    #print kmer
print len(lists)
