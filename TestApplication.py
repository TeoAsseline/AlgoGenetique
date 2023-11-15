# -*- coding: utf-8 -*-
import FonctionAlgorithme as FA
import matplotlib.pyplot as plt

# #CREER UNE SEED DE VILLE ET GENERER GRAPH
# coordonnees = FA.creerVille(21)#choisir seed
# FA.generergraph(coordonnees,I)

#AFFICHER LE SCORE DU MEILLEUR INDIVIDU POUR CHAQUE GENERATION
nbGeneration=55
nbIndividu=100
seed=21
nbVille=25
resultat=FA.schemaLePlusCourt(nbIndividu,nbGeneration,nbVille,seed)
print("Classement de la dernière génération : ",resultat)

#TESTER LA ROULETTE
# x = []
# y = []
# for i in range (100):
#     x.append(i)
#     y.append(FA.roulette(100))
#     print(FA.roulette(100))
# plt.scatter(x,y)
# plt.show()


