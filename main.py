from fastapi import FastAPI
import uuid
from app.SessionManager import SessionManager
from app.Inventory import Inventory
from app.ObjetInteractif import ObjetInteractif
from pydantic import BaseModel

class SessionManagerCreate(BaseModel):
    etat : str
    temps_restant : int
    niveau_actuel : int


app = FastAPI(title="EscapeEngine API Test")
games = {}

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}

@app.post("/start")
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

@app.delete("/{idGame}")
def deleteGame(idGame:str):
    if idGame in games:
        del games[idGame]
        return {"status":"ok"}
    return {"status":"error","message":"Wrong room id"},404




#GESTION SALLE
@app.get("/{idGame}/room/get")
def get_data_room(idGame:str):
    if idGame in games:
        return games[idGame].get_data()
    return {"status":"error","message":"Wrong room id"},404

@app.get('/{idGame}/indice')
def getInd(idGame:str):
    if idGame in games:
        return games[idGame].get_hint()
    return {"status":"error","message":"Wrong room id"},404
    

@app.patch('/{idGame}/tryescape/{code}')
def tryEscape(idGame:str,code:int):
    if idGame in games:
        return games[idGame].levelChange(code)
    return {"status":"error","message":"Wrong room id"},404




#GESTION INVENTAIRE
@app.patch("/{idGame}/inventory/addItem/{itemId}")
def addItem(idGame:str,itemId: int):
    if idGame in games:
        return games[idGame].inventory.addItem(itemId)
    return {"status":"error","message":"Wrong room id"},404

@app.patch("/{idGame}/inventory/removeItem/{itemId}")
def removeItem(idGame:str,itemId: int):
    if idGame in games:
        return games[idGame].inventory.removeItem(itemId)
    return {"status":"error","message":"Wrong room id"},404

@app.get("/{idGame}/inventory/showInventory")
def showInventory(idGame:str):
    if idGame in games:
        return games[idGame].inventory.showInventory()
    return {"status":"error","message":"Wrong room id"},404




#OBJETS 
@app.get('/{idGame}/objet/get')
def getObj(idGame:str):
    if idGame in games:
        return games[idGame].get_obj()
    return {"status":"error","message":"Wrong room id"},404

@app.get('/{idGame}/objet/inspect/{itemId}')
def getInspect(idGame:str,itemId:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemId:
                return item.inspecter()
        return {"status":"error","message":"This item isn't in the room"}
    return {"status":"error","message":"Wrong room id"},404

@app.patch('/{idGame}/objets/interact/{itemID1}-{itemID2}')
def interactObjs(idGame:str,itemID1:int ,itemID2:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemID1:
                if type(item)!=ObjetInteractif:
                    return {"status":"error","message":"This object is not interactive"}
                return item.utiliser(itemID2)
        return {"status":"error","message":"This item isn't in the room"}
    return {"status":"error","message":"Wrong room id"},404