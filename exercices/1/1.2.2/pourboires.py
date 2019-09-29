#!/usr/bin/python
from itertools import chain, combinations
import re

transaction_t = [2000, 6000, 800, 700, 1200, 1000, 1300, 600]
transaction_p = [13000, 9000, 2000, 1500, 3500, 2800, 5000, 1500]

T = 6000
f = 0
maxi = 0
sp = []
maxi_lst = []

# Fusion des listes
def fusion_lst(lst1 , lst2):
    lst_t = []
    f = 0
    while f < len(lst1):
        lst_t.append(str(lst1[f]) + ";" + str(lst2[f]))
        f = f + 1
    return lst_t

transaction = fusion_lst(transaction_t,transaction_p)
    
    

# somme des poids
def sumlst(lst):
    d = 0
    sup = []
    su = []
    while d < len(lst):
        sup.append(int(re.split(";",lst[d])[0]))
        su.append(int(re.split(";",lst[d])[1]))
        d += 1
    return (sum(sup),sum(su))



# Cas de figure
def it(iterable):
    s = list(iterable) 
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for i, compo in enumerate(it(transaction), 1):
    if len(compo) == 0:
        print
    else:
#         si valeur < Taille max, on prend
        if sumlst(compo)[0] < T:
            if sumlst(compo)[1] > maxi:
                maxi = sumlst(compo)[1]
                maxi_lst = compo
            sp.append((compo,sumlst(compo)[1]))


print(maxi_lst,maxi)
