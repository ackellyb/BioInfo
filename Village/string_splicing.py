def splice(s, a, b, c, d):
    return s[a:b+1] + " " + s[c:d+1]


def main():
    file = open("../Data/rosalind_ini3_3_dataset.txt")
    s = file.readline()
    integers = file.readline().split(" ")
    print(splice(s, int(integers[0]), int(integers[1]), int(integers[2]), int(integers[3])))

if __name__ == '__main__':
    main()
