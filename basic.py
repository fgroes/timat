class Schnittparameter(object):
    
    def __init__(self, schnittstaerke=0, randverschnitt=0):
        self.schnittstaerke = schnittstaerke
        self.randverschnitt = randverschnitt


class Anleimer(object):
    
    def __init__(self, vorne=0, hinten=0, links=0, rechts=0):
        self.vorne = vorne
        self.hinten = hinten
        self.links = links
        self.rechts = rechts


class Platte(object):
    
    def __init__(self, dicke, anleimer=Anleimer(), maserrichtung=False):
        self.dicke = dicke
        self.laenge = 0
        self.breite = 0
        self.anleimer = anleimer
        # maserrichtung in richtung laenge
        self.maserrichtung = maserrichtung
    
    
if __name__ == '__main__':
    p = Platte(15)
    p.laenge = 850
    p.breite = 150
    sp = Schnittparameter(schnittstaerke=4, randverschnitt=10)