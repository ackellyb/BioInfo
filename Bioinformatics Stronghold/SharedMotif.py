import BioLib

dna = map(lambda x: x.dna, BioLib.readFASTA(BioLib.getFile("lcsm")))
dna1 = dna.pop(0)
substrings = 
