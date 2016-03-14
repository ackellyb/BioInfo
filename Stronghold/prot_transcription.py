from rosalind_library import RNA


def main():
    with open('../Data/rosalind_prot.txt') as file:
        rna = RNA(file.readline())
        print(rna.transcribe_to_protein())

if __name__ == '__main__':
    main()


