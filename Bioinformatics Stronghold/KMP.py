import BioLib

s = BioLib.readFASTA(BioLib.getFile("kmp (1)")).pop().DNA
f = open("answer","w")
j = 0
i = 1
failure = [0]
string = "0"
while i < len(s):
    if s[i]==s[j]:
        j+=1
        failure.append(j)
        string+=" "+str(j)
        i+=1
    elif j > 0:
        j = failure[j-1]
    else:
        j = 0
        i+=1
        failure.append(j)
        string+=" 0"
f.write(string)
f.close()
print "end"
        
