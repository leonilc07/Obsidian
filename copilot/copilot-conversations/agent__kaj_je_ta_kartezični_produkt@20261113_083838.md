---
epoch: 1794555518863
mode: agent
backendId: claude
sessionId: "83084472-79d8-4beb-858b-4ddddb3dfbfa"
topic: "kaj je ta kartezični produkt?"
tags:
  - copilot-conversation
usage: '{"usedTokens":150313,"contextWindow":1000000,"inputTokens":2,"outputTokens":170,"cacheReadTokens":149846,"cacheWriteTokens":295,"updatedAt":1794571924427}'
lastAccessedAt: 1794571813384
---

**user**: kaj je ta kartezični produkt?
[Timestamp: 2026/11/13 08:38:41]

**ai**: **Kartezični produkt** dveh množic $A$ in $B$ je množica **vseh urejenih parov**, pri katerih je prva komponenta iz $A$, druga pa iz $B$:

$$A \times B = \{(a, b)\ ;\ a \in A \land b \in B\}$$

Preprosto povedano: vsak element iz $A$ združiš z vsakim elementom iz $B$.

**Primer**

Naj bo $A = \{1, 2\}$ in $B = \{x, y, z\}$. Potem je:

$$A \times B = \{(1,x), (1,y), (1,z), (2,x), (2,y), (2,z)\}$$

- **Število elementov:** $|A \times B| = |A| \cdot |B| = 2 \cdot 3 = 6$. Od tod ime „produkt“.
- Če si $A$ predstavljaš kot vrstice in $B$ kot stolpce, je $A \times B$ ravno mreža vseh kombinacij. Tako je tudi $\mathbb{R} \times \mathbb{R}$ koordinatna ravnina.

**Zakaj urejeni pari**

- Vrstni red je pomemben: $(1, x) \neq (x, 1)$. To sledi iz osnovne lastnosti urejenih parov $(a,b) = (c,d) \iff a = c \text{ in } b = d$.
- Zato je kartezični produkt **nekomutativen**: v splošnem $A \times B \neq B \times A$. V primeru zgoraj $B \times A$ vsebuje pare oblike $(x, 1)$, ki niso v $A \times B$.

**Več faktorjev**

- $A \times B \times C$ je množica vseh **urejenih trojic** $(a, b, c)$ z $a \in A$, $b \in B$ in $c \in C$.
- $A \times A \times A = A^3$ so torej **zaporedja dolžine 3** s členi iz $A$. To imaš že zapisano v zapiskih. Če je na primer $A = \{0, 1\}$, je $A^3$ množica vseh 8 trimestnih binarnih nizov: $(0,0,0), (0,0,1), \dots, (1,1,1)$.

**Lastnosti s prosojnice** pomenijo, da se kartezični produkt „lepo razdeli“ čez unijo in presek:

- $A \times (B \cup C) = (A \times B) \cup (A \times C)$
- $(A \cap B) \times (C \cap D) = (A \times C) \cap (B \times D)$

Če želiš, lahko to razlago dodam v [[13.11 - predavanje]].
[Timestamp: 2026/11/13 08:38:44]

**user**: razloži malo te lastnosti karteićnega zapisa
[Timestamp: 2026/11/13 08:48:24]

**ai**: Vse tri lastnosti dokažemo na enak način: vzamemo poljuben par $(x, y)$ in preverimo, da pripada levi strani **natanko takrat**, ko pripada desni. Pri tem uporabimo pravila logike.

**1. $A \times (B \cup C) = (A \times B) \cup (A \times C)$**

Kartezični produkt se **razdeli čez unijo**, podobno kot pri številih velja $a \cdot (b + c) = ab + ac$.

