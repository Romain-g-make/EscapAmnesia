from fastapi import FastAPI
from pydantic import BaseModel

players = [
    {
        "id": 1,
        "name": "Alice",.0
        "score": 1200,
        "level": 12,
    },
    {
        "id": 2,
        "name": "Bob",
        "score": 950,
        "level": 9,
    },
    {
        "id": 42,
        "name": "Zelda",
        "score": 3000,
        "level": 99,
    }
]

class Player(BaseModel):
    name: str
    score: int
    level: int

app = FastAPI()

@app.get("/players")
def get_players():
    return players

@app.get("/players/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player
        return {"error": "Player not found"}

@app.get("/players/{player_id}")
def get_player(player_id: int):
    # Pour tester, on renvoie juste l'ID converti
    return {
        "id": player_id
    }

@app.post("/players")
def create_player(player: Player):
    # 1. On transforme l'objet validé par Pydantic en dictionnaire
    new_player = player.model_dump()
    # 2. On génère un nouvel ID (par exemple, la taille de la liste + 1)
    new_player["id"] = len(players) + 1
    # 3. On l'ajoute à notre fausse base de données
    players.append(new_player)
    return new_player

@app.get("/")
def home():
    return {"message": "Bienvenue sur FastAPI"}