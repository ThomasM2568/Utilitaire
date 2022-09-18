from random import choice
def mdp():
    return choice('abcdefghijklmnopqrstuvwxyz1234567890')


a=''
nb=int(input("saisir le nombre de caract  res souhait  s:"))
for i in range(nb):
    a=a+mdp()
print("le mot de passe est " + a)