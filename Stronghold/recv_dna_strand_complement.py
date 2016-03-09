from rosalind_library import DNA

# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement of s


def format_string(dna):
    dna_rc = dna.reverse_complement()
    return dna_rc


def main():
    with open('../Data/rosalind_recv.txt', 'r') as file:
        dna = DNA(file.read())
        print(format_string(dna))

if __name__ == '__main__':
    main()
