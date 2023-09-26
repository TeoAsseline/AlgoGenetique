# -*- coding: utf-8 -*-
import FonctionAlgorithme as FA

I = FA.creerIndividusDepart(14)
result = FA.creerClassement(I)
print(result)
for i in range (100):
    result = FA.créationNouvelleGénération(result)
    result = FA.creerClassement(result)
print(result)
    

