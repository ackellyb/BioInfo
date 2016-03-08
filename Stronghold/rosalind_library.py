import itertools

class RNA:

    rna = str()

    def __init__(self, rna):
        self.rna = rna.strip()

    def to_dna(self):
        return DNA(self.rna.replace("U", "T"))

    
class DNA:
    
    dna = str()
    
    def __init__(self, dna):
        self.dna = dna.strip()
        
    def reverse_complement(self):
        translation_table = str.maketrans("ATCG", "TAGC")
        dna_complement = self.dna.translate(translation_table)[::-1]
        return dna_complement
    
    def nucleotide_counts(self):
        count = dict()
        for x in self.dna:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        return count

    def gc_percentage(self):
        count = self.nucleotide_counts()
        return (count["C"]+count["G"])/len(self.dna)
    
    def to_rna(self):
        return RNA(self.dna.replace("T", "U"))


class FASTADNA(DNA):

    name = str()

    def __init__(self, name, dna):
        DNA.__init__(self, dna)
        self.name = name

    @staticmethod
    def create_fasta_from_file(file):
        data = file.read().split(">")[1:]
        name_dna = list()
        for x in data:
            s = x.split("\n", 1)
            name_dna.append(FASTADNA(s[0], s[1]))
        return name_dna


class Tables:

    def get_rna_codon_table(self):
        return self.__get_translation_table(False)

    def get_dna_codon_table(self):
        return self.__get_translation_table(True)

    @staticmethod
    def __get_translation_table(is_dna):
        codon_table = dict()
        if is_dna:
            file = '../DNACodonTable.txt'
        else:
            file = '../RNACodonTable.txt'

        with open(file, 'r') as table:
            codons = table.read().split()
            for i in range(0, len(codons), 2):
                codon_table[codons[i]] = codons[i+1]
        return codon_table


def create_reading_frame(nstring):
    return [nstring[i:i+3] for i in range(0, len(nstring), 3)]


def hamming_distance(dna1, dna2):
    distance = 0
    for i, x in enumerate(dna1.dna):
        if x != dna2.dna[i]:
            distance += 1
    return distance


def get_kmers(iterable, number):
    kmers = list()
    for x in itertools.product(iterable, repeat=number):
        kmer = str()
        for y in x:
            kmer += y
        kmers.append(kmer)
    return kmers
