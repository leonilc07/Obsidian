zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

# zacetek = vrstica[i-1] == "." and vrstica[i] == "#"
# konec = vrstica[i] == "#" and vrstica[i+1] == "."

def dolzina_ovir(vrstica):
    n = 0
    for s in vrstica:
        if s == "#":
            n +=1
    return n

def stevilo_ovir(vrstica):
    vrstica = "." + vrstica + "."
    n=0
    for i in range(len(vrstica)):
        if vrstica[i] == "#" and vrstica[i-1] == ".":
            n += 1
    return n

def najsirsa_ovira(vrstica):
    max_dolzina = 0
    trenutna_dolzina = 0
    vrstica = "." + vrstica + "."
    for s in vrstica:
        if s == "#":
            trenutna_dolzina += 1
        else:
            if trenutna_dolzina > max_dolzina:
                max_dolzina = trenutna_dolzina
            trenutna_dolzina = 0
    return max_dolzina

def pretvori_vrstico(vrstica):
    ovire = []
    vrstica = "." + vrstica + "."
    for i in range(1, len(vrstica)):
        if vrstica[i-1] == "." and vrstica[i] == "#":
            zacetek = i
            
        if vrstica[i] == "#" and vrstica[i+1] == ".":
            konec = i
            ovire.append((zacetek, konec))
    return ovire

def pretvori_zemljevid(vrstice):
    zemljevid = []
    for i, vrstica in enumerate(vrstice):
        for zacetek, konec in pretvori_vrstico(vrstica):
            zemljevid.append((zacetek, konec, i+1))
    return zemljevid

def izboljsave(prej, potem): #mora dodati nove ovire
    zemljevid_novih = []
    for i, vrstica in enumerate(prej):
        vrstica_nova = ""
        for s in zip(vrstica, potem[i]):
            if s[0] == "." and s[1] == "#":
                vrstica_nova += "#"
            else:
                vrstica_nova += "."
        zemljevid_novih.append(vrstica_nova)
    return pretvori_zemljevid(zemljevid_novih)

def huligani(prej, potem):
    dodane = []
    odstranjene = []
    prej = pretvori_zemljevid(prej)
    potem = pretvori_zemljevid(potem)
    for ovira in potem:
        if ovira not in prej:
            dodane.append(ovira)
    for ovira in prej:
        if ovira not in potem:
            odstranjene.append(ovira)
    return dodane, odstranjene