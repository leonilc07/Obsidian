# Urejeni pari
**Urejeni par** s **prvo komponento** (koordinato) $a$ in **drugo komponento** (koordinato) $b$ označimo z $(a, b)$ in definiramo kot
$$(a, b) = \{\{a\}, \{a, b\}\}$$

**Trditev** (osnovna lastnost urejenih parov):
$$(a, b) = (c, d) \iff a = c \land b = d$$
- pri urejenem paru je **vrstni red pomemben**: $(1, 2) \neq (2, 1)$, čeprav je $\{1, 2\} = \{2, 1\}$

# Kartezični produkt
**Kartezični produkt** množic $A$ in $B$ je množica vseh urejenih parov
$$A \times B = \{(a, b) \,;\, a \in A \land b \in B\}$$
- vsak element iz $A$ združimo z vsakim elementom iz $B$
- kartezični produkt **ni komutativen**: v splošnem je $A \times B \neq B \times A$

## zgledi
- $A = \{a, b\}$, $B = \{1, 2, 3\}$: $A \times B = \{(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3)\}$
- $A = [1, 3]$, $B = [2, 5]$: $A \times B$ je **pravokotnik** v ravnini, pri katerem $x$ teče od 1 do 3, $y$ pa od 2 do 5
- $\mathbb{R} \times \mathbb{R}$ je cela koordinatna ravnina

## več faktorjev
$(a_1, a_2, \dots, a_n)$ je **urejena $n$-terica**. Definicijo kartezičnega produkta lahko razširimo na več faktorjev:
- $A \times B \times C$ je množica vseh urejenih trojic s prvo koordinato v $A$, drugo v $B$ in tretjo v $C$
- $A \times A \times A = A^3$ so **zaporedja dolžine 3** s členi iz $A$
- primer: $\{0, 1\}^3$ so vsi trimestni binarni nizi $(0, 0, 0), (0, 0, 1), \dots, (1, 1, 1)$

# Lastnosti kartezičnega produkta
Lastnosti dokazujemo tako, da vzamemo poljuben par $(x, y)$ in preverimo, da pripada levi strani **natanko takrat**, ko pripada desni. Pri tem uporabimo pravila logike.

## unija in presek
**1.** $A \times (B \cup C) = (A \times B) \cup (A \times C)$
- beremo: kartezični produkt se **razdeli čez unijo**, podobno kot pri številih velja $a \cdot (b + c) = ab + ac$
- zakaj: prva komponenta je vedno iz $A$, druga pa iz $B$ *ali* iz $C$
$$(x, y) \in A \times (B \cup C) \iff x \in A \land (y \in B \lor y \in C)$$
$$\iff (x \in A \land y \in B) \lor (x \in A \land y \in C) \iff (x, y) \in (A \times B) \cup (A \times C)$$
  Ključni korak je **distributivnost** $\land$ čez $\lor$.
- primer: $A = \{1, 2\}$, $B = \{x\}$, $C = \{y\}$
  - $A \times (B \cup C) = A \times \{x, y\} = \{(1, x), (1, y), (2, x), (2, y)\}$
  - $A \times B = \{(1, x), (2, x)\}$ in $A \times C = \{(1, y), (2, y)\}$, njuna unija je enaka množica

**2.** $(A \cup B) \times C = (A \times C) \cup (B \times C)$
- beremo: ista lastnost, le z unijo na levi strani
- zakaj: dokaz je enak kot pri 1. Ker kartezični produkt ni komutativen, moramo to lastnost zapisati posebej.

**3.** $(A \cap B) \times (C \cap D) = (A \times C) \cap (B \times D)$
- zakaj: na obeh straneh so isti 4 pogoji, le drugače združeni
$$(x, y) \in (A \cap B) \times (C \cap D) \iff x \in A \land x \in B \land y \in C \land y \in D$$
$$\iff (x \in A \land y \in C) \land (x \in B \land y \in D) \iff (x, y) \in (A \times C) \cap (B \times D)$$
- geometrijsko: presek dveh pravokotnikov je spet pravokotnik. Njegova stranica na osi $x$ je $A \cap B$, na osi $y$ pa $C \cap D$.
- posledica: če v 3 vstavimo $C = D$, dobimo
$$(A \cap B) \times C = (A \cap B) \times (C \cap C) = (A \times C) \cap (B \times C)$$

