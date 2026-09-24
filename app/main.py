from fastapi import FastAPI
from .app.services.game_route import game_route

app = FastAPI(title="EscapeEngine API Test")

app.include_router(game_route)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}

