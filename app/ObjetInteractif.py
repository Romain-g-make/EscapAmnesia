from .Item import Item

class ObjetInteractif(Item):
    def __init__(self, id,nom,description,etat,useEffect,objs : list[Item] = None):
        self.id = id
        self.nom = nom
        self.description = description
        self.etat = etat
        self.objs = objs
        self.useEffect = useEffect

    def inspecter(self):
        result = {"description":self.description}
        if self.objs:
            for i in range (len(self.objs)):
                result[self.objs[i].id]=self.objs[i].getData()
        return result

    def utiliser(self,itemID:int):
        for i in range (len(self.objs)):
            if self.objs[i].id==itemID:
                return {"effet":self.useEffect}
        return {"status":"error", "message":"This item is not compatible"}
        


    def getData(self):
        return {"id":self.id,"nom":self.nom,"description":self.description}