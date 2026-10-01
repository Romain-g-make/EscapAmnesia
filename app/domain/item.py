from dataclasses import dataclass
from .game_element import GameElement


@dataclass
class Item(GameElement):
    """Objet ramassable ou inspectable dans le jeu."""
    pass
