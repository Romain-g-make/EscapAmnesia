from .Item import Item
import logging

logger = logging.getLogger(__name__)

class Salle:
    id : int
    name : str
    state : str
    scenario : str
    indice : str
    listObj : list[Item]
    exitCode : str

    def __init__(self,id,name,state,scenario,indice,listObj,exitCode):
        self.id = id
        self.name = name
        self.state = state
        self.scenario = scenario
        self.indice = indice
        self.listObj = listObj
        self.exitCode = exitCode

    def tryEscape(self,codeP):
        if codeP==self.exitCode:
            logger.info('The player try to escape of this room : %s', self.id)
            self.state = "fini"
            return True
        else:
            logger.error('The player failed to get out of this room : %s', self.id)
            return False

    def getInfo(self):
        return{"id":self.id,"name":self.name,"state":self.state,"scenario":self.scenario}

    def getHint(self):
        logger.info('The player get the hint of this room : %s', self.id)
        return {"indice":self.indice}

    def getObjects(self):
        result = []
        logger.info('The player get all objects of this room : %s', self.id)
        for objet in self.listObj:
            result.append(objet.getData())
        return result

    