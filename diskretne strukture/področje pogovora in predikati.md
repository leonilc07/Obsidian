

**Področje pogovora** je neprazna **množica**, o kateri govorimo. Na primer ljudje, števila, živali.
# predikanti
**Predikati** so logične **funkcije**, ki za svoje argumente uporabijo elemente področja pogovora.

Če v predikate vstavljamo elemente področja pogovora, dobimo **izjave** (vrednost 0 ali 1).

- Primer: področje pogovora so naravna števila, predikat $P(x)$: „$x$ je sodo število“.
  - $P(4)$ je izjava z vrednostjo 1
  - $P(7)$ je izjava z vrednostjo 0
  - $P(x)$ sam po sebi ni izjava, dokler ne vstavimo konkretnega $x$

Predikate ločujemo po **mestnosti**, to je po številu argumentov, ki jih sprejmejo.
- **enomestni** predikat $P(x)$ ima en argument in opisuje **lastnost** elementa
  - primer: $P(x)$: „$x$ je praštevilo“, $P(5) = 1$, $P(6) = 0$
- **dvomestni** predikat $R(x, y)$ ima dva argumenta in opisuje **relacijo** med dvema elementoma
  - primer: $R(x, y)$: „$x < y$“, $R(2, 5) = 1$, $R(5, 2) = 0$
  - primer: $S(x, y)$: „$x$ je oče od $y$“ (področje pogovora so ljudje)
  - vrstni red argumentov je pomemben: $R(x, y)$ in $R(y, x)$ sta v splošnem različni izjavi

Predikat je izjava šele, ko vstavimo konkretne vrednosti za **vse** argumente. Če v $R(x, y)$ vstavimo samo $x = 2$, dobimo $R(2, y)$, kar je enomestni predikat „$2 < y$“.
# Kvantifikator
Poznamo dva kvantifikatorja:
- $\forall$ **univerzalni** kvantifikator, beremo „za vsak“
- $\exists$ **eksistenčni** kvantifikator, beremo „obstaja“

Resničnost izjave s kvantifikatorjem je odvisna od **izbrane interpretacije** (področja pogovora in pomena predikata).

$\forall x\, P(x)$ je izjava, ki je resnična natanko takrat, ko imajo **vsi** elementi področja pogovora lastnost $P$. Sicer je neresnična.
- primer: področje pogovora so naravna števila, $P(x)$: „$x > 0$“, potem je $\forall x\, P(x)$ resnična
- za neresničnost zadošča en element brez lastnosti $P$

$\exists x\, P(x)$ je izjava, ki je resnična natanko takrat, ko **obstaja (vsaj en)** element področja pogovora, ki ima lastnost $P$. Sicer je neresnična.
- primer: področje pogovora so naravna števila, $P(x)$: „$x$ je sodo število“, potem je $\exists x\, P(x)$ resnična (npr. $x = 2$)
- ista izjava je na področju lihih števil neresnična, zato je resničnost odvisna od interpretacije
## formalizacija
Definiraj ustrezne predikate in zapiši naslednje izjave:
- Nekateri politiki so nepošteni.
- Noben politik ni nepošten.
- Vsi politiki so nepošteni.

Predikati:
- $P(x)$: „$x$ je politik“
- $N(x)$: „$x$ je nepošten“
- $\neg N(x)$: „$x$ je pošten“

**Nekateri politiki so nepošteni:** $\exists x\, (P(x) \land N(x))$

**Noben politik ni nepošten:** to pomeni, da so vsi politiki pošteni. Če zapišemo
$$\forall x\, (P(x) \land \neg N(x))$$
izjava trdi, da je **vsak** element področja pogovora politik in pošten, kar ni to, kar želimo povedati. Tukaj bi bila bolje **implikacija**:
$$\forall x\, (P(x) \Rightarrow \neg N(x))$$
torej „za vsak $x$: če je $x$ politik, potem je pošten“.

**Vsi politiki so nepošteni:** $\forall x\, (P(x) \Rightarrow N(x))$

V večini primerov gre $\forall$ skupaj z **implikacijo**, $\exists$ pa s **konjunkcijo**.

## interpretacija
Dvomestni predikat $P(x, y)$ naj pomeni „$x$ pozna $y$-ona“. Področje pogovora so ljudje.

Na katere načine lahko formulo $P(x, y)$ spremeniš v izjavo?

Formula postane izjava, ko je **vsaka** spremenljivka vezana s kvantifikatorjem (ali zamenjana s konkretnim elementom, npr. $P(\text{Ana}, \text{Bor})$: „Ana pozna Bora“). S kvantifikatorji dobimo 8 možnosti:
- $\forall x\, \forall y\, P(x, y)$: vsak pozna vsakega
- $\forall y\, \forall x\, P(x, y)$: vsakega pozna vsak
- $\exists x\, \exists y\, P(x, y)$: nekdo pozna nekoga
- $\exists y\, \exists x\, P(x, y)$: nekoga pozna nekdo
- $\forall x\, \exists y\, P(x, y)$: vsak pozna nekoga
- $\exists y\, \forall x\, P(x, y)$: obstaja nekdo, ki ga poznajo vsi
- $\exists x\, \forall y\, P(x, y)$: obstaja nekdo, ki pozna vse
- $\forall y\, \exists x\, P(x, y)$: vsakega pozna nekdo

**Dva enaka kvantifikatorja lahko zamenjata vrstni red:**

$\forall x\, \forall y\, P(x, y) \iff \forall y\, \forall x\, P(x, y)$
- obe izjavi sta resnični natanko takrat, ko je $P(a, b) = 1$ za **vsak par** $(a, b)$, torej ko vsak pozna vsakega
- vrstni red, v katerem pregledujemo pare, ne vpliva na rezultat

$\exists x\, \exists y\, P(x, y) \iff \exists y\, \exists x\, P(x, y)$
- obe izjavi sta resnični natanko takrat, ko obstaja **vsaj en par** $(a, b)$, za katerega je $P(a, b) = 1$, torej ko nekdo pozna nekoga
- spet ni pomembno, katero spremenljivko izberemo prej

Pri **mešanih** kvantifikatorjih vrstnega reda ne smemo menjati: „vsak pozna nekoga“ ($\forall x\, \exists y$) ni isto kot „obstaja nekdo, ki ga poznajo vsi“ ($\exists y\, \forall x$).

# Izjavne formule
Izjavne formule predikatnega računa sestavljamo iz naslednjih simbolov:
- **spremenljivke** $x, y, z, \dots$ (označujejo poljuben element področja pogovora)
- **konstante** $a, b, c, \dots$ (označujejo točno določen element, npr. Ana, število 3)
- **predikati** $P, Q, R, \dots$
- **izjavni vezniki** $\neg, \land, \lor, \Rightarrow, \Leftrightarrow, \dots$
- **kvantifikatorja** $\forall$ in $\exists$
- **oklepaja** $($ in $)$

Spremenljivkam in konstantam pravimo tudi **termi**.

**Atome** dobimo tako, da terme vstavimo v predikate. Atomi predikatnega računa so na primer:
- $P(x)$: v enomestni predikat vstavimo spremenljivko
- $P(a)$: v enomestni predikat vstavimo konstanto
- $Q(x, y)$: v dvomestni predikat vstavimo dve spremenljivki
- $Q(a, x)$: v dvomestni predikat vstavimo konstanto in spremenljivko

Primer: če $Q(x, y)$ pomeni „$x$ pozna $y$-ona“ in je $a$ Ana, potem je $Q(a, x)$ „Ana pozna $x$-a“. Atom je izjava šele, ko so vsi termi konstante, npr. $Q(a, b)$.

Izjavne formule so definirane **induktivno** (začnemo z najpreprostejšimi formulami, iz njih pa po pravilih gradimo bolj sestavljene):
1. **Atomi** so izjavne formule.
2. Če sta $W$ in $V$ izjavni formuli in je $x$ spremenljivka, potem so izjavne formule tudi:
   - $(\neg W)$, $(W \land V)$, $(W \lor V)$, $(W \Rightarrow V)$, $(W \Leftrightarrow V)$, $\dots$
   - $(\exists x\, W)$ in $(\forall x\, W)$

Primer gradnje formule $(\forall x\, (P(x) \Rightarrow N(x)))$ iz razdelka o formalizaciji:
- $P(x)$ in $N(x)$ sta atoma, torej izjavni formuli (pravilo 1)
- $(P(x) \Rightarrow N(x))$ je izjavna formula, ker smo dve formuli povezali z veznikom (pravilo 2)
- $(\forall x\, (P(x) \Rightarrow N(x)))$ je izjavna formula, ker smo pred formulo postavili kvantifikator (pravilo 2)

# Doseg kvantifikatorjev
**Doseg** kvantifikatorja je **najmanjši možen**: najmanjša izjavna formula, ki jo preberemo desno od kvantifikatorja (skupaj z njegovo spremenljivko).
- $\forall x\, P(x) \land Q(x)$: doseg $\forall x$ je samo $P(x)$, saj je to najmanjša formula desno od kvantifikatorja
- $\forall x\, (P(x) \land Q(x))$: z oklepaji razširimo doseg, zdaj je doseg $\forall x$ celotna formula $(P(x) \land Q(x))$

Kvantifikator **veže** svojo spremenljivko in **proste** spremenljivke z istim imenom v svojem dosegu.
- v $\forall x\, (P(x) \land Q(x))$ kvantifikator $\forall x$ veže oba $x$
- v $\forall x\, (P(x) \land \exists x\, Q(x))$ veže $\forall x$ samo $x$ v $P(x)$; $x$ v $Q(x)$ je že vezan z $\exists x$, zato ni prost in ga $\forall x$ ne veže

## vezane in proste spremenljivke
V formuli imamo vezane in proste spremenljivke:
- **vstop** spremenljivke $x$ je **vezan**, če se ta $x$ nahaja v dosegu (območju delovanja) kvantifikatorja $\forall x$ ali $\exists x$
- vstop spremenljivke, ki ni vezan, je **prost**

Vstop pomeni posamezno pojavitev spremenljivke v formuli. Ista spremenljivka ima lahko v eni formuli vezane in proste vstope.
- $\forall x\, Q(x, y)$: $x$ je vezan, $y$ je prost
- $\forall x\, P(x) \land Q(x)$: $x$ v $P(x)$ je vezan, $x$ v $Q(x)$ je prost (je izven dosega $\forall x$)

# Interpretacija izjavne formule
**Interpretacija** $I$ izjavne formule $W$ je sestavljena iz neprazne množice $D$, ki ji pravimo **področje pogovora** interpretacije. Poleg tega:
- vsakemu **predikatu** ustreza 0/1 logična funkcija v $D$
- vsaki **konstanti** določimo vrednost v $D$ (ponavadi je implicitno določena že z imenom konstante)
- vsaki **prosti spremenljivki** v $W$ določimo vrednost v $D$, pri tem vsem prostim spremenljivkam z istim imenom določimo isto vrednost iz $D$

## razlaga
Formula sama po sebi je samo **niz simbolov** in nima vrednosti. Npr. $Q(x, y)$ ne pomeni ničesar, dokler ne povemo, kaj je $Q$ in kaj sta $x$ in $y$. Interpretacija je **vse, kar moramo povedati**, da formuli lahko določimo vrednost 0 ali 1.

Po točkah:
- **področje pogovora $D$**: povemo, o čem govorimo (ljudje, števila, ...)
- **predikati**: povemo, kaj predikat pomeni, torej za vsak element (ali par elementov) iz $D$ vrne 0 ali 1. Npr. $Q(x, y)$: „$x < y$“.
- **konstante**: povemo, kateri element iz $D$ je konstanta. Pri konstanti $5$ je to očitno že iz imena, pri konstanti $a$ pa moramo povedati, npr. $a = 5$.
- **proste spremenljivke**: tudi tem moramo dati konkretno vrednost, sicer formula ni izjava
  - **vezanim** spremenljivkam vrednosti ne določamo, ker zanje poskrbi kvantifikator: $\exists x$ sam preveri elemente iz $D$
  - če se ista prosta spremenljivka pojavi večkrat, je povsod **ista vrednost**. V $P(y) \land Q(y)$ ne moremo vzeti $y = 2$ v prvem in $y = 7$ v drugem delu.

Ista formula ima lahko v **različnih interpretacijah različno vrednost**.

## primer
Formula: $W = \exists x\, Q(x, y) \land Q(y, a)$
- $x$ je vezan (v dosegu $\exists x$), zato mu vrednosti ne določamo
- $y$ je prost (oba vstopa), zato mu določimo eno vrednost
- $a$ je konstanta, zato ji določimo vrednost

**Interpretacija $I_1$:** $D = \{1, 2, 3, \dots\}$, $Q(x, y)$: „$x < y$“, $a = 5$, $y = 3$
- $\exists x\, Q(x, 3)$: obstaja število, manjše od 3? Da ($x = 1$), torej 1
- $Q(3, 5)$: $3 < 5$, torej 1
- $W = 1 \land 1 = 1$

**Interpretacija $I_2$:** enako kot $I_1$, le $y = 1$
- $\exists x\, Q(x, 1)$: obstaja število iz $D$, manjše od 1? Ne, torej 0
- $W = 0$ (konjunkcija z 0 je 0)

