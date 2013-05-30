file = open("C:\\Users\\Aaron\\Downloads\\rosalind_subs.txt", "r")
DNAs = file.readline().strip()
DNAt = file.readline().strip()
index = list()
i = 0
while ( i < len(DNAs)):
    i = DNAs.find(DNAt, i) + 1
    if(i == 0): break
    index.append(str(i))
print " ".join(index,)

    
    
