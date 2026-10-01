from abc import ABC, abstractmethod
from dataclasses import dataclass
import hashlib
from .game_element import GameElement


@dataclass
class Puzzle(GameElement, ABC):
    """Classe abstraite polymorphe représentant une énigme ou un mécanisme."""

    @abstractmethod
    def check_solution(self, answer: str) -> bool:
        """Vérifie si la réponse fournie résout l'énigme."""
        pass


@dataclass
class CodePuzzle(Puzzle):
    """Énigme validée par comparaison directe avec un code secret en clair."""
    secret_code: str = ""

    def check_solution(self, answer: str) -> bool:
        """Compare directement la réponse fournie avec le code secret stocké."""
        if not answer:
            return False
        return answer.strip() == self.secret_code.strip()


@dataclass
class HashPuzzle(Puzzle):
    """Énigme de sécurité / cryptographie vérifiant une empreinte SHA-256."""
    expected_hash: str = ""

    def check_solution(self, answer: str) -> bool:
        """Calcule l'empreinte SHA-256 de la tentative et la compare au hash attendu."""
        if not answer:
            return False
        computed_hash = hashlib.sha256(answer.strip().encode("utf-8")).hexdigest()
        return computed_hash.lower() == self.expected_hash.strip().lower()
