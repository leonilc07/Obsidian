# Vrste

**Vrsta** je formalna vsota oblike
$$a_1 + a_2 + a_3 + \dots = \sum_{n=1}^{\infty} a_n$$

Če seštejemo samo končno mnogo členov ($n$ je končno število), dobimo **končno vsoto**:
$$a_1 + a_2 + \dots + a_n = \sum_{j=1}^{n} a_j$$

Pri vrsti med člene zaporedja damo $+$. Primeri, prvih 5 členov:

- $a_n = n$: $\;1 + 2 + 3 + 4 + 5$
- $a_n = \frac1n$: $\;1 + \frac12 + \frac13 + \frac14 + \frac15$
- $a_n = (-1)^n$: $\;-1 + 1 - 1 + 1 - 1$
- $a_n = \frac{1}{2^{n-1}}$: $\;1 + \frac12 + \frac14 + \frac18 + \frac{1}{16}$

Zapis s simbolom za vsoto:
$$a_1 + a_2 + a_3 + a_4 + a_5 = \sum_{i=1}^{5} a_i \qquad a_1 + a_2 + \dots + a_{100} = \sum_{i=1}^{100} a_i \qquad a_1 + a_2 + \dots + a_{100} + \dots = \sum_{i=1}^{\infty} a_i$$

## Delne vsote

Kako seštejemo neskončno členov? Tvorimo **zaporedje delnih vsot** $S_n$:

- $S_1 = a_1$
- $S_2 = a_1 + a_2$
- $S_3 = a_1 + a_2 + a_3$
- $S_n = a_1 + a_2 + \dots + a_n = \displaystyle\sum_{i=1}^{n} a_i = S_{n-1} + a_n$

**Vsota vrste** je limita zaporedja delnih vsot:
$$\sum_{n=1}^{\infty} a_n = \lim_{n\to\infty} S_n$$

- **Konvergentna** vrsta: zaporedje delnih vsot je konvergentno (vsota je končna).
- **Divergentna** vrsta: zaporedje delnih vsot ni konvergentno (npr. vsota je $\infty$).

Delne vsote za primere od zgoraj:

- $a_n = \frac{1}{2^{n-1}}$: $S_n = 1, \frac32, \frac74, \frac{15}{8}, \dots$ se vedno bolj približujejo $2$ → **konvergentna**, vsota je $2$
- $a_n = n$: $S_n = 1, 3, 6, 10, \dots$ rastejo čez vse meje → **divergentna** (vsota je $\infty$)
- $a_n = (-1)^n$: $S_n = -1, 0, -1, 0, \dots$ skačejo sem in tja in se ne ustalijo → **divergentna**, čeprav vsota ni $\infty$

Divergentna torej ne pomeni nujno "neskončno", pomeni samo, da delne vsote nimajo limite.

### Kaj točno je $S_n$ in zakaj iščemo njegovo limito

Neskončno členov ne moremo sešteti direktno. Lahko pa za vsak $n$ seštejemo prvih $n$ členov in dobimo eno število, $S_n$. Tako je $S_n$ spet **zaporedje**, torej funkcija $n \mapsto S_n$, ki vsakemu $n$ priredi vsoto prvih $n$ členov (glej [[zaporedja]]). Nato pogledamo, kam gredo te vsote, ko $n$ raste. To je $\lim_{n\to\infty} S_n$, in to je vsota vrste.

**Pozor:** vsota vrste je limita **delnih vsot $S_n$**, ne limita **členov $a_n$**. To sta dve različni zaporedji.

Primer: $a_n = \frac{1}{2^n}$, $n \ge 1$

- **členi** $a_n$: $\frac12, \frac14, \frac18, \frac{1}{16}, \dots \to 0$
- **delne vsote** $S_n$: $\frac12, \frac34, \frac78, \frac{15}{16}, \dots$, v splošnem $S_n = 1 - \frac{1}{2^n} \to 1$

Vsota vrste je torej $1$, čeprav gredo členi proti $0$. Vsak nov člen zapolni polovico tega, kar še manjka do $1$, zato se vsota $1$ približuje, a je nikoli ne preseže.

