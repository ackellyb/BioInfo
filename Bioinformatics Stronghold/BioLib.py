import itertools

class DNA:
    dna = str()
    
    def __init__(self,dna):
        self.dna = dna
        
    def reverseComplement(self):
        rc = str()
        for i in range(len(self.dna)-1, -1, -1):
            base = self.dna[i]
            if(base == 'A'): rc+="T"
            elif(base=='T'): rc+="A"
            elif(base=='C'): rc+="G"
            elif(base=='G'): rc+="C"
        return rc
    def GCContent(self):
        c = g = 0
        for x in self.dna:
            if("C" == x): c+=1
            elif("G" == x): g+=1
        return float(c+g)/len(self.dna)
    
    def dnaToRna(self):
        return self.dna.replace("T","U")
    def getDNA(self):
        return self.dna
        

class FASTADNA(DNA):
    name = str()
    def __init__(self, name, dna):
        DNA.__init__(self,dna)
        self.name = name
            
class Tables:
    def getRNACodonTable():
        return getCodonTranslationTable(false)
    def getDNACodonTable():
        return getCodonTranslationTable(true)
    def getCodonTranslationTable(dna):
        if(dna==True): file = "DNACodonTable.txt"
        else: file = "RNACodonTable.txt"
        codons = open(file, "r").read().split()
        codonsTable = dict()
        for i in range(0,len(codons), 2):
            codonsTable[codons[i]] = codons[i+1]
        codons.close()
        return codonsTable
        

def readFASTA(file):
    strings = file.read().split(">")[1:]
    NameDNA = list()
    for x in strings:
        s = x.split("\n",1)
        s[1] = s[1].replace("\n","")
        NameDNA.append(FASTADNA(s[0],s[1]))
    return NameDNA

def dnaToRna(dna):
    return dna.replace("T","U")
def rnaToDna(rna):
    return rna.replace("U","T")
def createReadingFrame(nstring):
    return [nstring[i:i+3] for i in range(0, len(nstring), 3)]

def getFile(code):
    return open("C:\\Users\Aaron\\Downloads\\rosalind_"+code+".txt","r")

def getKmers(iterable, number):
    kmers = list()
    for x in itertools.product(iterable,repeat=number):
        kmer = str()
        for y in x:
            kmer+=y
        kmers.append(kmer)
    return kmers
