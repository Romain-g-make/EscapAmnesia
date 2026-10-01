from app.domain import (
    GameElement,
    Item,
    Door,
    CodePuzzle,
    HashPuzzle,
    Room,
)


def test_game_element_to_dict():
    elem = GameElement(id="elem_1", name="Test Elem", description="Un élément de test")
    assert elem.id == "elem_1"
    assert elem.name == "Test Elem"
    data = elem.to_dict()
    assert data == {
        "id": "elem_1",
        "name": "Test Elem",
        "description": "Un élément de test"
    }


def test_item_inheritance():
    item = Item(id="item_key", name="Clé Rouillée", description="Une petite clé en laiton")
    assert isinstance(item, GameElement)
    assert item.to_dict()["id"] == "item_key"


def test_door_attributes_and_unlock():
    door = Door(
        id="door_exit",
        name="Porte de sortie",
        description="Porte en chêne massif",
        is_locked=True,
        required_item_id="item_key"
    )
    assert door.is_locked is True
    assert door.required_item_id == "item_key"
    door.unlock()
    assert door.is_locked is False


def test_code_puzzle_check_solution():
    code_puzzle = CodePuzzle(
        id="puz_code",
        name="Digicode",
        description="Entrez le code à 4 chiffres",
        secret_code="7635"
    )
    assert code_puzzle.check_solution("7635") is True
    assert code_puzzle.check_solution(" 7635 ") is True
    assert code_puzzle.check_solution("0000") is False
    assert code_puzzle.check_solution("") is False


def test_hash_puzzle_sha256_check_solution():
    expected_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    hash_puzzle = HashPuzzle(
        id="puz_hash",
        name="Coffre Cryptographique",
        description="Déverrouillable uniquement avec le mot de passe dont le hash correspond",
        expected_hash=expected_hash
    )
    assert hash_puzzle.check_solution("password") is True
    assert hash_puzzle.check_solution("wrongpassword") is False
    assert hash_puzzle.check_solution("") is False


def test_room_composition_and_to_dict():
    item = Item(id="it_1", name="Lampe UV", description="Révèle les traces")
    door = Door(id="dr_1", name="Porte Blindée", description="Accès sas", is_locked=True)
    puzzle = CodePuzzle(id="pz_1", name="Clavier", description="Code", secret_code="1234")

    room = Room(
        id="room_lab",
        name="Laboratoire",
        description="Une salle sombre",
        items=[item],
        doors=[door],
        puzzles=[puzzle]
    )

    data = room.to_dict()
    assert data["id"] == "room_lab"
    assert len(data["items"]) == 1
    assert data["items"][0]["id"] == "it_1"
    assert len(data["doors"]) == 1
    assert data["doors"][0]["id"] == "dr_1"
    assert len(data["puzzles"]) == 1
    assert data["puzzles"][0]["id"] == "pz_1"

    assert room.inspect_item("it_1")["name"] == "Lampe UV"
    assert "error" in room.inspect_item("it_inconnu")

    assert room.get_puzzle("pz_1") is puzzle
    assert room.get_puzzle("pz_inconnu") is None