- **Intuicija:** prva komponenta je vedno iz $A$, druga pa iz $B$ *ali* iz $C$. Vse take pare dobimo tako, da posebej vzamemo pare z drugo komponento iz $B$ in posebej tiste z drugo komponento iz $C$, nato pa ju združimo.
- **Primer:** $A = \{1, 2\}$, $B = \{x\}$, $C = \{y\}$
  - $A \times (B \cup C) = A \times \{x, y\} = \{(1,x), (1,y), (2,x), (2,y)\}$
  - $A \times B = \{(1,x), (2,x)\}$ in $A \times C = \{(1,y), (2,y)\}$, unija obeh da enako množico ✓
- **Dokaz:**
$$(x,y) \in A \times (B \cup C) \iff x \in A \land (y \in B \lor y \in C)$$
$$\iff (x \in A \land y \in B) \lor (x \in A \land y \in C) \iff (x,y) \in (A \times B) \cup (A \times C)$$
  Ključni korak je **distributivnost** $\land$ čez $\lor$ iz logike.

**2. $(A \cup B) \times C = (A \times C) \cup (B \times C)$**

To je **ista lastnost, le z unijo na levi strani**. Zdaj je prva komponenta iz $A$ ali iz $B$, druga pa vedno iz $C$. Ker kartezični produkt ni komutativen, je treba to lastnost zapisati posebej. Dokaz poteka enako kot pri prvi.

**3. $(A \cap B) \times (C \cap D) = (A \times C) \cap (B \times D)$**

- **Intuicija:** levo zahtevamo, da je $x$ hkrati v $A$ in $B$ ter $y$ hkrati v $C$ in $D$. Desno zahtevamo, da je par $(x,y)$ hkrati v $A \times C$ in v $B \times D$. To sta isti 4 pogoji, le drugače združeni.
- **Dokaz:**
$$(x,y) \in (A \cap B) \times (C \cap D) \iff x \in A \land x \in B \land y \in C \land y \in D$$
$$\iff (x \in A \land y \in C) \land (x \in B \land y \in D) \iff (x,y) \in (A \times C) \cap (B \times D)$$
  Ker so vsi pogoji povezani z $\land$, jih lahko poljubno premešamo.
- **Geometrijsko:** če si $A \times C$ in $B \times D$ predstavljaš kot dva pravokotnika v ravnini, je njun presek spet pravokotnik. Njegova stranica na osi $x$ je $A \cap B$, na osi $y$ pa $C \cap D$.

**Pozor: z unijo to ne deluje.** V splošnem je $(A \cup B) \times (C \cup D) \neq (A \times C) \cup (B \times D)$.

- **Protiprimer:** $A = \{1\}$, $B = \{2\}$, $C = \{x\}$, $D = \{y\}$
  - levo: $\{1, 2\} \times \{x, y\} = \{(1,x), (1,y), (2,x), (2,y)\}$
  - desno: $\{(1,x)\} \cup \{(2,y)\} = \{(1,x), (2,y)\}$
  - na desni manjkata „mešana“ para $(1,y)$ in $(2,x)$
- Geometrijsko: unija dveh pravokotnikov v splošnem ni pravokotnik.
[Timestamp: 2026/11/13 08:48:43]

**user**: dobro daj to noter v zapisek
[Timestamp: 2026/11/13 08:50:39]

**ai**: Razlago lastnosti sem dodal v [[13.11 - predavanje]], takoj pod prosojnico z lastnostmi kartezičnega produkta. Vključil sem vse tri lastnosti z intuicijo, primerom in dokazom ter opozorilo s protiprimerom, da pri uniji podobna enakost ne velja.

Medtem si zapisek urejal tudi sam. Tvojih sprememb nisem prepisal, le dodal sem novo besedilo za tisto prosojnico.
[Timestamp: 2026/11/13 08:50:52]

**user**: razloži mi še lastnosti kartzičnega produkta(tisto odspodaj)
[Timestamp: 2026/11/13 08:55:53]

**ai**: Na spodnji prosojnici so štiri lastnosti. Dokazujemo jih podobno kot prejšnje: vzamemo poljuben element in sledimo definiciji.

**1. $A \times B = \emptyset \iff A = \emptyset \lor B = \emptyset$**

Produkt je prazen natanko takrat, ko je **vsaj ena** od množic prazna.

