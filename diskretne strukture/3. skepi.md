# pravilen sklep

| p   | q   | r   | A1  | A2  | A3  | B                |
| --- | --- | --- | --- | --- | --- | ---------------- |
| 0   | 0   | 0   | ¸1  | 0   | 1   |                  |
| ... |     |     | 1   | 1   | 1   | 0  - protiprimir |
| 0   | 1   | 1   | 1   | 1   | 1   | 1                |
| .   | .   | .   | 1   | 1   | 1   | 1                |
| 1   | 1   | 1   | 0   | 0   | 0   |                  |
sklep je prailen če je rezulat sklepa povsod 1 kjer so vsi druge izjave 1, če je 0 je protiprimirje in kjer postavke niso 1 me ne briga

${}(p \implies q)\implies(r \implies s), \neg(r \implies q){}$

Premisa $A = (p \implies q)\implies(r \implies s)$, zaključek $B = \neg(r \implies q)$

| p | q | r | s | p⇒q | r⇒s | A | r⇒q | B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0  - protiprimer |

Pri $p=q=r=s=0$ je premisa 1, zaključek pa 0, zato je sklep **nepravilen**.

A1,...,An |= B natanko tedaj ko je izjavni izraz (a1 ${}\land{}$ a2 ${}\land{}$,..) ${}\implies{}$ B tavtologija

**Zakaj:** implikacija $X \implies B$ je 0 samo, ko je $X = 1$ in $B = 0$. $X = A_1 \land \dots \land A_n$ je 1 natanko takrat, ko so vse premise 1. Torej je $(A_1 \land \dots \land A_n) \implies B$ enaka 0 natanko v vrsticah, kjer so vse premise 1 in zaključek 0, to pa so ravno protiprimeri. Ni protiprimera ⇔ izraz je povsod 1 ⇔ tavtologija ⇔ sklep je pravilen.

**Na našem primeru:** ena premisa, torej preverimo ali je $A \implies B$ tavtologija:
$$\big((p \implies q)\implies(r \implies s)\big) \implies \neg(r \implies q)$$

| p | q | r | s | A | B | A⇒B |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 0 | 0 |

Izraz ima vrednost 0 pri $p=q=r=s=0$, zato **ni tavtologija** in sklep je **nepravilen** (isti protiprimer kot zgoraj).

## Primer: dežuje → oblačno

- Premisa 1: če dežuje, je oblačno: $d \implies o$
- Premisa 2: dežuje: $d$
- Zaključek: oblačno je: $o$

**S tabelo**

| d | o | $d \implies o$ | d | o (zaključek) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

Obe premisi sta 1 samo v zadnji vrstici, tam je tudi zaključek 1, zato je sklep **pravilen**.

**S tavtologijo** (preverimo, da je $((d \implies o) \land d) \implies o$ vedno 1)

$((d \implies o) \land d) \implies o$
$= \neg\big((\neg d \lor o) \land d\big) \lor o$
$= \big((d \land \neg o) \lor \neg d\big) \lor o$
$= \big((d \lor \neg d) \land (\neg o \lor \neg d)\big) \lor o$
$= (1 \land (\neg o \lor \neg d)) \lor o$
$= \neg o \lor o \lor \neg d$
$= 1 \lor \neg d = 1$

Izraz je tavtologija, zato je sklep **pravilen**.

![[Pasted image 20261023084657.png]]

| t   | k   | d   | ${}t \land d{}$ | ${}t \land k \implies \neg d{}$ | ${}\neg k{}$ |
| --- | --- | --- | --------------- | ------------------------------- | ------------ |
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- $t$: grem na tekmo, $k$: grem v kino, $d$: naredim domačo nalogo
- Premisi: $t \land d$ in $(t \land k) \implies \neg d$, zaključek: $\neg k$

Obe premisi sta 1 samo v vrstici $t=1, k=0, d=1$, tam je tudi $\neg k = 1$. Protiprimera ni, zato je sklep **pravilen**.

**Zakaj (z besedami):** iz 1. premise vemo $t = 1$ in $d = 1$. Če bi šel v kino ($k = 1$), bi bilo $t \land k = 1$ in po 2. premisi $d = 0$, kar je v protislovju z $d = 1$. Torej $k = 0$, v kino ne morem.

## pravila
Z $1$ označimo tavtologijo.

1. **Zamenjava enakovrednih:** če je $B \sim C$, potem $A \models B$ natanko tedaj, ko $A \models C$.
   - Primer: $\neg\neg p \sim p$, zato $p \land q \models \neg\neg p$ natanko tedaj, ko $p \land q \models p$.
