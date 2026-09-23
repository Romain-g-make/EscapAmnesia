from fastapi import FastAPI

app = FastAPI(title="Api de l'inventaire")

@app.patch("/inventory/addItem/{itemId}")
def addItem(itemId: int):
    
    return {"Ajout": 'Item {itemId} ajouté à l\'inventaire'}

@app.patch("/inventory/removeItem/{itemId}")
def removeItem(itemId: int):
    return {"Retrait": 'Item {itemId} retiré de l\'inventaire'}

@app.get("/inventory/showInventory")
def showInventory():
    return {"Affichage": 'Affichage des items de l\'inventaire.'}