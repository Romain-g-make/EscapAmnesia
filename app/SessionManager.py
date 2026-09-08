import datetime

class SessionManager:

    def __init__(self,idSession,etat,dateDebut,tempsRestant,niveauActuel):
        self.idSession = idSession
        self.etat = etat
        self.dateDebut = dateDebut
        self.tempsRestant = tempsRestant
        self.niveauActuel = niveauActuel

    def demarrerPartie(self) :
        self.dateDebut = datetime.date.today()

    def terminerPartie(self,v:bool):
        if v:
            print("Bravo vous avez gagnez en : ",datetime.date.today()-self.dateDebut)

    def changerNiveau(self,niveau:Salle,newNiv:Salle):
        niveau.etat = "fini"