Če pa bi šli **členi** proti $1$ (npr. $a_n = \frac{n}{n+1}$: $\frac12, \frac23, \frac34, \dots$), bi vsakič prišteli skoraj $1$. Potem je $S_n$ približno $n$ in raste čez vse meje, vrsta divergira. Da je vsota končna, morajo členi iti proti $0$ (glej [[#Kdaj je vrsta konvergentna?]]).

Enako s $100$: $a_n = \frac{100}{2^n}$ da vrsto $50 + 25 + 12{,}5 + 6{,}25 + \dots$

- delne vsote: $S_n = 100 - \frac{100}{2^n}$, torej $50, 75, 87{,}5, 93{,}75, \dots$
- vse so manjše od $100$, a se $100$ poljubno približajo, zato je vsota vrste $100$
- členi pa gredo proti $0$, ne proti $100$

## Premikanje indeksov

Ali začnemo pri $i = 0$ ali $i = 1$, se razlikuje samo za prvi člen:
$$\sum_{i=1}^{\infty} a_i = \sum_{i=0}^{\infty} a_i - a_0$$

Vsoto od $n$ do $m$ dobimo tako, da od vsote od $0$ do $m$ odštejemo vsoto od $0$ do $n-1$:
$$\sum_{i=n}^{m} a_i = \sum_{i=0}^{m} a_i - \sum_{i=0}^{n-1} a_i$$

Primer za $n = 3$: $(0, \dots, m) - (0, \dots, 2) = (3, \dots, m)$

## Geometrijska vrsta

Pri geometrijskem zaporedju je kvocient dveh zaporednih členov stalen, $\frac{a_{n+1}}{a_n} = q$:
$$a_1 + a_1 q + a_1 q^2 + a_1 q^3 + \dots = \sum_{n=0}^{\infty} a_1 q^n$$

- **Konvergentna**, če je $|q| < 1$
- **Divergentna**, če je $|q| \ge 1$ (in $a_1 \ne 0$)
- Če je $|q| < 1$, je vsota:
$$\sum_{n=0}^{\infty} a_1 q^n = \frac{a_1}{1-q}$$

Zakaj divergira pri $|q| \ge 1$?

- $q = 1$: seštevamo vedno isti člen, $a_1 + a_1 + a_1 + \dots \to \infty$
- $q = -1$: $a_1 - a_1 + a_1 - \dots$, delne vsote skačejo med $a_1$ in $0$
- $|q| > 1$: členi postajajo vedno večji, zato ne gredo proti $0$ (glej [[#Kdaj je vrsta konvergentna?]])

Primer: $1 + \frac12 + \frac14 + \frac18 + \dots = \displaystyle\sum_{i=0}^{\infty} \left(\tfrac12\right)^i = \frac{1}{1-\frac12} = 2$

### Izpeljava formule

Množimo $(1-x)$ z vedno daljšimi vsotami, vmesni členi se pokrajšajo:
$$(1-x)(1+x) = 1 - x^2$$
$$(1-x)(1+x+x^2) = 1 + x + x^2 - x(1+x+x^2) = 1 + x + x^2 - x - x^2 - x^3 = 1 - x^3$$
$$(1-x)(1+x+x^2+x^3) = 1 - x^4$$
$$(1-x)(1+x+\dots+x^n) = 1 - x^{n+1}$$

Če je $x \ne 1$, lahko delimo z $(1-x)$:
$$\sum_{i=0}^{n} x^i = \frac{1-x^{n+1}}{1-x}$$

Če je $|x| < 1$, gre $x^{n+1} \to 0$ (vsako množenje s številom, manjšim od $1$, ga zmanjša, npr. $\left(\frac12\right)^{10} \approx 0{,}001$; glej $\lim q^n$ v [[limita]]), zato:
$$\lim_{n\to\infty} \sum_{i=0}^{n} x^i = \lim_{n\to\infty} \frac{1-x^{n+1}}{1-x} = \frac{1}{1-x}$$

Primer končne vsote: $\displaystyle\sum_{i=0}^{n} \left(\tfrac12\right)^i = \frac{1-\left(\frac12\right)^{n+1}}{1-\frac12} = 2\left(1-\left(\tfrac12\right)^{n+1}\right)$

**Povzetek:**

- Če $x \ne 1$: $\displaystyle\sum_{i=0}^{n} x^i = \frac{1-x^{n+1}}{1-x}$
- Če $|x| < 1$: $\displaystyle\sum_{i=0}^{\infty} x^i = \frac{1}{1-x}$

Če je $0 < x < 1$, je vsaka delna vsota manjša od cele vrste:
$$\sum_{i=0}^{n} x^i \le \sum_{i=0}^{\infty} x^i = \frac{1}{1-x}$$
To uporabimo, kadar imamo grdo vsoto in jo želimo oceniti z lepšo. Npr. $\displaystyle\sum_{i=0}^{n} \left(\tfrac12\right)^i$ je za vsak $n$ največ $2$, ne da bi jo morali natančno izračunati.

Če imamo pred vsakim členom še faktor $a$, ga izpostavimo:
$$a + aq + aq^2 + \dots + aq^n = \sum_{i=0}^{n} a q^i = a\sum_{i=0}^{n} q^i = a\,\frac{1-q^{n+1}}{1-q}$$

### Primeri

**a)** Končna in neskončna vsota:
$$\sum_{i=0}^{20} 2\left(\tfrac13\right)^i = 2\sum_{i=0}^{20} \left(\tfrac13\right)^i = 2\cdot\frac{1-\left(\frac13\right)^{21}}{1-\frac13} = 3\left(1-\left(\tfrac13\right)^{21}\right)$$
$$\sum_{i=0}^{\infty} 2\left(\tfrac13\right)^i = 2\cdot\frac{1}{1-\frac13} = 2\cdot\frac{1}{\frac23} = 2\cdot\frac32 = 3$$

**b)** Začetek pri $i = 1$, odštejemo člen za $i = 0$:
$$\sum_{i=1}^{\infty} 2\left(\tfrac13\right)^i = \sum_{i=0}^{\infty} 2\left(\tfrac13\right)^i - 2\left(\tfrac13\right)^0 = 3 - 2 = 1$$

**c)** Začetek pri $i = n$ (za $|x| < 1$):
$$\sum_{i=n}^{\infty} x^i = \sum_{i=0}^{\infty} x^i - \sum_{j=0}^{n-1} x^j = \frac{1}{1-x} - \frac{1-x^n}{1-x} = \frac{1-1+x^n}{1-x} = \frac{x^n}{1-x}$$

**d)** Pozor:
$$\sum_{i=0}^{\infty} 2\left(\tfrac13\right)^i \ne \sum_{i=0}^{\infty} \left(\tfrac23\right)^i$$
Zakaj? $2$ je samo faktor pred potenco, ni del osnove: $2\left(\frac13\right)^i = \frac{2}{3^i}$, $\left(\frac23\right)^i = \frac{2^i}{3^i}$. Prva vrsta je $2 + \frac23 + \frac29 + \dots$, druga $1 + \frac23 + \frac49 + \dots$, torej to nista isti vrsti (čeprav po naključju obe seštejeta v $3$).

**e)**
$$\sum_{j=0}^{\infty} \left(\tfrac{1}{\sqrt3}\right)^j = \frac{1}{1-\frac{1}{\sqrt3}} = \frac{1}{\frac{\sqrt3-1}{\sqrt3}} = \frac{\sqrt3}{\sqrt3-1}$$
Če še racionaliziramo imenovalec (razširimo z $\sqrt3+1$):
$$\frac{\sqrt3}{\sqrt3-1}\cdot\frac{\sqrt3+1}{\sqrt3+1} = \frac{3+\sqrt3}{3-1} = \frac{3+\sqrt3}{2}$$

## Kdaj je vrsta konvergentna?

Če je vsota $\displaystyle\sum_{i=0}^{\infty} a_i$ končna, potem je $\displaystyle\lim_{n\to\infty} a_n = 0$.

Zakaj? $a_n = S_n - S_{n-1}$ in obe delni vsoti gresta proti isti vsoti $S$, zato $a_n \to S - S = 0$.

**Obrat ne velja:** če je $\lim_{n\to\infty} a_n = 0$, to **ne** pomeni, da $\displaystyle\lim_{n\to\infty} \sum_{i=0}^{n} a_i$ obstaja.

- **Harmonična vrsta:** $\displaystyle\sum_{n=1}^{\infty} \frac1n = \infty$, čeprav $\frac1n \to 0$
- $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}$ pa obstaja (členi gredo proti $0$ dovolj hitro)