2. **Tavtologija vedno sledi:** $A \models 1$.
   - Primer: $p \models q \lor \neg q$, ker je $q \lor \neg q$ vedno 1.
3. **Vsaka premisa sledi:** $A_1, A_2, \dots, A_n \models A_k$ za vsak $k \in \{1, \dots, n\}$.
   - Primer: $p,\ p \implies q \models p$
4. **Dodajanje tavtologije:** $A_1, \dots, A_n \models B$ natanko tedaj, ko $A_1, \dots, A_n, 1 \models B$.
   - Primer: $p,\ p \implies q \models q$ natanko tedaj, ko $p,\ p \implies q,\ r \lor \neg r \models q$ (premisa, ki je vedno 1, nič ne spremeni).
## pravila sklepanja
Pravilom sklepanja pravimo tudi **osnovni pravilni sklepi**.

- $A,\ A \implies B \models B$ — **modus ponens (MP)**
- $A \implies B,\ \neg B \models \neg A$ — **modus tollens (MT)**
- $A \lor B,\ \neg B \models A$ — **disjunktivni silogizem (DS)**
- $A \implies B,\ B \implies C \models A \implies C$ — **hipotetični silogizem (HS)**
- $A,\ B \models A \land B$ — **združitev (Zd)**
- $A \land B \models A$ — **poenostavitev (Po)**
- $A \models A \lor B$ — **pridružitev (Pr)**


| A   | B   | C   | ${}A \implies B{}$ | ${}B \implies C{}$ | ${}A \implies C{}$ |
| --- | --- | --- | ------------------ | ------------------ | ------------------ |
| 0   | 0   | 0   | 1                  | 1                  | 1                  |
| 0   | 0   | 1   | 1                  | 1                  | 1                  |
| 0   | 1   | 0   | 1                  | 0                  | 1                  |
| 0   | 1   | 1   | 1                  | 1                  | 1                  |
| 1   | 0   | 0   | 0                  | 1                  | 0                  |
| 1   | 0   | 1   | 0                  | 1                  | 1                  |
| 1   | 1   | 0   | 1                  | 0                  | 0                  |
| 1   | 1   | 1   | 1                  | 1                  | 1                  |

Obe premisi ($A \implies B$ in $B \implies C$) sta 1 v vrsticah 000, 001, 011 in 111. V vseh teh je tudi $A \implies C = 1$. Protiprimera ni, zato je **hipotetični silogizem pravilen sklep**.



## dokaz pravilnosti sklepa
Pravilnost sklepa $A_1, A_2, \dots, A_n \models B$ pokažemo tako, da sestavimo zaporedje izjavnih izrazov $C_1, C_2, \dots, C_m$, kjer je $C_m = B$ in za vsak $i = 1, 2, \dots, m$ velja:

- (a) $C_i$ je ena od predpostavk ali
- (b) $C_i$ je tavtologija ali
- (c) $C_i$ je enakovreden enemu od predhodnih izrazov v zaporedju ali
- (d) $C_i$ logično sledi iz predhodnih izrazov po enem od osnovnih pravilnih sklepov (MP, MT, DS, HS, Zd, Po, Pr).

**Razlaga:** namesto tabele delamo korake. Vsak nov izraz mora biti „upravičen“: ali je dan (premisa), ali je vedno resničen, ali je samo drugače zapisan prejšnji izraz, ali pa ga dobimo s pravilom sklepanja. Ko pridemo do $B$, je sklep dokazan. Pri vsakem koraku zraven napišemo, zakaj velja.

**Zgled:** ali iz predpostavk $t \land d,\ (t \land k) \implies \neg d$ sledi $\neg k$?

|     | izraz                         | razlog         |
| --- | ----------------------------- | -------------- |
| 1.  | $t \land d$                   | predpostavka   |
| 2.  | $(t \land k) \implies \neg d$ | predpostavka   |
| 3.  | $d$                           | Po(1)          |
| 4.  | $\neg\neg d$                  | $\sim$(3)      |
| 5.  | $\neg(t \land k)$             | MT(2,4)        |
| 6.  | $\neg k \lor \neg t$          | De Morgan(5)   |
| 7.  | $t$                           | Po(1)          |
| 8.  | $\neg\neg t$                  | $\sim$(7)      |
| 9.  | $\neg k$                      | DS(6,8)        |

Prišli smo do $\neg k$, zato sklep **velja**.

