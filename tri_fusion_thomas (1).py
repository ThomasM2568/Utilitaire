liste=[98,89,65,14,46,35,82,897,15,48]
l=[]

def tri_fusion_trie(l,l1,l2):
    if len(l1)==0:
        print("Liste 1 vide")
        if len(l2)!=0:
            for i in range(len(l2)):
                l.append(l2[0])
                l2.remove(l2[0])
            return(l)
        return(l)
    if len(l2)==0:
        print("Liste 2 vide")
        if len(l1)!=0:

            for i in range(len(l1)):
                l.append(l1[0])
                l1.remove(l1[0])
            return(l)
        return(l)
    #----------------------
    if l1[0]<l2[0]:
        l.append(l1[0])
        l1.remove(l1[0])
        return(tri_fusion_trie(l,l1,l2))
    elif l1[0]>l2[0]:
        l.append(l2[0])
        l2.remove(l2[0])
        return(tri_fusion_trie(l,l1,l2))
    return(l)




def tri_fusion(liste):
    if len(liste)==1:
        return(liste)
    else:
        milieu=int(len(liste)//2)
        l1=liste[:milieu]
        l2=liste[milieu:]
    return(tri_fusion_trie(l,tri_fusion(l1),tri_fusion(l2)))



print(tri_fusion(liste))