Zakaj je harmonična vrsta $\infty$? Člene združimo v skupine po $1, 2, 4, 8, \dots$ in vsako skupino ocenimo navzdol z njenim najmanjšim členom:
$$1 + \frac12 + \underbrace{\frac13 + \frac14}_{\ge \frac14+\frac14 = \frac12} + \underbrace{\frac15 + \frac16 + \frac17 + \frac18}_{\ge 4\cdot\frac18 = \frac12} + \dots$$
Vsaka skupina prispeva vsaj $\frac12$, skupin je neskončno, zato vsota raste čez vse meje.

**Alternirajoča vrsta:** če je $a_n$ padajoče, pozitivno in $\lim_{n\to\infty} a_n = 0$, potem $\displaystyle\sum_{i=0}^{\infty} (-1)^i a_i$ obstaja. Delne vsote skačejo enkrat gor, enkrat dol, skoki pa so vedno manjši, zato se ustalijo pri neki vrednosti. Primer:
$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = 1 - \frac12 + \frac13 - \frac14 + \dots = \log_e 2 = \ln 2$$

### Primer: $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{2^n}$ na tri načine

**1. način** – geometrijska vrsta s $q = -\frac12$:
$$\sum_{n=0}^{\infty} \left(-\tfrac12\right)^n = \frac{1}{1-\left(-\frac12\right)} = \frac{1}{1+\frac12} = \frac{1}{\frac32} = \frac23$$

