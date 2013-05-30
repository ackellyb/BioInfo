file = open("C:\\Users\\Aaron\\Downloads\\rosalind_rna.txt", 'r')
DNA = list(file.readline())
for i in range(len(DNA)):
    if(DNA[i]=='T'): DNA[i]='U'
print ''.join(DNA)
