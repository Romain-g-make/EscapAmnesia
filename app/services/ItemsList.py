from app.models.Item import Item
from app.models.ObjetInteractif import ObjetInteractif
from app.models.Conteneur import Conteneur

# 1. ARTICLES & PROPS SIMPLES (Item)

injecteur_uv = Item(
    id=1, 
    nom="Injecteur de Luminescence", 
    description="Lampe UV Swat / Cyberpunk permettant de révéler l'encre et le sérum invisible.", 
    etat="Possédé (Inventaire)"
)

partition_holoclavier = Item(
    id=3, 
    nom="Partition d'Holoclavier vierge", 
    description="Support physique en feuille plastifiée indiquant les 4 mesures de fréquences numériques.", 
    etat="Dans le tiroir de la table de chevet"
)

oculometre = Item(
    id=4, 
    nom="Oculomètre Portable", 
    description="Scanner optique factice permettant de lire les fréquences chiffrées (7-6-3-5) sur la partition.", 
    etat="À l'intérieur du Coffre-Fort Quantique"
)

pile_lithium = Item(
    id=6, 
    nom="Pile Lithium-Cristal", 
    description="Batterie stylisée marquée du chiffre '84', source d'énergie pour le Terminal.", 
    etat="Dans le boîtier du Drone de Maintenance"
)

puce_dechiffrement = Item(
    id=7, 
    nom="Puce de Déchiffrement", 
    description="Carte à puce décorative marquée '693' fournissant la clé logique pour le Terminal.", 
    etat="Boîtier électrique ouvert de l'ascenseur"
)

bande_donnees = Item(
    id=11, 
    nom="Bande de Données Magnétique", 
    description="Ruban physique raccordé au Module de Bypass à insérer dans l'Analyseur de Neuro-Trauma.", 
    etat="Raccordée au Module de Bypass"
)

# 2. OBJETS INTERACTIFS & CONTENEURS

coffre_quantique = ObjetInteractif(
    id=2, 
    nom="Coffre-Fort Quantique", 
    description="Coffre électronique sous le lit déverrouillable en révélant le schéma au sérum UV.", 
    etat="Sous le lit",
    useEffect="Le coffre-fort se déverrouille ! Vous y récupérez l'Oculomètre Portable.",
    objs=[injecteur_uv, oculometre]
)

porte_chambre = ObjetInteractif(
    id=12, 
    nom="Porte de la Chambre", 
    description="Digicode électronique contrôlant la sortie du confinement initial.", 
    etat="Armé",
    useEffect="Code 7635 validé ! La porte de la chambre s'ouvre sur la cage d'escalier.",
    objs=[partition_holoclavier, oculometre]
)

drone_maintenance = Conteneur(
    id=5, 
    nom="Drone de Maintenance HS", 
    description="Drone décoratif à trappe fermée hébergeant la pile au lithium-cristal.", 
    etat="Suspendu dans la cage d'escalier",
    estFerme=True, 
    codeSerrure="Mécanique",
    open="Vous ouvrez le boîtier du drone et récupérez la Pile Lithium-Cristal (84)."
)

terminal_decharge = ObjetInteractif(
    id=8, 
    nom="Terminal de Décharge", 
    description="Interface murale. Nécessite la pile et la puce pour s'allumer et valider le code du Sas.", 
    etat="Près de la porte de sortie Immeuble (Éteint)",
    useEffect="Terminal alimenté et déchiffré. Entrez la combinaison [84693] pour ouvrir le sas.",
    objs=[pile_lithium, puce_dechiffrement]
)

sas_rez_de_chaussee = ObjetInteractif(
    id=13, 
    nom="Sas du Rez-de-Chaussée", 
    description="Porte de sortie de l'immeuble reliée au Terminal de Décharge.", 
    etat="Verrouillé",
    useEffect="Code 84693 validé ! Le sas de sortie se déverrouille.",
    objs=[terminal_decharge]
)

analyseur_neuro_trauma = ObjetInteractif(
    id=9, 
    nom="Analyseur de Neuro-Trauma", 
    description="Écran fixe avec fente lectrice d'ondes. Affiche le diagnostic tricanal (Signal A: Haut(1), B: Plat(0), C: Haut(1)).", 
    etat="Console centrale de simulation",
    useEffect="Bande analysée : Signal A = 1, Signal B = 0, Signal C = 1. Alignez le Module de Bypass sur 101.",
    objs=[bande_donnees]
)

module_bypass = ObjetInteractif(
    id=10, 
    nom="Module de Bypass Cérébral", 
    description="Boîtier physique avec 3 interrupteurs bi-position [A, B, C] réglés sur [0, 0, 0].", 
    etat="Au sol près du corps dans le coma",
    useEffect="Bascule sur [1-0-1] confirmée ! Réalignement de la conscience réussi, fin de la séquence.",
    objs=[bande_donnees]
)
itemList = [
    injecteur_uv,
    coffre_quantique,
    partition_holoclavier,
    oculometre,
    drone_maintenance,
    pile_lithium,
    puce_dechiffrement,
    terminal_decharge,
    analyseur_neuro_trauma,
    module_bypass,
    bande_donnees,
    porte_chambre,
    sas_rez_de_chaussee
]