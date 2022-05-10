
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
    return "".join(mot[::-1]) # On parcours le mot à l'envers

print("miroir -> ", miroir('coucou'))

def concatene(L1, L2):
    L3 = set()
    for e1 in L1:
        for e2 in L2:
            L3.add(e1+e2)
    return list(L3)

print("concatene -> ",concatene(L1,L2))


def puis(L1,n):
    if n != 0:
        ans = L1[:]
        for _ in range(n - 1):
            ans = [word + char for word in ans for char in L1] # On concatene les mots de ans avec ceux de L1 n - 1 fois
        return list(set(ans)) # On supprime les doublons avec set() 
    return ['']

L1=['aa','ab','ba','bb']
print("puissance (L^n) -> ",puis(L1,2))

# Étant donné que A* a une taille infini, il est impossible de coder
# une fonction le calculant

def tousmots(L1,n):
    L = set() # set() pour éliminer les doublons
    for i in range(n+1):
        L = L.union(set(puis(L1, i))) # On fait l'union des puis de 1 à n
        
    return list(filter(lambda mot: len(mot)<=n,L))

print("tousmots -> ",tousmots(['a','b'],3))

def initTransitions(): # Fonction intermédiaire
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

# print(defauto())

auto = {"alphabet":['a','b'],"etats": [1,2,3,4],
"transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],
"I":[1],"F":[4]}
print("L'automate de base est :", auto)

def lirelettre(T, E, a):
	lst = []
	for transi in T:
		if transi[1] == a and transi[0] in E:
            # Si transi part d'un état de E et lis la letrre a, alors
            # on ajoute l'état d'arriver.
			lst.append(transi[2])
	return list(set(lst))
      
print("lirelettre -> ",lirelettre(auto["transitions"],auto["etats"],'a'))


def liremot(T,E,m): 
    # On lis chaque lettre du mot jusqu'à ce que le mot soit fini
    # puis on ajoute dans une liste l'états l'état d'arrivé de la dernière lettre
    new_E = E
    for a in m:
        new_E = lirelettre(T, new_E, a)
    return new_E
    
print("----------------------------------------------")	
print(liremot(auto["transitions"],auto["etats"],'aba'))
print("-----------------------------------------------")

def accepte(auto, m):
	return any(map(lambda x : x in auto["F"], liremot(auto["transitions"],auto["etats"],m)))
    # Si au moins un des états d'arrivés de liremot est dans la liste des états finaux de l'automate,
    # cela signifie que l'automate accepte le mot.
    # Alors on return true.
    
def langage_accept(auto, n):
	liste = []
	for m in tousmots(auto['alphabet'], n): 
        # On vérifie pour chaque mot de longueur inférieur à n s'il est accepté
        # par l'automate
		if (accepte(auto,m)):
			liste.append(m)
	return liste

# On ne peut pas faire de fonction calculant le langage accepté par 
# un automate car ce langage peut contenir
# une infinité de mots

def initNewDico(auto): # Fonction intermédiaire
    occurencesLettre = dict()
    for l in auto['alphabet']:
        occurencesLettre[l] = 0
    return occurencesLettre

def deterministe(auto):
    if len(auto["I"]) > 1:
        return False
        
    for etat in auto['etats']:
        tmpOccurencesLettre = initNewDico(auto)
        for t in auto['transitions']:
            if etat == t[0]:
                tmpOccurencesLettre[t[1]] += 1
                # On compte le nombre d'ocurrences d'une lettre dans les états de départs d'une transition
                # si la lettre apparait plus d'une fois, l'automate n'est pas deterministe.
        if (any(filter(lambda x : x > 1, tmpOccurencesLettre.values()))):
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
    while cptMarquage < len(etats):
        
        for e in etats[cptMarquage]:
            for l in auto['alphabet']:
                listeEtatArriveAvecLettre = lirelettre(auto['transitions'], etats[cptMarquage], l)
                if (len(listeEtatArriveAvecLettre) > 0):
                    if [etats[cptMarquage],l,listeEtatArriveAvecLettre] not in transitions:
                        transitions.append([etats[cptMarquage],l,listeEtatArriveAvecLettre])

                    if listeEtatArriveAvecLettre not in etats:
                        etats.append(listeEtatArriveAvecLettre)
                    
        cptMarquage += 1

    F = []
    for e in auto["F"]:
        for e2 in etats:
            if e in e2 and e2 not in F:
                F.append(e2)
    
    
    return {
            'alphabet': auto["alphabet"],
            'transitions': transitions,
            'etats': etats,
            "I": I,
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
    renomme = dict()
    for e in auto["etats"]:
        # Pour chaque états, on associe un nombre qui s'incremente à chaque état
        renomme[frozenset(e)] = cpt
        cpt += 1
        
    etats = list(renomme.values())
    alphabet = auto["alphabet"]
    I = list(map(lambda e :renomme[frozenset(e)], auto["I"] ))
    F = list(map(lambda e :renomme[frozenset(e)], auto["F"] ))
    transitions = list(map(lambda l : [renomme[frozenset(l[0])], l[1], renomme[frozenset(l[2])]], auto["transitions"]))
    return {'alphabet': alphabet, 
            'I': I, 
            'transitions': transitions, 
            'etats': etats, 
            'F': F
            }

auto2Renomme = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2],'transitions': [[0, 'a', 1], [1, 'a', 1],[1, 'b', 2], [2, 'a', 2], [2, 'b', 2]],'I': [0], 'F': [1, 2]}

print("renommage doc Test (doit être True)-> ", renommage(determinise(auto2)) == auto2Renomme)


# Complementation 

auto3 = {"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

def complet(auto):
  dico_verif = {}

  for transi in auto['transitions']: 
      # On créer un dico avec comme clés des états et comme valeurs un ensemble contenant les lettres qui partent de cet états
    if transi[0] not in dico_verif.keys():
      dico_verif[transi[0]] = set()
    dico_verif[transi[0]].add(transi[1])

  for etat in dico_verif.keys():
      # On vérifie que les états de l'automate ont autant de lettre qui partent d'eux qu'il y a de lettre dans l'alphabet
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
    if type(auto['etats'][0]) is tuple:
        nomEtatPuis = -1
    else:
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
  # Tous les états qui n'étaient pas terminaux le deviennent
  # Et ceux qui l'etaient ne le sont plus

  return auto_new

print()
print("Doc Test pour savoir si le complement est bon (doit être True) -> ",complement(auto3)=={'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3],
'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'b', 2],
[0, 'b', 3], [2, 'a', 3], [3, 'a', 3], [3, 'b', 3]], 'I': [0], 'F': [0, 1, 3]}
)

# Produit

auto4 ={"alphabet":['a','b'],"etats": [0,1,2],
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
        
        couple = etats[cptMarquage]
        for lettre in autos[0]['alphabet']:
            coupleDestination = [-1,-1]
            for i in range(len(couple)):
                #print(couple[i],"----",lettre)
                EtatArriveAvecLettre = lirelettre(autos[i]['transitions'],[couple[i]], lettre)
                if EtatArriveAvecLettre:
                    coupleDestination[i] = EtatArriveAvecLettre[0]
                    
            if -1 not in coupleDestination :
                for j in range(len(coupleDestination)):
                    if coupleDestination[j]==-1:
                        coupleDestination[j]= couple[j]
                
                coupleDestination = tuple(coupleDestination)
                #print(coupleDestination)
                if [couple, lettre, coupleDestination] not in transitions:
                    transitions.append([couple,lettre,coupleDestination])
                    #print([couple,lettre,coupleDestination])

                if coupleDestination not in etats:
                    etats.append(coupleDestination)
                    
        cptMarquage+=1
    return {
        'alphabet': auto1['alphabet'], 
        'I': [tuple([auto1['I'][0],auto2['I'][0]])], 
        'transitions': transitions, 
        'etats': etats, 
        'F': sorted(list(filter(lambda etat : etat[0] in auto1["F"] and etat[1] in auto2["F"], etats)))
    }
    
    
print("Doc Test Intersection (doit être True) ->",inter(auto4,auto5) == {'alphabet': ['a', 'b'], 'I': [(0, 0)], 
'transitions': [[(0, 0), 'a', (1, 0)], [(1, 0), 'b', (2, 1)], [(2, 1), 'a', (2, 1)],
                [(2, 1), 'b', (2, 2)],[(2, 2), 'a', (2, 2)], [(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)],[(2, 0), 'b', (2, 1)]],
'etats': [(0, 0), (1, 0), (2, 1), (2, 2), (2, 0)], 'F': [(2, 0), (2, 1)]})
    
print("Doc Test Intersection et renommage (doit être True) ->",renommage(inter(auto4,auto5))=={'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4], 'transitions': [[0, 'a', 1],
[1, 'b', 2], [2, 'a', 2], [2, 'b', 3], [3, 'a', 3], [3, 'b', 4], [4, 'a', 4],
[4, 'b', 2]], 'I': [0], 'F': [4, 2]})

