from abc import abstractmethod

class Item():

    listItem = []

    @abstractmethod
    def __init__(self, id, nom, description, etat):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat

    listItem.append(id)

    def inspecter(self):
        return print(f'Voici l\item : {self.nom}, il sert à : {self.description} !')

    def utiliser(self):
        return print(f'Vout utilisez actuellement l\'item : {self.nom} !')

    def getData(self):
        return {"id":self.id,"nom":self.nom,"description":self.description}