**Pozor: z unijo to ne deluje.** V splošnem je $(A \cup B) \times (C \cup D) \neq (A \times C) \cup (B \times D)$.
- primer: $A = C = [1, 3]$, $B = D = [2, 5]$
  - $A \times C = [1, 3] \times [1, 3]$ in $B \times D = [2, 5] \times [2, 5]$ sta kvadrata, ki se prekrivata
  - presek obeh je $[2, 3] \times [2, 3] = (A \cap B) \times (C \cap D)$, kar se ujema s 3
  - $(A \cup B) \times (C \cup D) = [1, 5] \times [1, 5]$ je cel velik kvadrat, unija obeh kvadratov pa ne pokrije dveh kotov
- primer s končnimi množicami: $A = \{1\}$, $B = \{2\}$, $C = \{x\}$, $D = \{y\}$
  - levo: $\{1, 2\} \times \{x, y\} = \{(1, x), (1, y), (2, x), (2, y)\}$
  - desno: $\{(1, x)\} \cup \{(2, y)\} = \{(1, x), (2, y)\}$
  - na desni manjkata „mešana“ para $(1, y)$ in $(2, x)$

![[Kartezični produkt - presek in unija.excalidraw]]

## prazna množica in vsebovanost
**1.** $A \times B = \emptyset \iff A = \emptyset \lor B = \emptyset$
- beremo: produkt je prazen natanko takrat, ko je **vsaj ena** od množic prazna
- zakaj (⇐): če je na primer $A = \emptyset$, ne obstaja noben $a \in A$, zato ne moremo sestaviti nobenega para $(a, b)$
- zakaj (⇒): če sta obe množici neprazni, vzamemo $a \in A$ in $b \in B$. Potem je $(a, b) \in A \times B$, zato produkt ni prazen.
- primer: $\emptyset \times \{1, 2, 3\} = \emptyset$

**2.** $A \subseteq C \land B \subseteq D \implies A \times B \subseteq C \times D$
- beremo: če povečamo množici, se poveča tudi produkt
- zakaj: vzamemo $(x, y) \in A \times B$. Potem je $x \in A \subseteq C$ in $y \in B \subseteq D$, torej $(x, y) \in C \times D$.
- geometrijsko: $A$ leži znotraj $C$ na osi $x$, $B$ pa znotraj $D$ na osi $y$. Zato je pravokotnik $A \times B$ v obeh smereh ožji od $C \times D$ in leži v celoti v njem.

![[Kartezični produkt - podmnožice.excalidraw]]

**3.** $A \times B \subseteq C \times D \land A \times B \neq \emptyset \implies A \subseteq C \land B \subseteq D$
- beremo: to je **obrat lastnosti 2**, vendar velja **samo, če produkt ni prazen**
- zakaj: vzamemo poljuben $a \in A$. Ker je $A \times B \neq \emptyset$, je po lastnosti 1 tudi $B \neq \emptyset$, zato obstaja nek $b \in B$. Potem je $(a, b) \in A \times B \subseteq C \times D$, torej $a \in C$. Ker je bil $a$ poljuben, velja $A \subseteq C$. Za $B \subseteq D$ dokažemo enako.
- zakaj potrebujemo pogoj $A \times B \neq \emptyset$: če je $A \times B = \emptyset$, je $A \times B \subseteq C \times D$ **pri vseh** $C$ in $D$, ker je prazna množica podmnožica vsake množice. Iz tega torej ne moremo nič sklepati o $A$ in $B$.
- protiprimer: $A = \emptyset$, $B = \mathbb{N}$, $C = \{c, č\}$, $D = \{1, 2, 3\}$
  - $A \times B = \emptyset \subseteq C \times D$
  - vendar $B = \mathbb{N} \not\subseteq \{1, 2, 3\} = D$