- **Intuicija:** za par $(a, b)$ potrebuješ element iz $A$ *in* element iz $B$. Če ena od množic nima nobenega elementa, ne moreš sestaviti niti enega para.
- **Primer:** $\emptyset \times \{1, 2, 3\} = \emptyset$
- **Dokaz (⇐):** če je na primer $A = \emptyset$, ne obstaja noben $a \in A$, zato ne obstaja noben par $(a,b)$.
- **Dokaz (⇒):** če sta obe množici neprazni, vzamemo $a \in A$ in $b \in B$. Potem je $(a, b) \in A \times B$, zato produkt ni prazen.

**2. $A \subseteq C \land B \subseteq D \implies A \times B \subseteq C \times D$**

Če povečaš množici, se poveča tudi produkt.

- **Dokaz:** vzamemo $(x, y) \in A \times B$. Potem je $x \in A \subseteq C$ in $y \in B \subseteq D$, torej $(x, y) \in C \times D$.
- **Geometrijsko:** če je pravokotnik $A \times B$ v obeh smereh ožji od $C \times D$, leži v celoti v njem.

**3. $A \times B \subseteq C \times D \land A \times B \neq \emptyset \implies A \subseteq C \land B \subseteq D$**

To je **obrat lastnosti 2**, vendar velja **samo, če produkt ni prazen**.

- **Dokaz:** vzamemo poljuben $a \in A$. Ker $A \times B \neq \emptyset$, je po lastnosti 1 tudi $B \neq \emptyset$, zato obstaja nek $b \in B$. Potem je $(a, b) \in A \times B \subseteq C \times D$, torej $a \in C$. Ker je bil $a$ poljuben, velja $A \subseteq C$. Za $B \subseteq D$ dokažemo enako.
- **Zakaj potrebujemo pogoj $\neq \emptyset$:** v dokazu potrebujemo nek $b$, ki ga postavimo v par z $a$. Če je $B$ prazna, takega $b$ ni.
- **Protiprimer brez pogoja:** $A = \{1, 2, 3\}$, $B = \emptyset$, $C = \{5\}$, $D = \{7\}$
  - $A \times B = \emptyset \subseteq C \times D$ velja, ker je prazna množica podmnožica vsake množice
  - vendar $A \not\subseteq C$

**4. $|A| = m,\ |B| = n \implies |A \times B| = m \cdot n$**

- **Intuicija:** za prvo komponento imaš $m$ možnosti, za vsako od njih pa $n$ možnosti za drugo komponento. Skupaj je to $m \cdot n$ parov.
- Pare lahko razporediš v mrežo z $m$ vrsticami (elementi $A$) in $n$ stolpci (elementi $B$). Vsako polje mreže je en par.
- **Primer:** $A = \{1, 2, 3\}$, $B = \{x, y\}$ da $3 \cdot 2 = 6$ parov: $(1,x), (1,y), (2,x), (2,y), (3,x), (3,y)$
- **Posledica:** $|A^k| = m^k$. Na primer $\{0,1\}^3$ ima $2^3 = 8$ elementov.

Če želiš, lahko tudi to dodam v [[13.11 - predavanje]] pod to prosojnico.
[Timestamp: 2026/11/13 08:55:55]

**user**: dobro daj to v zapisek in 2 tudi geometrisko pokaži
[Timestamp: 2026/11/13 08:58:30]

**ai**: Razlago vseh štirih lastnosti sem dodal v [[13.11 - predavanje]], takoj pod prosojnico s temi lastnostmi.

Za lastnost 2 sem narisal sliko in jo vstavil pod dokaz. Shranil sem jo kot [[Kartezični produkt - podmnožice.excalidraw]] v isto mapo:

![[Kartezični produkt - podmnožice.excalidraw]]

