from rosalind_library import FASTADNA

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
#         Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated


def compute(dna_list):
    highest_gc_dna = max(map(lambda dna: (dna.gc_content(), dna.name), dna_list))
    return highest_gc_dna


def format_string(gc_dna):
    return '{1}\n{0}'.format(gc_dna[0], gc_dna[1])


def main():
    dna_list = FASTADNA.read_list_from_file("../Data/rosalind_gc.txt")
    print(format_string(compute(dna_list)))

if __name__ == '__main__':
    main()

