from Classes.nucleic_acid import FASTADNA
from Classes.helper_functions import get_rosalind_data_path


# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection. (If several possible consensus
#         strings exist, then you may return any one of them.)
#


def main():
    dna_list = FASTADNA.read_list_from_file(get_rosalind_data_path('cons'))
    profile_matrix = FASTADNA.create_profile_matrix(dna_list)
    print(profile_matrix.create_consensus_string())
    print(profile_matrix.to_string())

if __name__ == '__main__':
    main()

