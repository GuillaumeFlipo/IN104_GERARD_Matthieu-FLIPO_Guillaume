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
        print("Le prix par metre carré est : ",a, " euros/m²")




class maison(habitation):
    def __str__(self):
        return "Je suis une maison coûtant " +str(self.getPrix()) + " euros"


    def nbr_Etage(self,etage):
        self.nbrEtage=etage
        print("Cette maison possède ",etage,"etage")

    def jardin(self,jardin):
            self.jardin= jardin


    def avoirJardin(self):
        if self.jardin==1:
            print("Cette appartement possède un jardin")
            return True
        else:
            print("Cette appartement ne possède pas de jardin")
            return False

    def superficieParEtage(self):
        self.superficieParEtage=self.superficie/self.nbrEtage
        print("La surperficie moyenne par étage est : ",self.superficieParEtage, "m²/etage")






class appartement(habitation):
    def __str__(self):
        return "Je suis un appartement coûtant " +str(self.getPrix()) + " euros"

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
        self.superficieParPiece = self.superficie/self.nbr_pieces
        print("La surperficie moyenne par pièce est : ",self.superficieParPiece, "m²/pièce")



