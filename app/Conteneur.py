from Item import Item

class Conteneur(Item):
    def __init__(self, estFerme, codeSerrure):
        self.estFerme = estFerme
        self.codeSerrure = codeSerrure

    def inspecter(self):
        return print(f'Voici l\item : {self.nom}, il sert à : {self.description} !')

    def utiliser(self):
        return print(f'Vout utilisez actuellement l\'item : {self.nom} !')

    def deverouiller(self):
        return print(f'Vous êtes actuellement entrain de déverouiller l\'objet !')