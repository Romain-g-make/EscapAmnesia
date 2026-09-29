import uuid
from fastapi import APIRouter,HTTPException,status
from app.models.SessionManager import SessionManager
from app.models.Inventory import Inventory
from pydantic import BaseModel

global games
games = {}

router_game = APIRouter(tags=["Game"])

class SessionManagerCreate(BaseModel):
    etat : str
    temps_restant : int
    niveau_actuel : int


@router_game.post("/start")
def start(session:SessionManagerCreate):
    mess = ""
    idG = str(uuid.uuid4())
    inventaire = Inventory(10)
    game = SessionManager(
        etat=session.etat,
        tempsRestant=session.temps_restant,
        niveauActuel=session.niveau_actuel,
        inventory=inventaire
        
    )
    games[idG]=game
    return {"status": "ok", "message": mess,"id":idG}

@router_game.delete("/{idGame}")
def deleteGame(idGame:str):
    if idGame in games:
        del games[idGame]
        return {"status":"ok"}
    else :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La partie avec l'ID {idGame} n'existe pas."
        )