- **Modri pravokotnik** je $C \times D$. Na osi $x$ ga omejuje množica $C$, na osi $y$ pa množica $D$.
- **Oranžni pravokotnik** je $A \times B$. Ker je oranžni $A$ znotraj modrega $C$ in oranžni $B$ znotraj modrega $D$, oranžni pravokotnik leži v celoti znotraj modrega.
[Timestamp: 2026/11/13 08:58:32]

**user**: kaj je pri teh končnih množicah in t atrditev. kaj predstavlja trditev 2
[Timestamp: 2026/11/13 09:00:26]

**ai**: Na prosojnici je **Trditev s formulami za število elementov** (moč) končnih množic, ki jih sestavimo iz $A$, $B$ in $C$. Najprej na kratko vseh šest, nato podrobneje točka 2.

**Na kratko vse točke**

1. $|A \times B| = |A| \cdot |B|$: to je lastnost 4 od prej. Vsak element iz $A$ združiš z vsakim elementom iz $B$.
2. $|B^A| = |B|^{|A|}$: število vseh funkcij iz $A$ v $B$. Podrobneje spodaj.
3. $|\mathcal{P}A| = 2^{|A|}$: potenčna množica (množica vseh podmnožic) ima $2^{|A|}$ elementov. Za vsak element se odločiš, ali ga vzameš v podmnožico ali ne, kar sta 2 možnosti.
4. $|A \setminus B| = |A| - |A \cap B|$: od $A$ odšteješ tiste elemente, ki so tudi v $B$. Če je $B \subseteq A$, je $A \cap B = B$, zato je to kar $|A| - |B|$.
5. $|A \cup B| = |A| + |B| - |A \cap B|$: elemente iz preseka bi sicer šteli dvakrat, zato jih enkrat odštejemo. Če sta množici disjunktni ($A \cap B = \emptyset$), ni kaj odšteti.
6. $|A \cup B \cup C|$: enaka ideja za tri množice. Ta postopek se imenuje **načelo vključitev in izključitev**: seštej posamezne množice, odštej preseke parov in prištej presek vseh treh, ker si ga pri odštevanju vzel preveč.

**Točka 2: $|\{f\ ;\ f : A \to B\}| = |B^A| = |B|^{|A|}$**

- **Kaj predstavlja:** $\{f\ ;\ f : A \to B\}$ je množica **vseh funkcij** iz $A$ v $B$. Zanjo uporabljamo oznako $B^A$. Trditev pravi, da je takih funkcij $|B|^{|A|}$.
- **Zakaj:** funkcija vsakemu elementu iz $A$ priredi **natanko en** element iz $B$.
  - Za vsak element iz $A$ imaš $|B|$ možnosti, kam ga preslikati.
  - Elementov iz $A$ je $|A|$ in vsak izbira neodvisno od drugih.
  - Skupaj je to $\underbrace{|B| \cdot |B| \cdots |B|}_{|A| \text{-krat}} = |B|^{|A|}$.
- **Primer:** $A = \{1, 2\}$, $B = \{x, y, z\}$
  - $1$ lahko preslikaš v $x$, $y$ ali $z$ (3 možnosti), prav tako $2$ (3 možnosti).
  - Vseh funkcij je $3^2 = 9$. Če vsako zapišeš kot par $(f(1), f(2))$, so to: $(x,x), (x,y), (x,z), (y,x), (y,y), (y,z), (z,x), (z,y), (z,z)$.
- **Zakaj takšna oznaka $B^A$:** osnova je **kodomena** $B$, eksponent pa **domena** $A$, ker je število funkcij $|B|^{|A|}$. Pazi na vrstni red: funkcij iz $B$ v $A$ je v splošnem drugače veliko, in sicer $|A|^{|B|}$.
- **Povezava s kartezičnim produktom:** funkcija iz $\{1, 2, \dots, n\}$ v $B$ je v resnici zaporedje $(f(1), f(2), \dots, f(n))$ dolžine $n$ s členi iz $B$. To je ravno element iz $B^n = B \times \dots \times B$. Zato je oznaka $B^A$ smiselna posplošitev $B^n$.
- **Povezava s točko 3:** podmnožico $S \subseteq A$ lahko opišeš s funkcijo $f : A \to \{0, 1\}$. Pri tem je $f(a) = 1$, če $a \in S$, in $f(a) = 0$, če $a \notin S$. Takih funkcij je po točki 2 natanko $2^{|A|}$, zato je tudi podmnožic $2^{|A|}$.