## pogojni sklep (PS)
Pogojni sklep uporabljamo, kadar ima zaključek obliko implikacije.

**Izrek:** $A_1, A_2, \dots, A_k \models B \implies C$ natanko tedaj, ko $A_1, A_2, \dots, A_k, B \models C$.

**Zakaj to velja:** implikacija $B \implies C$ je 0 samo, ko je $B = 1$ in $C = 0$.
- V vrsticah, kjer je $B = 0$, je $B \implies C$ vedno 1, zato jih ni treba preverjati.
- Preveriti moramo samo vrstice, kjer je $B = 1$. To naredimo tako, da $B$ začasno predpostavimo in pokažemo, da potem sledi $C$.

**Kako ga uporabimo:**
1. Zaključek ima obliko $B \implies C$.
2. Odpremo **podračun**: $B$ zapišemo kot začasno predpostavko (npr. vrstica 3.1, razlog „predpostavka PS“).
3. V podračunu izpeljujemo kot običajno (3.2, 3.3, …). Uporabimo lahko vse prejšnje vrstice (1, 2, …) in vrstice znotraj podračuna.
4. Ko pridemo do $C$, podračun zapremo in zapišemo $B \implies C$ z razlogom PS(3.1–3.3).

**Pravilo:** vrstic iz podračuna (3.1, 3.2, 3.3) **zunaj podračuna ne smemo uporabljati**. $B$ ni dan, samo začasno smo ga predpostavili, zato vse v podračunu velja le ob predpostavki, da je $B$ resničen. Ko podračun zapremo, nam ostane samo $B \implies C$ („če $B$, potem $C$“), ta pa velja brez dodatne predpostavke.

**Zgled:** pokaži, da iz predpostavk $p \implies q \lor r$ in $\neg r$ sledi $p \implies q$.

Zaključek je implikacija, zato odpremo podračun s predpostavko $p$ in v njem dokazujemo $q$.

|     | izraz                 | razlog            |
| --- | --------------------- | ----------------- |
| 1.  | $p \implies q \lor r$ | predpostavka      |
| 2.  | $\neg r$              | predpostavka      |
| 3.1 | $p$                   | predpostavka PS   |
| 3.2 | $q \lor r$            | MP(1, 3.1)        |
| 3.3 | $q$                   | DS(3.2, 2)        |
| 3.  | $p \implies q$        | PS(3.1–3.3)       |

Vrstica 3 je zaključek, zato $p \implies q \lor r,\ \neg r \models p \implies q$.

**Zakaj je pravilo pomembno:** če bi za vrstico 3 zapisali še $q$ z razlogom 3.3, bi trdili, da iz $p \implies q \lor r$ in $\neg r$ sledi $q$. To ni res: pri $p = q = r = 0$ sta obe premisi 1, $q$ pa je 0. Vrstica 3.3 velja samo, če je $p = 1$, zunaj podračuna pa tega ne vemo več.

## sklep s protislovjem (RA)
Sklep s protislovjem lahko uporabljamo **kadarkoli**, ne glede na obliko zaključka.

**Izrek:** $A_1, A_2, \dots, A_k \models B$ natanko tedaj, ko $A_1, A_2, \dots, A_k, \neg B \models 0$.

Z $0$ označimo protislovje, to je izraz, ki je vedno 0 (npr. $C \land \neg C$).

**Zakaj to velja:** iz premis sledi $0$ samo takrat, ko premise nikoli niso hkrati vse 1 (sicer bi bil to protiprimer, ker je $0$ vedno 0).
- $A_1, \dots, A_k, \neg B \models 0$ torej pomeni, da ni vrstice, kjer so vsi $A_i = 1$ in $\neg B = 1$.
- Kjer so vsi $A_i = 1$, mora biti $\neg B = 0$, torej $B = 1$. To pa pomeni ravno $A_1, \dots, A_k \models B$.

Z besedami: predpostavimo nasprotno ($\neg B$) in pokažemo, da pridemo do nesmisla. Zato nasprotno ne more veljati in velja $B$.

**Kako ga uporabimo:**
1. Želimo dokazati $B$.
2. Odpremo **podračun**: $\neg B$ zapišemo kot začasno predpostavko (npr. vrstica 3.1, razlog „predpostavka RA“).
3. V podračunu izpeljujemo kot običajno (3.2, 3.3, …), dokler ne dobimo nekega izraza $C$ in tudi njegove negacije $\neg C$.
4. Z združitvijo dobimo $C \land \neg C$, kar je $\sim 0$ (protislovje).
5. Podračun zapremo in zapišemo $B$ z razlogom RA(3.1–3.n).

