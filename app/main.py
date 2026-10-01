from fastapi import FastAPI
from app.routers.game_router import router_game
from app.routers.object_router import router_obj
from app.routers.inventory_router import router_inventory
from app.routers.room_router import router_room

app = FastAPI(title="EscapeEngine API Test")

app.include_router(router_game)
app.include_router(router_inventory)
app.include_router(router_obj)
app.include_router(router_room)


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "online",
        "game_title": "EscapAmnesia",
        "engine_version": "1.0.0"
    }


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Environnement Conda prêt pour l'Escape Game !"}
