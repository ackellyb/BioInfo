file = open("../Data/rosalind_ini5_1_dataset.txt", 'r')
list = file.readlines()
for i in range(len(list)):
    if i%2==1: print (list[i])
file.close()

