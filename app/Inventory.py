from Item import Item

class Inventaire(Item):
    inventaire = [];
    def __init__(self, capaciteMax):
        self.capaciteMax = capaciteMax

    def ajouterItem(self, itemId, quantity):
        self.inventaire.append(itemId)