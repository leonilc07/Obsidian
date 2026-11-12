zemljevid = """ (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
 (4)           9---
(13)         22---- 17---"""



def koordinate(s):
    stevec =0
    stevilo = ""
    for i in s:
        if i.isdigit():
            stevilo += i
        else:
            stevec += 1
    
    return (int(stevilo), int(stevilo) + stevec - 1)

def vrstica(s):
    tab = []
    y =0
    for i, ovira in enumerate(s.split()):
        if i == 0:
            y = int(ovira.lstrip("(").rstrip(")"))
            continue
        tab.append((*koordinate(ovira), y))
    return tab

def preberi(s):
    tab = []
    for vrstica_ in s.splitlines():
        tab.extend(vrstica(vrstica_))
    return tab

def intervali(xs): # prejme  (x0, x1)
    tab = []
    for x0, x1 in xs:
        tab.append((""+str(x0)+"-"*(x1-x0+1)))
    return tab

def zapisi_vrstico(y, xs):
    vrstica = f"({y})"
    for par in intervali(xs):
        vrstica += " " + par
    return vrstica

def zapisi(ovire):
    vsi_y = []
    for x0, x1, y in ovire:
        if y not in vsi_y:
            vsi_y.append(y)

    niz_ovir = ""
    for y in sorted(vsi_y):
        pari_vrstice = []
        for x0, x1, y_ in ovire:
            if y_ == y:
                pari_vrstice.append((x0, x1))
        niz_ovir += zapisi_vrstico(y, sorted(pari_vrstice)) + "\n"
    return niz_ovir
