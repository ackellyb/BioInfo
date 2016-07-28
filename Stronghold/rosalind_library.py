import itertools
import re
from os import path


class _PolyNucleotideStringFormat:
    def __init__(self, regex, error_msg):
        self.regex = re.compile(regex, re.IGNORECASE)
        self.errorMsg = ValueError(error_msg)


class _PolyNucleotides:
    def __init__(self, string, string_format=None):
        string = re.sub(r'\s', '', string)
        if string_format is not None and string_format.regex.search(string):
            raise string_format.errorMsg
        self.string = string.upper()

    def __eq__(self, other):
        return self.string == other.string and type(self) == type(other)

    def length(self):
        return len(self.string)

    def _transcribe_to_protein(self, codon_table):
        protein_list = list()
        for i in range(0, len(self.string), 3):
            codon = self.string[i:i+3]
            if codon_table[codon] == 'Stop':
                break
            else:
                protein_list.append(codon_table[codon])
        return "".join(protein_list)

    def find_substring_locations(self, other):
        if self.length() < other.length():
            return list()
        i = 0
        index_list = list()
        while i < len(self.string) - len(other.string):
            i = self.string.find(other.string, i) + 1
            if i == 0:
                break
            index_list.append(i)
        return index_list


rnaStringFormat = _PolyNucleotideStringFormat(r'[^ACGU]+?', 'RNA String had a value not of A, C, G or U')
dnaStringFormat = _PolyNucleotideStringFormat(r'[^ACGT]+?', 'DNA string had a value not of A, C, G or T')


class RNA(_PolyNucleotides):
    def __init__(self, string):
        _PolyNucleotides.__init__(self, string, rnaStringFormat)

    def to_dna(self):
        return DNA(self.string.replace('U', 'T'))

    def transcribe_to_protein(self):
        return _PolyNucleotides._transcribe_to_protein(self, Tables.get_rna_codon_table())

    
class DNA(_PolyNucleotides):
    def __init__(self, string):
        _PolyNucleotides.__init__(self, string, dnaStringFormat)
        
    def reverse_complement(self):
        translation_table = str.maketrans('ATCG', 'TAGC')
        dna_complement = self.string.translate(translation_table)[::-1]
        return dna_complement
    
    def nucleotide_counts(self):
        count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for x in self.string:
            count[x] += 1
        return count

    def gc_content(self):
        count = self.nucleotide_counts()
        return (count['C']+count['G'])/len(self.string) * 100
    
    def to_rna(self):
        return RNA(self.string.replace('T', 'U'))

    def get_hamming_distance(self, other):
        distance = 0
        for (a, b)in zip(self.string, other.string):
            if a != b:
                distance += 1
        return distance

    def transcribe_to_protein(self):
        return _PolyNucleotides._transcribe_to_protein(self, Tables.get_dna_codon_table())


class FASTADNA(DNA):

    name = str()

    def __init__(self, name, string):
        self.name = name
        DNA.__init__(self, string)

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

    @staticmethod
    def get_rna_codon_table():
        return Tables.__get_translation_table(False)

    @staticmethod
    def get_dna_codon_table():
        return Tables.__get_translation_table(True)

    @staticmethod
    def __get_translation_table(is_dna):
        codon_table = dict()
        if is_dna:
            file = get_data_path("DNACodonTable.txt")
        else:
            file = get_data_path("RNACodonTable.txt")

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


def get_rosalind_data_path(file_code):
    return get_data_path('rosalind_'+file_code+'.txt')


def get_data_path(file_name):
    return path.join(path.dirname(__file__), path.pardir, 'Data', file_name)
