from Classes.nucleic_acid import DNA
from Classes.helper_functions import get_rosalind_data_path


# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).


def main():
    with open(get_rosalind_data_path('hamm')) as file:
        dna = DNA(file.readline())
        dna2 = DNA(file.readline())
        print(dna.get_hamming_distance(dna2))

if __name__ == '__main__':
    main()


