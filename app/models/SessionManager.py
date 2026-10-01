import datetime
import logging
from .Salle import Salle
from .Inventory import Inventory
from ..services.ItemsList import (
    injecteur_uv, coffre_quantique, partition_holoclavier, oculometre, porte_chambre,
    drone_maintenance, pile_lithium, puce_dechiffrement, terminal_decharge, sas_rez_de_chaussee,
    analyseur_neuro_trauma, module_bypass, bande_donnees
)

logger = logging.getLogger(__name__)


class SessionManager:

    scenar1 = (
        "ZONE 1 - LA CHAMBRE (CONFINEMENT INITIAL)\n"
        "Tu te réveilles, seul, dans une chambre inconnue. Des grattes-ciels sombres sont visibles par la fenêtre.\n"
        "Pour sortir, tu dois déverrouiller la porte de la chambre via son digicode."
    )

    scenar2 = (
        "ZONE 2 - L'IMMEUBLE (ESCALIER & COULOIR)\n"
        "Tu accèdes aux parties communes. La sortie au rez-de-chaussée est verrouillée par le Sas.\n"
        "Tu dois réalimenter et configurer le Terminal de Décharge mural pour ouvrir la porte."
    )

    scenar3 = (
        "ZONE 3 - L'ACCIDENT / LA SAUVEGARDE (ESPACE NEURO-VIRTUEL)\n"
        "Un accident survient ! Ton corps bascule dans le coma. Une sauvegarde de ta conscience est active.\n"
        "Restaure ta séquence cérébrale en configurant les signaux d'ondes sur l'Analyseur."
    )

    scenar4 = (
        "ZONE 4 - L'HÔPITAL (RÉVEIL FINAL)\n"
        "« Bonjour Etsilon, comment vas-tu ? » La séquence de réalignement est terminée.\n"
        "Tu es tiré d'affaire, la simulation prend fin."
    )

    indice1 = "Révèle le schéma du scanner avec la lumière UV, puis associe la partition d'holoclavier à l'oculomètre[cite: 1]."
    indice2 = "Trouve la pile '84' dans le drone et la puce '693' dans l'ascenseur pour alimenter le terminal mural[cite: 1]."
    indice3 = "Insère la bande de données dans l'analyseur pour lire les signaux A, B, C et aligne les 3 interrupteurs[cite: 1]."
    indice4 = "Séquence terminée[cite: 1]."

    def __init__(self, etat, tempsRestant, niveauActuel, inventory: Inventory):
        self.etat = etat
        self.dateDebut = datetime.date.today()
        self.tempsRestant = tempsRestant
        self.inventory = inventory

        self.salle1 = Salle(
            id=1,
            name="Chambre",
            state="en_jeu",
            scenario=self.scenar1,
            indice=self.indice1,
            listObj=[injecteur_uv, coffre_quantique, partition_holoclavier, oculometre, porte_chambre],
            exitCode="7635"
        )

        self.salle2 = Salle(
            id=2,
            name="Immeuble",
            state="en_jeu",
            scenario=self.scenar2,
            indice=self.indice2,
            listObj=[drone_maintenance, pile_lithium, puce_dechiffrement, terminal_decharge, sas_rez_de_chaussee],
            exitCode="84693"
        )

        self.salle3 = Salle(
            id=3,
            name="Accident / Sauvegarde",
            state="en_jeu",
            scenario=self.scenar3,
            indice=self.indice3,
            listObj=[analyseur_neuro_trauma, module_bypass, bande_donnees],
            exitCode="101"
        )

        self.salle4 = Salle(
            id=4,
            name="Hôpital",
            state="en_jeu",
            scenario=self.scenar4,
            indice=self.indice4,
            listObj=[],
            exitCode=""
        )

        match niveauActuel:
            case 1:
                self.niveauActuel = self.salle1
            case 2:
                self.niveauActuel = self.salle2
            case 3:
                self.niveauActuel = self.salle3
            case 4:
                self.niveauActuel = self.salle4

    def endGame(self, v: bool):
        if v:
            logger.info('The player end the game')
            print("Bravo vous avez gagné en : ", datetime.date.today() - self.dateDebut)

    def levelChange(self, code: str):
        logger.info('The player change the level')

        if self.niveauActuel.tryEscape(code):
            self.niveauActuel = self.nextLevel()
            return {"status": "true"}
        return {"status": "false"}

    def nextLevel(self):
        if self.niveauActuel.id == 1:
            return self.salle2
        elif self.niveauActuel.id == 2:
            return self.salle3
        elif self.niveauActuel.id == 3:
            return self.salle4
        return self.salle4

    def get_data(self):
        return self.niveauActuel.getInfo()

    def get_obj(self):
        return self.niveauActuel.getObjects()

    def get_hint(self):
        return self.niveauActuel.getHint()

    def get_objects(self):
        return self.niveauActuel.listObj