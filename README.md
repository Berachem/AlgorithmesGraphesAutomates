# ⚛️ Algorithmie : Graphes & Automates
![download](https://user-images.githubusercontent.com/61350744/167305594-a64c5f66-7296-4549-8b49-1b4fa44d89a1.jpg)

## Définition : Graphes 📈
La théorie des graphes est la discipline mathématique et informatique qui étudie les graphes, lesquels sont des modèles abstraits de dessins de réseaux reliant des objets1. Ces modèles sont constitués par la donnée de sommets (aussi appelés nœuds ou points, en référence aux polyèdres), et d'arêtes(aussi appelées liens ou lignes) entre ces sommets ; ces arêtes sont parfois non-symétriques (les graphes sont alors dits orientés) et sont appelées des flèches ou des arcs.

## Définition : Automates 🤖

En informatique théorique, l'objectif de la théorie des automates est de proposer des modèles de mécanismes mathématiques qui formalisent les méthodes de calcul1. Cette théorie est le fondement de plusieurs branches importantes de l'informatique théorique, comme :

 - La calculabilité, par le modèle des machines de Turing ;
 - Les automates finis, et leurs variantes, qui sont utilisés dans l'analyse des langues naturelles, la traduction des programmes par les compilateurs, divers algorithmes de manipulation de textes comme les algorithmes de recherche de sous-chaîne, ou la vérification automatique du fonctionnement de circuits logiques;
 - La théorie de la complexité des algorithmes, visant à classifier les algorithmes en fonction des ressources temporelles et en mémoire nécessaires à leur exécution ;
 - La vérification de modèle qui sert à établir la conformité de programmes à leurs spécifications. Voir par exemple Coq.

## Programme #️⃣:

Avant toutes choses, il est important de mentionner que le langage utilisé pour ce projet est **python**🐍.

Le programme est composé de plusieurs fonctions permettant de représenter et manipuler des **langages** et **automates** simplement. De plus, il est possible d'opérer plusieurs transformations sur ces automates comme la **deterministation**, la **minimisation** ou encore la **complementation**. 

Un automate est représenté par un dictionnaire ayant comme clés des chaines de caractères et comme valeurs des listes. Les voici :
- "alphabet" : liste de caractères représentant **l'alphabet** de l'automate. 🅱️
- "etats" : liste de caractères représentant **les états** de l'automate. 🔹
- "transitions" : liste de listes, ces dernières sont composées de trois éléments. L'état de départ, l'étiquette (caractère), l'état d'arrivée. Elles représentent les **transitions** de l'automate. ↔
- "I" : liste de caractères représentant les états **initiaux** de l'automate. 🚩
- "F" : liste de caractères représentant les états **terminaux** de l'automate. 🏁
