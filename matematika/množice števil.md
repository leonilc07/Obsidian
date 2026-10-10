# Matematični jezik
Deli se na:
- koncepte
- Algoritme
- Mehanike (najbolje delati vaje za to)

# števila
## Naravna števila

**Naravna števila** so števila, s katerimi štejemo:

$$
\mathbb{N} = \{1, 2, 3, 4, \dots\}
$$

Če vključimo še 0, pišemo $\mathbb{N}_0 = \{0, 1, 2, 3, \dots\}$.

### Lastnosti

- **Seštevanje in množenje** dasta spet naravno število: $a, b \in \mathbb{N} \Rightarrow a + b \in \mathbb{N},\ a \cdot b \in \mathbb{N}$.
- **Odštevanje in deljenje** ne dasta vedno naravnega števila: $3 - 5 \notin \mathbb{N}$, $3 : 2 \notin \mathbb{N}$.

### Razširitve števil

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

| Množica | Pomen | Latex Suite |
|-|-|-|
| $\mathbb{N}$ | naravna števila | `NN` |
| $\mathbb{Z}$ | cela števila | `ZZ` |
| $\mathbb{Q}$ | racionalna števila | `QQ` |
| $\mathbb{R}$ | realna števila | `RR` |
| $\mathbb{C}$ | kompleksna števila | `CC` |

### Deljivost in praštevila

- $a \mid b$ pomeni, da $a$ deli $b$, torej $b = a \cdot k$ za neko $k \in \mathbb{Z}$.
- **Sodo število:** $n = 2k$. **Liho število:** $n = 2k + 1$, $k \in \mathbb{Z}$.
- **Praštevilo:** naravno število večje od 1, ki je deljivo samo z 1 in s samim seboj (2, 3, 5, 7, 11, …).

## Cela števila 

**Cela števila** so naravna števila, njihova nasprotna števila:

$$
\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}
$$

**Negativna naravna števila** so nasprotna števila naravnih števil:

$$
\mathbb{N}^- = \{-n \mid n \in \mathbb{N}\} = \{-1, -2, -3, \dots\}
$$

Cela števila so zato unija treh množic:

$$
\mathbb{Z} = \mathbb{N}^-\cup \mathbb{N}
$$

- Seštevanje, odštevanje in množenje celih števil da spet celo število. Deljenje ne vedno: $3 : 2 \notin \mathbb{Z}$.
- Vsako $a \in \mathbb{Z}$ ima nasprotno število $-a \in \mathbb{Z}$, za katero velja $a + (-a) = 0$.

## Racionalna števila

**Racionalna števila** so števila, ki jih lahko zapišemo kot ulomek celega in naravnega števila:

$$
\mathbb{Q} = \left\{ \frac{a}{b} \;\middle|\; a \in \mathbb{Z},\ b \in \mathbb{N},\ b \neq 0 \right\}
$$

- **Enakost ulomkov:** $\dfrac{a}{b} = \dfrac{c}{d} \iff a \cdot d = b \cdot c$. Isto število ima več zapisov, npr. $\frac{1}{2} = \frac{2}{4}$.
- **Cela števila so racionalna:** $a = \frac{a}{1}$, torej $\mathbb{Z} \subset \mathbb{Q}$.
- **Decimalni zapis** racionalnega števila je končen ($\frac{1}{4} = 0{,}25$) ali periodičen ($\frac{1}{3} = 0{,}\overline{3}$).
- Seštevanje, odštevanje, množenje in deljenje z neničelnim številom da spet racionalno število. Zato je $\mathbb{Q}$ prvi sistem števil, v katerem lahko vedno delimo.
- Niso vsa števila racionalna: $\sqrt{2} \notin \mathbb{Q}$.

## Iracionalna števila

**Iracionalna števila** so realna števila, ki niso racionalna, torej jih ni mogoče zapisati kot ulomek $\frac{a}{b}$, $a \in \mathbb{Z}$, $b \in \mathbb{N}$:

