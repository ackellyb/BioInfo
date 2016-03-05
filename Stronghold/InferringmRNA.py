import BioLib

def getCodonFrequencies():
    strings = open("RNACodonTable.txt").read().split()
    frequencies = dict()
    for i in range(1,len(strings),2):
        if strings[i] not in frequencies:
            frequencies[strings[i]] = 1
        else:
            frequencies[strings[i]]+=1
    return frequencies

file = BioLib.getFile("mrna")
freq = getCodonFrequencies()
nums = 1
for x in file.readline():
    for y in x:
        if y !="\n":
            nums*=freq[x]
nums*=freq["Stop"]
nums = nums%1000000
print nums
    
