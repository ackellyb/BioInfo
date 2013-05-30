file = open("C:\\Users\\Aaron\\Downloads\\rosalind_ini5.txt", 'r')
list = file.readlines()
for i in range(len(list)):
    if i%2==1: print list[i].strip()
file.close()

