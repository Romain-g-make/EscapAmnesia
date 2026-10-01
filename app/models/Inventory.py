import logging
from app.services.ItemsList import itemList

logger = logging.getLogger(__name__)


class Inventory:
    def __init__(self, maxSlots: int = 10):
        self.maxSlots = maxSlots
        self.inventory: dict[int, object] = {}

    def hasItem(self, itemId: int) -> bool:
        logger.info("Search for the item ID %s in the inventory's player", itemId)
        return itemId in self.inventory

    def addItem(self, itemId: int) -> dict:
        if self.hasItem(itemId):
            return {
                "status": "error",
                "cause": f"You already have {itemId} in your inventory",
                "item": itemId
            }
        else:
            logger.info("Add item with id %s in the player's inventory", itemId)
            for item in itemList:
                if item.id == itemId:
                    self.inventory[itemId] = item
                    break
        return {"status": "ok"}

    def removeItem(self, itemId: int) -> dict:
        if self.hasItem(itemId):
            logger.info("Remove item with id %s in the player's inventory", itemId)
            self.inventory.pop(itemId)
            return {"status": "ok"}
        else:
            logger.error("Object isn't in the inventory")
            return {"status": "error", "cause": "Object isn't in the inventory"}

    def showInventory(self) -> dict:
        result = {"Voici la liste de vos items :": {}}
        logger.info("Print of the inventory's item")
        for itemId, item in self.inventory.items():
            result["Voici la liste de vos items :"][itemId] = item.getData()
        return result