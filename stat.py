import numpy as np
import matplotlib.pyplot as plt
import math

#Constantes du problème
beta=0.1


#Commencons par n=16 et k=9 et m=4
n=16
#Matrice des nj
N=[4,4,5,3]

k=9
m=4

#C'est ici où on met les vi
V=[0,1,9,2]
#on commence par X0 qui appartient k1=2 k2=0 k3=4 k4=3
X0=np.array([2,0,4,3])
proba2=np.ones_like(X0)/m
proba1=X0/k

#Algorithme ...Mais sans condition d'arrêt


#on utilise le truc de simulation des variables aléatoire
def simulation(proba):
    U=np.random.uniform(1)
    d=0#c'est la somme des pi
    for i in range(1,len(proba)+1):
        if d<=U[0]<=d+proba[i-1]:
            return i
        else:
            d+=proba[i-1]
#1) On choisit i avec ki/k
i=simulation(proba1)

#2)Maintenant on choisit j avec probabilité 1/m
j=simulation(proba2)

#3)Maintenant on échange avec proba p :
r=beta*V[j]-math.log(N[j]-*X0[j])-beta*V[i]*math.log(N[i]-X0[i]+1)

#C'est le r+ !
if(r<0):
    r=0

p=np.exp(-r)

#La probabilité que ça change
U_changement=np.random.uniform(1)
if U_changement[0]<=p:
    X[i]+=-1
    X[j]+=1

#sinon , on ne fait rien
#Et ainsi on construit la suite des variables aléatoires (Xn)

