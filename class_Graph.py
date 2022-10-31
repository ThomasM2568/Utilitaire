class Graphe:
    def __init__(self):
        self.sommet={}

    def ajoute_sommet(self,valeur_sommet):
        self.sommet[valeur_sommet]=[]

    def liste_sommets(self):
        return self.sommet

    def liste_noeuds(self):
        return self.sommet.keys()

    def liste_arretes(self):
        return self.sommet.values()

    def liste_arretes_sommet(self,sommet1):
        if sommet1 in self.liste_noeuds():
            return self.sommet[sommet1]

    def ajoute_arrete(self,sommet1,sommet2):
        self.arrete=str(sommet2)

        if sommet1 in self.sommet:
            if self.arrete not in self.sommet[sommet1]:
                self.sommet[sommet1].append(self.arrete)

            else:
                return ("Arrete deja presente")
        else:
            return ("Arrete deja presente")

    def sous_graphe(self,listevaleurs2):
        sousgraphe=Graphe()
        for i in listevaleurs2:
            liste=[]
            sousgraphe.ajoute_sommet(i)
            c=self.liste_arretes_sommet(i)
            for y in range(len(c)):
                if c[y] in listevaleurs2:
                    sousgraphe.ajoute_arrete(i,c[y])
        return(sousgraphe.liste_sommets())

    def adjacence(self):
        adj=[]
        liste=[]
        lettres=self.liste_noeuds()
        l=sorted(lettres)
        for i in l:
            liste.append(self.liste_arretes_sommet(i))
            liste.append(" ")
        for a in l:
            adj2=[]
            for b in l:
                if b in self.liste_arretes_sommet(a):
                    adj2.append(1)
                else:
                    adj2.append(0)
            adj.append(adj2)
        return(adj)

    def dictionnaire(self,matrice,listesommets):
        graphe=Graphe()
        for a in range(len(listesommets)):
            graphe.ajoute_sommet(listesommets[a])
            for b in range(len(listesommets)):
                if matrice[a][b]==1:
                    graphe.ajoute_arrete(listesommets[a],listesommets[b])
        return(graphe.liste_sommets())

    def parcours_profondeur(self):
        self.sommets_marques=[]
        for sommet in self.sommets:
            print(profondeur_recursive(sommet))
            self.profondeur_recursive(sommet)


    def profondeur_recursive(self,sommet):
        if sommet not in self.sommets_marques:
            print("Sommet non marqué")
            self.sommets_marques.append(sommet)
            for successeur in self.sommets(sommet):
                self.profondeur_recursive(successeur)

    def largeur(self):
        self.sommets_marques = []
        for sommet in self.sommets :
            if not sommet in self.sommets_marques:
                liste_successeurs=[sommet]
            while len(liste_successeurs)!=0:
                s = liste_successeurs.pop(0)
                if s not in self.sommets_marques:
                    print(s)
                    self.sommets_marques.append(s)
                    for successeur_de_s in self.sommets_marques:
                        if not successeur_de_s in liste_successeurs:
                            liste_successeurs.append(successeur_de_s)

    def recherche_chemin(self,sommet1,sommet2):
        self.sommets_marques=[]
        chemin=[]
        resultat_recherche=self.recherche_chemin_recursive(sommet1,sommet2,chemin)
        if resultat_recherche==True:
            chemin.insert(0,sommet1)
            return(chemin)
        return([])

    def recherche_chemin_recursive(self,sommet1,sommet2,chemin):
        if sommet1 == sommet2:
            return(self.sommets_marques)
        if not sommet1 in self.sommets_marques:
            self.sommets_marques.append(sommet1)
            for successeur in self.sommets[sommet1]:
                resultat_recherche=self.recherche_chemin(sommet1,successeur)
                if resultat_recherche==True:
                    chemin.insert(0,sommet1)
                    return(True)
        return(False)



#--------------------------------------------
#5)
graphe1=Graphe()
listelettres=["A","B","C","D","E"]
for i in listelettres:
    graphe1.ajoute_sommet(i)
print(graphe1.liste_sommets())
graphe1.ajoute_arrete("A","B")
graphe1.ajoute_arrete("A","C")
graphe1.ajoute_arrete("B","D")
graphe1.ajoute_arrete("C","D")
graphe1.ajoute_arrete("B","A")
graphe1.ajoute_arrete("C","E")
graphe1.ajoute_arrete("D","E")
graphe1.ajoute_arrete("E","A")

print(graphe1.liste_sommets())
print(graphe1.sous_graphe(["A","B","C"]))
#--------------------------------------------
liste=list(graphe1.liste_noeuds())











