#On se limite pour l'instant au cas m = 2, on adaptera les fonctions si on souhaite augmenter m

##Bibliothèques
from math import *


##Variables
m = 2
k = 100
n1 = 100
n2 = 100

##Fonctions utiles
def mu(k1,k2):
    return math.comb(n1,k1)*exp(-b*k1*v1)*math.comb(n2,k2)*exp(-b*k2*v2)

def partie_positive(a):
    return max(0,a)

def norme_VT():

def psi_1(k):
    return b*v1 + math.log(n1-k)
    
def psi_2(k):
    return b*v2 + math.log(n2-k)
    
##L'algorithme

def matrice_transition():
    X = []
    for i in range(k+1):
        X.append([k-i,i])
    M = np.zeros(k+1,k+1)
    
    for i in range(1,k):
        M[i][i-1] = X[i][1]*(1/2)*exp(-partie_positive(psi_2(X[i][1]-psi_1(X[i][])))
        M[i][i] = 
        M[i][i+1] = X[i][
                                                      
        
            

def metropolis(beta,epsilon):
    L = [(100,100)] #on part initialement avec 100 particules sur le 1er état, et 0 sur le 2nd
    while norme_VT())
