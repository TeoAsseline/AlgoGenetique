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
    
    # Afficher la matrice résultante
    print(matrice)
    
creerMatrice(5)
