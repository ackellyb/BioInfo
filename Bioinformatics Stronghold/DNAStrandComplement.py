import BioLib

##Given: A DNA string s of length at most 1000 bp.
##
##Return: The reverse complement of s

dna = BioLib.DNA(BioLib.getFile("revc").read())
rc = dna.reverseComplement()
print rc
