import os.path
import os
from math import sqrt
import random 

# Fonction qui récupère la map en fichier texte  et retourne un dictionnaire
# contenant les positions des bateaux
# On rentre un nombre qui correspond à une map type : map_(numéro de la map) -> ex : map_1

class Map:

    def __init__(self):
        self.dico = {}
        self.nb_map = 10

    def open_map(self) :

        try :
            # créaction du chemin jusqu'au fichier contenant la map
            s1 = "/"
            seq = ("BattleShip Project\Map","Map")
            path = s1.join(seq)
            s2 = "_"
            seq = (path,str(random.randint(1,self.nb_map)))
            path = s2.join(seq)
            s3 = "."
            seq = (path,'txt')
            path = s3.join(seq)

            # lecture du fichier
            self.dico = self.get_map(path)
            return self.dico

        except FileNotFoundError :
            print('Fichier introuvable')
        except IOError :
            print('Erreur d\'entrée/sortie.')

    def split_char(self, word): 
        return [char for char in word]

    def split_submarine (self, L):
        x1 = 0
        y1 = 0
        x = 0
        y = 0
        L1 = []
        L2 = []
        for elem in L:
            x, y = elem
            for elem1 in L:
                x1,y1 = elem1
                D = sqrt((x1-x)**2 + ((y1-y)**2))
                if (len(L1) < 3):
                    if(  (D == 1 or D == 0) and (elem1 not in L1) ):
                        L1.append(elem1) 
        for elem2 in L:
            if elem2 not in L1:
                L2.append(elem2)
        return (L1,L2)
    
    def get_map (self, path):
        with open(path) as file :
                y = 0 #row
                List_Char = []
                dico = {}
                L1 = []
                L2 = []
                L3 = []
                L4 = []
                L5 = []
                L6 = []    
                for line in file:
                    if (y>0 and y<= 10) :
                        word = line.rstrip()
                        List_Char = self.split_char(word)
                        x = 0 #col
                        for char in List_Char:
                            if (char == 'c'):
                                L1.append((x,y))
                                dico['Cruiser'] = L1
                            elif (char == 'p'):
                                L2.append((x,y))
                                dico['Aircraft Carrier'] = L2
                            elif (char == 's'):
                                L3.append((x,y))
                            elif (char == 't'):
                                L4.append((x,y))
                                dico['Destroyer'] = L4
                            x += 1
                    y += 1
                L5, L6 = self.split_submarine(L3)
                dico['Submarine n°1'] = L5
                dico['Submarine n°2'] = L6
                return dico