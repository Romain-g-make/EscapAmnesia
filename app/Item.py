from abc import abstractmethod

class Item():
    @abstractmethod
    def __init__(self, id, nom, description, etat):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat

    def inspecter(self):
        return print(f'Voici l\item : {self.nom}, il sert à : {self.description} !')

    def utiliser(self):
        return print(f'Vout utilisez actuellement l\'item : {self.nom} !')