# Zaporedja

**Zaporedje** je funkcija $a: \mathbb{N} \to \mathbb{R}$, ki vsakemu naravnemu številu $n$ priredi število $a_n$ (n-ti člen). Zapišemo ga kot $(a_n)_{n\in\mathbb{N}} = a_1, a_2, a_3, \dots$

Zaporedje lahko podamo na dva glavna načina:

- **Eksplicitno** – s formulo za splošni člen $a_n$, ki je odvisna samo od $n$. Vsak člen izračunamo direktno, brez poznavanja prejšnjih.
- **Rekurzivno** – podamo začetni člen (ali več njih) in pravilo, kako iz prejšnjega člena dobimo naslednjega: $a_{n+1} = f(a_n)$. Za izračun $a_{10}$ moramo poznati $a_9$, za tega $a_8$ itd.

## Primer: $a_n = \dfrac{n-1}{n+1}$

Prvi členi: $0, \dfrac{1}{3}, \dfrac{2}{4}, \dfrac{3}{5}, \dfrac{4}{6}, \dots$

**Eksplicitno:**
$$a_n = \frac{n-1}{n+1}$$

**Rekurzivno:** iz $a_n = \frac{n-1}{n+1}$ izrazimo $n$:
$$a_n(n+1) = n-1 \;\Rightarrow\; n = \frac{1+a_n}{1-a_n}$$

To vstavimo v $a_{n+1} = \frac{n}{n+2}$:
$$a_{n+1} = \frac{\frac{1+a_n}{1-a_n}}{\frac{1+a_n}{1-a_n} + 2} = \frac{1+a_n}{1+a_n + 2 - 2a_n}$$

Torej:
$$a_1 = 0, \qquad a_{n+1} = \frac{1+a_n}{3-a_n}$$

**Preverba:** $a_2 = \frac{1+0}{3-0} = \frac{1}{3}$, $\;a_3 = \frac{1+\frac13}{3-\frac13} = \frac{\frac43}{\frac83} = \frac{1}{2} = \frac{2}{4}$ ✓

## Aritmetično zaporedje

- **Eksplicitno:** $a_n = a_1 + (n-1)d$
- **Rekurzivno:** $a_{n+1} = a_n + d$
- **Primera:** $2, 5, 8, 11, \dots$ ($a_1 = 2,\ d = 3$); $\;10, 8, 6, 4, \dots$ ($a_1 = 10,\ d = -2$)

## Geometrijsko zaporedje

- **Eksplicitno:** $a_n = a_1 \cdot q^{n-1}$
- **Rekurzivno:** $a_{n+1} = a_n \cdot q$
- **Primera:** $3, 6, 12, 24, \dots$ ($a_1 = 3,\ q = 2$); $\;1, -\frac12, \frac14, -\frac18, \dots$ ($a_1 = 1,\ q = -\frac12$)

## Fibonaccijevo zaporedje

- **Rekurzivno:** $F_1 = F_2 = 1,\ F_{n+2} = F_{n+1} + F_n$
- **Primera:** $1, 1, 2, 3, 5, 8, \dots$ (začetek $1, 1$); $\;2, 1, 3, 4, 7, 11, \dots$ (Lucasovo, začetek $2, 1$)

## Lastnosti: monotonost

- **Naraščajoče:** $\forall n \in \mathbb{N}: a_n \le a_{n+1}$ — npr. $1, 1, 2, 3, 5, \dots$ (Fibonacci); $\;1, 1, 2, 2, 3, 3, \dots$
- **Strogo naraščajoče:** $\forall n \in \mathbb{N}: a_n < a_{n+1}$ — npr. $a_n = 2n$: $2, 4, 6, \dots$; $\;a_n = \frac{n-1}{n+1}$: $0, \frac13, \frac12, \dots$
- **Padajoče:** $\forall n \in \mathbb{N}: a_n \ge a_{n+1}$ — npr. $5, 5, 4, 4, 3, 3, \dots$; $\;a_n = 7$: $7, 7, 7, \dots$
- **Strogo padajoče:** $\forall n \in \mathbb{N}: a_n > a_{n+1}$ — npr. $a_n = \frac1n$: $1, \frac12, \frac13, \dots$; $\;a_n = -n$: $-1, -2, -3, \dots$

## Lastnosti: omejenost

Omejenost pove, ali členi zaporedja ostanejo znotraj nekega območja, ali pa lahko zrastejo (ali padejo) poljubno daleč.

### Navzgor omejeno

$$\exists M \in \mathbb{R}\ \forall n \in \mathbb{N}: a_n \le M$$

Obstaja število $M$, nad katerega noben člen ne seže. Takemu $M$ rečemo **zgornja meja**. Zgornja meja ni ena sama: če je $M$ zgornja meja, je tudi vsako večje število (npr. $M+1$) zgornja meja. Zato je definicija ekvivalentna tudi z $a_n < M+1$.

