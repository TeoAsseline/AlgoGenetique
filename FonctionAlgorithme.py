# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:34:39 2023

@author: assel
"""
import numpy as np

def creerMatrice(n):
    
    # Générer une matrice aléatoire de taille n x n
    matrice = np.random.randint(1, 100, size =(n,n))
    
    # Remplacer la diagonale par des zéros
    np.fill_diagonal(matrice, 0)
    
    for i in range(n):
        for j in range(i, n):
            matrice[j][i] = matrice[i][j]
    
    # Afficher la matrice résultante
    return matrice
    
def creerIndividusDepart(n):
    liste = list(range(0, n))
    np.random.shuffle(liste)
    
    return liste
    
def calculerDistance(M,I,n):
    distance = 0
    for i in range(n):
        depart = I[i]
        if (i==n-1):
            arriver = I[0]
        else:
            arriver = I[i+1]
        distance += M[depart,arriver]
        
    return(distance)
    
M = creerMatrice(5)
classement = []
for i in range(5):
    I = creerIndividusDepart(5)
    classement.append((I,calculerDistance(M, I, 5)))
tableau_trie = sorted(classement, key=lambda x: x[1])
print(tableau_trie)
print(tableau_trie[2])
