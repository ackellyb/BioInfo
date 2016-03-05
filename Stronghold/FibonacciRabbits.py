# -*- coding: utf-8 -*-
import BioLib

##Given: Positive integers n≤40 and k≤5.
##
##Return: The total number of rabbit pairs that will
##        be present after n months if each pair of
##        reproduction-age rabbits produces a litter of
##        k rabbit pairs in each generation (instead of only 1 pair).
  

f1 = 1
f2 = 1
file = BioLib.getFile("fib")
kn = map(lambda x: int(x), file.readline().split())
fn = 0;
for i in range(3, kn[0]+1):
    fn = kn[1]*f2 + f1
    f2 = f1
    f1 = fn
print fn
