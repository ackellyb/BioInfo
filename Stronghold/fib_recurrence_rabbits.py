# Given: Positive integers n≤40 and k≤5.
#
# Return: The total number of rabbit pairs that will
#        be present after n months if each pair of
#        reproduction-age rabbits produces a litter of
#        k rabbit pairs in each generation (instead of only 1 pair).


def fibonacci_sequence(months, litter_size):
    if months <= 2:
        return 1
    f1 = 1
    f2 = 1
    fn = 0
    for i in range(2, months):
        fn = litter_size*f2 + f1
        f2 = f1
        f1 = fn
    return fn


def main():
    with open('../Data/rosalind_fib.txt', 'r') as file:
        integers = file.readline().split(' ')
        print(fibonacci_sequence(int(integers[0]), int(integers[1])))

if __name__ == '__main__':
    main()