**Interpretacija $I_3$:** $D = \{1, 2, 3, \dots\}$, $Q(x, y)$: „$x > y$“, $a = 5$, $y = 3$
- $\exists x\, Q(x, 3)$: obstaja število, večje od 3? Da ($x = 4$), torej 1
- $Q(3, 5)$: $3 > 5$, torej 0
- $W = 1 \land 0 = 0$

Ista formula $W$ je torej v $I_1$ resnična, v $I_2$ in $I_3$ pa neresnična.

# Pomen kvantifikatorjev
Naj bo $W$ formula. Z $W(x/a)$ označimo formulo, ki jo dobimo tako, da v formuli $W$ vse **proste** vstope spremenljivke $x$ nadomestimo z $a$.

$W$: $P(x) \lor \exists x\, Q(x, y) \land R(b, x)$
$W(x/a)$: $P(a) \lor \exists x\, Q(x, y) \land R(b, a)$

Zakaj se je zamenjal samo prvi in zadnji $x$:
- $x$ v $P(x)$ je prost, zato ga zamenjamo z $a$
- $x$ v $Q(x, y)$ je v dosegu $\exists x$, torej vezan, zato ostane
- $x$ v $R(b, x)$ je prost, ker je doseg $\exists x$ samo $Q(x, y)$ (najmanjša formula desno od kvantifikatorja), zato ga zamenjamo z $a$

S tem lahko natančno povemo, kdaj je formula s kvantifikatorjem resnična:

Formula $\forall x\, W$ je **resnična** v interpretaciji $I$, če je za **vsak** element področja pogovora $d \in D$ resnična formula $W(x/d)$. Sicer je $\forall x\, W$ neresnična.

Formula $\exists x\, W$ je **resnična** v interpretaciji $I$, če v področju pogovora **obstaja** $d \in D$, za katerega je formula $W(x/d)$ resnična. Sicer je $\exists x\, W$ neresnična.

Torej: namesto $x$ po vrsti vstavljamo elemente iz $D$ in gledamo, ali je dobljena formula resnična.

Primer: $D = \{1, 2, 3\}$, $Q(x, y)$: „$x < y$“
- $\forall x\, Q(x, 4)$: preverimo $Q(1, 4)$, $Q(2, 4)$, $Q(3, 4)$, vse so resnične, zato je formula **resnična**
- $\exists x\, Q(x, 1)$: preverimo $Q(1, 1)$, $Q(2, 1)$, $Q(3, 1)$, nobena ni resnična, zato je formula **neresnična**

## triki pri določanju resničnosti (vaje)
Na neskončnem področju ne moremo preveriti vseh elementov, zato:
- $\forall$ **ovržemo z enim protiprimerom**, $\exists$ **potrdimo z enim primerom**
- $\forall x\, (W \Rightarrow V)$: gledamo samo $x$, pri katerih je $W$ resnična, pri ostalih je implikacija itak 1
- pazimo na **robne elemente**, v $\mathbb{N}$ sta to $0$ in $1$

Primer: $D = \mathbb{N}$, $P(x)$: „$x$ je praštevilo“, $D(x, y)$: „$x$ deli $y$“
- $\forall x\, (P(x) \lor D(2, x))$: **0**, protiprimer $x = 9$ (ni praštevilo in ni sod)
- $\exists x\, (P(x) \land D(2, x))$: **1**, primer $x = 2$
- $\forall x\, (D(4, x) \Rightarrow D(2, x))$: **1**, kar je deljivo s 4, je deljivo tudi z 2
- $\forall x\, \exists y\, D(x, y)$: **1**, vzamemo $y = x$ (ali $y = 0$, ker vsako število deli $0$)
- $\exists x\, \forall y\, D(x, y)$: **1**, $x = 1$ deli vsa števila
- $\forall x\, \exists y\, (P(y) \land D(y, x))$: **0**, protiprimer $x = 1$ nima nobenega praštevilskega delitelja
- $\exists x\, \forall y\, (D(x, y) \Rightarrow \neg P(y))$: **1**, $x = 10$, ker število, deljivo z 10, ni praštevilo
- $\forall x\, \exists y\, (P(x) \Rightarrow P(y) \land D(y, x))$: **1**. Če je $x$ praštevilo, vzamemo $y = x$, saj vsako število deli samo sebe. Če ni, je predpostavka 0 in implikacija velja

