f1 = 1
f2 = 1
file = open("C:\\Users\\Aaron\\Downloads\\rosalind_fib.txt", 'r')
kn = file.readline().split()
k = int(kn[0])
n = int(kn[1])
fn = 0;
for i in range(3, k+1):
    fn = n*f2 + f1
    f2 = f1
    f1 = fn
print fn
