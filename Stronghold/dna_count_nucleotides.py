from rosalind_library import DNA
from rosalind_library import get_rosalind_data_path

#
# Given: A DNA string s of length at most 1000 nt.
#
# Return: Four integers (separated by spaces) counting the respective number of times
#        that the symbols 'A', 'C', 'G', and 'T' occur in s.


def format_string(dna):
    counts = dna.nucleotide_counts()
    return "{0} {1} {2} {3}".format(counts['A'], counts['C'], counts['G'], counts['T'])


def main():
    with open(get_rosalind_data_path('dna')) as file:
        dna = DNA(file.read())
        print(format_string(dna))

if __name__ == '__main__':
    main()
