import matplotlib.pyplot as plt
l=[]

class Parti:
    fusion=[]
    def __init__(self,nom,debut,fin,color):
        self.nom=nom
        self.debut=debut
        self.fin=fin
        self.fusion=[]
        self.color=color
        self.pos=0
        l.append(self)

    def fused (self,p,date):
        self.fusion.append([p,date])















ps = Parti("Parti Socialiste",1969,2023,"#FF8080")
mdc = Parti("Mouvement des citoyens",1993,2023,"#ffc0c0")

pcf = Parti("PCF",1920,2023,"#DD0000")

lnd=Parti("Les Nouveaux Démocrates",2020,2022,"#3B2A82")

ge=Parti("Génération écologie",1990,2023,"#77FF77")


mdp=Parti("Mouvement des progressistes",2009,2023,"#C71585")
pp=Parti("Place Publique",2018,2023,"#FEF10A")
prv=Parti("Parti Radical",1901,2023,"#1960AB")
prg=Parti("Parti Radical de Gauche",1972,2023,"#4C6099")
tdp=Parti("Territoires de progrès",2020,2022,"#FFC0C0")

pe=Parti("Parti écologiste",2015,2023,"#00CCFF")
lrem=Parti("La République En Marche",2016,2022,"#FFD600")
ren=Parti("Renaissance",2022,2023,"#00205B")
ges=Parti("Génération.s",2017,2023,"#D6245F")
ens=Parti("Ensemble!",2013,2023,"#FF0000")
pg=Parti("Parti de gauche",2008,2023,"#DD0000")
lfi=Parti("La France Insoumise",2017,2023,"#C9462C")
poi=Parti("Parti Ouvrier Indépendant",2008,2023,"#BB0000")
eelv=Parti("Europe Écologie Les Verts",1984,2023,"#00C000")
sfio=Parti("Section française de l'Internationale ouvrière",1905,1969,"#FC0D1B")
ucrg=Parti("Union des clubs pour le renouveau de la gauche",1966,1969,"#F943C0")#couleur non-contractuelle
ugcs=Parti("Union des groupes et clubs socialistes",1967,1969,"#F7227B")# couleur non contractuelle
psu=Parti("Parti Socialiste Unifié",1960,1990,"#E7471E")
arev=Parti("Alternative rouge et verte",1989,1998,"#A9212B")
alt=Parti("Les Alternatifs",1998,2015,"#FF0000")
ugs=Parti("Union de la gauche socialiste",1957,1960,"#FF72F7") #pas contra
psa=Parti("Parti socialiste autonome",1958,1960,"#FF3D63") #pas contra
cir=Parti("Convention des institutions républicaines",1964,1971,"#494949") #pas contra
udsr=Parti("Union démocratique et socialiste de la Résistance",1945,1964,"#EB599B")
rs=Parti("République souveraine",2019,2023,"#0A71B4")
grs=Parti("Gauche républicaine et socialiste",2018,2023,"#D23150")
mrc=Parti("Mouvement républicain et citoyen",2003,2023,"#CC6666")
ec=Parti("En Commun",2020,2023,"#105099")
lgm=Parti("La Gauche moderne",2007,2017,"#9D3475")
udi=Parti("Union Des Démocrates et Indépendants",2012,2023,"#5F4490")
nd=Parti("Nouvelle Donne",2013,2023,"#D6009E")
poit=Parti("Parti ouvrier internationaliste",1936,1944,"#D50000")
PCI_SFQI=Parti("Parti communiste internationaliste",1944,1968,"#FF0000")
lc=Parti("Ligue communiste",1969,1973,"#940202")
lcr=Parti("Ligue communiste révolutionnaire",1973,2009,"#E60000")
npa=Parti("Nouveau Parti Anticapitaliste",2009,2023,"#E21F20")
canda=Parti("Convergences et alternative",2011,2014,"#8F194E")
ga=Parti("Gauche anticapitaliste",2011,2014,"#E31838")
fase=Parti("Fédération pour une alternative sociale et écologique",2008,2014,"#00B000")
cu=Parti("Communistes unitaires",2007,2019,"#E31C39")

fase.fused(ens,2014)
cu.fused(fase,2008)
pcf.fused(cu,2007)
ga.fused(ens,2014)
npa.fused(ga,2011)
canda.fused(ens,2014)
npa.fused(canda,2011)
lcr.fused(npa,2009)
lc.fused(lcr,1973)
PCI_SFQI.fused(lc,1968)
poit.fused(PCI_SFQI,1944)
sfio.fused(poit,1936)
ps.fused(lgm,2013)
lgm.fused(udi,2012)
prv.fused(udi,2012)
prv.fused(prg,1972)
pcf.fused(mdp,2009)
ec.fused(lrem,2020)
mdc.fused(mrc,2003)
mrc.fused(grs,2019)
ps.fused(grs,2018)
lfi.fused(rs,2019)
ps.fused(pg,2008)
pg.fused(lfi,2016)
cir.fused(ps,1971)
udsr.fused(cir,1964)
psa.fused(psu,1960)
ugs.fused(ugs,1960)
psu.fused(ugcs,1967)
psu.fused(ucrg,1966)
psu.fused(eelv,1989)
psu.fused(arev,1989)
arev.fused(alt,1998)
alt.fused(ens,2013)
sfio.fused(psa,1958)
sfio.fused(ugs,1957)
ugcs.fused(ps,1969)
ucrg.fused(ps,1969)
ps.fused(mdc,1993)
sfio.fused(ps,1969)
sfio.fused(pcf,1920)
eelv.fused(pe,2015)
ps.fused(lrem,2016)
lrem.fused(ren,2022)
lrem.fused(tdp,2020)
tdp.fused(ren,2022)


"""
x_values = [ps.fusion[0][1], ps.fusion[0][1]]
y_values = [1, 2]
plt.plot(x_values, y_values,ps.color,linewidth=5.0




    for k in range(0,len(p.fusion)):
        x_values = [p.fusion[k][1], p.fusion[k][1]]
        y_values = [p.pos, p.fusion[k][0].pos]
        plt.plot(x_values, y_values,p.fusion[k][0].color,linewidth=5.0)
)"""
#plt.legend()

i=1
for p in l:
    x_values = [p.debut, p.fin]
    y_values = [i, i]
    p.pos=i
    i+=1
    plt.plot(x_values, y_values,p.color,linewidth=7.0,label=p.nom
    )
for p in l:
    for fusion in p.fusion:
        y_values = [p.pos, fusion[0].pos]
        x_values = [fusion[1], fusion[1]]
        plt.plot(x_values, y_values,fusion[0].color,linewidth=3.5)


plt.show()


plt.show()








