import BioLib

dna = BioLib.readFASTA(BioLib.getFile("gc"))
  
imax = 0
dna = map(lambda x: (x, x.GCContent), dna)
maxDNA = max(dna, key= (lambda x: x[1]))
print maxDNA[0].name
print maxDNA[1]

    
