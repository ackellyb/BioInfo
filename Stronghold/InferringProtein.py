import BioLib

def getMonoMassTable():
    values = open("MonoIsoMassTable.txt","r").read().split("\n")
    monotable = list()
    for x in values:
        x = x.split()
        monotable.append((float(x[1]),x[0]))
    return monotable

def findFragment(monotable, weight):
    for x in monotable:
        if(x[0]-0.001 < weight < x[0]+0.001):
            return x[1]
    

numbers = map(lambda x: float(x), BioLib.getFile("spec").read().split())
mono = getMonoMassTable()
protein = str()
for i in range(1, len(numbers)):
    diff = numbers[i]-numbers[i-1]
    protein+=findFragment(mono,diff)
print protein
    

    
