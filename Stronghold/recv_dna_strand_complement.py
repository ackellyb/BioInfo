from rosalind_library import DNA
from rosalind_library import get_rosalind_data_path

# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement of s


def format_string(dna):
    dna_rc = dna.reverse_complement()
    return dna_rc


def main():
    with open(get_rosalind_data_path('recv')) as file:
        dna = DNA(file.read())
        print(format_string(dna))

if __name__ == '__main__':
    main()
