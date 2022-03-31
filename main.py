
L1=['aa','ab','ba','bb']
L2=['a', 'b', '']

def pref(mot):
    L = []
    for i in range(len(mot)+1):
        L.append(mot[:i])
    return list(L)

print("prefixe ->",pref('coucou'))

def suf(mot):
    L = []
    for i in range(len(mot)+1):
        L.append(mot[i:])
    return list(L)

print("suffixe -> ",suf('coucou'))

def fact(mot):
    L = set()
    for i in range(len(mot)):
        for j in range(i,len(mot)):
            L.add(mot[i:j+1])
    L.add("")
    return sorted(list(L))

print("facteur -> ",fact('coucou'))


def miroir(mot):
    return "".join(mot[::-1])

print("miroir -> ", miroir('coucou'))

def concatene(L1, L2):
    L3 = set()
    for e1 in L1:
        for e2 in L2:
            L3.add(e1+e2)
    return list(L3)

print("concatene -> ",concatene(L1,L2))


def puis(L1,n):
    if n!=0:
        ans = L1[:]
        for _ in range(n - 1):
            ans = [word + char for word in ans for char in L1]
        return list(set(ans))
    return ['']

L1=['aa','ab','ba','bb']
print("puissance (L^n) -> ",puis(L1,2))


def tousmots(L1,n):
    L = set()
    for i in range(n+1):
        L = L.union(set(puis(L1,i)))
        
    return list(filter(lambda mot: len(mot)<=n,L))

print("tousmots -> ",tousmots(['a','b'],3))
