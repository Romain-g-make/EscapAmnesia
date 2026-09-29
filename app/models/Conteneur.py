from .Item import Item
import logging

logger = logging.getLogger(__name__)

class Conteneur(Item):
    def __init__(self, id,nom,description,etat,estFerme, codeSerrure,open):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat
        self.estFerme = estFerme
        self.codeSerrure = codeSerrure
        self.open = open

    
    def getData(self):
        return {"id":self.id,"nom":self.nom,"description":self.description}

    def inspecter(self):
        logger.debug('Inspection in progress')
        return {"description":self.description}

    def deverouiller(self,t):
        logger.debug('Unlocking in progress')
        if t==self.codeSerrure:
            return {"open":self.open}