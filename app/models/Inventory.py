import logging
from .Item import Item

logger = logging.getLogger(__name__)

class Inventory(Item):
    inventory = {}
    
    def __init__(self: object, maxSlots: int):
        self.maxSlots = maxSlots

    def getItemData(itemId: int):
        return Item.getData()

    def hasItem(self: object, itemId: int):
        logger.info('Search for the item ID %s in the inventory\'s player', itemId)
        return self.inventory[itemId]

    def addItem(self: object, itemId: int):
        if self.hasItem:
            logger.info('Add item with id %s in the player\'s inventory', itemId)
            self.inventory[itemId] += 1
        else:
            logger.info('Add item with id %s in the player\'s inventory', itemId)
            self.inventory[itemId] = 1
        
        return {"status":"ok"}

    def removeItem(self: object, itemId: int):
        if self.hasItem(itemId):
            if self.inventory[itemId] - 1 == 0:
                logger.info('Remove item with id %s in the player\'s inventory', itemId)
                self.inventory.pop(itemId)
            else:
                logger.info('Remove item with id %s in the player\'s inventory', itemId)
                self.inventory[itemId] = self.inventory[itemId] - 1
            return {"status":"ok"}
        else:
            logger.error('Object isn\'t in the inventory')
            return {"status":"error","cause":"Object isn't in the inventory"}

    def showInventory(self: object):
        logger.info('Print of the inventory\'s item')
        print(f'Voici la liste de vos items :\n')
        for item, quantity in self.inventory.items():
            print(f'- {item} | x{quantity}\n');