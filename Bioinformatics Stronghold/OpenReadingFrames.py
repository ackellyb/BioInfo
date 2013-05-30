import BioLib

file = BioLib.getFile("orf")
fasta = BioLib.readFASTA(file)[0]
dnastrings = (fasta.reverseComplement(), fasta.DNA)
codons = BioLib.codonTable(True)
proteins = list()
it = 0
for x in dnastrings:
    while("ATG" in x):
        it = x.find("ATG", it)
        x = x[it:]
        protein = str()
        for i in range(0, len(x),3):
            if i+3 >= len(x):
                break
            elif codons[x[i:i+3]]=="Stop":
                proteins.append(protein)
                break;
            else:
                protein+=codons[x[i:i+3]]            
        it=+3
proteins = set(proteins)
for x in proteins:
    print x

    
    
    

        
        

