
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
		if transi[1] == a and transi[0] in E:
			lst.append(transi[2])
	return list(set(lst))
      
print("lirelettre -> ",lirelettre(auto["transitions"],auto["etats"],'a'))


def liremot(T,E,m):
    new_E = E
    for a in m:
        new_E = lirelettre(T, new_E, a)
    return new_E
    
print("----------------------------------------------")	
print(liremot(auto["transitions"],auto["etats"],'aba'))
print("-----------------------------------------------")


def accepte(auto, m):
	return len(liremot(auto["transitions"],auto["etats"],m)) > 0

	   
	
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

print("est déterministe ? doc Test 1 (doit être True) ->" ,deterministe(auto0))
print("est déterministe ? doc Test 2 (doit être False) ->", deterministe(auto2))

def determinise(auto):
    I = [auto["I"]]
    etats = I.copy()
    transitions = list()
    cptMarquage = 0
    while cptMarquage<len(etats):
        
        for e in etats[cptMarquage]:
            for l in auto['alphabet']:
                listeEtatArriveAvecLettre = lirelettre(auto['transitions'],etats[cptMarquage], l)
                if (len(listeEtatArriveAvecLettre)>0):
                    if [etats[cptMarquage],l,listeEtatArriveAvecLettre] not in transitions:
                        transitions.append([etats[cptMarquage],l,listeEtatArriveAvecLettre])

                    if listeEtatArriveAvecLettre not in etats:
                        etats.append(listeEtatArriveAvecLettre)
                    
        cptMarquage+=1

    F = []
    for e in auto["F"]:
        for e2 in etats:
            if e in e2 and e2 not in F:
                F.append(e2)
    
    
    return {
            'alphabet': auto["alphabet"],
            'transitions' : transitions,
            'etats':etats,
            "I" :I,
            "F": F
            }
		
auto2Determinise = {'alphabet': ['a', 'b'], 
'I': [[0]], 
'transitions': [[[0], 'a', [0, 1]], [[0, 1], 'a', [0, 1]], [[0, 1], 'b', [1]], [[1], 'a', [1]], [[1], 'b' ,[1]]], 
'etats': [[0], [0, 1], [1]], 
'F': [[0, 1], [1]]}

print("déterminisation doc Test (doit être True) -> ",determinise(auto2)==auto2Determinise)

def renommage(auto):
    cpt = 0
    renomme=dict()
    for e in auto["etats"]:
        renomme[frozenset(e)] = cpt
        cpt+=1
        
    etats = list(renomme.values())
    alphabet = auto["alphabet"]
    I = list(map(lambda e :renomme[frozenset(e)], auto["I"] ))
    F = list(map(lambda e :renomme[frozenset(e)], auto["F"] ))
    transitions = list(map(lambda l : [renomme[frozenset(l[0])], l[1], renomme[frozenset(l[2])]], auto["transitions"] ))
    return {'alphabet': alphabet, 
'I': I, 
'transitions': transitions, 
'etats': etats, 
'F': F}

auto2Renomme = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2],'transitions': [[0, 'a', 1], [1, 'a', 1],[1, 'b', 2], [2, 'a', 2], [2, 'b', 2]],'I': [0], 'F': [1, 2]}

print("renommage doc Test (doit être True)-> ",renommage(determinise(auto2))==auto2Renomme)


# Complementation 

auto3 = {"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

def complet(auto):
  dico_verif = {}
  for transi in auto['transitions']:
    if transi[0] not in dico_verif.keys():
      dico_verif[transi[0]] = set()
    dico_verif[transi[0]].add(transi[1])

  for etat in dico_verif.keys():
    if len(dico_verif[etat]) != len(auto['alphabet']):
      return False

  return True


print()
print("test complet (doit être False) -> " + str(complet(auto0)))
print("test complet (doit être True) -> " + str(complet(auto1)))

def complete(auto):
  if complet(auto):
    return auto
  else:
    transitions = auto['transitions']
    nomEtatPuis = max(auto['etats'])+1
    dico_verif = {}
    for transi in auto['transitions']:
      if transi[0] not in dico_verif.keys():
        dico_verif[transi[0]] = set()
        dico_verif[transi[2]] = set()
      dico_verif[transi[0]].add(transi[1])

    for etat in dico_verif.keys():
      for lettre in auto['alphabet']:
        if lettre not in dico_verif[etat]:
          transitions.append([etat, lettre, nomEtatPuis])

    transitions.append([nomEtatPuis, 'a', nomEtatPuis])
    transitions.append([nomEtatPuis, 'b', nomEtatPuis])

    etats = auto['etats']
    etats.append(nomEtatPuis)

    return {'alphabet': auto['alphabet'], 
'I': auto['I'], 
'transitions': transitions, 
'etats': etats, 
'F': auto['F']}

print()
print("Doc Test pour savoir si ça complète bien (doit être True) -> " ,complete(auto0)=={'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4],
'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3],
[0, 'b', 4], [2, 'b', 4], [3, 'a', 4], [3, 'b', 4], [4, 'a', 4], [4, 'b', 4]],
'I': [0], 'F': [3]})
print("test pour savoir si c'est bien complet (doit être True) -> " + str(complet(auto0)))

def complement(auto):
  auto_new = determinise(auto)
  auto_new = renommage(auto_new)
  auto_new = complete(auto_new)
  
  new_etat = []
  for etat in auto_new['etats']:
    if etat not in auto_new['F']:
        new_etat.append(etat)

  auto_new['F'] = new_etat

  return auto_new

print()
print("Doc Test pour savoir si le complement est bon (doit être True) -> ",complement(auto3)=={'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3],
'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'b', 2],
[0, 'b', 3], [2, 'a', 3], [3, 'a', 3], [3, 'b', 3]], 'I': [0], 'F': [0, 1, 3]}
)

# Produit

auto4 ={"alphabet":['a','b'],"etats": [0,1,2,],
"transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}

auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
"I":[0],"F":[0,1]}

def inter(auto1,auto2):
    autos = [auto1,auto2]
    etats = [(auto1["I"][0],auto2["I"][0])]
    transitions = list()
    cptMarquage = 0
    while cptMarquage<len(etats):
        
        for couple in etats:
            
            for i in range(len(etats[cptMarquage])):
                for lettre in autos[i]['alphabet']:
                    listeEtatArriveAvecLettre = lirelettre(autos[i]['transitions'],[etats[cptMarquage][i]], lettre)
                    print("avec un "+lettre+" on peut aller d'un "+str(etats[cptMarquage][i]) + " à "+str(listeEtatArriveAvecLettre) + " cf automate " + str(i+1))
                    for EtatArrive in listeEtatArriveAvecLettre:
                        
                        coupleDestination = list(etats[cptMarquage])
                        coupleDestination[i] = EtatArrive
                        coupleDestination = tuple(coupleDestination)
                        if [etats[cptMarquage], lettre, coupleDestination] not in transitions:
                            transitions.append([etats[cptMarquage],lettre,coupleDestination])
                            print([etats[cptMarquage],lettre,coupleDestination])

                        if (coupleDestination) not in etats:
                            etats.append(coupleDestination)
                            print(etats)
                    
        cptMarquage+=1
    return {
        'alphabet': auto1['alphabet'], 
        'I': [tuple([auto1['I'][0],auto2['I'][0]])], 
        'transitions': transitions, 
        'etats': etats, 
        'F': list(filter(lambda etat : etat[0] in auto1["F"] and etat[1] in auto2["F"], etats))
    }
    
    
print(inter(auto4,auto5))
    