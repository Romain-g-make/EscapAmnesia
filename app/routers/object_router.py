from .game_router import games
from fastapi import APIRouter,HTTPException,status
from app.models.ObjetInteractif import ObjetInteractif

router_obj = APIRouter(tags=["Objects"])
#OBJETS 
@router_obj.get('/{idGame}/objet/get')
def getObj(idGame:str):
    if idGame in games:
        return games[idGame].get_obj()
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_obj.get('/{idGame}/objet/inspect/{itemId}')
def getInspect(idGame:str,itemId:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemId:
                return item.inspecter()
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"L'item avec l'ID {itemId} n'est pas dans l'inventaire."
            )
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_obj.patch('/{idGame}/objets/interact/{itemID1}-{itemID2}')
def interactObjs(idGame:str,itemID1:int ,itemID2:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemID1:
                if type(item)!=ObjetInteractif:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"L'item n'est pas interactif."
                        )
                return item.utiliser(itemID2)
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tout les items ne sont pas dans l'inventaire."
            )
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )