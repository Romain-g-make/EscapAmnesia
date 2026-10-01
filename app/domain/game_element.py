from dataclasses import dataclass, asdict


@dataclass
class GameElement:
    """Classe de base pour tous les éléments interactifs du jeu."""
    id: str
    name: str
    description: str

    def to_dict(self) -> dict:
        """Sérialise l'élément en dictionnaire."""
        return asdict(self)
