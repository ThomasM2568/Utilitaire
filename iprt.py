
ip1=int(input("IP1= "))
ip2=int(input("IP2= "))
ip3=int(input("IP3= "))
ip4=int(input("IP4= "))
mask1=int(input("mask1= "))
mask2=int(input("mask2= "))
mask3=int(input("mask3= "))
mask4=int(input("mask4= "))
imask1=255-mask1
imask2=255-mask2
imask3=255-mask3
imask4=255-mask4

smask1=255-mask1
smask2=255-mask2
smask3=255-mask3
smask4=255-mask4


def longueur(arg):
    if len(arg)<8:
        valeur=8-len(arg)
        narg=arg
        arg=""
        for i in range(valeur):
            arg+="0"
        arg+=narg
    print("")
    return(arg)

def calcmask(arg):
    l=32-arg
    result=""
    for i in range(0,arg):
        result+='1'
    for j in range(0,l):
        result+='0'

    return(result)


imask1=bin(imask1)[2:len(bin(imask1))]
imask2=bin(imask2)[2:len(bin(imask2))]
imask3=bin(imask3)[2:len(bin(imask3))]
imask4=bin(imask4)[2:len(bin(imask4))]

iimask1=longueur(imask1)
iimask2=longueur(imask2)
iimask3=longueur(imask3)
iimask4=longueur(imask4)



def f(nb):
    nip=""
    if len(nb)<8:

        v=8-len(nb)
        for i in range(0,v):
            nip+="0"
        nip+=nb
    else:
        nip=nb
    return(nip)

def calcul(ip,mask):
    ip=bin(ip)[2:len(bin(ip))]
    mask=bin(mask)[2:len(bin(mask))]
    #-------
    ip=f(ip)
    mask=f(mask)
    #--------
    result=""
    for j in range(0,len(ip)):
        result+=str(int(ip[j])&int(mask[j]))

    return(result)

r1=calcul(ip1,mask1)
r2=calcul(ip2,mask2)
r3=calcul(ip3,mask3)
r4=calcul(ip4,mask4)


def broadcast(ad,mi): #adresse reseau et mask inverse
    result=""
    for i in range(len(ad)):
        result+=str(int(ad[i])|int(mi[i]))
    return(result)

b1=broadcast(r1,iimask1)
b2=broadcast(r2,iimask2)
b3=broadcast(r3,iimask3)
b4=broadcast(r4,iimask4)

def bintodec(valeur):
    return(int(valeur,2))

"""ou entre adresse reseau et mask inverse"""
"""| = ou"""
"""& = et"""

vmask=int(input("Entre /combien"))
if vmask!=0:
    print("/",vmask," = ",calcmask(vmask))
    print(32-vmask, " nb bits hotes")
    print(2**(32-vmask)-2, " nb hotes")



print("IP =",ip1,".",ip2,".",ip3,".",ip4)
print("Mask =",mask1,".",mask2,".",mask3,".",mask4)
print("Mask inverse =",smask1,".",smask2,".",smask3,".",smask4)
print("Adresse reseau =",r1,".",r2,".",r3,".",r4)
print("Adresse reseau =",bintodec(r1),".",bintodec(r2),".",bintodec(r3), ".",bintodec(r4))
print("Adresse broadcast =",b1,".",b2,".",b3,".",b4)
print("Adresse broadcast =",bintodec(b1),".",bintodec(b2),".",bintodec(b3),".",bintodec(b4))



