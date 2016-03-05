import BioLib

##Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
##
##Return: The Hamming distance dH(s,t).

st = map(lambda x: BioLib.DNA(x), BioLib.getFile("hamm").read().split())
distance = BioLib.hammingDistance(st[0], st[1])
print distance
