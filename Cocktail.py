class Cocktail:
    def __init__(self,name,lied,**zutat):
        self.name = name
        self.inhalt = {'rum':0,'gin':0, 'limette':0, 'wasser':0, 'sirup':0}
        self.inhalt.update(zutat)
        self.lied = lied
    
    def pumpZeit(self):
        self.maxTime = max(self.inhalt.values()) + 10 # evtl Zeit drauf rechnen
        return self.maxTime

    def __repr__(self):
        return "Cocktail('{}','{}')".format(self.name,self.inhalt)

#Cocktails definieren
mojito = Cocktail(['mojito'],'music/Mojito.mp3',rum=10,limette=5,wasser=20,sirup=5)
caipi = Cocktail(['caipirinha','caipi'],'music/Caipirinha.mp3',rum=10,limette=5,wasser=20)
ginsour = Cocktail(['ginsour','gin sour'],'music/GinSour.mp3',gin=10,limette=5,wasser=20,sirup=5)
cocktails = [mojito,caipi,ginsour]

cocktailNames = mojito.name + caipi.name + ginsour.name