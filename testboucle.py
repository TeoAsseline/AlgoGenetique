# -*- coding: utf-8 -*-
import FonctionAlgorithme as FA
import matplotlib.pyplot as plt

I = FA.creerIndividusDepart(100)
result = FA.creerClassement(I)
print(result)
x = []
y = []
for i in range (2):
    x.append(i)
    result = FA.créationNouvelleGénération(result)
    result = FA.creerClassement(result)
    y.append(result[0][1])
plt.scatter(x,y)
plt.show
print(result)


# x = []
# y = []
# for i in range (100):
#     x.append(i)
#     y.append(FA.roulette(100))
# plt.scatter(x,y)
# plt.show

