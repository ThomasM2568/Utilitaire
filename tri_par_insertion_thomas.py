def tri_insertion(liste):

    for i in range(1,len(liste)):
        valeur=liste[i]
        posvaleur=i-1
        while posvaleur>=0 and valeur>liste[posvaleur]:

            liste[posvaleur+1] = liste[posvaleur]
            posvaleur-=1

        liste[posvaleur+1]=valeur
    liste.reverse()
    print ("Le tableau trié est:")
    for t in range(len(liste)):
        print (liste[t])







