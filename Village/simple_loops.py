def sum_odd_integers(a, b):
    c = 0
    for i in range(a, b):
        if i % 2 == 1:
            c = c+i
    return c

def main():
    integers = open("../Data/rosalind_ini4.txt", 'r').readline().split(" ")
    print(sum_odd_integers(int(integers[0]), int(integers[1])))

if __name__ == "__main__":
    main()