## preimenovanje spremenljivk
**Dejstvo:** če je $W$ formula, potem imen **prostih** spremenljivk ne smemo spreminjati, če želimo pridelati enakovredno formulo.
- $P(x)$ in $P(z)$ nista enakovredni: v interpretaciji lahko določimo $x = 1$ in $z = 2$, pa imata formuli različno vrednost

**Želja:** **vezane** spremenljivke lahko **preimenujemo** tako, da ista spremenljivka (tj. spremenljivka z istim imenom):
- ne nastopa pri več kvantifikatorjih
- ni hkrati vezana in prosta

Vezane spremenljivke lahko preimenujemo, ker kvantifikator itak preveri vse elemente iz $D$ in ime spremenljivke pri tem ni pomembno: $\exists x\, Q(x)$ in $\exists z\, Q(z)$ pomenita isto. Novo ime mora biti takšno, ki ga v formuli še ni.

Primeri:
- $\forall x\, P(x) \land \exists x\, Q(x)$: $x$ nastopa pri dveh kvantifikatorjih, preimenujemo drugega: $\forall x\, P(x) \land \exists z\, Q(z)$
- $P(x) \lor \exists x\, Q(x, y) \land R(b, x)$: $x$ je hkrati vezan in prost, preimenujemo vezanega: $P(x) \lor \exists z\, Q(z, y) \land R(b, x)$

# Enakovredne izjavne formule
Izjavni formuli $W$ in $V$ sta **enakovredni**, če imata isto logično vrednost v **vseh** možnih interpretacijah. V tem primeru pišemo $W \sim V$.
- primer: $\forall x\, \forall y\, P(x, y) \sim \forall y\, \forall x\, P(x, y)$ (pokazano v razdelku o interpretaciji)
- ni dovolj, da se ujemata v eni interpretaciji, ujemati se morata v vsaki

Izjavna formula $W$ je **splošno veljavna**, če je **resnična** v vsaki interpretaciji.
- primer: $P(x) \lor \neg P(x)$, ne glede na $D$, pomen $P$ in vrednost $x$ je vedno 1

Izjavna formula $V$ je **neizpolnljiva**, če je **neresnična** v vsaki interpretaciji.
- primer: $P(x) \land \neg P(x)$, vedno je 0

## triki pri (ne)enakovrednosti (vaje)
**Neenakovrednost** pokažemo z **eno interpretacijo**, v kateri imata formuli različno vrednost. Vzamemo čim manjše področje, npr. $D = \{a\}$ ali $D = \{a, b\}$, in vrednosti predikatov zapišemo v tabelo.

- $W = \forall x\, (P(x) \Rightarrow R(x))$ in $V = \exists x\, (P(x) \Rightarrow R(x))$, iščemo interpretacijo, kjer je $W = 0$ in $V = 1$
  - $D = \{a, b\}$, $P(a) = P(b) = 1$, $R(a) = 1$, $R(b) = 0$
  - $P(a) \Rightarrow R(a) = 1$, zato $V = 1$, in $P(b) \Rightarrow R(b) = 0$, zato $W = 0$
  - isto v $\mathbb{N}$: $P(x)$: „$x$ je praštevilo“, $R(x)$: „$x$ je sod“ ($x = 2$ ustreza, $x = 3$ ne)
- $\forall x\, (P(x) \Leftrightarrow R(x))$ in $\forall x\, (P(x) \Rightarrow R(x))$
  - $D = \{a\}$, $P(a) = 0$, $R(a) = 1$: implikacija je 1, ekvivalenca 0
  - v $\mathbb{N}$: $P(x)$: „$4 \mid x$“, $R(x)$: „$2 \mid x$“. Implikacija velja povsod, ekvivalenca pa ne ($x = 2$)
- $\forall x\, \forall y\, (P(x) \Rightarrow P(y))$ je **0**, če $P$ za en element velja, za drugega pa ne: $D = \{a, b\}$, $P(a) = 1$, $P(b) = 0$, za $x = a$, $y = b$ dobimo $1 \Rightarrow 0 = 0$

