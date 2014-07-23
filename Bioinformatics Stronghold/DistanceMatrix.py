##Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp).
##        Strings are given in FASTA format.
##
##Return: The matrix D corresponding to the p-distance dp on the given strings.
##        As always, note that your answer is allowed an absolute error of 0.001.


import BioLib


dna = BioLib.readFASTA(BioLib.getFile("pdst"))
dmatrix = list()
length = len(dna[0].dna)
for x in dna:
    dmatrix.append(map(lambda y: float(BioLib.hammingDistance(x,y))/length, dna))
for x in dmatrix:
    for y in x:
        print y,
    print
        