**4.** $|A| = m,\ |B| = n \implies |A \times B| = m \cdot n$
- beremo: če je $A$ končna z $m$ elementi in $B$ končna z $n$ elementi, je $A \times B$ končna z $m \cdot n$ elementi
- zakaj: za prvo komponento imamo $m$ možnosti, za vsako od njih pa $n$ možnosti za drugo komponento. Pare lahko razporedimo v mrežo z $m$ vrsticami in $n$ stolpci.
- primer: $A = \{1, 2, 3\}$, $B = \{x, y\}$: $3 \cdot 2 = 6$ parov, in sicer $(1, x), (1, y), (2, x), (2, y), (3, x), (3, y)$
- posledica: $|A^k| = m^k$, na primer $\{0, 1\}^3$ ima $2^3 = 8$ elementov

# Moč končnih množic
Naj bo $A$ končna množica. Potem $|A|$ označuje **število elementov** ali **moč** množice $A$.

Končni množici $A$ in $B$ sta **enako močni**, $A \sim B$, če je $|A| = |B|$.

Zgledi:
- $|\emptyset| = 0$
- $|\{0, 1\}| = 2$
- $|\{\{0, 1\}\}| = 1$: množica ima en sam element, to je množica $\{0, 1\}$

## trditev
Naj bodo $A$, $B$ in $C$ končne množice.

**1.** $|A \times B| = |A| \cdot |B|$
- zakaj: vsak element iz $A$ združimo z vsakim elementom iz $B$ (glej lastnost 4 kartezičnega produkta)

**2.** $|\{f \,;\, f : A \to B\}| = |B^A| = |B|^{|A|}$
- beremo: $B^A$ je množica **vseh funkcij** iz $A$ v $B$, takih funkcij je $|B|^{|A|}$
- zakaj: funkcija vsakemu elementu iz $A$ priredi **natanko en** element iz $B$. Za vsak element iz $A$ imamo $|B|$ možnosti, elementov iz $A$ je $|A|$ in vsak izbira neodvisno od drugih, zato je funkcij $|B| \cdot |B| \cdots |B| = |B|^{|A|}$.
- primer: $A = \{1, 2\}$, $B = \{x, y, z\}$: funkcij je $3^2 = 9$
  - vse možne puščice so elementi $A \times B = \{(1, x), (1, y), (1, z), (2, x), (2, y), (2, z)\}$, teh je 6
  - ena funkcija izbere **eno puščico za 1 in eno za 2**, na primer $\{(1, x), (2, y)\}$. Za 1 so 3 možnosti in za 2 tudi 3, zato je funkcij $3 \cdot 3 = 9$.
- oznaka $B^A$: osnova je **kodomena** $B$, eksponent pa **domena** $A$. Funkcija iz $\{1, \dots, n\}$ v $B$ je zaporedje $(f(1), \dots, f(n))$, torej element $B^n$.

**3.** $|\mathcal{P}A| = 2^{|A|}$
- zakaj: za vsak element se odločimo, ali ga vzamemo v podmnožico ali ne. To sta 2 možnosti, zato je podmnožic $2^{|A|}$.
- povezava z 2: podmnožico $S \subseteq A$ opišemo s funkcijo $f : A \to \{0, 1\}$, kjer je $f(a) = 1$, če $a \in S$, sicer pa $f(a) = 0$. Takih funkcij je $2^{|A|}$.

**4.** Če je $B \subseteq A$, potem je $|A \setminus B| = |A| - |B|$. V splošnem je $|A \setminus B| = |A| - |A \cap B|$.
- zakaj ($B \subseteq A$): število elementov v $A \setminus B$ je število elementov v $A$ minus število elementov v $B$
- zakaj (v splošnem): od $A$ odvzamemo le tiste elemente, ki so tudi v $B$
$$A \setminus B = A \setminus (A \cap B)$$
  ker je $A \cap B \subseteq A$, smemo uporabiti prvi del, zato $|A \setminus B| = |A| - |A \cap B|$
