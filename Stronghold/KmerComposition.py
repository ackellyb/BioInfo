import BioLib
import collections

dna = BioLib.readFASTA(BioLib.getFile("kmer"))[0].dna
kmers1 = BioLib.getKmers("ACGT",4)
kmers = dict(zip(kmers1,range(len(kmers1))))
kmercount = dict()
i = 0
while i+4 <= len(dna):
    s = dna[i:i+4]   
    kmercount[kmers[s]] = kmercount.get(kmers[s],0)+1
    i+=1
    
for i in range(len(kmers)):
    print kmercount.get(i,0),

