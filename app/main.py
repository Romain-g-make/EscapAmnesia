from fastapi import FastAPI
from SessionManager import SessionManager

app = FastAPI(title="EscapeEngine API Test")


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}


@app.get("/start")
def start():
    mess = ""
    global game
    game = SessionManager(1,"en_jeu",60,1)
    return {"status": "ok", "message": mess}

@app.get("/get-data-room")
def get_data_room():
    return game.get_data()


@app.patch("/inventory/addItem/{itemId}")
def addItem(itemId: int):
    return {"Ajout": 'Item {itemId} ajouté à l\'inventaire'}

@app.patch("/inventory/removeItem/{itemId}")
def removeItem(itemId: int):
    return {"Retrait": 'Item {itemId} retiré de l\'inventaire'}

@app.get("/inventory/showInventory")
def showInventory():
    return {"Affichage": 'Affichage des items de l\'inventaire.'}