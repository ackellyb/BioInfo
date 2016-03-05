import BioLib


##Given: A DNA string s of length at most 1000 nt.
##
##Return: Four integers (separated by spaces) counting the respective number of times
##        that the symbols 'A', 'C', 'G', and 'T' occur in s.

file = BioLib.getFile("dna")
counts = BioLib.DNA(file.read()).nucleotideCounts()

for x in "ACGT":
   print counts[x], 
