def add_squares(a,b):
    return a**2 + b**2


def main():
    integers = open("../Data/rosalind_ini2_1_dataset.txt", 'r').readline().split(" ")
    print(add_squares(int(integers[0]), int(integers[1])))

if __name__ == "__main__":
    main()