- **Primera:** $a_n = \frac{n-1}{n+1}$, ki je vedno $< 1$, zato je $M = 1$; $\;a_n = -n$: $-1, -2, -3, \dots$, $M = -1$
- **Ni navzgor omejeno:** $a_n = 2n$, saj za vsak $M$ najdemo $n$ z $2n > M$

### Navzdol omejeno

$$\exists m \in \mathbb{R}\ \forall n \in \mathbb{N}: a_n \ge m$$

Obstaja število $m$, pod katerega noben člen ne pade. Takemu $m$ rečemo **spodnja meja**. Tudi tu je vsako manjše število (npr. $m-1$) spet spodnja meja.

- **Primera:** $a_n = 2n$: $2, 4, 6, \dots$, $m = 2$; $\;a_n = \frac1n$: $1, \frac12, \frac13, \dots$, vsi členi so $> 0$, $m = 0$
- **Ni navzdol omejeno:** $a_n = -n$, ki pada čez vse meje

### Omejeno

Zaporedje je **omejeno**, če je hkrati navzgor in navzdol omejeno:

$$\exists m, M \in \mathbb{R}\ \forall n \in \mathbb{N}: m \le a_n \le M$$

Vsi členi torej ležijo na intervalu $[m, M]$. Ekvivalentno lahko zapišemo z absolutno vrednostjo: $\exists M > 0\ \forall n \in \mathbb{N}: |a_n| \le M$.

- **Primera:** $a_n = \frac{n-1}{n+1}$ leži na $[0, 1]$; $\;a_n = (-1)^n$: $-1, 1, -1, 1, \dots$ leži na $[-1, 1]$
- **Opomba:** Monotono naraščajoče zaporedje je vedno navzdol omejeno s prvim členom ($m = a_1$), padajoče pa navzgor omejeno ($M = a_1$).

## Stekališče

Število $s$ je **stekališče** zaporedja $(a_n)$, če se okoli njega nabira neskončno mnogo členov, ne glede na to, kako ozko okolico okoli $s$ vzamemo.

$$\forall \varepsilon > 0: \text{ na intervalu } (s-\varepsilon,\ s+\varepsilon) \text{ leži neskončno mnogo členov } a_n$$

**Formalno:** $\forall \varepsilon > 0\ \forall n_0 \in \mathbb{N}\ \exists n \ge n_0: |a_n - s| < \varepsilon$. Ne glede na to, kako daleč v zaporedje greš ($n_0$), vedno najdeš še kak člen v pasu, torej jih je v pasu neskončno mnogo. ($|a_n - s| < \varepsilon$ pomeni isto kot $a_n \in (s-\varepsilon, s+\varepsilon)$.)

### Kako preveriš, ali je $s$ stekališče

1. Izbereš kandidata $s$: število na realni osi, ki ni nujno člen zaporedja.
2. Okoli $s$ vzameš pas $(s-\varepsilon, s+\varepsilon)$. $\varepsilon$ je **polmer** pasu, torej kako daleč od $s$ še gledaš.
3. Pogledaš, ali je v pasu neskončno mnogo členov.
4. To mora veljati za **vsak** $\varepsilon > 0$, tudi poljubno majhen. Če najdeš en sam $\varepsilon$, pri katerem je v pasu le končno mnogo členov (ali nobeden), $s$ **ni** stekališče.

**Pozor:**
- Šteje **število členov** (indeksov $n$), ne število različnih vrednosti. Pri $(-1)^n$ sta le dve vrednosti, a vrednost $1$ se ponovi neskončnokrat.
- Členi lahko $s$ **dosežejo** (so enaki $s$) ali pa se mu le približujejo. Oboje je v redu.

### Primer: $a_n = (-1)^n$

$-1, 1, -1, 1, \dots$

- $s = 1$: v vsakem pasu $(1-\varepsilon, 1+\varepsilon)$ ležijo vsi sodi členi $a_2, a_4, a_6, \dots$ → neskončno mnogo → **stekališče**
- $s = -1$: enako za vse lihe člene $a_1, a_3, a_5, \dots$ → **stekališče**
- $s = 0$: za $\varepsilon = \frac12$ v pasu $(-\frac12, \frac12)$ ni nobenega člena → **ni stekališče**
- Vsak drug $s$: vzameš tako majhen $\varepsilon$, da pas ne zajame niti $1$ niti $-1$ → ni stekališče

Zaporedje ima torej natanko dve stekališči: **$-1$ in $1$**.

### Še nekaj primerov

