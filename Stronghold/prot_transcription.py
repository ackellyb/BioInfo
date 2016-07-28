from rosalind_library import RNA
from rosalind_library import get_rosalind_data_path

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: The protein string encoded by s.

def main():
    with open(get_rosalind_data_path('prot')) as file:
        rna = RNA(file.readline())
        print(rna.transcribe_to_protein())

if __name__ == '__main__':
    main()


