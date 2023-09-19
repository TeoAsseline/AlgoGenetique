# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:34:39 2023

@author: assel
"""
import numpy as np

def creerVille(nbV):
    abscisses = []
    ordonnees = []
    
    for _ in range(nbV):
        x = np.random.uniform(0, 100)  # Abscisse aléatoire entre 0 et 10
        y = np.random.uniform(0, 100)  # Coordonnée aléatoire entre 0 et 10
        abscisses.append(x)
        ordonnees.append(y)
    return abscisses, ordonnees

def creerMatrice(nbV):
    
    coordonnees = creerVille(nbV)
    print(coordonnees)
    print("------------------")
    abscisses = coordonnees[0]
    ordonnees = coordonnees[1]
    
    matrice = np.zeros((nbV, nbV))
    
    for depart in range (nbV):
        for arrive in range (nbV):
            if depart != arrive :
                distance = np.sqrt(((abscisses[arrive]-abscisses[depart])**2)+((ordonnees[arrive]-ordonnees[depart])**2))
                matrice[depart,arrive] = distance
    
    return matrice
    
def creerIndividusDepart(nbV):
    liste = list(range(0, nbV))
    np.random.shuffle(liste)
    
    return liste
    
def calculerDistance(M,I,nbV):
    distance = 0
    for i in range(nbV):
        depart = I[i]
        if (i==nbV-1):
            arriver = I[0]
        else:
            arriver = I[i+1]
        distance += M[depart,arriver]
        
    return(distance)

def creerClassement(nbI,nbV):
    M = creerMatrice(nbV)
    classementNonTrie = []
    for i in range(nbI):
        I = creerIndividusDepart(nbV)
        classementNonTrie.append((I,calculerDistance(M, I, nbV)))
    classementFinal = sorted(classementNonTrie, key=lambda x: x[1])
    return(classementFinal)

def croisement():
    return("coucou")

def mutation():
    return("saucisse")

def créationNouvelleGénération:
    

result = (creerClassement(100, 50))
print(result)
#print("----------------")
#print(result[0][0])