**2. način** – posebej seštejemo sode ($n = 2k$) in lihe ($n = 2l+1$) člene. Pri sodih je $(-1)^{2k} = 1$ (členi so pozitivni), pri lihih $(-1)^{2l+1} = -1$ (členi so negativni):
$$\sum_{k=0}^{\infty} \frac{1}{2^{2k}} - \sum_{l=0}^{\infty} \frac{1}{2^{2l+1}} = \sum_{k=0}^{\infty} \left(\tfrac14\right)^k - \sum_{l=0}^{\infty} \tfrac12\left(\tfrac14\right)^l = \frac{1}{1-\frac14} - \frac12\cdot\frac{1}{1-\frac14} = \frac43 - \frac12\cdot\frac43 = \frac23$$

**3. način** – združimo po dva sosednja člena (sod in lih):
$$\sum_{k=0}^{\infty} \left(\frac{1}{2^{2k}} - \frac{1}{2^{2k+1}}\right) = \sum_{k=0}^{\infty} \frac{1}{2^{2k}}\left(1-\tfrac12\right) = \frac12\sum_{k=0}^{\infty} \left(\tfrac14\right)^k = \frac12\cdot\frac43 = \frac23$$

# Vaje

## Naloga 1: $a_n = \dfrac{1}{n(n+1)}$

**a)** $\displaystyle\lim_{n\to\infty} a_n = \lim_{n\to\infty} \frac{1}{n(n+1)} = \lim_{n\to\infty} \frac{1}{n^2+n} = 0$

**b)** S formulo izrazi $n$-to delno vsoto $S_n$ vrste $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$.

Najprej $\frac{1}{n(n+1)}$ zapišemo kot vsoto **parcialnih ulomkov**:
$$\frac{1}{n(n+1)} = \frac{A}{n} + \frac{B}{n+1} = \frac{A(n+1) + Bn}{n(n+1)}$$
$$1 = A(n+1) + Bn = An + A + Bn = (A+B)n + A$$

Primerjamo koeficiente na obeh straneh. Levo je $1 = 0\cdot n + 1$: pred $n$ je $0$, prost člen je $1$. Zato mora biti $A + B = 0$ in $A = 1$. Torej $A = 1$, $B = -1$:
$$\frac{1}{n(n+1)} = \frac1n - \frac{1}{n+1}$$

Tvorimo $S_n$:

- $S_1 = a_1 = \frac11 - \frac12 = \frac12$
- $S_2 = \left(\frac11 - \frac12\right) + \left(\frac12 - \frac13\right) = \frac23$
- $S_3 = \left(\frac11 - \frac12\right) + \left(\frac12 - \frac13\right) + \left(\frac13 - \frac14\right) = \frac34$

V splošnem se vsi vmesni členi pokrajšajo, ostaneta samo prvi in zadnji:
$$S_n = \left(\tfrac11 - \tfrac12\right) + \left(\tfrac12 - \tfrac13\right) + \dots + \left(\tfrac{1}{n-1} - \tfrac1n\right) + \left(\tfrac1n - \tfrac{1}{n+1}\right) = 1 - \frac{1}{n+1} = \frac{n+1-1}{n+1} = \frac{n}{n+1}$$

**c)** Seštej vrsto $\displaystyle\sum_{n=1}^{\infty} a_n$:
$$\sum_{n=1}^{\infty} a_n = \lim_{n\to\infty} S_n = \lim_{n\to\infty} \frac{n/n}{(n+1)/n} = \lim_{n\to\infty} \frac{1}{1+\frac1n} = \frac{1}{1+0} = 1$$

## Naloga 2: vsote geometrijskih vrst

