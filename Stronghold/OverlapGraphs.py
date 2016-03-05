import BioLib

dna = BioLib.readFASTA(BioLib.getFile("grph"))
for x in dna:
    for y in dna:
        if(x.dna != y.dna and x.dna.endswith(y.dna[:3])):
            print x.name, y.name

