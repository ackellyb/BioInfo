from rosalind_library import DNA
from rosalind_library import get_rosalind_data_path

# Given: A DNA string t having length at most 1000 nt.
#
# Return: The transcribed RNA string of t.


def format_string(dna):
    rna = dna.to_rna()
    return rna.string


def main():
    with open(get_rosalind_data_path('rna')) as file:
        dna = DNA(file.read())
        print(format_string(dna))

if __name__ == '__main__':
    main()
