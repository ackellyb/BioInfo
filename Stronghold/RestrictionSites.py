import BioLib

basepairs = {"A":"T","C":"G","G":"C","T":"A"}
dna = BioLib.readFASTA(BioLib.getFile("revp"))[0].dna
results = list()
for i in range(len(dna)):
    it = 1
    while i - it >= 0  and i + it < len(dna) and dna[i+1-it] == basepairs[dna[i+it]]:
        print dna[i+1-it], dna[i+it]
        print it
        it+=1
    if 4 <= it*2 <= 12:
        results.append((i-it+1, it*2))
#for x in results:
#    print x[0], x[1], dna[x[0]:x[0]+x[1]]
                                           
    
        
