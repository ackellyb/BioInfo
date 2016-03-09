from rosalind_library import DNA

#
# Given: A DNA string s of length at most 1000 nt.
#
# Return: Four integers (separated by spaces) counting the respective number of times
#        that the symbols 'A', 'C', 'G', and 'T' occur in s.


def create_nucleotide_count_string(dna):
    counts = dna.nucleotide_counts()
    return "{0} {1} {2} {3}".format(counts['A'], counts['C'], counts['G'], counts['T'])


def main():
    with open('../Data/rosalind_dna.txt', 'r') as file:
        dna = DNA(file.read())
        print(create_nucleotide_count_string(dna))

if __name__ == '__main__':
    main()
