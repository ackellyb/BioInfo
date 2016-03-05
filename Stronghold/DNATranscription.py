import BioLib

##Given: A DNA string t having length at most 1000 nt.
##
##Return: The transcribed RNA string of t.

dna = BioLib.DNA(BioLib.getFile("rna").read())
rna = dna.toRNA()
print rna
