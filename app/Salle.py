from Item import Item
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
            self.state = "fini"
        else:
            return {"Ce n'est pas ça..."}

    def getInfo(self):
        return{"id":self.id,"name":self.name,"state":self.state,"scenario":self.scenario}

    def getIndice(self):
        return {"indice":self.indice}

    def getObjets(self):
        result = []
        for objet in self.listObj:
            result.append(objet.getData())
        return result