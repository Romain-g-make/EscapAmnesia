import FastAPI
import uuid
from app.SessionManager import SessionManager
from app.Inventory import Inventory
from app.ObjetInteractif import ObjetInteractif

app = FastAPI(title="EscapeEngine API Test")
games = {}

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}


#DEBUT DU JEU 

@app.get("/start")
def start():
    mess = ""
    uuid = str(uuid.uuid4())
    inventaire = Inventory(10)
    game = SessionManager(1,"en_jeu",60,1,inventaire)
    games[uuid]=game
    return {"status": "ok", "message": mess,"id":uuid}


#GESTION SALLE
@app.get("/{idGame}/room/get")
def get_data_room(idGame:int):
    if idGame in games:
        return games[idGame].get_data()
    return {"status":"error","message":"Wrong room id"}

@app.get('/{idGame}/indice')
def getInd(idGame:int):
    if idGame in games:
        return games[idGame].get_hint()
    return {"status":"error","message":"Wrong room id"}
    

@app.patch('/{idGame}/tryescape/{code}')
def tryEscape(idGame:int,code:int):
    if idGame in games:
        return games[idGame].levelChange(code)
    return {"status":"error","message":"Wrong room id"}




#GESTION INVENTAIRE
@app.patch("/{idGame}/inventory/addItem/{itemId}")
def addItem(idGame:int,itemId: int):
    if idGame in games:
        return games[idGame].inventory.addItem(itemId)
    return {"status":"error","message":"Wrong room id"}

@app.patch("/{idGame}/inventory/removeItem/{itemId}")
def removeItem(idGame:int,itemId: int):
    if idGame in games:
        return games[idGame].inventory.removeItem(itemId)
    return {"status":"error","message":"Wrong room id"}

@app.get("/{idGame}/inventory/showInventory")
def showInventory(idGame:int):
    if idGame in games:
        return games[idGame].inventory.showInventory()
    return {"status":"error","message":"Wrong room id"}




#OBJETS 
@app.get('/{idGame}/objet/get')
def getObj(idGame:int):
    if idGame in games:
        return games[idGame].get_obj()
    return {"status":"error","message":"Wrong room id"}

@app.get('/{idGame}/objet/inspect/{itemId}')
def getInspect(idGame:int,itemId:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemId:
                return item.inspecter()
        return {"status":"error","message":"This item isn't in the room"}
    return {"status":"error","message":"Wrong room id"}

@app.patch('/{idGame}/objets/interact/{itemID1}-{itemID2}')
def interactObjs(idGame:int,itemID1:int ,itemID2:int):
    if idGame in games:
        for item in games[idGame].get_objects():
            if item.id == itemID1:
                if type(item)!=ObjetInteractif:
                    return {"status":"error","message":"This object is not interactive"}
                return item.utiliser(itemID2)
        return {"status":"error","message":"This item isn't in the room"}
    return {"status":"error","message":"Wrong room id"}