import itertools
import re


class RNA:

    rna = str()

    def __init__(self, rna):
        rna = re.sub(r'\s', '', rna)
        rna_regex = re.compile(r'[^ACGU]+?', re.IGNORECASE)
        if rna_regex.search(rna):
            raise ValueError('RNA String had a value not of A, C, G or U')
        self.rna = rna.upper()

    def __eq__(self, other):
        return self.rna == other.rna

    def to_dna(self):
        return DNA(self.rna.replace('U', 'T'))

    
class DNA:
    
    dna = str()
    
    def __init__(self, dna):
        dna = re.sub(r'\s', '', dna)
        dna_regex = re.compile(r'[^ACGT]+?', re.IGNORECASE)
        if dna_regex.search(dna):
            raise ValueError('DNA string had a value not of A, C, G or T')
        self.dna = dna.upper()

    def __eq__(self, other):
        return self.dna == other.dna
        
    def reverse_complement(self):
        translation_table = str.maketrans('ATCG', 'TAGC')
        dna_complement = self.dna.translate(translation_table)[::-1]
        return dna_complement
    
    def nucleotide_counts(self):
        count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for x in self.dna:
            count[x] += 1
        return count

    def gc_content(self):
        count = self.nucleotide_counts()
        return (count['C']+count['G'])/len(self.dna) * 100
    
    def to_rna(self):
        return RNA(self.dna.replace('T', 'U'))

    def get_hamming_distance(self, other):
        distance = 0
        for (a, b)in zip(self.dna, other.dna):
            if a != b:
                distance += 1
        return distance


class FASTADNA(DNA):

    name = str()

    def __init__(self, name, dna):
        DNA.__init__(self, dna)
        self.name = name

    @staticmethod
    def read_list_from_file(file_name):
        with open(file_name) as file:
            data = file.read().split('>')[1:]
            dna_list = list()
            for x in data:
                s = x.split('\n', 1)
                dna_list.append(FASTADNA(s[0], s[1]))
            return dna_list


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


def get_kmers(iterable, number):
    kmers = list()
    for x in itertools.product(iterable, repeat=number):
        kmer = str()
        for y in x:
            kmer += y
        kmers.append(kmer)
    return kmers
