import itertools
n = int(open("C:\\Users\\Aaron\\Downloads\\rosalind_perm.txt", "r").readline())
perms = list(itertools.permutations(range(1,n+1)))
print len(perms)
for x in perms:
    for y in x:
        print y,
    print
    
