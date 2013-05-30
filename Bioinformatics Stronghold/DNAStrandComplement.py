file = open("C:\\Users\\Aaron\\Downloads\\rosalind_revc.txt", 'r')
dnastrand = file.readline();
bp = ""
for i in range(len(dnastrand)-1, -1, -1):
    base = dnastrand[i];
    if(base == 'A'): bp+="T"
    elif(base=='T'): bp+="A"
    elif(base=='C'): bp+="G"
    elif(base=='G'): bp+="C"
print bp
