

class File :
    """Classe File"""
    def __init__(self):
        """Constructeur de la classe"""
        self.file = []

    def enfiler(self, x):
        """enfiler l'ÃƒÂ©lement x en queue de la file"""
        self.file.append(x)

    def defiler(self):
        """defile l'ÃƒÂ©lement de tÃƒÂªte de la liste et le retourne"""
        return self.file.pop(0)

    def est_vide(self):
        """si la file est vide elle retourne True et False sinon"""
        if len(self.file) != 0:
            return False
        else:
            return True

class Arbre:
    """classe Arbre"""
    def __init__(self, cle, Sag=None, Sad=None):
        """Constructeur de la classe"""
        self.Racine = cle
        self.Sag = Sag
        self.Sad = Sad


    def Taille(self,a):
        """Retourne la taille de l'arbre c'est ÃƒÂ  dire le nombre de noeuds"""
        if a == None :
            return 0
        else :
            return 1+ self.Taille(a.Sag) + self.Taille(a.Sad)


    def Hauteur(self, a):
        """Retourne la hauteur de l'arbre"""

        if a == None :
            return -1
        else :
            return 1+ max(self.Hauteur(a.Sag) , self.Hauteur(a.Sad))

    def ParcoursLargeur(self):
        """Parcours l'arbre en largeur et retourne la liste des clÃƒÂ©s des noeuds"""
        lst =[]
        if self != None :
            file =File()
            file.enfiler(self)

            while file.est_vide() == False:
                arbre_courant = file.defiler()
                lst.append(arbre_courant.Racine)

                #ajouter le sous arbre gauche de l'arbre dÃƒÂ©filÃƒÂ©
                if arbre_courant.Sag is not None :
                    file.enfiler(arbre_courant.Sag)

                #ajouter le sous arbre gauche de l'arbre dÃƒÂ©filÃƒÂ©
                if arbre_courant.Sad is not None :
                    file.enfiler(arbre_courant.Sad)
        return lst

    def ParcoursPrefixeRec(self, lst, arbre):
        """Parcours l'arbre en prÃƒÂ©fixe rÃƒÂ©cursivement"""
        if arbre != None :
            lst.append(arbre.Racine)
            self.ParcoursPrefixeRec(lst, arbre.Sag)
            self.ParcoursPrefixeRec(lst, arbre.Sad)

    def ParcoursInfixeRec(self, lst, arbre):
        """Parcours l'arbre en inffixe rÃƒÂ©cursivement"""
        if arbre != None :
            self.ParcoursInfixeRec(lst, arbre.Sag)
            lst.append(arbre.Racine)
            self.ParcoursInfixeRec(lst, arbre.Sad)

    def ParcoursPostfixeRec(self, lst, arbre):
        """Parcours l'arbre en inffixe rÃƒÂ©cursivement"""
        if arbre != None :
            self.ParcoursPostfixeRec(lst, arbre.Sag)
            self.ParcoursPostfixeRec(lst, arbre.Sad)
            lst.append(arbre.Racine)

    def Recherche_clef(self,clef):
        if self == None :
            return false
        else:
             if self.Racine==clef :
                return "Erreur"
             else:
                if clef<self.Racine:
                    if self.Sag==None:
                        return False
                    else :
                        return self.Sag.Recherche_clef(clef)
                else:
                    if self.Sad==None:
                        return False
                    else:
                        return self.Sad.Recherche_clef(clef)



    def Inserer_clef(self,clef):
        if self == None :
            return Arbre(clef)
        else:
             if self.Racine==clef :
                return "Erreur"
             else:
                if clef<self.Racine:
                    if self.Sag==None:
                        self.Sag=Arbre(clef)

                    else :
                        return self.Sag.Inserer_clef(clef)
                else:
                    if self.Sad==None:
                        self.Sad=Arbre(clef)
                    else:
                        return self.Sad.Inserer_clef(clef)




    def est_binaire(self):
        a=[]
        self.ParcoursInfixeRec(a,self)
        n=len(a)
        for i in range(n-1):
            if a[i+1]<a[i]:
                return ("il n'est pas binaire")
            return ("l'arbre est binaire")








#################### Programme principal #####################################"
arbre = Arbre(25)
arbre.Sag = Arbre(7)
arbre.Sad = Arbre(50)
arbre.Sag.Sag = Arbre(3)
arbre.Sag.Sad = Arbre(18)
arbre.Sag.Sag.Sad= Arbre(6)
arbre.Sag.Sad.Sag= Arbre(8)
arbre.Sad.Sag = Arbre(30)
arbre.Sad.Sad = Arbre(51)

print("Taille : ")
print(arbre.Taille(arbre))

print("Hauteur : ")
print(arbre.Hauteur(arbre))

lst_larg = arbre.ParcoursLargeur()
print("parcours en largeur")
print(lst_larg)

print("parcours en prÃƒÂ©fixe")
lst_pref= []
arbre.ParcoursPrefixeRec(lst_pref, arbre)
print(lst_pref)

print("parcours en infixe")
lst_pref= []
arbre.ParcoursInfixeRec(lst_pref, arbre)
print(lst_pref)

print("parcours en postfixe")
lst_pref= []
arbre.ParcoursPostfixeRec(lst_pref,arbre)
print(lst_pref)



print("recherche clef")
print(arbre.Recherche_clef(19))

print("inserer clef")
arbre.Inserer_clef(19)

print("parcours en infixe")
lst_pref= []
arbre.ParcoursInfixeRec(lst_pref, arbre)
print(lst_pref)

print("Est binaire : ",end="")
print(arbre.est_binaire(  ))
