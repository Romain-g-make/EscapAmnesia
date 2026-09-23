from .Item import Item

class ObjetInteractif(Item):
    def __init__(self, id,nom,description,etat,estFerme, codeSerrure):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat
        self.estFerme = estFerme
        self.codeSerrure = codeSerrure

    def inspecter(self):
        return print(f'Voici l\item : {self.nom}, il sert à : {self.description} !')

    def utiliser(self):
        return print(f'Vout utilisez actuellement l\'item : {self.nom} !')

    def deverouiller(self):
        return print(f'Vous êtes actuellement entrain de déverouiller l\'objet !')