file = open("C:\\Users\\Aaron\\Downloads\\rosalind_dna (2).txt", 'r')
acgt = [0,0,0,0]
dna = file.readline()
for i in range(len(dna)):
    if(dna[i]=='A'): acgt[0] +=1
    elif(dna[i]=='C'): acgt[1] +=1
    elif(dna[i]=='G'): acgt[2] += 1
    elif(dna[i]=='T'): acgt[3] += 1
for x in acgt:
    print x
