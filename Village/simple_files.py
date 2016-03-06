def remove_odd_lines(file_name):
    file = open(file_name, 'r')
    file_lines = file.readlines()
    even_file_lines = []
    for i in range(len(file_lines)):
        if i % 2 == 1:
            even_file_lines.append(file_lines[i])
    file.close()
    return even_file_lines


def main():
    print(remove_odd_lines("../Data/rosalind_ini5.txt"))

if __name__ == "__main__":
    main()
