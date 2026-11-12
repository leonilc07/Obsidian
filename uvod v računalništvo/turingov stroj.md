# Turingov stroj
Turingov stroj sestavljajo:
- **trak**, razdeljen na celice, v vsaki celici je en simbol: $0$, $1$ ali $b$ (prazna celica, *blank*)
- **glava**, ki bere in piše simbol v celici, nad katero stoji, in se premakne za eno celico levo (**L**) ali desno (**R**)
- **stanje**, v katerem je stroj (zapišemo ga ob glavi, npr. $2$)

## ukaz
Ukaz ima pet delov:
$$\underbrace{1 \;\; 1}_{\text{pogoj}} \;\; 0 \;\; \underbrace{2}_{\text{stanje}} \;\; \underbrace{L}_{\text{premik glave}}$$
1. trenutno stanje
2. prebran simbol
3. simbol, ki ga zapišemo
4. novo stanje
5. premik glave (L ali R)

Prva dva dela sta **pogoj**: ukaz se izvede samo, če je stroj v tem stanju **in** glava bere ta simbol. Če ne velja eno ali drugo, ukaz ne pride v poštev.

Primer ukaza `1 1 0 2 L` beremo: „če si v stanju 1 in bereš 1, zapiši 0, pojdi v stanje 2 in se premakni levo“.

## konfiguracija
**Konfiguracija** je vsebina traku skupaj s položajem glave in stanjem. Stanje zapišemo v oklepaju **za simbolom**, nad katerim je glava:
- $b\,1_{(1)}\,0\,b$: trak je $b\,1\,0\,b$, glava je nad $1$, stroj je v stanju 1

Stroj se **ustavi**, ko za trenutno stanje in prebran simbol ni nobenega ukaza.

# Naloge
## naloga 1
Ukaz `1 1 0 2 L` izvedemo na $b\,1_{(1)}\,0\,b$:
- pogoj velja (stanje 1, bere 1)
- zapišemo 0, gremo v stanje 2, glava gre levo

$$b\,1_{(1)}\,0\,b \Rightarrow b_{(2)}\,0\,0\,b$$

## naloga 2
Preverjamo, ali se ukaz lahko izvede na traku $b\,0\,1\,b$ v stanju 1.
- `1 1 1 1 R`: ne gre, ker glava bere 0 in ne 1
- `1 b 1 2 R`: ne gre, ker glava ne bere $b$

Ukaz se izvede samo, ko se ujemata **oba** dela pogoja.

## naloga 3
Program:
- `1 1 1 2 R`
- `1 0 0 2 R`
- `1 b 1 2 R`
- `2 0 0 2 R`
- `2 1 0 1 R`

Začetna konfiguracija $b\,1_{(1)}\,0\,0\,1\,b$:
$$
\begin{aligned}
b\,1_{(1)}\,0\,0\,1\,b &\Rightarrow b\,1\,0_{(2)}\,0\,1\,b && \texttt{1 1 1 2 R} \\
&\Rightarrow b\,1\,0\,0_{(2)}\,1\,b && \texttt{2 0 0 2 R} \\
&\Rightarrow b\,1\,0\,0\,1_{(2)}\,b && \texttt{2 0 0 2 R} \\
&\Rightarrow b\,1\,0\,0\,0\,b_{(1)} && \texttt{2 1 0 1 R} \\
&\Rightarrow b\,1\,0\,0\,0\,1\,b_{(2)} && \texttt{1 b 1 2 R}
\end{aligned}
$$
Zdaj je stroj v stanju 2 in bere $b$. Ukaza `2 b ...` ni, zato se stroj **ustavi**.

## naloga 4
$$b\,1\,b \Rightarrow b_{(2)}\,1\,b \Rightarrow b_{(3)}\,0\,1\,b \Rightarrow 1\,0_{(4)}\,1\,b \Rightarrow 1\,1\,1_{(4)}\,b$$
Ukazi za to nalogo v zapiskih niso zapisani.

## naloga 5
Iz $b\,1\,1\,1\,1\,1\,b$ naredi $b\,0\,1\,1\,1\,1\,b$ (prvo 1 zamenjaj z 0).

Če glava ni podana, si izberemo **prvo pozicijo, ki ima 1 ali 0**: $b\,1_{(1)}\,1\,1\,1\,1\,b$.

Ukaz: `1 1 0 2 R`
- zapiše 0 in gre v stanje 2, za stanje 2 ni ukazov, zato se stroj ustavi
- stanje se mora nekoč spremeniti, sicer bi stroj isti ukaz ponavljal po celem nizu

## naloga 6
- **vhod:** poljuben niz enic
- **izhod:** $1\,0\,1\,0\,1\,0 \dots$ (vsaka druga enica postane 0)

Ukazi:
- `1 1 1 2 R`: v stanju 1 pusti 1 in gre v stanje 2
- `2 1 0 1 R`: v stanju 2 zapiše 0 in gre nazaj v stanje 1

$$1_{(1)}\,1\,1 \Rightarrow 1\,1_{(2)}\,1 \Rightarrow 1\,0\,1_{(1)}$$

## naloga 7
- **vhod:** poljuben niz enic
- **izhod:** $1\,1\,0\,1\,1\,0 \dots$ (vsaka tretja enica postane 0)

Ukazi:
- `1 1 1 2 R`
- `2 1 1 3 R`
- `3 1 0 1 R`

$$1_{(1)}\,1\,1 \Rightarrow 1\,1_{(2)}\,1 \Rightarrow 1\,1\,1_{(3)} \Rightarrow 1\,1\,0\;{}_{(1)}$$

Isti program kot **diagram stanj**: krogi so stanja, puščica z oznako `a/b/D` pomeni „če bereš $a$, zapiši $b$ in se premakni v smer $D$“.

![[Turingov stroj - naloga 7.excalidraw]]

## naloga 10 (dodatna)
![[Turingov stroj - naloga 10.excalidraw]]

Ukazi iz diagrama:
- `1 0 1 1 R`, `1 1 0 1 R`: v stanju 1 gre desno in obrne vsak bit
- `1 b b 2 L`: na koncu niza se obrne in gre levo v stanje 2
- `2 1 0 2 L`: v stanju 2 enice spreminja v 0 in gre levo
- `2 0 1 3 R`: prvo 0 spremeni v 1 in gre v stanje 3, kjer se ustavi

Stroj torej najprej obrne vse bite, nato pa številu prišteje 1 (enice na desni postanejo 0, prva 0 postane 1). To je **dvojiški komplement** števila.

**Za kolokvij:** dobro poglej diagrame.