def difference(auto1,auto2):
    # On les redéfinis localement par leurs versions complétées
    auto1 = complete(auto1)
    auto2 = complete(auto2)
    autos = [auto1,auto2]
    etats = [(auto1["I"][0],auto2["I"][0])]
    transitions = list()
    cptMarquage = 0
    while cptMarquage < len(etats):
        
        couple = etats[cptMarquage]
        for lettre in autos[0]['alphabet']:
            coupleDestination = [-1,-1]
            for i in range(len(couple)):
                #print(couple[i],"----",lettre)
                EtatArriveAvecLettre = lirelettre(autos[i]['transitions'],[couple[i]], lettre)
                if EtatArriveAvecLettre:
                    coupleDestination[i] = EtatArriveAvecLettre[0]
                    
            if -1 not in coupleDestination :
                for j in range(len(coupleDestination)):
                    if coupleDestination[j]==-1:
                        coupleDestination[j]= couple[j]
                
                coupleDestination = tuple(coupleDestination)
                #print(coupleDestination)
                if [couple, lettre, coupleDestination] not in transitions:
                    transitions.append([couple,lettre,coupleDestination])
                    #print([couple,lettre,coupleDestination])

                if coupleDestination not in etats:
                    etats.append(coupleDestination)
                    
        cptMarquage+=1
    return {
        'alphabet': auto1['alphabet'], 
        'etats': sorted(etats), 
        'transitions': sorted(transitions), 
        'I': [tuple([auto1['I'][0],auto2['I'][0]])], 
        'F': sorted(list(filter(lambda etat : etat[0] in auto1["F"] and etat[1] not in auto2["F"], etats))) 
    }
    
print("Doc Test Différence (doit être True) ->",difference(auto4,auto5)['etats'] =={'alphabet': ['a', 'b'], 'I': [(0, 0)], 'transitions': sorted([[(0, 0), 'a', (1, 0)],
[(0, 0), 'b', (3, 1)], [(3, 1), 'a', (3, 1)], [(3, 1), 'b', (3, 2)],
[(3, 2), 'a', (3, 2)], [(3, 2), 'b', (3, 0)], [(3, 0), 'a', (3, 0)],
[(3, 0), 'b',(3, 1)], [(1, 0), 'a', (3, 0)], [(1, 0), 'b', (2, 1)],
[(2, 1), 'a', (2, 1)], [(2, 1), 'b', (2, 2)], [(2, 2), 'a', (2, 2)],
[(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)], [(2, 0), 'b', (2, 1)]]),
'etats': sorted([(0, 0), (3, 1), (3, 2), (3, 0), (1, 0), (2, 1), (2, 2), (2, 0)]),
'F': [(2, 2)]}['etats'])


autoDiffRenommage = {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4, 5, 6, 7],
'transitions': [[0, 'a', 4], [0, 'b', 1], [1, 'a', 1], [1, 'b', 2],
[2, 'a', 2], [2, 'b', 3], [3, 'a', 3], [3, 'b', 1], [4, 'a', 3],
[4, 'b', 5], [5, 'a', 5], [5, 'b', 6], [6, 'a', 6], [6, 'b', 7],
[7, 'a', 7], [7, 'b', 5]], 'I': [0], 'F': [6]}
print("Différence et Renommage marche correctement (vérifiée à la main)")

# Propriétés de fermeture

def prefixe(auto):
    new_F = []
    for etat in auto['etats']:
        new_F.append(etat)
        # Tous les états deviennent finaux

    return {"alphabet": auto['alphabet'], 
            "etats": auto['etat'],
            "transitions": auto['transitions'],
            "I": auto['I'],
            "F": new_F}

def suffixe(auto):
    new_I = []
    for etat in auto['etats']:
        new_I.append(etat)
        # Tous les états deviennent initiaux
        
    return {"alphabet": auto['alphabet'], 
            "etats": auto['etat'],
            "transitions": auto['transitions'],
            "I": new_I,
            "F": auto['F']}

def facteur(auto):
    new_F = []
    new_I = []
    for etat in auto['etats']:
        new_F.append(etat)
        new_I.append(etat)
        # Tous les états deviennent initiaux et finaux
        
    return {"alphabet": auto['alphabet'], 
            "etats": auto['etat'],
            "transitions": auto['transitions'],
            "I": new_I,
            "F": new_F}

def miror(auto): # le nom n'est pas celui de l'énoncé car une fonction porte déjà le nom "miroir"
    new_transitions = []
    for transi in auto['transitions']:
        # on inverse le sens des flèches
        new_transitions.append([transi[2], transi[1], transi[0]])
        
    return {"alphabet": auto['alphabet'], 
            "etats": auto['etat'],
            "transitions": new_transitions,
            "I": auto['F'], # On inverse etat initiaux et terminaux
            "F": auto['I']}


# Minimisation

auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],
[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],
"I":[0],"F":[0,1,2,5]}

def tableTransitions(auto):
    # Renvoie la table de transitions d'un automate
    table = dict()
    nbLettres= len(auto["alphabet"])
    for e in auto["etats"]:
        table[e] = list()
        for i in range(nbLettres):
            table[e].append(lirelettre(auto['transitions'],[e],auto["alphabet"][i])[0])
    return table

def memeClasseEquivalenceAuRang(auto,rang,a,b):
    # Renvoie vrai si a et b appartiennent à la meme
    # classe d'équivalence à un rang 'rang'
    for sous_classe in classe(auto,rang):
        if (a in sous_classe) and (b in sous_classe):
            return True
    return False

def ajouteDansLaListe(listeClasse, e, e2):
    # S'occupe de bien place deux etats équivalents
    added = False
    for ensemble in listeClasse:
        if e in ensemble or e2 in ensemble:
            ensemble.add(e)
            ensemble.add(e2)
            added = True
            break
    if not added:
        # On crée une classe juste pour eux deux
        listeClasse.append(set([e,e2]))		
        
            

def classe(auto,rang):
    # Renvoie la classe d'équivalence à un certain rang d'un automate
    # réprésenté sous la forme d'une liste d'ensembles
    
    if rang ==0:
        # On renvoie 2 classes : ceux terminaux et les autres
        set_difference = set(auto['etats']) - set(auto["F"])
        return [set_difference,set(auto["F"])]
    else:
        # On va s'aider de la table de transitions
        listeClasse = list()
        
        nbLettres= len(auto["alphabet"])
        table = tableTransitions(auto)
        for e in table.keys():
            estEquivalentAvecLesAutres=[]
            for e2 in table.keys():
                if (e != e2):
                    
                    sontEquivalents = True
                    for i in range(nbLettres):
                        # On applique la formule (ici négation) pour d'ils qu'ils NE sont PAS équivalents
                        if not( memeClasseEquivalenceAuRang(auto,rang-1,e,e2) and\
                        memeClasseEquivalenceAuRang(auto,rang-1,table[e][i],table[e2][i])):
                            sontEquivalents = False
                            break

                            
                    if sontEquivalents:
                        #On les place dans la même sous liste
                        ajouteDansLaListe(listeClasse,e,e2)

                    estEquivalentAvecLesAutres.append(sontEquivalents)
                    
            if not any(estEquivalentAvecLesAutres):
                #On le place seul car il est équivalent à personne
                listeClasse.append(set([e]))

        return listeClasse

def reassembleAutomate(auto, lst_classes): # Réassemble l'automate à partir des classes d'équivalences
    new_auto = {"alphabet": auto['alphabet'],
                "etats": [],
                "transitions": [],
                "I": [],
                "F": []}

    # On determine l'etat initial
    for classe in lst_classes:
        if auto['I'][0] in classe:
            etat_i = classe
    new_auto['I'].append(list(etat_i))

    # Les etats 
    etats = []
    for etat in lst_classes:
        etats.append(list(etat))
    new_auto['etats'] = etats

    # Les transitions
    for etat_depart in new_auto['etats']:
        for lettre in auto['alphabet']:
            etat_arrivée = lirelettre(auto['transitions'], etat_depart, lettre)
            for classe in lst_classes:
                if etat_arrivée[0] in classe:
                    classe_arrivée = classe
            new_auto['transitions'].append([list(etat_depart), lettre, list(classe_arrivée)])

    # etats finaux
    for classe in lst_classes:
        for etat_f in auto['F']:
            if etat_f in classe and list(classe) not in new_auto['F']:
                new_auto['F'].append(list(classe))

    return new_auto
                
def EtatMinimise(auto):
    # Regarde quand on obtient deux classes d'équivalences équivalentes successives
    # lorsque c'est le cas, on réassemble à partir de cet classe d'équivalence
    rang = 0
    listeClassePrecedente = []
    listeClasseActuel = sorted(classe(auto,rang))
    print("rang ",rang," - ",listeClasseActuel)
    while listeClasseActuel != listeClassePrecedente:
        listeClassePrecedente = listeClasseActuel
        rang += 1
        listeClasseActuel = sorted(classe(auto,rang))
        print("rang ",rang," - ",listeClasseActuel)
    return reassembleAutomate(auto, listeClasseActuel)
        
						

print("-----------------------------------")
print("Doc Test Minimise (Doit être True): ",EtatMinimise(auto6)=={'alphabet': ['a', 'b'], 'etats': [[0], [1, 2, 5], [3], [4]], 
'transitions': [[[0], 'a', [4]], [[0], 'b', [3]], [[1, 2, 5], 'a', [1, 2, 5]],
[[1, 2, 5], 'b', [1, 2, 5]], [[3], 'a', [1, 2, 5]], [[3], 'b', [0]],
[[4], 'a', [1, 2, 5]], [[4], 'b', [1, 2, 5]]], 'I': [[0]], 'F': [[0], [1, 2, 5]]})
print()
print()
print("---------------------------------")

print("Doc Test renommage : ",renommage(EtatMinimise(auto6))=={'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3], 'transitions': [[0, 'a', 3],
[0, 'b', 2], [1, 'a', 1], [1, 'b', 1], [2, 'a', 1], [2, 'b', 0], [3, 'a', 1],
[3, 'b', 1]], 'I': [0], 'F': [0, 1]})

print("------Moment de stresse------")

auto1 = {
    'alphabet' : ['a', 'b'],
    'etats' : [1,2,3,4],
    'transitions' : [[1,'a',2], [1, "b" ,2], [2 , "b", 1], [2, "a", 4], [4, "a", 2], [3, "b", 4], [4, "b", 3], [1, "a", 3]],
    'I' : [1,4],
    'F' : [3,4]
}

print()
print(renommage(determinise(auto1)))
print()

auto2 = {
    'alphabet' : ['a', 'b'],
    'etats' : [0,1],
    'I' : [0],  
    'F' : [0], 
    'transitions' : [[0,'a',0], [0,'b',1],[1,'a',1],[1,'b',0]]
}

auto3 = {
    'alphabet' : ['a', 'b'],
    'etats' : [0,1,2],
    'I' : [0],  
    'F' : [0], 
    'transitions' : [[0,'b',0], [0,'a',1],[1,'b',1],[1,'a',2],[2,'b',2],[2,'a',0]]
}

print(renommage(inter(auto2,auto3)))
print()

auto4 = {
    'alphabet' : ['a', 'b'],
    'etats': [1,2,3,4,5,6],
    'I' : [1],  
    'F' : [5,6],
    'transitions' : [[1,'a',2],[1,'b',2] ,[2,'a',3],[2,'b',4],[3,'b',5],[3,'a',4],[4,'a',3],[4,'b',6],[5,'b',5],[5,'a',6],[6,'b',6],[6,'a',5]] 
    
}
print(EtatMinimise(auto4))