Če želiš, lahko tudi to dodam v [[13.11 - predavanje]] pod to prosojnico.
[Timestamp: 2026/11/13 09:00:28]

**user**: r: 𝐴 ={1,2}, 𝐵 ={𝑥,𝑦,𝑧}
1 lahko preslikaš v 𝑥, 𝑦 ali 𝑧 (3 možnosti), prav tako 2 (3 možnosti).
Vseh funkcij je 32 =9. Če vsako zapišeš kot par (𝑓(1),𝑓(2)), so to: (𝑥,𝑥),(𝑥,𝑦),(𝑥,𝑧),(𝑦,𝑥),(𝑦,𝑦),(𝑦,𝑧),(𝑧,𝑥),(𝑧,𝑦),(𝑧,𝑧). a ni tukaj 1,x 1,y 1,z 2,x 2,y 2,z in jih je 6 ne 9
[Timestamp: 2026/11/13 09:05:34]

**ai**: Ne, funkcij je res 9. Tvojih 6 parov ni 6 funkcij, ampak **6 posameznih puščic**, iz katerih funkcije sestavljamo. Tvoji pari so ravno elementi kartezičnega produkta $A \times B$:

$$A \times B = \{(1,x), (1,y), (1,z), (2,x), (2,y), (2,z)\}$$

Vsak tak par pove le, kam gre **en** element. Na primer $(1, x)$ pomeni „$1$ se preslika v $x$“.

**Ena funkcija pa mora povedati, kam gre vsak element iz $A$, torej oba hkrati.** Zato je funkcija sestavljena iz **dveh** puščic: ene za $1$ in ene za $2$.

- za $1$ izbereš eno puščico izmed $(1,x), (1,y), (1,z)$, kar so 3 možnosti
- za $2$ izbereš eno puščico izmed $(2,x), (2,y), (2,z)$, kar so 3 možnosti
- vsako izbiro za $1$ lahko kombiniraš s katerokoli izbiro za $2$, zato je funkcij $3 \cdot 3 = 9$

**Vseh 9 funkcij**, vsaka zapisana kot množica svojih puščic:

- $f_1 = \{(1,x), (2,x)\}$
- $f_2 = \{(1,x), (2,y)\}$
- $f_3 = \{(1,x), (2,z)\}$
- $f_4 = \{(1,y), (2,x)\}$
- $f_5 = \{(1,y), (2,y)\}$
- $f_6 = \{(1,y), (2,z)\}$
- $f_7 = \{(1,z), (2,x)\}$
- $f_8 = \{(1,z), (2,y)\}$
- $f_9 = \{(1,z), (2,z)\}$

V prejšnji razlagi sem vsako funkcijo zapisal krajše kot par $(f(1), f(2))$. Tako $(x, y)$ pomeni isto kot $f_2$: $1 \mapsto x$ in $2 \mapsto y$. To je bil drug zapis kot tvoji pari, zato je verjetno prišlo do zmede.

**Na kratko:**
- $|A \times B| = 3 \cdot 2 = 6$ je število vseh možnih **puščic**.
- $|B^A| = 3^2 = 9$ je število vseh **funkcij**. Vsaka funkcija iz teh 6 puščic izbere natanko eno puščico za vsak element iz $A$.
[Timestamp: 2026/11/13 09:05:45]

**user**: do naslova moč množice v teh zapiskih jih uredi tako da use slike in zapiske izbrišeš in jih nadomestiš. in še normalno uredi zapiske kakor so drugi v tej datoteki
[Timestamp: 2026/11/13 09:12:21]

