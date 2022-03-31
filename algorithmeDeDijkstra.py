# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:33:08 2021

@author: assane
"""
donnees=('GrapheDeTest', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
         [('A', 'A', 2), ('A', 'B', 5), ('A', 'C', 8), ('B', 'C', 6),
          ('B', 'D', 8), ('B', 'E', 6), ('C', 'B', 2), ('C', 'D', 1),
          ('C', 'E', 2), ('D', 'E', 3), ('D', 'F', 1), ('E', 'A', 5),
          ('E', 'D', 1), ('E', 'G', 5), ('F', 'D', 4), ('F', 'E', 1),
          ('F', 'G', 3), ('F', 'H', 6), ('E', 'I', 3), ('G', 'H', 2),
          ('H', 'B', 6), ('H', 'B', 7), ('I', 'J', 4), ('J', 'I', 5)])

nomGraphe, nomSommets, donneesArc = donnees

# On importe les blibliothèques requises pour représenter le graphe
from graphviz import Digraph
from graphviz import Source

class Graphe():
    
    # Classe utilisée pour représenter un graphe
    def __init__(self, nomDonne):
        self.nom = nomDonne         # le nom du graphe
        self.listeSommets = []      # liste des sommets du graphe
        self.listeArcs = []         # liste des arcs du graphe
        self.sommetNomme = {}       # dictionnaire ayant pour clé le nom d'un sommet et pour valeur l'objet sommet correspondant 
        
    # Cette méthode retourne l'objet graphe
    def __repr__(self):
        return f'Graphe : {self}'
        
    # Méthode affichant le nom du graphe en utilisant la fonction "print"
    def __str__(self):
        return f'{self.nom}'
    
    # Méthode qui permet d'ajouter l'item : "nom de sommet, objet sommet" dans sommetNomme
    def ajouterSommet(self, nomSommet):
        objSommet = Sommet(nomSommet)
        self.listeSommets.append(objSommet)
        self.sommetNomme[nomSommet] = objSommet
    
    # Méthode qui permet d'ajouter un arc à la liste des arcs
    def ajouterArc(self, poids, nomDepart, nomArrivee):
        sommetDepart = self.sommetNomme[nomDepart]
        sommetArrivee = self.sommetNomme[nomArrivee]
        objArc = Arc(poids, sommetDepart, sommetArrivee)
        self.listeArcs.append(objArc)
    
    # Méthode
    def calculerDistance(self):
        for sommet in self.listeSommets:
            sommet.calculerSuccesseur()
            
    # Méthode qui affiche le plus long des plus courts chemin sous forme textuel en cosole
    # et retourne une liste des sommets constituant ce chemin.
    def plusLongDesPlusCourtsChemins(self) :
        resultat = 0
        texte2 = "\nPlus long des plus courts chemins :\n"
        for depart in g1.listeSommets:
            for arrivee in g1.listeSommets:
                if depart in arrivee.distanceDepuis.keys():
                    if arrivee.distanceDepuis[depart] > resultat:
                        resultat = arrivee.distanceDepuis[depart]
                        sommetDarrivee = arrivee
                        sommetDeDepart = depart
        listeSommets = []
        sommetPrecedent = sommetDarrivee
        while sommetPrecedent != sommetDeDepart:
            listeSommets.append(str(sommetPrecedent))
            sommetPrecedent = sommetPrecedent.dernierArcDepuis[sommetDeDepart].sommetDepart
        listeSommets.append(str(sommetDeDepart))
        listeSommets.reverse()
        chemin = "\n\t- "
        chemin += " -> ".join(listeSommets)
        texte2 += f"\n- Entre {sommetDeDepart} et {sommetDarrivee} : distance de {resultat}\n"
        texte2 += chemin
        print(texte2)
        return(listeSommets)
            
    # Méthode qui permet d'afficher le tableau des distances minimales entre les sommets
    # d'un graphe dans la console et de générer un fichier html contenant ce tableau
    def afficherGraphe(self):
        
        # On initialise une variable "texte" qui sera le texte affiché sur la console
        texte="\nDistance entre les sommets :\n\n" 
        
        # On crée un fichier html en mode écriture
        fileOut = open("fichierHTML.html","w")
        
        # On initialise une variable "table" dans lequel sera codé notre
        # table en langage html
        table = '<table cellpadding="10" border= "1" align="center">\n'     # On centre le tableau sur la page html
        table += '<caption align="top"> Distance minimale entre les sommets</caption>\n' # j'intitule le tableau "Distance minimale entre les sommets"
        table += '<tr>\n'       # On crée la première ligne du tableau
        table += "<th></th>\n"  # On crée une case vide correspondant à la 1ère ligne 1ère colonne
        
        # On parcours la liste des sommets la liste des sommets du graphe d'arrivée
        # et à chaque itération on enrichie notre texte et table d'un sommet 
        for arrivee in g1.listeSommets :
            texte += f'\t{arrivee}'
            table += f"<th>{arrivee}</th>\n" # Chaque sommet d'arrivée est le titre d'une colonne
        table += "</tr>\n"  # Après avoir inscrit tous les sommets, on en a fini avec la 1ère ligne du tableau html
        table += '<tr>\n'   # On remplis les autres lignes du tableau successivement
        
        # On parcours la liste des sommets de départ en remplissant 
        # à chaque itération une ligne du tableau html et la ligne du texte correspondante
        for depart in g1.listeSommets:
            texte += f'\n{depart}'  # On ajoute le sommet de départ en début de ligne du texte
            table += f"\t<th>{depart}</th>\n"   # Chaque sommet de départ est le titre d'une ligne du tableau
            
            # Pour chaque sommet de départ, on enrichie respectivement le texte et le tableau
            # hrml de la distance qui le sépare des autres sommets du graphe s'il existe
            # sinon on insére le caractère "-" à la cellule correspondante
            for arrivee in g1.listeSommets :
                if depart in arrivee.distanceDepuis.keys():
                    texte += f'\t{arrivee.distanceDepuis[depart]}'
                    table += f'<td>{arrivee.distanceDepuis[depart]}</td>\n'
                else:
                    texte += "\t-"
                    table += "\t<td>-</td>"
            table += "</tr>\n" # On en a fini avec cette ligne du tableau html, oncontinue de parcourir la liste des sommets de départ
        
        # Une fois la lise des sommets de départ intégralement parcourue, on affiche
        # le texte qui est sous forme de tableau dans la console
        print(texte)
        fileOut.writelines(table) # On écrit le code html généré par le programme sur le fichier html ouvert
        fileOut.close() # On ferme le fichier une fois le code entièrement écrite
        
    
class Sommet():
    
    # Classe utilisée pour représenter un sommet
    def __init__(self, nom):
        self.nomSommet = nom    # Le nom du sommet
        self.arcSortants = []   # liste des arcs sortants
        self.distanceDepuis = {}    # dictionnaire ayant pour clé le nom d'un sommet A et pour valeur la distance le entre ce sommet A et un sommet B en paramètre 
        self.dernierArcDepuis = {}  # dictionnaire ayant pour clé le nom d'un sommet A et pour valeur l'arc entre ce sommet A et un sommet B en paramètre
        
    # Méthode pour déterminer les arcs sortnts d'un sommet
    def ajouterArcSortant(self, nouvelArc):
        self.arcSortants.append(nouvelArc)
        
    # Méthode qui détermine successeur d'un sommet ainsi que la distance entre les deux sommets
    def calculerSuccesseur(self):
        sommetDepart = self         # On initialise le sommet de départ
        sommetPlusProche = self     # On initialise le sommet le plus proche au sommet en question
        distanceDepuisDepart = 0    # On initialise la distance depuis départ à 0
        sommetsDecouverts = [sommetPlusProche]  # Liste des sommets découverts, ne contenant que le sommet le plus proche
        sommetsAtteintsAuPlusCourt = []     # liste des sommets atteints au plus proche initialisé vide
        
        # Tant qu'on découvre des sommets
        while sommetsDecouverts:
            
            # Actualisation des listes
            sommetsDecouverts.remove(sommetPlusProche)
            sommetsAtteintsAuPlusCourt.append(sommetPlusProche)
            
            # Traitement du sommet le plus proche en utilisant tous les arcs sortants du sommet de départ        
            for arc in sommetPlusProche.arcSortants:
                sommetAtteint = arc.sommetArrivee
                distanceDepuisDepart += arc.poidsArc    # On ajoute le poids de l'arc à la distance depuis départ
                
                # Si le sommet atteint est dans la liste des sommets atteints au plus court
                # on continue
                if sommetAtteint in sommetsAtteintsAuPlusCourt:
                    continue
                
                # Sinon et que le sommet a déjà été découvert,
                elif sommetAtteint in sommetsDecouverts:
                    
                    # on compare et actualise nos variables
                    if distanceDepuisDepart < sommetAtteint.distanceDepuis[sommetDepart]:
                        sommetAtteint.distanceDepuis[sommetDepart] = distanceDepuisDepart
                        sommetAtteint.dernierArcDepuis[sommetDepart] = arc
                
                # Si par contre le sommet n'a pas encore été découvert,
                # On l'intégre dans les données avec la distance du sommet de départ et l'arc
                else:
                    sommetsDecouverts.append(sommetAtteint)
                    sommetAtteint.distanceDepuis[sommetDepart] = distanceDepuisDepart
                    sommetAtteint.dernierArcDepuis[sommetDepart] = arc
            
            # Recherche du plus proche sommet qui sera le successeur du sommet actuel
            if sommetsDecouverts:
                sommetPlusProche = sommetsDecouverts[0]
                for sommet in sommetsDecouverts:
                    if sommet.distanceDepuis[sommetDepart] < sommetPlusProche.distanceDepuis[sommetDepart]:
                        sommetPlusProche = sommet
                    distanceDepuisDepart = sommetPlusProche.distanceDepuis[sommetDepart]
    
    def __str__(self):
        return f'{self.nomSommet}'
    
    def __repr__(self):
        return f'{self}'

class Arc():
    
    # Classe utilisée pour définir un arc
    def __init__(self, poids, origine, arrivee):
        self.sommetDepart = origine     # On définie le sommet de départ de l'arc
        self.sommetArrivee = arrivee    # On définie le sommet d'arrivée de l'arc
        self.poidsArc = poids           # On définie le poids de l'arc 
        self.sommetDepart.ajouterArcSortant(self)   # On crée l'objet arc à partir d'un sommet 
        
        
    def __str__(self):
        return f'{self.sommetDepart}, {self.sommetArrivee}, {self.poidsArc}'
    
    def __repr__(self):
        return f'{self}'
    
g1 = Graphe(nomGraphe)

g1.calculerDistance()

for nom in nomSommets:
    g1.ajouterSommet(nom)
    
gra = Digraph() # On initialise la méthode Digraph

for triplet in donneesArc:
    nomDepart, nomArrivee, poids = triplet
    g1.ajouterArc(poids, nomDepart, nomArrivee)
    gra.edge(nomDepart, nomArrivee, f"{poids}")
    
for sommet in g1.listeSommets:
    sommet.calculerSuccesseur()
    gra.node(f"{sommet}",f"{sommet}")

g1.afficherGraphe()
sommetsLesPluseloignes = g1.plusLongDesPlusCourtsChemins()
for i in range(len(sommetsLesPluseloignes)-1):
    gra.node(sommetsLesPluseloignes[i-1], sommetsLesPluseloignes[i], color = "red")
    gra.edge(sommetsLesPluseloignes[i-1], sommetsLesPluseloignes[i], color = "red")


dot = Source(gra)
dot.format = 'png'
dot.render(f'{nomGraphe}', view=True)

with open("fichierHTML.html", "a") as fic:
    inserImage = '<p style="text-align:center;">'
    inserImage += f'<img src={nomGraphe}.png style="transform:rotate(-90deg);"/></p>'
    fic.writelines(inserImage)