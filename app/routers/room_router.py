from .game_router import games
from fastapi import APIRouter,HTTPException,status
from app.models.SessionManager import SessionManager
from app.models.Inventory import Inventory
from app.models.ObjetInteractif import ObjetInteractif

router_room = APIRouter(tags=["Room"])
#GESTION SALLE
@router_room.get("/{idGame}/room/get")
def get_data_room(idGame:str):
    if idGame in games:
        return games[idGame].get_data()
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )

@router_room.get('/{idGame}/indice')
def getInd(idGame:str):
    if idGame in games:
        return games[idGame].get_hint()
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )
    

@router_room.patch('/{idGame}/tryescape/{code}')
def tryEscape(idGame:str,code:int):
    if idGame in games:
        return games[idGame].levelChange(code)
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )
