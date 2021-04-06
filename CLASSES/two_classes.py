class habitation:
    def __init__(self,superficie,nbr_pieces,prix):
        self.superficie = superficie
        self.nbr_pieces = nbr_pieces
        self.__prix = prix

    def __privateMethod(self):
        print(self.prix)

    def getPrix(self):
        return self.__prix

    def prixParMetreCarre(self):
        a=self.__prix/self.superficie
        print("Le prix par metre carré est : ",a, "€/m²")




class maison(habitation):
    def __str__(self):
        return "Je suis une maison coûtant " +str(self.getPrix()) + "€"


    def nbr_Etage(self,etage):
        self.nbrEtage=etage
        print("Cette maison possède ",etage,"etage")

    def jardin(self,jardin):
            self.jardin= jardin


    def avoirJardin(self):
        if self.jardin==1:
            print("Cette appartement possède un jardin")
        else:
            print("Cette appartement ne possède pas de jardin")

    def superficieParEtage(self):
        superficieParEtage=self.superficie/self.nbrEtage
        print("La surperficie moyenne par étage est : ",superficieParEtage, "m²/etage")





class appartement(habitation):
    def __str__(self):
        return "Je suis un appartement coûtant " +str(self.getPrix()) + "€"

    def garage(self,garage):
        self.garage=garage



    def numero_Etage(self,etage):
        self.numeroEtage=etage
        print("Cette appartement est à l'étage : ",etage)

    def avoirGarage(self):
        if self.garage==1:
            print("Cette appartement possède un garage")
        else:
            print("Cette appartement ne possède pas de garage")

    def superficieParPiece(self):
        superficieparpiece = self.superficie/self.nbr_pieces
        print("La surperficie moyenne par pièce est : ",superficieparpiece, "m²/pièce")



print(" Definition d'un appartement")         
appartement1=appartement(100,4,100000)
print(appartement1)
print("Superficie")
print(appartement1.superficie, "m²")
print("Nombre de pièces")
print(appartement1.nbr_pieces)
print("Prix")
print(appartement1.getPrix())

appartement1.prixParMetreCarre()
print("definiton du numero d'étage")

appartement1.numero_Etage(4)

#      definition pas de garage

appartement1.garage(0)
appartement1.avoirGarage()

appartement1.superficieParPiece()
#

print("Definition d'une maison") 

maison1=maison(300,10,300000)
print(maison1)
print("Superficie")
print(maison1.superficie,"m²")
print("Nombre de pièces")
print(maison1.nbr_pieces)
print("Prix")
print(maison1.getPrix())

maison1.prixParMetreCarre()
#        Definition du nombre d'étage

maison1.nbr_Etage(2)


#       Definition avoir jardin 

maison1.jardin(1)
maison1.avoirJardin()
maison1.superficieParEtage()
#
#
