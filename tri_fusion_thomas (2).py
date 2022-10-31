# Créé par thomas.mirbey, le 16/11/2020 en Python 3.7

def fusion(L1,L2):
    L=[]
    compteur=0
    while len(L1)!=0 and len(L2)!=0:
        compteur+=1
        d1=L1.pop(0)
        d2=L2.pop(0)
        if d1>d2:
            L.append(d2)
            L1.insert(0, d1)
        elif d2>d1:
            L.append(d1)
            L2.insert(0, d2)
    if len(L1)!=0:
        while len(L1)!=0:
            compteur+=1
            a=L1.pop(0)
            L.append(a)
    elif len(L2)!=0:
        while len(L2)!=0:
            compteur+=1
            a=L2.pop(0)
            L.append(a)
    return L,compteur

def tri_fusion(L):
    if len(L)==1:
        return L
    L1=L[:len(L)//2]
    L2=L[len(L)//2:]
    return fusion(tri_fusion(L1),tri_fusion(L2))

from random import *
L=[]
while len(L)!=5:
    valeur=randint(1,90)
    if valeur not in L:
        L.append(valeur)
    print(L,type(L))

print(tri_fusion(list(L)))

