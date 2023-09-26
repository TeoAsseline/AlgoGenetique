# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:34:39 2023

@author: assel
"""
import numpy as np
import random
import matplotlib.pyplot as plt

nbV = 20

def rangerCoordonnees(coord):
    result=[]
    for i in range(len(coord[0])):
        point = [coord[0][i],coord[1][i]]
        result.append(point)
    return result

def recuperercoordpoint(coord,listeI):
    result=[]
    for i in listeI:
        point = [coord[0][i],coord[1][i]]
        result.append(point)
    point = [coord[0][listeI[0]],coord[1][listeI[0]]]
    result.append(point)
    return result

def creerVille():
    global nbV
    abscisses = []
    ordonnees = []
    for _ in range(nbV):
        x = np.random.uniform(0, 100)
        y = np.random.uniform(0, 100)  
        abscisses.append(x)
        ordonnees.append(y)
    return abscisses, ordonnees

def creerMatrice():
    global nbV
    coordonnees = creerVille()
    abscisses = coordonnees[0]
    ordonnees = coordonnees[1]
    matrice = np.zeros((nbV, nbV))
    for depart in range (nbV):
        for arrive in range (nbV):
            if depart != arrive :
                distance = np.sqrt(((abscisses[arrive]-abscisses[depart])**2)+((ordonnees[arrive]-ordonnees[depart])**2))
                matrice[depart,arrive] = distance
    return matrice
    
def creerIndividusDepart(nbI):
    global nbV
    listeFinal =[]
    for i in range (nbI):
        liste=list(range(0, nbV))
        np.random.shuffle(liste)
        listeFinal.append(liste)
    return listeFinal
    
def calculerDistance(M,I):
    global nbV
    distance = 0
    for i in range(nbV):
        depart = I[i]
        if (i==nbV-1):
            arriver = I[0]
        else:
            arriver = I[i+1]
        distance += M[depart,arriver]
    return(distance)

def creerClassement(I):
    global nbV
    M = creerMatrice()
    classementNonTrie = []
    for i, ind in enumerate(I):
        classementNonTrie.append((ind,calculerDistance(M, ind)))
    classementFinal = sorted(classementNonTrie, key=lambda x: x[1])
    return(classementFinal)

def croisement(ind1, ind2):
    global nbV
    print("Croisement effectué")
    coupe1 = np.random.randint(0,nbV)
    coupe2 = np.random.randint(0,nbV)
    while (coupe2==coupe1):
        coupe2 = np.random.randint(0,nbV)
    if (coupe1>coupe2):
        x = coupe1
        coupe1 = coupe2
        coupe2 = x
    gene1 =[]
    gene2 =[]
    for i in range (coupe2-coupe1):
        gene1.append(ind1[coupe1+i])
        gene2.append(ind2[coupe1+i])
        ind2[coupe1+i]="x"
        ind1[coupe1+i]="x"
    for element in ind1:
        if element in gene2:
            ind1[ind1.index(element)] = "y"
    for element in ind2:
        if element in gene1:
            ind2[ind2.index(element)] = "y"
    for i in range (coupe2-coupe1):
        ind1[coupe1+i]=gene2[i]
        ind2[coupe1+i]=gene1[i]
    ensembleVille = [i for i in range(nbV)]
    vManquante1 = []
    vManquante2 = []
    for element in ensembleVille:
        if element not in ind1:
            vManquante1.append(element)
    for element in ensembleVille:
        if element not in ind2:
            vManquante2.append(element)
    random.shuffle(vManquante1)
    for i in range(nbV):
        if ind1[i] == "y":
            ind1[i] = vManquante1.pop()
    random.shuffle(vManquante2)
    for i in range(nbV):
        if ind2[i] == "y":
            ind2[i] = vManquante2.pop()
    return(ind1, ind2)

def mutation(ind):
    print("MUTATION")
    global nbV
    v1 = np.random.randint(0,nbV)
    v2 = np.random.randint(0,nbV)
    while (v2==v1):
        v2 = np.random.randint(0,nbV)
    ind[v1],ind[v2]=ind[v2],ind[v1]
    return(ind)

def créationNouvelleGénération(genPr):
    taille = len(genPr)
    genPr = genPr[:taille//2]
    newGen = []
    for i in range(taille//2):
        alea1 = np.random.randint(0,taille//2)
        alea2 = np.random.randint(0,taille//2)
        while (alea2==alea1):
            alea2 = np.random.randint(0,taille//2)
        ind1 = genPr[alea1][0]
        ind2 = genPr[alea2][0]
        ind1_copy = ind1[:]
        ind2_copy = ind2[:]
        individusFini = croisement(ind1_copy, ind2_copy)
        indFini1 = individusFini[0]
        indFini2 = individusFini[1]
        if (np.random.rand()<0.1):    
            indFini1 = mutation(indFini1)
        if (np.random.rand()<0.1):    
            indFini2 = mutation(indFini2)
        newGen.append(indFini1)
        newGen.append(indFini2)
    return newGen

def generergraph(coordonnees,meilleurchemin):
    listexy=recuperercoordpoint(coordonnees,meilleurchemin[0])
    global nbV
    print("------------------")
    for i in range (nbV):
        print("Point numéro ",i+1," / Abscisse :",coordonnees[0][i]," / Ordonné :",coordonnees[1][i])
    rangecoord=rangerCoordonnees(coordonnees)
    listeville=[]
    for i in range (len(rangecoord)):
        listeville.append(i)
    x, y = zip(*rangecoord)
    plt.scatter(x,y,marker="*",color='b')
    w, z = zip(*listexy)
    plt.plot(w, z,color='g')
    for i in range(len(listeville)):   
        plt.text(x[i]+.09, y[i]+.09,listeville[i], fontsize=9)
    plt.title("Liste des emplacements des Villes")
    plt.xlabel("Abscisses")
    plt.ylabel("Ordonnees")
    plt.show()
    print("------------------")
    return 1;
    
I=creerIndividusDepart(5)
print(I)
result = creerClassement(I)
result2 = créationNouvelleGénération(result)
print(result2)
coordonnees = creerVille()
generergraph(coordonnees,result2)