**Enakovrednost** pokažemo s preoblikovanjem po zakonih. Trik je v tem, da $\exists$ združimo čez $\lor$:
$$
\begin{aligned}
\forall x\, (P(x) \lor Q(x)) \Rightarrow \exists x\, (P(x) \land Q(x)) &\sim \neg \forall x\, (P(x) \lor Q(x)) \lor \exists x\, (P(x) \land Q(x)) \\
&\sim \exists x\, (\neg P(x) \land \neg Q(x)) \lor \exists x\, (P(x) \land Q(x)) \\
&\sim \exists x\, \big((\neg P(x) \land \neg Q(x)) \lor (P(x) \land Q(x))\big) \\
&\sim \exists x\, (P(x) \Leftrightarrow Q(x))
\end{aligned}
$$
- $(P \land Q) \lor (\neg P \land \neg Q)$ je ravno $P \Leftrightarrow Q$ (obe 1 ali obe 0)
- $\exists x\, P(x) \Leftrightarrow \exists x\, Q(x)$ pa **ni** enakovredna. V $\mathbb{N}$ vzamemo $P(x)$: „$x$ je praštevilo“ in $Q(x) = \neg P(x)$. Potem je $P(x) \Leftrightarrow \neg P(x)$ vedno 0, zato $\exists x\, (P(x) \Leftrightarrow Q(x)) = 0$, a $\exists x\, P(x) \Leftrightarrow \exists x\, Q(x) = 1 \Leftrightarrow 1 = 1$

# Zakoni predikatnega računa
So nekateri pomembni pari enakovrednih izjavnih formul.

**Negacija kvantifikatorja:** negacija gre skozi kvantifikator, kvantifikator pa se zamenja ($\forall \leftrightarrow \exists$).
$$\neg \forall x\, W \sim \exists x\, \neg W$$
$$\neg \exists x\, W \sim \forall x\, \neg W$$
- „ni res, da so vsi politiki pošteni“ = „obstaja politik, ki ni pošten“
- „ni res, da obstaja pošten politik“ = „vsi politiki so nepošteni“
- pri več kvantifikatorjih gre negacija skozi **vse** in obrne vsakega, na koncu uporabimo De Morgana:
$$\neg \forall x\, \exists y\, (P(x) \land \neg Q(y)) \sim \exists x\, \forall y\, \neg (P(x) \land \neg Q(y)) \sim \exists x\, \forall y\, (\neg P(x) \lor Q(y)) \sim \exists x\, \forall y\, (P(x) \Rightarrow Q(y))$$

**Zamenjava enakih kvantifikatorjev:**
$$\forall x\, \forall y\, W \sim \forall y\, \forall x\, W$$
$$\exists x\, \exists y\, W \sim \exists y\, \exists x\, W$$
- to smo pokazali v razdelku o interpretaciji (vsak pozna vsakega, nekdo pozna nekoga)

**Kvantifikator in veznik:** $\forall$ lahko razdelimo čez $\land$, $\exists$ pa čez $\lor$.
$$\forall x\, (W \land V) \sim \forall x\, W \land \forall x\, V$$
$$\exists x\, (W \lor V) \sim \exists x\, W \lor \exists x\, V$$
- „vsi so pametni in pošteni“ = „vsi so pametni in vsi so pošteni“
- „nekdo je pameten ali pošten“ = „nekdo je pameten ali nekdo je pošten“

## zakoni z omejitvami
Če se $x$ **ne pojavi (prosto)** v formuli $C$, potem veljajo naslednje enakovrednosti:
$$\forall x\, (C \lor W) \sim C \lor \forall x\, W$$
$$\exists x\, (C \lor W) \sim C \lor \exists x\, W$$
$$\forall x\, (C \land W) \sim C \land \forall x\, W$$
$$\exists x\, (C \land W) \sim C \land \exists x\, W$$

Če $C$ ne vsebuje prostega $x$, se njena vrednost ne spreminja, ko kvantifikator preverja različne $x$. Zato jo lahko prestavimo iz dosega kvantifikatorja.
- primer: $\forall x\, (P(a) \lor Q(x)) \sim P(a) \lor \forall x\, Q(x)$, ker $P(a)$ ne vsebuje $x$
- brez omejitve ne gre: $\forall x\, (P(x) \lor \neg P(x))$ je splošno veljavna, $P(x) \lor \forall x\, \neg P(x)$ pa ne (npr. $D = \{1, 2\}$, $P$ velja samo za 2, $x = 1$ da vrednost 0)

## zamenjava raznovrstnih kvantifikatorjev
Zamenjava raznovrstnih kvantifikatorjev v splošnem **ni možna**:
$$\forall x\, \exists y\, P(x, y) \not\sim \exists y\, \forall x\, P(x, y)$$
- $P(x, y)$: „$x$ pozna $y$-ona“
- $\forall x\, \exists y\, P(x, y)$: vsak pozna nekoga
- $\exists y\, \forall x\, P(x, y)$: obstaja nekdo, ki ga poznajo vsi
- protiprimer: $D = \{\text{Ana}, \text{Bor}\}$, Ana pozna Bora, Bor pozna Ano, nihče ne pozna sebe. Vsak pozna nekoga (1), ni pa nikogar, ki bi ga poznala oba (0).

