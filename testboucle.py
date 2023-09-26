# -*- coding: utf-8 -*-
import FonctionAlgorithme as FA

I = FA.creerIndividusDepart(10)
result = FA.creerClassement(I)
for i in range (5):
    result = FA.créationNouvelleGénération(result)
    result = FA.creerClassement(result)
print(result)
    
