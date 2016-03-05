import BioLib

file = BioLib.getFile("iev")
couples = map(lambda x: int(x), file.readline().split())
probs = [1,1,1,0.75, 0.5,0]
ex = 0
for i in range(len(couples)):
    ex+=couples[i]*probs[i]*2
print ex