**Postopek:** zapišemo prvih nekaj členov, $a_1$ je prvi člen, $q$ je kvocient dveh zaporednih členov ($q = \frac{a_2}{a_1}$). Preverimo $|q| < 1$ in vstavimo v $\frac{a_1}{1-q}$.

**a)** $q = \frac14 < 1$, $a_1 = 1$
$$\sum_{n=0}^{\infty} \frac{1}{4^n} = 1 + \frac14 + \frac{1}{4^2} + \frac{1}{4^3} + \dots = \frac{1}{1-\frac14} = \frac{1}{\frac34} = \frac43$$

**b)** $q = \frac13 < 1$, $a_1 = \frac{10}{3}$
$$\sum_{n=1}^{\infty} \frac{10}{3^n} = \frac{10}{3} + \frac{10}{9} + \frac{10}{27} + \dots = \frac{\frac{10}{3}}{1-\frac13} = \frac{\frac{10}{3}}{\frac23} = \frac{30}{6} = 5$$

**c)** $q = \frac{2}{3^2} = \frac29 < 1$, $a_1 = \frac{2^2}{3^3} = \frac{4}{27}$
$$\sum_{n=2}^{\infty} \frac{2^n}{3^{2n-1}} = \frac{2^2}{3^3} + \frac{2^3}{3^5} + \frac{2^4}{3^7} + \dots = \frac{\frac{4}{27}}{1-\frac29} = \frac{\frac{4}{27}}{\frac79} = \frac{4\cdot 9}{27\cdot 7} = \frac{4}{21}$$
Kvocient: števec se pri vsakem členu pomnoži z $2$, imenovalec pa s $3^2$ (eksponent $2n-1$ zraste za $2$), zato $q = \frac{2}{3^2}$. Vrsta se začne pri $n = 2$, zato je $a_1$ člen za $n = 2$.

**d)** $a_1 = \frac32$, $q = \frac23 < 1$
$$\frac32 + 1 + \frac23 + \frac49 + \frac{8}{27} + \dots = \frac{\frac32}{1-\frac23} = \frac{\frac32}{\frac13} = \frac92$$

**e)** $q = \frac{-2}{2^3} = -\frac14$, $|q| < 1$, $a_1 = \frac{-2}{3\cdot 2} = -\frac13$
$$\sum_{n=1}^{\infty} \frac{(-2)^n}{3\cdot 2^{3n-2}} = \frac{-2}{3\cdot 2^1} + \frac{(-2)^2}{3\cdot 2^4} + \frac{(-2)^3}{3\cdot 2^7} + \dots = \frac{-\frac13}{1+\frac14} = \frac{-\frac13}{\frac54} = -\frac{4}{15}$$
Kvocient: števec se pomnoži z $-2$, imenovalec pa z $2^3$ (eksponent $3n-2$ zraste za $3$), zato $q = \frac{-2}{2^3}$.

**f)** Za katere $x \in \mathbb{R}$ vrsta $\displaystyle\sum_{n=1}^{\infty} \left(\frac x2\right)^{3n}$ konvergira?
$$\sum_{n=1}^{\infty} \left(\frac x2\right)^{3n} = \left(\frac x2\right)^3 + \left(\frac x2\right)^6 + \left(\frac x2\right)^9 + \dots$$
$a_1 = \left(\frac x2\right)^3$, $q = \left(\frac x2\right)^3$. Pogoj $|q| < 1$:
$$\left|\left(\frac x2\right)^3\right| < 1$$

- $x \ge 0$: $\left(\frac x2\right)^3 < 1 \Rightarrow \frac x2 < 1 \Rightarrow x < 2$, torej $x \in [0, 2)$
- $x < 0$: $\left(\frac x2\right)^3$ je negativno, zato je absolutna vrednost $-\left(\frac x2\right)^3$: $\;-\left(\frac x2\right)^3 < 1 \Rightarrow \left(\frac x2\right)^3 > -1 \Rightarrow \frac x2 > -1 \Rightarrow x > -2$, torej $x \in (-2, 0)$

Skupaj: $x \in (-2, 2)$. Takrat je vsota:
$$\frac{\left(\frac x2\right)^3}{1-\left(\frac x2\right)^3} = \frac{\frac{x^3}{8}}{\frac{8-x^3}{8}} = \frac{x^3}{8-x^3}$$

Za $x$ iz intervala $(-2, 2)$ vrsta konvergira proti $\frac{x^3}{8-x^3}$, za ostale $x$ pa divergira.

## Naloga 3: $0{,}\overline{12}$ kot ulomek

