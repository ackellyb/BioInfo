def count_words(s):
    s = s.rstrip("\n")
    word_dict = {}
    for word in s.split(" "):
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


def main():
    s = open("../Data/rosalind_ini6.txt").readline()
    result = count_words(s)
    for key, value in result.items():
        print("{0} {1}".format(key, value))

if __name__ == "__main__":
    main()