- izpeljava enakosti:
$$
\begin{aligned}
A \setminus (A \cap B) &= A \cap (A \cap B)^c = A \cap (A^c \cup B^c) \\
&= (A \cap A^c) \cup (A \cap B^c) = \emptyset \cup (A \cap B^c) = A \setminus B
\end{aligned}
$$

**5.** Če je $A \cap B = \emptyset$, potem je $|A \cup B| = |A| + |B|$. V splošnem je $|A \cup B| = |A| + |B| - |A \cap B|$.
- zakaj (disjunktni): ni skupnih elementov, zato nobenega ne štejemo dvakrat
- zakaj (v splošnem): $A \cup B$ zapišemo kot unijo disjunktnih množic
$$A \cup B = A \cup (B \setminus A)$$
  $A$ in $B \setminus A$ sta disjunktni, ker je $A \cap (B \setminus A) = A \cap B \cap A^c = \emptyset$. Zato je
$$|A \cup B| = |A| + |B \setminus A| = |A| + |B| - |A \cap B|$$
  pri čemer smo uporabili 4
- intuicija: elemente iz $A \cap B$ štejemo v $|A|$ in v $|B|$, torej dvakrat, zato jih enkrat odštejemo
- formulo lahko obrnemo, ko poznamo unijo in iščemo presek: $|A \cap B| = |A| + |B| - |A \cup B|$, oziroma $|A \cap B| + |A \cup B| = |A| + |B|$

![[Moč unije dveh množic.excalidraw]]

**6.** $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
- zakaj: element, ki je v vseh treh množicah, prištejemo 3-krat in pri presekih parov odštejemo 3-krat, zato ga moramo na koncu še enkrat prišteti
- to je **načelo vključitev in izključitev** za tri množice

# Načelo vključitev in izključitev
**Izrek:** naj bo $A$ končna množica in $A_1, A_2, \dots, A_n \subseteq A$. Potem je
$$
\begin{aligned}
|A_1 \cup A_2 \cup \dots \cup A_n| = {} & |A_1| + |A_2| + \dots + |A_n| \\
& - |A_1 \cap A_2| - |A_1 \cap A_3| - \dots - |A_{n-1} \cap A_n| \\
& + \dots \\
& + (-1)^{n+1} |A_1 \cap A_2 \cap \dots \cap A_n|
\end{aligned}
$$
Krajše zapisano:
$$|A_1 \cup \dots \cup A_n| = \sum_{k=1}^{n} (-1)^{k+1} S_k, \qquad S_k = \sum_{\substack{\mathcal{J} \subseteq \{1, \dots, n\} \\ |\mathcal{J}| = k}} \left| \bigcap_{i \in \mathcal{J}} A_i \right|$$
- $S_k$ je vsota moči vseh presekov **natanko $k$ množic**: $S_1 = |A_1| + \dots + |A_n|$, $S_2$ so vsi preseki parov, $S_3$ vsi preseki trojic itd.
- predznaki se izmenjujejo: posamezne množice **prištejemo**, preseke parov **odštejemo**, preseke trojic **prištejemo** …
- za $n = 2$ in $n = 3$ dobimo ravno točki 5 in 6 iz trditve
- na prosojnici je zapisano $\sum_{i=0}^{n} (-1)^i S_i$, kjer je $S_0 = |A|$. Ta vsota je pravzaprav enaka $|A| - |A_1 \cup \dots \cup A_n|$, torej številu elementov iz $A$, ki **niso v nobeni** od množic $A_i$.

# Nalogi
## naloga 1
**Koliko je števil na celoštevilskem intervalu $[1 \dots 96]$, ki so deljiva s 6 in niso deljiva niti s 24 niti z 32?**

Z $A_k$ označimo množico števil iz $[1 \dots 96]$, ki so deljiva s $k$. Velja
$$|A_k| = \left\lfloor \frac{96}{k} \right\rfloor$$

