from Conteneur import Conteneur
from Item import Item
from ObjetInteractif import ObjetInteractif

# --- INVENTAIRE & CHAMBRE ---
injecteur_uv = Item(
    id=1, 
    nom="Injecteur de Luminescence", 
    description="Lampe UV Swat / Cyberpunk permettant de révéler l'encre et le sérum invisible", 
    etat="Possédé (Inventaire)"
)

coffre_quantique = ObjetInteractif(
    id=2, 
    nom="Coffre-Fort Quantique", 
    description="Coffre électronique sous le lit déverrouillable via schéma UV", 
    etat="Sous le lit",
    estFerme=True, 
    codeSerrure="Schéma UV"
)

partition_holoclavier = Item(
    id=3, 
    nom="Partition d'Holoclavier vierge", 
    description="Support physique en feuille plastifiée indiquant les fréquences numériques", 
    etat="Dans le tiroir de la table de chevet"
)

oculometre = Item(
    id=4, 
    nom="Oculomètre Portable", 
    description="Scanner optique factice permettant d'associer la partition aux fréquences chiffrées", 
    etat="À l'intérieur du Coffre-Fort Quantique"
)

# --- L'IMMEUBLE ---
drone_maintenance = Conteneur(
    id=5, 
    nom="Drone de Maintenance HS", 
    description="Drone décoratif à trappe ouverte hébergeant la pile au lithium-cristal", 
    etat="Suspendu dans la cage d'escalier",
    estFerme=True, 
    codeSerrure="Mécanique"
)

pile_lithium = Item(
    id=6, 
    nom="Pile Lithium-Cristal", 
    description="Batterie stylisée avec marqueur '84', source d'énergie pour le Terminal", 
    etat="Dans le boîtier du Drone de Maintenance"
)

puce_dechiffrement = Item(
    id=7, 
    nom="Puce de Déchiffrement", 
    description="Carte à puce décorative '693' fournissant la clé logique pour le Terminal", 
    etat="Boîtier électrique ouvert de l'ascenseur"
)

terminal_decharge = ObjetInteractif(
    id=8, 
    nom="Terminal de Décharge", 
    description="Écran/Interface murale qui accepte la pile + puce et valide le code du Sas", 
    etat="Près de la porte de sortie Immeuble",
    estFerme=True, 
    codeSerrure="84693"
)

# --- ESPACE NEURO-VIRTUEL ---
analyseur_neuro_trauma = ObjetInteractif(
    id=9, 
    nom="Analyseur de Neuro-Trauma", 
    description="Écran fixe + fente lectrice qui lit la bande magnétique et affiche le diagnostic d'ondes", 
    etat="Console centrale de simulation",
    estFerme=False, 
    codeSerrure=None
)

module_bypass = ObjetInteractif(
    id=10, 
    nom="Module de Bypass Cérébral", 
    description="Boîtier physique avec 3 interrupteurs bi-position permettant de basculer les canaux [A, B, C] sur 101", 
    etat="Au sol près du corps dans le coma",
    estFerme=True, 
    codeSerrure="101"
)

bande_donnees = Item(
    id=11, 
    nom="Bande de Données Magnétique", 
    description="Ruban physique à insérer dans l'Analyseur de Neuro-Trauma", 
    etat="Raccordée au Module de Bypass"
)

porte_chambre = ObjetInteractif(
    id=12, 
    nom="Porte de la Chambre", 
    description="Digicode électronique contrôlant la sortie du confinement initial", 
    etat="Armé",
    estFerme=True, 
    codeSerrure="7635"
)

sas_rez_de_chaussee = ObjetInteractif(
    id=13, 
    nom="Sas du Rez-de-Chaussée", 
    description="Porte de sortie de l'immeuble reliée au Terminal de Décharge", 
    etat="Verrouillé",
    estFerme=True, 
    codeSerrure="84693"
)