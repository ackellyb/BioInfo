import itertools
from os import path


def get_rna_codon_table():
    return __get_translation_table(get_data_path("RNACodonTable.txt"))


def get_dna_codon_table():
    return __get_translation_table(get_data_path("DNACodonTable.txt"))


def __get_translation_table(file):
    codon_table = dict()
    with open(file) as table:
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
    return path.join(path.dirname(__file__), path.pardir, 'resources', file_name)