Iščemo
$$|A_6 \setminus (A_{24} \cup A_{32})| = |A_6| - |A_6 \cap (A_{24} \cup A_{32})|$$
po točki 4 trditve. Presek z unijo razpišemo po točki 5:
$$|A_6 \cap (A_{24} \cup A_{32})| = |A_6 \cap A_{24}| + |A_6 \cap A_{32}| - |A_6 \cap A_{24} \cap A_{32}|$$

Preseki: število je deljivo z $a$ in z $b$ natanko takrat, ko je deljivo z njunim najmanjšim skupnim večkratnikom.
- $A_6 \cap A_{24} = A_{24}$, ker je vsako število, deljivo s 24, deljivo tudi s 6
- $A_6 \cap A_{32} = A_{96}$
- $A_6 \cap A_{24} \cap A_{32} = A_{96}$

Rezultat:
$$|A_6| - |A_{24}| - |A_{96}| + |A_{96}| = \frac{96}{6} - \frac{96}{24} = 16 - 4 = 12$$

## naloga 2
**Zaposleni v nekem podjetju programirajo v treh jezikih: Java, C in Python. V vsakem jeziku programira tri petine programerjev, v C in Pythonu dve petini, v C-ju in Javi tri desetine ter v jezikih Java in Python ena petina. V vseh treh jezikih programira 10 programerjev. Koliko programerjev je zaposlenih v podjetju? Koliko jih programira v natanko dveh jezikih?**

Naj bo $n$ število programerjev, $J$, $C$ in $P$ pa množice programerjev, ki programirajo v Javi, C-ju in Pythonu.
- $|J| = |C| = |P| = \frac{3}{5} n$
- $|C \cap P| = \frac{2}{5} n$, $|C \cap J| = \frac{3}{10} n$, $|P \cap J| = \frac{1}{5} n$
- $|J \cap C \cap P| = 10$

Vsak programer programira v vsaj enem jeziku, zato je $n = |J \cup C \cup P|$. Po načelu vključitev in izključitev:
$$
\begin{aligned}
n &= 3 \cdot \tfrac{3}{5} n - \tfrac{2}{5} n - \tfrac{3}{10} n - \tfrac{1}{5} n + 10 \\
&= \tfrac{18}{10} n - \tfrac{4}{10} n - \tfrac{3}{10} n - \tfrac{2}{10} n + 10 = \tfrac{9}{10} n + 10
\end{aligned}
$$
Od tod $\frac{1}{10} n = 10$, torej je **$n = 100$**.

Moči so torej $|J| = |C| = |P| = 60$, $|C \cap P| = 40$, $|C \cap J| = 30$, $|P \cap J| = 20$ in $|J \cap C \cap P| = 10$.

**V natanko dveh jezikih** programirajo tisti, ki so v preseku nekega para, niso pa v vseh treh:
$$|((J \cap P) \cup (J \cap C) \cup (P \cap C)) \setminus (J \cap P \cap C)|$$
Vsak presek para vsebuje tudi 10 programerjev, ki programirajo v vseh treh jezikih. Ko seštejemo vse tri preseke parov, smo te programerje šteli 3-krat, zato jih 3-krat odštejemo:
$$(30 + 20 + 40) - 3 \cdot 10 = 60$$
V natanko dveh jezikih torej programira **60 programerjev**.

![[Naloga programerji.excalidraw]]

## naloga 3
**V anketi je sodelovalo 100 dijakov. 32 jih zanima matematika, 20 fizika, 45 biologija, 15 matematika in biologija, 7 matematika in fizika, 10 fizika in biologija, 30 pa ne zanima noben od teh treh predmetov. Določi število dijakov, ki jih zanima natanko eden od teh treh predmetov.**

Naj bo $S$ množica vseh dijakov, $M$, $F$ in $B$ pa množice dijakov, ki jih zanima matematika, fizika in biologija.
- $|S| = 100$, $|M| = 32$, $|F| = 20$, $|B| = 45$
- $|M \cap B| = 15$, $|M \cap F| = 7$, $|F \cap B| = 10$
- $|M^c \cap F^c \cap B^c| = 30$

