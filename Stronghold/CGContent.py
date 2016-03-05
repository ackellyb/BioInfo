import BioLib

##Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
##
##Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
##        Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated

dna = BioLib.readFASTA(BioLib.getFile("gc"))
dna = max(map(lambda x: (x.GCContent(),x), dna))

print dna[1].name
print dna[0] * 100


    
