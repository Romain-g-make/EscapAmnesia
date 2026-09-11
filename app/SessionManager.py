import datetime
from Salle import Salle

class SessionManager:

    scenar1 = "Tu viens de te réveiller, seul, dans une chambre que tu ne connais pas.\n Autour de toi des lumières vives, une petite photo de famille orne le meuble de télé,\n un homme brun, yeux marrons avec des tâches de rousseurs, par la fenêtre des grattes ciels sombres,\n et une petite musique de jazz vient des voisins."
    scenar2 = "Enfin sorti, l'immeuble s'ouvre à toi, rien d'intéressant donc tu files au rez de chaussé\n. La porte est aussi fermé de l'intérieur, verrouillé par un code à 5 chiffre."
    scenar3 = "Débarasser de cet enfer, tu est libre et.\n !! BAM !! \nUne voiture, un homme à terre, un accident stupide mais te voilà dans le coma.\n Par chance ton corps possède une sauvegarde de ta conscience, mais pour la restaurer il faut trouver..."
    scenar4 = "Te voilà debout, le médecin vient te voir : \"Bonjour Etsilon, comment vas-tu ?\" \nTu ne sais pas, à vrai dire tu ne te souvenais pas de ton prénom, peut être que l'accident t'as chamboulé ?\n La chambre est quasi vide, un miroir, ton lit, une commode, des toilettes et une vue sur la place central."
    salle1 = Salle(1,"Chambre","en_jeu",scenar1,[],"indice1",7635)
    salle2 = Salle(1,"Immeuble","en_jeu",scenar2,[],"indice2",84693)
    salle3 = Salle(1,"Accident","en_jeu",scenar3,[],"indice3",101)
    salle4 = Salle(1,"Hôpital","en_jeu",scenar4,[],"indice4",-1)

    idSession : int
    etat : str
    dateDebut : datetime
    tempsRestant : int
    niveauActuel : Salle
    
    def __init__(self,idSession,etat,tempsRestant,niveauActuel):
        self.idSession = idSession
        self.etat = etat
        self.dateDebut = datetime.date.today()
        self.tempsRestant = tempsRestant
        match niveauActuel:
            case 1:
                self.niveauActuel = self.salle1
            case 2:
                self.niveauActuel = self.salle2
            case 3:
                self.niveauActuel = self.salle3
            case 4:
                self.niveauActuel = self.salle4


    def terminerPartie(self,v:bool):
        v & print("Bravo vous avez gagnez en : ",datetime.date.today()-self.dateDebut)

    def changerNiveau(self,niveau:Salle,newNiv:Salle):
        niveau.etat = "fini"

    def get_data(self):
        return self.niveauActuel.getInfo()