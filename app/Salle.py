class Salle:

    def __init__(self,id,nom,etat,scenario,indice,listeObj,codeSortie):
        self.id = id
        self.nom = nom
        self.etat = etat
        self.scenario = scenario
        self.indice = indice
        self.listeObj = listeObj
        self.codeSortie = codeSortie

    def tenterEchapper(self,codeP):
        if codeP==self.codeSortie:
            self.etat = "fini"
        else:
            print("Ce n'est pas ça...")