$$
\mathbb{I} = \mathbb{R} \setminus \mathbb{Q} = \{ x \in \mathbb{R} \mid x \notin \mathbb{Q} \}
$$

Oznaka $\mathbb{I}$ ni povsod enaka, zato se pogosto piše kar $\mathbb{R} \setminus \mathbb{Q}$.

- Primeri: $\sqrt{2}$, $\pi$, $e$.
- Decimalni zapis je neskončen in neperiodičen.
- Vsota racionalnega in iracionalnega števila je iracionalna. Vsota dveh iracionalnih pa ni nujno iracionalna: $\sqrt{2} + (-\sqrt{2}) = 0$.

## Realna števila

**Realna števila** so vsa racionalna in vsa iracionalna števila skupaj:

$$
\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q}), \qquad \mathbb{Q} \cap (\mathbb{R} \setminus \mathbb{Q}) = \emptyset
$$

Vsako realno število je ali racionalno ali iracionalno, nikoli oboje. Realna števila ustrezajo točkam na številski premici, brez lukenj.

Verigo števil lahko zdaj zaključimo:

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}
$$

## Neskončne decimalke in pretvorba v ulomek

Decimalni zapis racionalnega števila je končen ali periodičen. Obe vrsti lahko pretvorimo v ulomek. Neperiodične neskončne decimalke (npr. $\pi$, $\sqrt{2}$) so iracionalne in jih v ulomek **ni mogoče** pretvoriti.

**Končna decimalka:** zapišemo jo kot ulomek z imenovalcem $10, 100, 1000, \dots$ in krajšamo:

$$
0{,}25 = \frac{25}{100} = \frac{1}{4}
$$

**Periodična decimalka:** ponavljajoči se del (perioda) označimo s črto, npr. $0{,}\overline{36} = 0{,}363636\dots$

### Postopek

1. Decimalko označimo z $x$.
2. $x$ pomnožimo z $10^k$, kjer je $k$ dolžina periode, da se zapisa "poravnata".
3. Odštejemo: neskončni repi so enaki in se uničijo.
4. Rešimo enačbo za $x$ in okrajšamo.

### Primer 1: čista perioda

$$
\begin{align}
x &= 0{,}\overline{36} = 0{,}3636\dots \\
100x &= 36{,}\overline{36} = 36{,}3636\dots \\
100x - x &= 36 \\
99x &= 36 \\
x &= \frac{36}{99} = \frac{4}{11}
\end{align}
$$

### Primer 2: število pred periodo

$$
\begin{align}
x &= 0{,}1\overline{6} = 0{,}1666\dots \\
10x &= 1{,}\overline{6} \\
100x &= 16{,}\overline{6} \\
100x - 10x &= 16 - 1 \\
90x &= 15 \\
x &= \frac{15}{90} = \frac{1}{6}
\end{align}
$$

Pomnožimo dvakrat: prvič, da pride pred decimalno vejico samo neperiodični del, drugič pa še perioda. Potem odštejemo.

### Primer 3: celi del

$$
\begin{align}
x &= 2{,}\overline{45} \\
100x &= 245{,}\overline{45} \\
99x &= 243 \\
x &= \frac{243}{99} = \frac{27}{11}
\end{align}
$$

### Posebnost: $0{,}\overline{9} = 1$

$$
\begin{align}
x &= 0{,}\overline{9} \\
10x &= 9{,}\overline{9} \\
9x &= 9 \\
x &= 1
\end{align}
$$

Torej $0{,}999\dots$ ni "skoraj 1", ampak je **enako** 1. Isto število ima dva decimalna zapisa.

### Bližnjica

- Čista perioda: $0{,}\overline{a_1 a_2 \dots a_k} = \dfrac{a_1 a_2 \dots a_k}{99\dots9}$, v imenovalcu je $k$ devetk. Npr. $0{,}\overline{36} = \frac{36}{99}$.
- Z neperiodičnim delom: števec je (število do konca prve periode) $-$ (število pred periodo), imenovalec pa devetke za periodo in ničle za neperiodični del. Npr. $0{,}1\overline{6} = \frac{16-1}{90}$.

