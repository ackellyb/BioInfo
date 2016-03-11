import rosalind_library

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).


def main():
    with open('../Data/rosalind_hamm.txt', 'r') as file:
        dna = DNA(file.readline())
        dna2 = DNA(file.readline())
        print(dna.get_hamming_distance(dna2))

if __name__ == '__main__':
    main()


