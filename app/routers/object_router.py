from .game_router import games
import logging
from fastapi import APIRouter,HTTPException,status
from app.models.ObjetInteractif import ObjetInteractif

logger = logging.getLogger(__name__)


router_obj = APIRouter(tags=["Objects"])
#OBJETS 
@router_obj.get('/{idGame}/objet/get')
def getObj(idGame:str):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        logger.info("Search for items")
        return games[idGame].get_obj()
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_obj.get('/{idGame}/objet/inspect/{itemId}')
def getInspect(idGame:str,itemId:int):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        logger.info("Search for items in game")
        for item in games[idGame].get_objects():
            if item.id == itemId:
                return item.inspecter()
        logger.warning("Item %s not found",itemId)
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"L'item avec l'ID {itemId} n'est pas dans l'inventaire."
            )
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_obj.patch('/{idGame}/objets/interact/{itemID1}-{itemID2}')
def interactObjs(idGame:str,itemID1:int ,itemID2:int):
    logger.info("Search for the game %s",idGame)
    if idGame in games:
        logger.info("Search for items in inventory")
        if games[idGame].inventory.hasItem(itemID1) & games[idGame].inventory.hasItem(itemID2):
            for item in games[idGame].get_objects():
                if item.id == itemID1:
                    if type(item)!=ObjetInteractif:
                        logger.warning("Item isn't interactive")
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The item is not interactive."
                            )
                    return item.utiliser(itemID2)
        logger.warning("Items not found")
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Not all the items are in the inventory."
            )
    else :
        logger.warning("Game %s not found",idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )