from .game_router import games
from fastapi import APIRouter,HTTPException,status

router_inventory = APIRouter(tags=["Inventory"])
#GESTION INVENTAIRE
@router_inventory.patch("/{idGame}/inventory/addItem/{itemId}")
def addItem(idGame:str,itemId: int):
    if idGame in games:
        if itemId>13:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"L'item avec l'ID {itemId} n'existe pas."
                )
        return games[idGame].inventory.addItem(itemId)
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_inventory.patch("/{idGame}/inventory/removeItem/{itemId}")
def removeItem(idGame:str,itemId: int):
    if idGame in games:
        if itemId>13:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"L'item avec l'ID {itemId} n'existe pas."
                )
        return games[idGame].inventory.removeItem(itemId)
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_inventory.get("/{idGame}/inventory/showInventory")
def showInventory(idGame:str):
    if idGame in games:
        return games[idGame].inventory.showInventory()
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )