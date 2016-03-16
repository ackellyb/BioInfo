import re

from Classes.helper_functions import get_rna_codon_table, get_dna_codon_table
from Classes.profile_matrix import ProfileMatrix


class _NucleicAcidStringFormat:
    def __init__(self, regex, error_msg):
        self.regex = re.compile(regex, re.IGNORECASE)
        self.errorMsg = ValueError(error_msg)

rnaStringFormat = _NucleicAcidStringFormat(r'[^ACGU]+?', 'RNA String had a value not of A, C, G or U')
dnaStringFormat = _NucleicAcidStringFormat(r'[^ACGT]+?', 'DNA string had a value not of A, C, G or T')


class _NucleicAcid:
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


class RNA(_NucleicAcid):
    def __init__(self, string):
        _NucleicAcid.__init__(self, string, rnaStringFormat)

    def to_dna(self):
        return DNA(self.string.replace('U', 'T'))

    def transcribe_to_protein(self):
        return _NucleicAcid._transcribe_to_protein(self, get_rna_codon_table())

    @staticmethod
    def create_profile_matrix(string_list):
        return ProfileMatrix(string_list, ['A', 'G', 'C', 'U'])


class DNA(_NucleicAcid):
    def __init__(self, string):
        _NucleicAcid.__init__(self, string, dnaStringFormat)

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
        return _NucleicAcid._transcribe_to_protein(self, get_dna_codon_table())

    @staticmethod
    def create_profile_matrix(string_list):
        return ProfileMatrix(string_list, ['A', 'G', 'C', 'T'])


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

    @staticmethod
    def create_profile_matrix(string_list):
        string_list = list(map(lambda x: x.string, string_list))
        return DNA.create_profile_matrix(string_list)