**1. korak: unija prek komplementa.** Dijaki, ki jih ne zanima nič, so po De Morganu $M^c \cap F^c \cap B^c = (M \cup F \cup B)^c$, zato
$$|M \cup F \cup B| = |S| - 30 = 70$$

**2. korak: presek vseh treh iz načela vključitev in izključitev.** Neznanka je samo $|M \cap F \cap B|$:
$$70 = 32 + 20 + 45 - 15 - 7 - 10 + |M \cap F \cap B| = 65 + |M \cap F \cap B|$$
torej je $|M \cap F \cap B| = 5$.

**3. korak: vsako območje „samo ena množica“ posebej.** Od $|M|$ odštejemo oba preseka parov. Pri tem smo presek vseh treh odšteli dvakrat, zato ga enkrat prištejemo:
$$|M \cap F^c \cap B^c| = |M| - |M \cap F| - |M \cap B| + |M \cap F \cap B|$$
- samo matematika: $32 - 7 - 15 + 5 = 15$
- samo fizika: $20 - 7 - 10 + 5 = 8$
- samo biologija: $45 - 15 - 10 + 5 = 25$

Natanko eden od predmetov zanima **$15 + 8 + 25 = 48$ dijakov**.

**Preverba:** natanko dva predmeta zanimata $(7 - 5) + (15 - 5) + (10 - 5) = 17$ dijakov, vsi trije pa $5$. Skupaj $48 + 17 + 5 = 70 = |M \cup F \cup B|$ ✓

**Trik, krajša pot:** z oznakami $S_1 = |M| + |F| + |B|$, $S_2 = $ vsota presekov parov in $S_3 = |M \cap F \cap B|$ velja
$$\text{natanko ena} = S_1 - 2 S_2 + 3 S_3 = 97 - 2 \cdot 32 + 3 \cdot 5 = 48$$
- element v natanko eni množici štejemo v $S_1$ enkrat, v $S_2$ in $S_3$ nič, skupaj $1$
- element v natanko dveh štejemo v $S_1$ dvakrat in v $S_2$ enkrat: $2 - 2 \cdot 1 = 0$
- element v vseh treh štejemo v $S_1$ trikrat, v $S_2$ trikrat in v $S_3$ enkrat: $3 - 2 \cdot 3 + 3 \cdot 1 = 0$

Formula torej šteje točno tiste, ki so v eni sami množici. Podobno je pri nalogi 2 število v **natanko dveh** enako $S_2 - 3 S_3$.

![[Naloga dijaki.excalidraw]]

# Relacije
Množica $R$ je **(dvomestna) relacija**, če je vsak njen element urejen par.
$$R \text{ je relacija} \iff \forall x \in R\ \exists u, v : x = (u, v)$$

Množica $R$ je **(dvomestna) relacija v množici $A$**, če je $R \subseteq A \times A$.

Namesto $(x, y) \in R$ pišemo **$xRy$**.
- primer: namesto $(3, 5) \in\ \leq$ pišemo kar $3 \leq 5$

## zgledi
1. $A = \{e, f, g, h\}$, $R = \{(e, f), (f, g), (g, h)\}$
   - pišemo $eRf$ in ne $(e, f) \in R$
2. $A = \mathbb{N}$, $R = \{(x, y) \,;\, x, y \in \mathbb{N} \land x \leq y\}$
   - $R = \{(0, 0), (0, 1), \dots, (7, 14), \dots\}$: ta množica parov **je** relacija $\leq$
3. $\mathrm{id}_A = \{(x, x) \,;\, x \in A\}$, **identiteta**
   - deluje kot enakost: $1 \,\mathrm{id}_{\mathbb{N}}\, 1$ pomeni $1 = 1$
   - primer: $A = \{0, 1, 2, 3\}$, $\mathrm{id}_A = \{(0, 0), (1, 1), (2, 2), (3, 3)\}$
4. $\emptyset \subseteq A \times A$, **prazna relacija**
5. $U_A = A \times A \subseteq A \times A$, **univerzalna relacija**

