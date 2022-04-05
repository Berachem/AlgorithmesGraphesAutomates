
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

def initTransitions() :
	transi = list()
	n = int(input("Combien y'a't'il de transistions ? : "))
	for i in range(n):
		l = input("Entrez l'état de départ, l'étiquette et l'état d'arrivé (séparé par un espace) : ").split(" ")
		if l not in transi:
			transi.append(l)
	return list(transi)

def defauto():
    auto = dict()
    auto['alphabet'] = []
    auto['etats'] = []
    auto ['transitions'] = []
    auto ['I'] = []
    auto ['F'] = []
    
    auto['alphabet'] = list(set(input("Entrez l'alphabet (le séparateur est un espace) : ").split(" ")))
    auto['etats'] = list(set(input("Entrez le nom des états (le séparateur est un espace) : ").split(" ")))
    auto['transitions'] = initTransitions()
		
    auto['I'] = input("Entrez vos état initiaux : ").split(" ")
    auto['F'] = input("Entrez vos états terminaux : ").split(" ")

    return auto

#print(defauto())

auto ={"alphabet":['a','b'],"etats": [1,2,3,4],
"transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],
"I":[1],"F":[4]}
print("L'automate de base est :", auto)



def lirelettre(T, E, a):
	lst = []
	for transi in T:
		if transi[1] == a:
			lst.append(transi[2])
	return list(set(lst))
      
print(lirelettre(auto["transitions"],auto["etats"],'a'))

"""
def liremot(T,E,m):
  En = lirelettre(T, E, a)
  for a in m:
    lirelettre(T, En, a)

  return En

		
print(liremot(auto["transitions"],auto["etats"],'aba'))


def accepte(auto, m):
	return len(liremot(auto["transitions"],auto["etats"],m))>0
"""
	   
	
def langage_accept(auto, n):
	liste = []
	for m in tousmots(auto['alphabet'],n):
		if (accepte(auto,m)):
			liste.append(m)
	return liste

def initNewDico(auto):
    occurencesLettre = dict()
    for l in auto['alphabet']:
        occurencesLettre[l]=0
    return occurencesLettre

def deterministe(auto):
    if len(auto["I"])>1:
        return False
        
    for etat in auto['etats']:
        tmpOccurencesLettre = initNewDico(auto)
        for t in auto['transitions']:
            if etat==t[0]:
                tmpOccurencesLettre[t[1]]+=1
        if (any(filter(lambda x:x>1, tmpOccurencesLettre.values()))):
            return False
    return True
			
auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
"transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
auto1 ={"alphabet":['a','b'],"etats": [0,1],
"transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
auto2={"alphabet":['a','b'],"etats": [0,1],
"transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

print(deterministe(auto0))
print(deterministe(auto2))

def determinise(auto):
	I = list(auto["I"])
	etats = list()
	etats.append(I)
	transitions = list()
	cptMarquage = 0
	while cptMarquage<len(etats):
		
		for l in auto['alphabet']:
			listeEtatArriveAvecLettre = lirelettre(auto['transitions'],auto['etats'], l)
			if (len(listeEtatArriveAvecLettre)>0):
				transitions.append([etats[cptMarquage],l,listeEtatArriveAvecLettre])
				etats.append(listeEtatArriveAvecLettre)
		cptMarquage+=1
	return {
			'transitions' : transitions
		}
		
print(determinise(auto2))