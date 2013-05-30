def split_block(seq,length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

strings = open("RNACodonTable.txt", "r").read().split()
codons = dict()
stopcodons = ["UAA", "UAG", "UGA"]
for i in range(0,len(strings), 2):
    codons[strings[i]] = strings[i+1]
DNA = open("C:\\Users\Aaron\\Downloads\\rosalind_prot.txt", "r").read().replace("\n","")
Protein = map(lambda x: codons[x], split_block(DNA,3))
for i, x in enumerate(Protein):
    if(x=="Stop"):
        Protein = Protein[0:i]
        continue
print "".join(Protein)