## Dokaz, da je $\sqrt{2}$ iracionalno

Dokazujemo s protislovjem. PREDPOSTAVIMO, da je $\sqrt{2} = \dfrac{a}{b}$, kjer je ulomek okrajšan, $a, b \in \mathbb{N}$.

$$
\begin{align}
2 &= \frac{a^2}{b^2} \\
a^2 &= 2b^2
\end{align}
$$

Torej je $a^2$ sodo, zato je $a$ sodo ($a$ liho $\Rightarrow$ $a^2$ liho). Naj bo $a = 2c$:

$$
\begin{align}
4c^2 &= 2b^2 \\
b^2 &= 2c^2
\end{align}
$$

Zdaj je $b^2$ sodo, zato je $b$ sodo. Oba, $a$ in $b$, sta soda, ulomek pa je okrajšan. To je protislovje, zato je $\sqrt{2}$ iracionalno. $\blacksquare$

## Intervali

Naj bo $a < b$, $a, b \in \mathbb{R}$.

| Ime | Zapis | Množica |
|-|-|-|
| odprti interval | $(a, b)$ | $\{ x \in \mathbb{R} \mid a < x < b \}$ |
| zaprti interval | $[a, b]$ | $\{ x \in \mathbb{R} \mid a \leq x \leq b \}$ |
| levo zaprt, desno odprt | $[a, b)$ | $\{ x \in \mathbb{R} \mid a \leq x < b \}$ |
| levo odprt, desno zaprt | $(a, b]$ | $\{ x \in \mathbb{R} \mid a < x \leq b \}$ |

Okrogli oklepaj pomeni, da krajišče **ni** v intervalu, oglati pa da **je**.

### Neomejeni intervali

$$
(a, \infty) = \{ x \in \mathbb{R} \mid x > a \}, \qquad [a, \infty) = \{ x \in \mathbb{R} \mid x \geq a \}
$$

Podobno $(-\infty, b) = \{ x \in \mathbb{R} \mid x < b \}$ in $(-\infty, b] = \{ x \in \mathbb{R} \mid x \leq b \}$. Cela premica je $\mathbb{R} = (-\infty, \infty)$.

$\infty$ ni število, zato je ob njem **vedno okrogli oklepaj**.

### Presek intervalov

Presek vsebuje števila, ki so v obeh intervalih hkrati. Zgornja meja je manjša izmed zgornjih, spodnja pa večja izmed spodnjih:

$$
(a, b) \cap (c, d) = \left( \max(a, c),\ \min(b, d) \right)
$$

če je $\max(a, c) < \min(b, d)$. Sicer je presek prazna množica $\emptyset$.

Primera:

$$
\begin{align}
(1, 5) \cap (3, 8) &= (3, 5) \\
(1, 3) \cap (3, 5) &= \emptyset
\end{align}
$$

Pri drugem 3 ni v nobenem od njiju (okrogli oklepaj), zato skupnih števil ni.

### Presek in unija z zaprtim intervalom

Vsako število iz $(a, b)$ je tudi v $[a, b]$, torej je $(a, b) \subseteq [a, b]$. Za $A \subseteq B$ velja splošno:

$$
A \cap B = A, \qquad A \cup B = B
$$

Pokažemo za naš primer:

$$
\begin{align}
x \in (a, b) \cap [a, b] &\iff (a < x < b) \text{ in } (a \leq x \leq b) \\
&\iff a < x < b \\
&\iff x \in (a, b)
\end{align}
$$

Drugi pogoj je že posledica prvega, zato ga lahko izpustimo. Torej $(a, b) \cap [a, b] = (a, b)$.

$$
\begin{align}
x \in (a, b) \cup [a, b] &\iff (a < x < b) \text{ ali } (a \leq x \leq b) \\
&\iff a \leq x \leq b \\
&\iff x \in [a, b]
\end{align}
$$

