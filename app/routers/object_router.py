from .game_router import games
import logging
from fastapi import APIRouter, HTTPException, status
from app.models.ObjetInteractif import ObjetInteractif

logger = logging.getLogger(__name__)

router_obj = APIRouter(tags=["Objects"])


# OBJETS
@router_obj.get('/{idGame}/objet/get')
def getObj(idGame: str):
    logger.info("Search for the game %s", idGame)
    if idGame in games:
        logger.info("Search for items")
        return games[idGame].get_obj()
    else:
        logger.warning("Game %s not found", idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )


@router_obj.get('/{idGame}/objet/inspect/{itemId}')
def getInspect(idGame: str, itemId: int):
    logger.info("Search for the game %s", idGame)
    if idGame in games:
        logger.info("Search for item %s in game or inventory", itemId)
        # Vérification dans les objets de la pièce
        for item in games[idGame].get_objects():
            if item.id == itemId:
                return item.inspecter()
        # Vérification dans l'inventaire du joueur
        if games[idGame].inventory.hasItem(itemId):
            return games[idGame].inventory.inventory[itemId].inspecter()

        logger.warning("Item %s not found", itemId)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'item avec l'ID {itemId} n'est ni dans la pièce ni dans l'inventaire."
        )
    else:
        logger.warning("Game %s not found", idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )


@router_obj.patch('/{idGame}/objets/interact/{itemID1}-{itemID2}')
def interactObjs(idGame: str, itemID1: int, itemID2: int):
    logger.info("Search for the game %s", idGame)
    if idGame in games:
        game = games[idGame]
        logger.info("Interact %s with %s", itemID1, itemID2)

        # 1. Rechercher l'objet interactif (dans la pièce ou l'inventaire)
        target_obj = None
        for item in game.get_objects():
            if item.id == itemID1:
                target_obj = item
                break
        if target_obj is None and game.inventory.hasItem(itemID1):
            target_obj = game.inventory.inventory[itemID1]

        if target_obj is None:
            logger.warning("Target object %s not found", itemID1)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"L'objet {itemID1} n'a pas été trouvé dans la pièce ou l'inventaire."
            )

        if not isinstance(target_obj, ObjetInteractif):
            logger.warning("Item %s is not interactive", itemID1)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"L'objet {itemID1} n'est pas interactif."
            )

        # 2. Vérifier que le second objet est possédé dans l'inventaire ou présent dans la pièce
        item2_present = game.inventory.hasItem(itemID2) or any(it.id == itemID2 for it in game.get_objects())
        if not item2_present:
            logger.warning("Item %s not found in inventory or room", itemID2)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"L'objet {itemID2} n'est ni dans l'inventaire ni dans la pièce."
            )

        # 3. Exécuter l'interaction
        return target_obj.utiliser(itemID2)
    else:
        logger.warning("Game %s not found", idGame)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )