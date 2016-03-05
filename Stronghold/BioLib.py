import itertools
class RNA:

    rna = str()


    def __init__(self,dna):
        self.rna = rna

        
    def toDNA(self):
        return self.rna.replace("U","T")

    
class DNA:
    
    dna = str()
    
    def __init__(self,dna):
        self.dna = dna.replace("\n","")
        
    def reverseComplement(self):
        rc = str()
        for i in range(len(self.dna)-1, -1, -1):
            base = self.dna[i]
            if(base == 'A'): rc+="T"
            elif(base=='T'): rc+="A"
            elif(base=='C'): rc+="G"
            elif(base=='G'): rc+="C"
        return rc

    
    def nucleotideCounts(self):
        count = dict()
        for x in self.dna:
            count[x] = count.get(x,0)+1
        return count


    def GCContent(self):
        count = self.nucleotideCounts()
        return float(count["C"]+count["G"])/len(self.dna)

    
    def toRNA(self):
        return self.dna.replace("T","U")

        

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
        NameDNA.append(FASTADNA(s[0],s[1]))
    return NameDNA



def createReadingFrame(nstring):
    return [nstring[i:i+3] for i in range(0, len(nstring), 3)]


def hammingDistance(dna1,dna2):
    distance = 0
    for i, x in enumerate(dna1.dna):
        if(x != dna2.dna[i]): distance+=1
    return distance


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
