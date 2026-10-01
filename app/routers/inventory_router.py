from .game_router import games
import logging
from fastapi import APIRouter,HTTPException,status

logger = logging.getLogger(__name__)
router_inventory = APIRouter(tags=["Inventory"])
#GESTION INVENTAIRE
@router_inventory.patch("/{idGame}/inventory/addItem/{itemId}")
def addItem(idGame:str,itemId: int):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        logger.info("Search the item : %s",itemId)
        if itemId>13:
            logger.warning("The item %s is not in the item list",itemId)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"L'item avec l'ID {itemId} n'existe pas."
                )
        return games[idGame].inventory.addItem(itemId)
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_inventory.delete("/{idGame}/inventory/removeItem/{itemId}")
def removeItem(idGame:str,itemId: int):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        logger.info("Search the item : %s",itemId)
        if itemId>13 :
            logger.warning("The item %s is not in the game",itemId)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"L'item avec l'ID {itemId} n'existe pas."
                )
        return games[idGame].inventory.removeItem(itemId)
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_inventory.get("/{idGame}/inventory/showInventory")
def showInventory(idGame:str):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        return games[idGame].inventory.showInventory()
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )