from .Item import Item

class Inventory(Item):
    inventory = {}
    
    def __init__(self, maxSlots):
        self.maxSlots = maxSlots

    def hasItem(self, key):
        return self.inventory[key]

    def addItem(self, key):
        if self.maxSlots<=len(self.inventory):
            return {"status":"ok","cause":"inventory full"}
        if self.hasItem:
            self.inventory[key] += 1
        else:
            self.inventory[key] = 1
        return {"status":"ok"}

    def removeItem(self, key, quantity):
        if self.hasItem(key):
            if self.inventory[key] - quantity == 0:
                self.inventory.pop(key)
            else:
                self.inventory[key] = self.inventory[key] - quantity
            return {"status":"ok"}
        else:
            return {"status":"error","cause":"Object isn't in inventory"}

    def showInventory(self):
        return self.inventory