**Včasih vseeno lahko:**
$$\forall x\, \exists y\, (P(x) \land Q(y)) \sim \exists y\, \forall x\, (P(x) \land Q(y))$$

Tu je vsak predikat odvisen samo od **ene** spremenljivke, zato lahko z zakoni z omejitvami kvantifikatorje premikamo naprej in nazaj:
$$
\begin{aligned}
\forall x\, \exists y\, (P(x) \land Q(y)) &\sim \forall x\, (P(x) \land \exists y\, Q(y)) && P(x) \text{ ne vsebuje } y \\
&\sim \forall x\, P(x) \land \exists y\, Q(y) && \exists y\, Q(y) \text{ ne vsebuje prostega } x \\
&\sim \exists y\, (\forall x\, P(x) \land Q(y)) && \forall x\, P(x) \text{ ne vsebuje } y \\
&\sim \exists y\, \forall x\, (P(x) \land Q(y)) && Q(y) \text{ ne vsebuje } x
\end{aligned}
$$

# Preneksna normalna oblika
**Trditev:** vsako formulo lahko enakovredno zapišemo tako, da se kvantifikatorji nahajajo **samo na začetku**.

Formula $W_{PNO}$ je **preneksna normalna oblika** formule $W$, če velja:
- $W_{PNO} \sim W$
- $W_{PNO}$ ima vse kvantifikatorje na začetku

Kako?
1. **Preimenujemo** spremenljivke (vezane, tako da ima vsak kvantifikator svojo spremenljivko in nobena ni hkrati vezana in prosta).
2. Znebimo se $\Rightarrow$ in $\Leftrightarrow$, raje imamo $\neg$, $\land$ in $\lor$.
3. **Izvlečemo** kvantifikatorje na začetek z uporabo zakonov predikatnega računa.

Preimenovanje naredimo zato, ker zakoni z omejitvami zahtevajo, da $C$ ne vsebuje spremenljivke kvantifikatorja. Ko ima vsak kvantifikator svoje ime, je ta pogoj vedno izpolnjen.

## primer
$$\forall x\, A(x) \lor \exists x\, B(x) \Rightarrow D(x) \land \exists x\, D(x)$$

**1. Preimenovanje.** $x$ nastopa pri treh kvantifikatorjih, v $D(x)$ pa je prost (doseg $\forall x$ je samo $A(x)$). Prostega $x$ ne smemo preimenovati, vezane pa preimenujemo v $y$, $z$, $w$:
$$\forall y\, A(y) \lor \exists z\, B(z) \Rightarrow D(x) \land \exists w\, D(w)$$

**2. Odstranimo implikacijo** ($W \Rightarrow V \sim \neg W \lor V$, $\Rightarrow$ veže najšibkeje, zato je levo cela disjunkcija):
$$\neg (\forall y\, A(y) \lor \exists z\, B(z)) \lor (D(x) \land \exists w\, D(w))$$

**3. Negacijo spravimo noter** (De Morgan, nato negacija kvantifikatorja):
$$
\begin{aligned}
&\sim (\neg \forall y\, A(y) \land \neg \exists z\, B(z)) \lor (D(x) \land \exists w\, D(w)) && \text{De Morgan} \\
&\sim (\exists y\, \neg A(y) \land \forall z\, \neg B(z)) \lor (D(x) \land \exists w\, D(w)) && \neg \forall \sim \exists \neg, \ \neg \exists \sim \forall \neg
\end{aligned}
$$

**4. Izvlečemo kvantifikatorje** (zakoni z omejitvami, po enega naenkrat):
$$
\begin{aligned}
&\sim \exists w\, \big((\exists y\, \neg A(y) \land \forall z\, \neg B(z)) \lor (D(x) \land D(w))\big) && \text{ostalo ne vsebuje } w \\
&\sim \exists w\, \exists y\, \big((\neg A(y) \land \forall z\, \neg B(z)) \lor (D(x) \land D(w))\big) && \text{ostalo ne vsebuje } y \\
&\sim \exists w\, \exists y\, \forall z\, \big((\neg A(y) \land \neg B(z)) \lor (D(x) \land D(w))\big) && \text{ostalo ne vsebuje } z
\end{aligned}
$$