**ai**: Prerisal sem ročne zapiske v slike, da jih lahko preberem. Zdaj jih pregledam in nato uredim zapisek.Uredil sem [[13.11 - predavanje]] do prosojnice „Moč končnih množic“. Vse slike prosojnic in ročne zapiske sem odstranil iz zapiska in jih nadomestil z napisanim besedilom. Oblika je enaka kot v [[Množice]]: naslovi `#` in `##`, lastnosti pa oštevilčene s podpičji **beremo / zakaj / primer**.

**Nova zgradba zapiska:**
- **Urejeni pari:** definicija in osnovna lastnost
- **Kartezični produkt:** definicija, zgledi in več faktorjev ($A^3$, $n$-terice)
- **Lastnosti kartezičnega produkta**
  - **unija in presek:** vse tri lastnosti, posledica s $C = D$ in opozorilo, da z unijo ne deluje
  - **prazna množica in vsebovanost:** vse štiri lastnosti s prosojnice

**Iz ročnih zapiskov sem prenesel:**
- primer $\{a, b\} \times \{1, 2, 3\}$ in pravokotnik $[1, 3] \times [2, 5]$
- izpeljavo $(A \cap B) \times C = (A \times C) \cap (B \times C)$ in primer s kvadratoma $A = C = [1, 3]$, $B = D = [2, 5]$
- opombo, da je pri $A \times B = \emptyset$ produkt podmnožica vsakega $C \times D$, s protiprimerom $A = \emptyset$, $B = \mathbb{N}$
  - v ročnem zapisu sem množico $C$ prebral kot $\{c, č\}$; preveri, ali je to prav

Tvojo skico s kvadratoma sem prerisal v novo risbo [[Kartezični produkt - presek in unija.excalidraw]]. Prejšnja risba za vsebovanost je ostala v zapisku.

Prosojnici o moči končnih množic sem pustil, kot sta bili. Slikovne datoteke in ročni zapiski so še vedno v mapi `stvari/`, odstranil sem jih le iz zapiska. Če želiš, jih lahko tudi izbrišem.
[Timestamp: 2026/11/13 09:12:24]

**user**: uredi sedaj še ta zapisek do konca
[Timestamp: 2026/11/13 10:00:22]

**ai**: Prebral sem še zadnji prosojnici. Zdaj si ogledam tvoja ročna zapiska.Uredil sem še preostali del [[13.11 - predavanje]]. Iz zapiska sem odstranil vse slike prosojnic in ročne zapiske ter jih nadomestil z besedilom v enaki obliki kot prej.

**Nove sekcije:**
- **Moč končnih množic:** definicija, enako močni množici in zgledi
  - vseh 6 točk trditve s podpičji **beremo / zakaj / primer**
  - pri točki 2 je vključen primer z 9 funkcijami in razlaga, zakaj jih ni 6
  - pri točkah 4 in 5 sem prenesel tvoje ročne izpeljave: $A \setminus B = A \setminus (A \cap B)$ in $A \cup B = A \cup (B \setminus A)$
- **Načelo vključitev in izključitev:** izrek in razlaga, kaj pomeni $S_k$
- **Nalogi:**
  - **naloga 1:** rešena prek $A_k$; rezultat je **12**
  - **naloga 2:** rešena po tvojem postopku; zaposlenih je **100** programerjev, v natanko dveh jezikih jih programira **60**

**Dve novi risbi:**
- [[Moč unije dveh množic.excalidraw]] prikazuje, zakaj presek odštejemo enkrat
- [[Naloga programerji.excalidraw]] je tvoj Vennov diagram s številom programerjev v vsakem delu. Vrednosti sem preveril: skupaj dajo 100.

**Pazi na prosojnico z izrekom.** Tam je na koncu zapisano $\sum_{i=0}^{n} (-1)^i S_i$. Ta vsota ni enaka moči unije, ampak številu elementov iz $A$, ki niso v nobeni $A_i$. V zapisek sem dal pravilno formulo $\sum_{k=1}^{n} (-1)^{k+1} S_k$ in dodal opombo o razliki. Mogoče je napaka na prosojnici, zato je vredno preveriti pri profesorju.

