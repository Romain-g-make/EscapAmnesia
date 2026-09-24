from .Item import Item

class Inventory(Item):
    inventory = {}
    
    def __init__(self: object, maxSlots: int):
        self.maxSlots = maxSlots

    def hasItem(self: object, itemId: int):
        return self.inventory[itemId]

    def addItem(self: object, itemId: int, quantity: int):
        if self.hasItem:
            self.inventory[key] += 1
        else:
            self.inventory[key] = 1
        return {"status":"ok"}

    def removeItem(self: object, itemId: int, quantity):
        if self.hasItem(itemId):
            if self.inventory[itemId] - quantity == 0:
                self.inventory.pop(itemId)
            else:
                self.inventory[key] = self.inventory[key] - quantity
            return {"status":"ok"}
        else:
            return {"status":"error","cause":"Object isn't in inventory"}

    def showInventory(self: object):
        print(f'Voici la liste de vos items :\n')
        for item, quantity in self.inventory.items():
            print(f'- {item} | x{quantity}\n');