Prvi pogoj je že vsebovan v drugem, zato ostane samo drugi. Torej $(a, b) \cup [a, b] = [a, b]$.

## Ulomki

Velja $b, d \neq 0$ (in $c \neq 0$ pri deljenju).

| Operacija | Formula |
|-|-|
| krajšanje in razširjanje | $\dfrac{a}{b} = \dfrac{a \cdot k}{b \cdot k}, \quad k \neq 0$ |
| seštevanje z istim imenovalcem | $\dfrac{a}{c} + \dfrac{b}{c} = \dfrac{a + b}{c}$ |
| seštevanje | $\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{a \cdot d + b \cdot c}{b \cdot d}$ |
| odštevanje | $\dfrac{a}{b} - \dfrac{c}{d} = \dfrac{a \cdot d - b \cdot c}{b \cdot d}$ |
| množenje | $\dfrac{a}{b} \cdot \dfrac{c}{d} = \dfrac{a \cdot c}{b \cdot d}$ |
| deljenje | $\dfrac{a}{b} : \dfrac{c}{d} = \dfrac{a}{b} \cdot \dfrac{d}{c} = \dfrac{a \cdot d}{b \cdot c}$ |
| enakost ulomkov | $\dfrac{a}{b} = \dfrac{c}{d} \iff a \cdot d = b \cdot c$ |

Pri deljenju ulomek, s katerim delimo, **obrnemo** in množimo.

## Odstotki: podražitev in pocenitev

Odstotek je ulomek s stotico v imenovalcu: $p\,\% = \dfrac{p}{100}$.

- **Podražitev** za $p\,\%$ pomeni množenje cene s faktorjem $\left(1 + \dfrac{p}{100}\right)$.
- **Pocenitev** za $p\,\%$ pomeni množenje cene s faktorjem $\left(1 - \dfrac{p}{100}\right)$.

Naj bo prvotna cena $C$. Cena po pocenitvi in nato podražitvi za $p\,\%$:

$$
C \cdot \left(1 - \frac{p}{100}\right) \cdot \left(1 + \frac{p}{100}\right)
$$

Cena po podražitvi in nato pocenitvi za $p\,\%$:

$$
C \cdot \left(1 + \frac{p}{100}\right) \cdot \left(1 - \frac{p}{100}\right)
$$

Ker je množenje komutativno ($x \cdot y = y \cdot x$), sta obe ceni **enaki**. To velja tudi, če sta odstotka različna ($p$ in $q$):

$$
C \cdot \left(1 - \frac{p}{100}\right) \cdot \left(1 + \frac{q}{100}\right) = C \cdot \left(1 + \frac{q}{100}\right) \cdot \left(1 - \frac{p}{100}\right)
$$

### Zakaj ni prvotna cena

Pri enakem $p$ uporabimo razliko kvadratov $(1-x)(1+x) = 1 - x^2$:

$$
C \cdot \left(1 - \frac{p}{100}\right)\left(1 + \frac{p}{100}\right) = C \cdot \left(1 - \frac{p^2}{10\,000}\right)
$$

To je manj kot $C$. Razlog: drugi odstotek se računa od **druge osnove**.

### Primer: $C = 100$, $p = 20\,\%$

$$
\begin{align}
100 \cdot 0{,}8 \cdot 1{,}2 &= 80 \cdot 1{,}2 = 96 \\
100 \cdot 1{,}2 \cdot 0{,}8 &= 120 \cdot 0{,}8 = 96 \\
100 \cdot \left(1 - \frac{20^2}{10\,000}\right) &= 100 \cdot 0{,}96 = 96
\end{align}
$$

- Najprej pocenitev: $100 \to 80$, nato $20\,\%$ od $80$ je $16$, ne $20$, zato $80 \to 96$.
- Najprej podražitev: $100 \to 120$, nato $20\,\%$ od $120$ je $24$, ne $20$, zato $120 \to 96$.