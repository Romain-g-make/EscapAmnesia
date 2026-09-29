from abc import abstractmethod
import logging

logger = logging.getLogger(__name__)

class Item():

    listItem = []

    @abstractmethod
    def __init__(self, id, nom, description, etat):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat

    listItem.append(id)

    def inspecter(self):
        logger.debug('Inspection of an item in progress')
        return {"description":self.description}

    def getData(self):
        return {"id":self.id,"nom":self.nom,"description":self.description}