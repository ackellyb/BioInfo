import BioLib
file = open("C:\\Users\\Aaron\\Downloads\\rosalind_cons (1).txt","r")
NameDNA = BioLib.readFASTA(file)
pMatrix = {"A": list(), "C": list(), "G": list(), "T": list()}
consensus = str()
for i in range(len(NameDNA[0][1])):
    a = c = g = t = 0
    for x in NameDNA:
        if(x[1][i]=="A"): a+=1
        elif(x[1][i]=="C"): c+=1
        elif(x[1][i]=="G"): g+=1
        elif(x[1][i]=="T"): t+=1
    pMatrix["A"].append(a)
    pMatrix["C"].append(c)
    pMatrix["G"].append(g)
    pMatrix["T"].append(t)
    if  (a >= c and a >= g and a >=t): consensus+="A"
    elif(c >= a and c >= g and c >=t): consensus+="C"
    elif(g >= a and g >= c and g >=t): consensus+="G"
    else: consensus+="T"

print consensus
for y in "ACGT":
    print y+": ",
    print " ".join(map(str,pMatrix[y]))
    

    
    