## domena in zaloga vrednosti
Naj bo $R$ relacija v $A$.
- **domena** ali **definicijsko območje**: $\mathcal{D}_R = \{x \,;\, \exists y : xRy\}$, torej vsi elementi, iz katerih gre kakšna puščica
- **zaloga vrednosti**: $\mathcal{Z}_R = \{y \,;\, \exists x : xRy\}$, torej vsi elementi, v katere gre kakšna puščica

Zgledi:
- $R = \{(e, f), (f, g), (g, h)\}$: $\mathcal{D}_R = \{e, f, g\}$, $\mathcal{Z}_R = \{f, g, h\}$
- $\leq$ v $\mathbb{N}$: $\mathcal{D}_\leq = \mathbb{N}$, $\mathcal{Z}_\leq = \mathbb{N}$
- $<$ v $\mathbb{N}$: $\mathcal{D}_< = \mathbb{N}$, $\mathcal{Z}_< = \mathbb{N} \setminus \{0\}$, ker ni nobenega $x < 0$
- $>$ v $\mathbb{N}$: $\mathcal{D}_> = \mathbb{N} \setminus \{0\}$, $\mathcal{Z}_> = \mathbb{N}$, ker ni nobenega $y$, da bi bil $0 > y$

## lastnosti relacij
Naj bo $R$ relacija v $A$. Pravimo, da je $R$:
1. **refleksivna** $\iff \forall x \in A : xRx$
   - vsak element je v relaciji sam s sabo
2. **simetrična** $\iff \forall x, y \in A : xRy \Rightarrow yRx$
   - če velja v eno smer, velja tudi v drugo
3. **antisimetrična** $\iff \forall x, y \in A : xRy \land yRx \Rightarrow x = y$
   - v obe smeri sta lahko v relaciji le enaka elementa
4. **tranzitivna** $\iff \forall x, y, z \in A : xRy \land yRz \Rightarrow xRz$
   - iz $x$ v $y$ in iz $y$ v $z$ sledi iz $x$ v $z$
5. **sovisna** $\iff \forall x, y \in A : x \neq y \Rightarrow xRy \lor yRx$
   - vsaka dva različna elementa sta primerljiva
6. **enolična** $\iff \forall x, y, z \in A : xRy \land xRz \Rightarrow y = z$
   - vsak $x$ je v relaciji z največ enim $y$

## zgledi lastnosti
1. relacija $\mathrm{id}_A$ v $A$
2. relacija $\leq$ v $\mathbb{N}$
3. relacija $<$ v $\mathbb{N}$
4. relacija $\subseteq$ v $\mathcal{P}A$
5. relacija „oče“ v množici ljudi: $x$ oče $y$ preberemo kot „$x$ je oče $y$-ona“

|                | refl. | sim. | antisim. | tranz. | sovisna | enolična |
| -------------- | ----- | ---- | -------- | ------ | ------- | -------- |
| $\mathrm{id}_A$ | ✓     | ✓    | ✓        | ✓      | ✗       | ✓        |
| $\leq$         | ✓     | ✗    | ✓        | ✓      | ✓       | ✗        |
| $<$            | ✗     | ✗    | ✓ **!**  | ✓      | ✓       | ✗        |
| $\subseteq$    | ✓     | ✗    | ✓        | ✓      | ✗       | ✗        |
| oče            | ✗     | ✗    | ✓ **!**  | ✗      | ✗       | ✗        |

**Pozor (!):** $<$ in „oče“ sta antisimetrični, ker predpostavka $xRy \land yRx$ **ni nikoli izpolnjena**. Ne more veljati hkrati $x < y$ in $y < x$, prav tako ne more biti $x$ oče $y$ in $y$ oče $x$. Implikacija z neresnično predpostavko je vedno resnična.

## grafična predstavitev relacije
Naj bo $R$ relacija v **končni** množici $A$.
- elemente $A$ narišemo kot **točke** v ravnini
- če velja $aRb$, narišemo **usmerjeno puščico** od $a$ do $b$

Zgled: $A = \{e, f, g, h\}$, $R = \{(e, f), (f, g), (g, h)\}$

![[Graf relacije e f g h.excalidraw]]