Dobili smo PNO: vsi kvantifikatorji so na začetku. $x$ ostane prost, ker je bil prost že v začetni formuli.

## triki pri PNO (vaje)
**Kvantifikator na levi strani implikacije se obrne.** $W \Rightarrow V \sim \neg W \lor V$, zato negacija pri izvlečenju zamenja $\forall \leftrightarrow \exists$:
$$
\begin{aligned}
\forall x\, P(x) \Rightarrow \forall x\, Q(x) &\sim \forall x\, P(x) \Rightarrow \forall y\, Q(y) && \text{preimenovanje} \\
&\sim \exists x\, \neg P(x) \lor \forall y\, Q(y) \\
&\sim \exists x\, \forall y\, (\neg P(x) \lor Q(y)) \sim \exists x\, \forall y\, (P(x) \Rightarrow Q(y))
\end{aligned}
$$
- **pogosta napaka:** $\forall x\, \forall y\, (P(x) \Rightarrow Q(y))$ ni pravilno, $\forall$ z leve strani postane $\exists$

**Kvantifikator na desni strani implikacije ostane enak**, implikacijo lahko celo pustimo:
$$\forall x\, \forall y\, \big(P(x, y) \Rightarrow \exists z\, (P(x, z) \land P(y, z))\big) \sim \forall x\, \forall y\, \exists z\, \big(P(x, y) \Rightarrow P(x, z) \land P(y, z)\big)$$
- velja, ker $P(x, y)$ ne vsebuje $z$

**PNO ni enolična.** Kvantifikatorje, ki prihajajo iz **ločenih** delov formule, lahko izvlečemo v poljubnem vrstnem redu:
$$
\begin{aligned}
\forall x\, \big(\exists y\, P(x, y) \Rightarrow \forall y\, R(y, x) \lor \exists x\, T(x)\big) &\sim \forall x\, \big(\exists y\, P(x, y) \Rightarrow \forall z\, R(z, x) \lor \exists w\, T(w)\big) \\
&\sim \forall x\, \big(\forall y\, \neg P(x, y) \lor \forall z\, R(z, x) \lor \exists w\, T(w)\big) \\
&\sim \forall x\, \forall y\, \forall z\, \exists w\, \big(P(x, y) \Rightarrow R(z, x) \lor T(w)\big)
\end{aligned}
$$
- enako pravilno je $\forall x\, \exists w\, \forall z\, \forall y\, (\dots)$, ker so $y$, $z$ in $w$ vsak v svojem delu
- $\forall x$ pa mora ostati spredaj, ker ga vsebujeta $P(x, y)$ in $R(z, x)$

**Preimenujemo, preden izvlečemo, ker $\exists$ ne gre čez $\land$:**
$$\forall x\, \big(\exists y\, P(x, y) \land \exists y\, R(x, y)\big) \sim \forall x\, \exists y\, \exists z\, \big(P(x, y) \land R(x, z)\big)$$
- **ni pa** enakovredno $\forall x\, \exists y\, (P(x, y) \land R(x, y))$: tam bi moral isti $y$ ustrezati obema predikatoma

**Neenakovrednost pokažemo s protiprimerom** v majhnem področju pogovora. Ali je $\neg \forall x\, \exists y\, (P(x) \land R(x, y)) \sim \forall y\, \exists x\, (\neg P(x) \lor \neg R(x, y))$?
- pravilno je $\neg \forall x\, \exists y\, (\dots) \sim \exists x\, \forall y\, (\neg P(x) \lor \neg R(x, y))$ (za nek $x$ ne obstaja $y$), na desni pa sta kvantifikatorja **zamenjana**
- protiprimer: $D = \{a, b\}$, $P(a) = P(b) = 1$, $R$ velja samo za $(a, b)$ in $(b, a)$
- $\exists x\, \forall y\, (\neg P(x) \lor \neg R(x, y))$: za $x = a$ odpove $y = b$, za $x = b$ odpove $y = a$, torej **0**
- $\forall y\, \exists x\, (\neg P(x) \lor \neg R(x, y))$: za $y = a$ vzamemo $x = a$, za $y = b$ vzamemo $x = b$, torej **1**
- formuli imata različno vrednost, zato **nista enakovredni**

Ročni zapiski z vaj: [[DS - Predikati in množice - vaje.excalidraw]], [[DS - Predikati - vaje 4.excalidraw]]