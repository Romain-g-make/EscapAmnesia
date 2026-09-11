from Item import Item

class Inventory(Item):
    inventory = {};
    def __init__(self, maxSlots):
        self.maxSlots = maxSlots

    def hasItem(self, itemId):
        return self.inventory[itemId]

    def addItem(self, itemId, quantity):
        self.inventory[itemId] = quantity

    def removeItem(self, itemId, quantity):
        if self.hasItem(itemId):
            if self.inventory[itemId] - quantity == 0:
                self.inventory.pop(itemId)
            else:
                self.inventory[itemId] = self.inventory[itemId] - quantity
        else:
            print(f'Vous ne possédez pas l\'item !')

    def showInventory(self):
        print(f'Voici la liste de vos items :\n')
        for item, quantity in self.inventory.items():
            print(f'- {item} | x{quantity}\n');