from Bio import Entrez
file = open(r"c:\users\aaron\downloads\rosalind_gbk.txt","r")
genus = file.readline()
begin = file.readline()
end = file.readline()
Entrez.email = "aaron.kelly.barker@gmail.com"
handle = Entrez.esearch(db="nucleotide",term = genus+'[Organism] AND ("'+begin+'"[PDAT]: "'+end+'"[PDAT])')
record = Entrez.read(handle)
print record["Count"]
