
L1=['aa','ab','ba','bb']
L2=['a', 'b', '']

def pref(mot):
    L = []
    for i in range(len(mot)+1):
        L.append(mot[:i])
    return list(L)

print(pref('coucou'))

def suf(mot):
    L = []
    for i in range(len(mot)+1):
        L.append(mot[i:])
    return list(L)

print(suf('coucou'))

def fact(mot):
    L = []
    
    return L

print(fact('coucou'))

def concatene(L1, L2):
    L3 = set()
    for e1 in L1:
        for e2 in L2:
            L3.add(e1+e2)
    return list(L3)

print(concatene(L1,L2))


# A CORRIGER
def puis(L1,n):
    L3 = set()
    for e1 in L1:
        for e2 in L1:
            L3.add(e1+e2)
    return list(filter(lambda s : len(s)==n,L3))

L1=['aa','ab','ba','bb']
print(puis(L1,2))
