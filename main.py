from fastapi import FastAPI
from fastapi import FastAPI
from app.SessionManager import SessionManager
from app.Inventory import Inventory

app = FastAPI(title="EscapeEngine API Test")
inventaire = Inventory(10)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}


@app.get("/start")
def start():
    mess = ""
    global game
    game = SessionManager(1,"en_jeu",60,1)
    return {"status": "ok", "message": mess}

@app.get("/room/get")
def get_data_room():
    return game.get_data()


@app.patch("/inventory/addItem/{itemId}")
def addItem(itemId: int):
    return inventaire.addItem(itemId)

@app.patch("/inventory/removeItem/{itemId}")
def removeItem(itemId: int):
    return inventaire.removeItem(itemId)

@app.get("/inventory/showInventory")
def showInventory():
    return inventaire.showInventory()

@app.get('/objet/get')
def getObj():
    return game.get_obj()

@app.get('/indice')
def getInd():
    return game.get_hint()

@app.get('/tryescape/{code}')
def tryEscape(code:int):
    return game.levelChange(code)