- $a_n = \frac1n$: $1, \frac12, \frac13, \dots$ ima stekališče $0$ (členi se mu približujejo, a ga nikoli ne dosežejo)
- $a_n = (-1)^n \frac{n}{n+1}$: $-\frac12, \frac23, -\frac34, \frac45, \dots$ ima stekališči $-1$ in $1$
- $a_n = 7$ ima stekališče $7$ (vsi členi so točno $7$)
- $a_n = 2n$: $2, 4, 6, \dots$ nima stekališča, ker členi bežijo v neskončnost in okoli nobenega števila jih ni neskončno mnogo

**Povezava z omejenostjo:** vsako omejeno zaporedje ima vsaj eno stekališče (Bolzano-Weierstrassov izrek).

## Limita zaporedja

Število $L$ je **limita** zaporedja $(a_n)$, če se členi, ko gre $n$ proti neskončnosti, približajo $L$ in tam tudi ostanejo. Ne glede na to, kako ozek pas $(L-\varepsilon, L+\varepsilon)$ okoli $L$ vzamemo, so od nekega člena naprej v njem **vsi** členi.

$$\lim_{n\to\infty} a_n = L \iff \forall \varepsilon > 0\ \exists N \in \mathbb{N}\ \forall n \ge N: |a_n - L| < \varepsilon$$

### Branje definicije po delih

- $\forall \varepsilon > 0$: za vsako širino pasu okoli $L$, tudi poljubno majhno,
- $\exists N \in \mathbb{N}$: obstaja indeks $N$,
- $\forall n \ge N$: da so vsi členi od $N$-tega naprej
- $|a_n - L| < \varepsilon$: od $L$ oddaljeni manj kot $\varepsilon$, torej v pasu $(L-\varepsilon, L+\varepsilon)$.

$N$ je odvisen od $\varepsilon$: ožji kot je pas, dlje v zaporedje moraš iti, da so vsi členi v njem.

### Zapis

- $\lim\limits_{n\to\infty} a_n = L$ beremo: "limita $a_n$, ko gre $n$ proti neskončnosti, je $L$".
- $n \to \infty$ pove, da gledamo, kaj se dogaja s členi, ko $n$ raste čez vse meje (vedno dlje v zaporedju). Za $n$ ne vstavimo $\infty$, ker neskončnost ni število.
- Krajše pišemo tudi $a_n \to L$ ("$a_n$ gre proti $L$").
- Zaporedje, ki ima limito, je **konvergentno**, zaporedje brez limite pa **divergentno**.

### Primer: $\lim\limits_{n\to\infty} \frac1n = 0$

Členi $1, \frac12, \frac13, \frac14, \dots$ se bližajo $0$, zato je kandidat $L = 0$. Pokazati moramo: za vsak $\varepsilon > 0$ najdemo $N$, da je $|a_n - 0| < \varepsilon$ za vse $n \ge N$.

1. Vzamemo poljuben $\varepsilon > 0$.
2. Pogoj poenostavimo: $|\frac1n - 0| = \frac1n$, ker je $n > 0$. Iščemo torej $n$, za katere je $\frac1n < \varepsilon$.
3. Neenačbo preoblikujemo: $\frac1n < \varepsilon \iff 1 < \varepsilon n \iff n > \frac1\varepsilon$. Množimo z $n$ in delimo z $\varepsilon$; oba sta pozitivna, zato se znak ne obrne.
4. Za $N$ vzamemo katerokoli naravno število, večje od $\frac1\varepsilon$. Potem za vsak $n \ge N$ velja $n \ge N > \frac1\varepsilon$, zato $\frac1n < \varepsilon$. ✓
5. Ker tak $N$ najdemo za vsak $\varepsilon$, je $\lim\limits_{n\to\infty} \frac1n = 0$.

**Konkretno:**
- $\varepsilon = 0{,}1$: $\frac1\varepsilon = 10$, vzamemo $N = 11$. Od $a_{11} = \frac1{11} \approx 0{,}09$ naprej so vsi členi manjši od $0{,}1$.
- $\varepsilon = 0{,}01$: $\frac1\varepsilon = 100$, vzamemo $N = 101$.

Ožji pas pomeni večji $N$.

### Še primeri

- $a_n = 7$: limita je $7$, saj je $|7 - 7| = 0 < \varepsilon$ za vse $n$ ($N = 1$). Členi so lahko tudi točno enaki $L$.
- $a_n = \frac{n-1}{n+1}$: limita je $1$. Velja $|\frac{n-1}{n+1} - 1| = \frac{2}{n+1} < \varepsilon \iff n > \frac2\varepsilon - 1$, torej za $N$ vzamemo naravno število, večje od $\frac2\varepsilon - 1$.
- $a_n = 2n$: nima limite (divergentno), ker členi rastejo čez vse meje in ne ostanejo v nobenem pasu.
