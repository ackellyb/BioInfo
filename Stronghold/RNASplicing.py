import BioLib
    
file = BioLib.getFile("splc")
introns = map(lambda x: x.DNA, BioLib.readFASTA(file))
codons = BioLib.codonTable(True)
exon = introns.pop(0)
for x in introns:
    if x in exon:
        exon = exon.replace(x,"")
blocks = BioLib.DNAtoCodon(exon)
protein = str()
for x in blocks:
    if(codons[x]=="Stop"):
        break
    protein+=codons[x]
print protein