Slikovne datoteke in ročni zapiski so še vedno v mapi `stvari/`, odstranil sem jih le iz zapiska.
[Timestamp: 2026/11/13 10:00:24]

**user**: te lastnosti relaciji ni treba na dolgo razlagat kot prej. lahko malo krajše.  seda uredi do konca
[Timestamp: 2026/11/13 10:55:24]

**ai**: Prebral sem prosojnice o relacijah. Zdaj preberem še tri ročne zapiske.Uredil sem še del o relacijah do konca zapiska [[13.11 - predavanje]]. Prosojnice in tri ročne zapiske sem odstranil in jih nadomestil z besedilom. Lastnosti relacij sem razložil krajše, z eno vrstico za vsako lastnost.

**Nove sekcije pod `# Relacije`:**
- **definicija** relacije in zapis $xRy$
- **zgledi:** $\{e,f,g,h\}$, $\leq$, $\mathrm{id}_A$, prazna in univerzalna relacija, skupaj s tvojimi opombami
- **domena in zaloga vrednosti:** tvoji primeri za $R$, $\leq$, $<$ in $>$
- **lastnosti relacij:** vseh 6 lastnosti
- **zgledi lastnosti:** tvojo ročno tabelo s kljukicami sem prepisal v tabelo s ✓ in ✗. Dodal sem kratko pojasnilo za oznaki „!“: $<$ in „oče“ sta antisimetrični le zato, ker predpostavka $xRy \land yRx$ ni nikoli izpolnjena.
- **grafična predstavitev:** dodal sem risbo [[Graf relacije e f g h.excalidraw]] s puščicami $e \to f \to g \to h$

Slike in ročni zapiski so še vedno v mapi `stvari/`, odstranil sem jih samo iz zapiska.
[Timestamp: 2026/11/13 10:55:27]

**user**: preimenuj to datoteko v nekaj smiselnega in jo dodaj na ds glavno ter vse slike preloži v mapo stvari in popravi povezave
[Timestamp: 2026/11/13 13:10:52]

**ai**: Drugi zapiski imajo risbe v mapi `stvari`. Tja premaknem tudi teh pet risb in preimenujem zapisek.Opravljeno:

- **Preimenovanje:** zapisek `13.11 - predavanje` se zdaj imenuje [[Kartezični produkt, moč množic in relacije]].
- **DS glavno:** v [[DS glavno]] sem pod „predavanja“ dodal vrstico `13. 11. 2026: [[Kartezični produkt, moč množic in relacije]]`.
- **Risbe:** vseh 5 risb iz zapiska sem premaknil iz `diskretne strukture/` v `stvari/`, kjer so tudi risbe za [[Množice]].
- **Povezave:** popravki niso bili potrebni. Zapisek vstavlja risbe samo po imenu (na primer `![[Naloga programerji.excalidraw]]`), zato jih Obsidian najde tudi v novi mapi. Drugih povezav na stari naslov zapiska nisem našel.
- **Prosojnice:** te so bile že v `stvari/`. Iz zapiska sem jih odstranil že prej, zato jih nisem premikal.

V zapisku nisem odprl nobene vstavljene risbe, da bi preveril, ali se po premiku res prikaže.

Opazil sem še, da tudi [[Množice]] ni navedena v [[DS glavno]]. Če želiš, jo dodam.
[Timestamp: 2026/11/13 13:10:52]

**user**: dodaj
[Timestamp: 2026/11/13 13:11:56]

**ai**: [[Množice]] sem dodal v [[DS glavno]] pod „predavanja“, pred zapisek s 13. 11. Datuma predavanja ne vem, zato sem vpisal samo povezavo. Če ga poveš, ga dodam.

Priložen je bil tudi zapisek [[01 Zahteve in uporabniške zgodbe]], vendar ga nisem spreminjal. „Dodaj“ sem razumel kot odgovor na moj prejšnji predlog.
[Timestamp: 2026/11/13 13:11:56]