**Brez vrste:**
$$x = 0{,}\overline{12} \quad / \cdot 100$$
$$100x = 12{,}\overline{12}$$
Odštejemo prvo enačbo od druge:
$$99x = 12 \;\Rightarrow\; x = \frac{12}{99} = \frac{4}{33}$$

**Z geometrijsko vrsto:** $a_1 = \frac{12}{10^2}$, $q = \frac{1}{10^2} < 1$
$$0{,}\overline{12} = 0{,}12 + 0{,}0012 + 0{,}000012 + \dots = \frac{12}{10^2} + \frac{12}{10^4} + \frac{12}{10^6} + \dots = \frac{\frac{12}{100}}{1-\frac{1}{100}} = \frac{\frac{12}{100}}{\frac{99}{100}} = \frac{12}{99} = \frac{4}{33}$$

## Naloga 4: Kochova snežinka

Začnemo z enakostraničnim trikotnikom s stranico $a$ ($n = 0$). V vsakem koraku vsako stranico razdelimo na tretjine in na srednjo tretjino dodamo nov enakostraničen trikotnik. Iz vsake stranice tako nastanejo $4$ nove, vsaka $3$-krat krajša.

### Obseg

Obseg $=$ število stranic $\cdot$ dolžina stranice:

- $O_0 = 3a$
- $O_1 = 3\cdot 4\cdot \frac a3$
- $O_2 = 3\cdot 4\cdot 4\cdot \frac{a}{3^2} = 3\cdot 4^2\cdot \frac{a}{3^2}$
- $O_n = 3\cdot 4^n\cdot \dfrac{a}{3^n} = 3a\left(\dfrac43\right)^n$

Ker je $q = \frac43 > 1$, obseg raste čez vse meje:
$$O = \lim_{n\to\infty} 3a\left(\tfrac43\right)^n = \infty$$

### Ploščina

Ploščina enakostraničnega trikotnika s stranico $a$ je $\frac{a^2\sqrt3}{4}$. V $n$-tem koraku na vsako stranico iz prejšnjega koraka dodamo en trikotnik. Prejšnji korak ima $3\cdot 4^{n-1}$ stranic, vsaka dolga $\frac{a}{3^{n-1}}$, novi trikotnik pa ima stranico tretjino tega, $\frac{a}{3^n}$. Torej v $n$-tem koraku dodamo $3\cdot 4^{n-1}$ trikotnikov s stranico $\frac{a}{3^n}$:

- $P_0 = \dfrac{a^2\sqrt3}{4}$
- $P_1 = P_0 + 3\cdot \dfrac{\left(\frac a3\right)^2\sqrt3}{4}$
- $P_2 = P_1 + 3\cdot 4\cdot \dfrac{\left(\frac{a}{3^2}\right)^2\sqrt3}{4}$
- $P_n = P_{n-1} + 3\cdot 4^{n-1}\cdot \dfrac{\left(\frac{a}{3^n}\right)^2\sqrt3}{4}$

Skupaj:
$$P = \frac{a^2\sqrt3}{4} + \sum_{n=1}^{\infty} 3\cdot 4^{n-1}\cdot \frac{\left(\frac{a}{3^n}\right)^2\sqrt3}{4} = \frac{a^2\sqrt3}{4} + \sum_{n=1}^{\infty} 3\cdot 4^n\cdot 4^{-1}\cdot \frac{\frac{a^2}{9^n}\sqrt3}{4}$$
$$= \frac{a^2\sqrt3}{4} + \frac{3a^2\sqrt3}{16}\sum_{n=1}^{\infty} \frac{4^n}{9^n}$$
Tu smo uporabili $\left(\frac{a}{3^n}\right)^2 = \frac{a^2}{9^n}$ in $4^{n-1} = \frac{4^n}{4}$, nato pa vse, kar ni odvisno od $n$, izpostavili pred vsoto.

To je geometrijska vrsta z $a_1 = \frac49$, $q = \frac49$:
$$P = \frac{a^2\sqrt3}{4} + \frac{3a^2\sqrt3}{16}\cdot \frac{\frac49}{1-\frac49} = \frac{a^2\sqrt3}{4} + \frac{3a^2\sqrt3}{16}\cdot \frac45 = \frac{a^2\sqrt3}{4} + \frac{3a^2\sqrt3}{20} = \frac{8a^2\sqrt3}{20} = \frac{2a^2\sqrt3}{5}$$

Snežinka ima torej **neskončen obseg**, a **končno ploščino** ($\frac85$ ploščine začetnega trikotnika).
