from dataclasses import dataclass
from typing import Optional
from .game_element import GameElement


@dataclass
class Door(GameElement):
    """Porte reliant des pièces ou bloquant une issue."""
    is_locked: bool = True
    required_item_id: Optional[str] = None

    def unlock(self) -> None:
        """Déverrouille la porte."""
        self.is_locked = False
