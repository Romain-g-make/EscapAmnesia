from dataclasses import dataclass, field
from typing import Optional
from .game_element import GameElement
from .item import Item
from .door import Door
from .puzzle import Puzzle


@dataclass
class Room(GameElement):
    """Salle de jeu contenant des objets, des portes et des énigmes."""
    items: list[Item] = field(default_factory=list)
    doors: list[Door] = field(default_factory=list)
    puzzles: list[Puzzle] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Sérialise la salle avec l'ensemble de ses éléments interactifs."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "items": [item.to_dict() for item in self.items],
            "doors": [door.to_dict() for door in self.doors],
            "puzzles": [puzzle.to_dict() for puzzle in self.puzzles],
        }

    def inspect_item(self, item_id: str) -> dict:
        """Inspecte un objet spécifique présent dans la pièce."""
        for item in self.items:
            if item.id == item_id:
                return item.to_dict()
        return {"error": f"Item '{item_id}' non trouvé dans la pièce."}

    def get_puzzle(self, puzzle_id: str) -> Optional[Puzzle]:
        """Recherche une énigme par son identifiant."""
        for puzzle in self.puzzles:
            if puzzle.id == puzzle_id:
                return puzzle
        return None
