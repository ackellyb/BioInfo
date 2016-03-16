from Classes.helper_functions import get_rosalind_data_path

# Given: Three positive integers k, m, and n, representing a population containing
#        k+m+nk+m+n organisms: k individuals are homozygous dominant for a factor,
#        m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce
#         an individual possessing a dominant allele (and thus displaying the
#         dominant phenotype). Assume that any two organisms can mate.


def compute(k, m, n):
    p = k + m + n
    homo_rec_chance = (n*n - n)/(p*p - p)
    het_chance = (m*m - m)/(4*p*p - 4*p)
    rec_het_chance = (n*m)/(p*p - p)
    dom_allele_chance = 1 - (homo_rec_chance + het_chance + rec_het_chance)
    return dom_allele_chance


def main():
    with open(get_rosalind_data_path('iprb')) as file:
        kmn = list(map(lambda x: int(x), file.readline().split(" ")))
        print(compute(kmn[0], kmn[1], kmn[2]))


if __name__ == '__main__':
    main()
