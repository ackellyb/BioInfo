from rosalind_library import get_rosalind_data_path
from rosalind_library import DNA

# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.


def format_string(index_list):
    return ' '.join(index_list)


def main():
    with open(get_rosalind_data_path('subs')) as file:
        DNAs = DNA(file.readline())
        DNAt = DNA(file.readline())
        index_list = map(lambda x: x, DNAs.find_substring_locations(DNAt))
        print(format_string(index_list))

if __name__ == '__main__':
    main()