**Pravilo:** vrstic iz podračuna **zunaj podračuna ne smemo uporabljati**. Vse v podračunu velja le ob predpostavki $\neg B$, za katero smo ravno pokazali, da vodi v protislovje. Ko podračun zapremo, nam ostane samo $B$.

**Zgled:** pokaži, da iz $p \implies \neg(q \implies r)$, $(s \land q) \implies r$ in $s$ sledi $\neg p$.

Odpremo podračun z negacijo zaključka $\neg\neg p$ in v njem iščemo protislovje.

|     | izraz                         | razlog           |
| --- | ----------------------------- | ---------------- |
| 1.  | $p \implies \neg(q \implies r)$ | predpostavka   |
| 2.  | $(s \land q) \implies r$      | predpostavka     |
| 3.  | $s$                           | predpostavka     |
| 4.1 | $\neg\neg p$                  | predpostavka RA  |
| 4.2 | $p$                           | $\sim$(4.1)      |
| 4.3 | $\neg(q \implies r)$          | MP(1, 4.2)       |
| 4.4 | $q \land \neg r$              | $\sim$(4.3)      |
| 4.5 | $q$                           | Po(4.4)          |
| 4.6 | $\neg r$                      | Po(4.4)          |
| 4.7 | $s \land q$                   | Zd(3, 4.5)       |
| 4.8 | $r$                           | MP(2, 4.7)       |
| 4.9 | $r \land \neg r \sim 0$       | Zd(4.8, 4.6)     |
| 4.  | $\neg p$                      | RA(4.1, 4.9)     |

Pri 4.4: $\neg(q \implies r) \sim \neg(\neg q \lor r) \sim q \land \neg r$ (implikacija zapisana z disjunkcijo, nato De Morgan).

Predpostavka $\neg\neg p$ nas je pripeljala v protislovje, zato velja $\neg p$ in sklep je **pravilen**.

## analiza primerov (AP)
Analizo primerov uporabljamo, kadar ima ena od predpostavk obliko **disjunkcije** $B_1 \lor B_2$.

**Izrek:** $A_1, A_2, \dots, A_k, B_1 \lor B_2 \models C$ natanko tedaj, ko $A_1, A_2, \dots, A_k, B_1 \models C$ **in** $A_1, A_2, \dots, A_k, B_2 \models C$.

**Zakaj to velja:** če je $B_1 \lor B_2 = 1$, je vsaj eden od $B_1$, $B_2$ enak 1.
- Vrstice, kjer so vse premise 1, razdelimo na dva primera: tiste z $B_1 = 1$ in tiste z $B_2 = 1$.
- Če $C$ sledi v obeh primerih, potem sledi v vseh vrsticah, kjer so premise 1.
- Dokazati moramo **oba** primera (zato „in“). Če dokažemo samo enega, ne pokrijemo vrstic, kjer velja samo drugi.

Z besedami: vemo, da velja $B_1$ ali $B_2$, ne vemo pa katero. Zato preverimo oba primera. Če v vsakem pridemo do $C$, potem $C$ zagotovo velja.
- Primer iz življenja: grem z avtom ali z vlakom. Če grem z avtom, bom v Ljubljani. Če grem z vlakom, bom v Ljubljani. Torej bom v Ljubljani.

**Kako ga uporabimo:**
1. Med predpostavkami je disjunkcija $B_1 \lor B_2$ (npr. vrstica 2), dokazujemo $C$.
2. Odpremo **prvi podračun**: $B_1$ zapišemo kot začasno predpostavko (npr. 4.1, „predpostavka AP“) in izpeljemo $C$.
3. Odpremo **drugi podračun**: $B_2$ zapišemo kot začasno predpostavko (npr. 5.1, „predpostavka AP“) in spet izpeljemo $C$.
4. Oba podračuna zapremo in zapišemo $C$ z razlogom AP(2, 4.1–4.n, 5.1–5.m).

**Pravilo:**
- Vrstic iz podračunov **zunaj njih ne smemo uporabljati** (kot pri PS in RA).
- Vrstic iz prvega podračuna **ne smemo uporabljati v drugem** (in obratno). V prvem smo predpostavili $B_1$, v drugem $B_2$, to sta ločena primera.
- Oba podračuna morata končati z **istim** $C$.

**Namig:** če imamo med premisami tudi $\neg B_1$ ali $\neg B_2$, je hitreje uporabiti DS. AP uporabimo, ko ne vemo, kateri del disjunkcije velja.
