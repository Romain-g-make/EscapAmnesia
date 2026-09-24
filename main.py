from fastapi import FastAPI
from app.SessionManager import SessionManager
from app.Inventory import Inventory
from app.ObjetInteractif import ObjetInteractif

app = FastAPI(title="EscapeEngine API Test")
inventaire = Inventory(10)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}


#DEBUT DU JEU 

@app.get("/start")
def start():
    mess = ""
    global game
    game = SessionManager(1,"en_jeu",60,1)
    return {"status": "ok", "message": mess}


#GESTION SALLE
@app.get("/room/get")
def get_data_room():
    return game.get_data()

@app.get('/indice')
def getInd():
    return game.get_hint()

@app.patch('/tryescape/{code}')
def tryEscape(code:int):
    return game.levelChange(code)




#GESTION INVENTAIRE
@app.patch("/inventory/addItem/{itemId}")
def addItem(itemId: int):
    return inventaire.addItem(itemId)

@app.patch("/inventory/removeItem/{itemId}")
def removeItem(itemId: int):
    return inventaire.removeItem(itemId)

@app.get("/inventory/showInventory")
def showInventory():
    return inventaire.showInventory()




#OBJETS 
@app.get('/objet/get')
def getObj():
    return game.get_obj()

@app.get('/objet/inspect/{itemId}')
def getInspect(itemId:int):
    for item in game.get_objects():
        if item.id == itemId:
            return item.inspecter()
    return {"status":"error","message":"This item isn't in the room"}

@app.patch('/objets/interact/{itemID1}-{itemID2}')
def interactObjs(itemID1:int ,itemID2:int):
    for item in game.get_objects():
        if item.id == itemID1:
            if type(item)!=ObjetInteractif:
                return {"status":"error","message":"This object is not interactive"}
            return item.utiliser(itemID2)
    return {"status":"error","message":"This item isn't in the room"}