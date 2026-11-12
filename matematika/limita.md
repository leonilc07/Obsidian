# Limite

Osnove o zaporedjih (monotonost, omejenost, stekališča) so v [[zaporedja]].

## Definicija limite

$L \in \mathbb{R}$ je **limita** zaporedja $(a_n)_{n\in\mathbb{N}}$, $L = \displaystyle\lim_{n\to\infty} a_n$, če:
$$\forall \varepsilon > 0\ \exists N \in \mathbb{N}\ \forall n > N: |a_n - L| < \varepsilon$$
oziroma $a_n \in (L-\varepsilon, L+\varepsilon)$. Ne glede na to, kako ozek pas okoli $L$ vzamemo, so od nekega člena naprej **vsi** členi v tem pasu.

**Stekališče** (ponovitev): $c$ je stekališče zaporedja $a_n$, če je množica $\{\, n \in \mathbb{N} \mid |a_n - c| < \varepsilon \,\}$ za vsak $\varepsilon > 0$ neskončna.

- Zaporedje ima lahko več stekališč.
- Limita je stekališče (v pasu so vsi členi od $N$ naprej, torej neskončno mnogo).

**Izrek:** monotono in omejeno zaporedje je konvergentno, torej ima limito.

### Primer: $\displaystyle\lim_{n\to\infty} \frac1n = 0$

Vzamemo poljuben $\varepsilon > 0$ in iščemo $N$:
$$\left|\frac1n - 0\right| < \varepsilon \;\Rightarrow\; \frac1n < \varepsilon \;\Rightarrow\; n > \frac1\varepsilon$$
Torej je $N = \left\lceil \frac1\varepsilon \right\rceil$.

Konkretno: za $\varepsilon = 0{,}1$ je $N = 10$. Od $11.$ člena naprej ($\frac{1}{11}, \frac{1}{12}, \dots$) so vsi členi manjši od $0{,}1$. Za $\varepsilon = 0{,}01$ je $N = 100$. Manjši kot je $\varepsilon$, dlje moramo iti, a nek $N$ vedno obstaja.

- $\lceil x \rceil$ je najmanjše celo število, ki je $\ge x$ (zaokrožimo navzgor)
- $\lfloor x \rfloor$ je največje celo število, ki je $\le x$ (zaokrožimo navzdol)

### Primer: $\displaystyle\lim_{n\to\infty} \frac{1}{\log n} = 0$

$$\left|\frac{1}{\log n} - 0\right| < \varepsilon \;\Rightarrow\; \frac{1}{\log n} < \varepsilon \;\Rightarrow\; \log n > \frac1\varepsilon \;\Rightarrow\; 10^{\log n} > 10^{1/\varepsilon} \;\Rightarrow\; n > 10^{1/\varepsilon}$$
Torej je $N = \left\lceil 10^{1/\varepsilon} \right\rceil$.

Ker je $\log n < n$, je $\frac1n < \frac{1}{\log n}$: zaporedje $\frac{1}{\log n}$ gre proti $0$ veliko počasneje kot $\frac1n$. Za $\varepsilon = 0{,}1$ potrebujemo $n > 10^{10}$, pri $\frac1n$ pa je dovolj že $n > 10$.

## Računanje z limitami

Naj bo $\displaystyle\lim_{n\to\infty} a_n = a$ in $\displaystyle\lim_{n\to\infty} b_n = b$. Potem:

1. $\displaystyle\lim_{n\to\infty} (a_n + b_n) = a + b$
2. $\displaystyle\lim_{n\to\infty} (a_n \cdot b_n) = a \cdot b$
3. Če je $b_n \ne 0$ za vse $n$ in $b \ne 0$: $\displaystyle\lim_{n\to\infty} \frac{a_n}{b_n} = \frac ab$
4. Če je $a_n > 0$ za vse $n$ in $a > 0$: $\displaystyle\lim_{n\to\infty} a_n^{b_n} = a^b$

### Dokaz pravila 1

Ker $a_n \to a$, obstaja $N_a$, da je $|a_n - a| < \frac\varepsilon2$ za $n > N_a$. Ker $b_n \to b$, obstaja $N_b$, da je $|b_n - b| < \frac\varepsilon2$ za $n > N_b$. Za $n > \max(N_a, N_b)$ veljata obe neenakosti, zato s trikotniško neenakostjo $|x + y| \le |x| + |y|$:
$$|a_n + b_n - (a+b)| = |(a_n - a) + (b_n - b)| \le |a_n - a| + |b_n - b| < \frac\varepsilon2 + \frac\varepsilon2 = \varepsilon$$

### Primeri

**a)** $a_n = 1$, $b_n = \frac1n$ (pravilo 1):
$$\lim_{n\to\infty} \left(1 + \frac1n\right) = \lim_{n\to\infty} a_n + \lim_{n\to\infty} b_n = 1 + 0 = 1$$

**b)** $a_n = 3$, $b_n = \frac1n$ (pravilo 2):
$$\lim_{n\to\infty} \frac3n = \lim_{n\to\infty} a_n \cdot b_n = 3 \cdot 0 = 0$$
Če bi pisali $\frac{a_n}{b_n}$ z $a_n = 3$ in $b_n = n$, pravila 3 ne moremo uporabiti, ker $\lim b_n$ ne obstaja.

**c)** Izpostavimo najvišjo potenco. Tako v oklepajih ostanejo členi oblike $\frac{\text{število}}{n^k}$, ki gredo proti $0$, $n^2$ pa se pokrajša:
$$\lim_{n\to\infty} \frac{(n+2)^2}{3n^2+n+1} = \lim_{n\to\infty} \frac{n^2+4n+4}{3n^2+n+1} = \lim_{n\to\infty} \frac{n^2\left(1+\frac4n+\frac{4}{n^2}\right)}{n^2\left(3+\frac1n+\frac{1}{n^2}\right)} = \frac13$$

**d)** $a_n = 2$, $b_n = \frac1n$ (pravilo 4):
$$\lim_{n\to\infty} \sqrt[n]{2} = \lim_{n\to\infty} 2^{1/n} = 2^0 = 1$$

**e)** Najprej razvijemo $(1-n)^3$:
$$\lim_{n\to\infty} \frac{(1-n)^3}{1+2n^2+n^3} = \lim_{n\to\infty} \frac{(1-n)(1-2n+n^2)}{1+2n^2+n^3} = \lim_{n\to\infty} \frac{1-2n+n^2-n+2n^2-n^3}{1+2n^2+n^3}$$
$$= \lim_{n\to\infty} \frac{n^3\left(\frac{1}{n^3} - \frac{3}{n^2} + \frac3n - 1\right)}{n^3\left(\frac{1}{n^3} + \frac2n + 1\right)} = \frac{-1}{1} = -1$$

**f)** Delimo s $3^n$:
$$\lim_{n\to\infty} \frac{2^n+3^n}{3^n+1} = \lim_{n\to\infty} \frac{\left(\frac23\right)^n + 1}{1+\frac{1}{3^n}} = \frac{0+1}{1+0} = 1$$

## Izrek o sendviču

Če za vse $n$ velja
$$a_n \le b_n \le c_n \qquad \text{in} \qquad \lim_{n\to\infty} a_n = \lim_{n\to\infty} c_n = a,$$
potem je tudi $\displaystyle\lim_{n\to\infty} b_n = a$.

Zaporedje $b_n$ je "stisnjeno" med $a_n$ in $c_n$. Ker se obe zunanji zaporedji približujeta istemu $a$, nima $b_n$ kam drugam. Uporabimo ga, kadar $b_n$ ne znamo izračunati direktno, znamo pa ga oceniti od spodaj in od zgoraj.

**a)** $0 \le \frac{1}{n^2} \le \frac1n$. Levo je $0$, desno gre $\frac1n \to 0$, zato $\displaystyle\lim_{n\to\infty} \frac{1}{n^2} = 0$.

**b)** $\displaystyle\lim_{n\to\infty} \frac{\sin n}{n}$: ker je $-1 \le \sin n \le 1$, je
$$-\frac1n \le \frac{\sin n}{n} \le \frac1n$$
Obe meji gresta proti $0$, zato $\displaystyle\lim_{n\to\infty} \frac{\sin n}{n} = 0$.

**c)** $\displaystyle\lim_{n\to\infty} \frac{(-1)^n}{\sqrt{n+1}}$:
$$-\frac{1}{\sqrt{n+1}} \le \frac{(-1)^n}{\sqrt{n+1}} \le \frac{1}{\sqrt{n+1}}$$
Obe meji gresta proti $0$, zato je limita $0$.

## Pomembne limite

$$\lim_{n\to\infty} \left(1 + \frac1n\right)^n = e \qquad \lim_{n\to\infty} \left(1 - \frac1n\right)^n = e^{-1}$$

$$\lim_{n\to\infty} \frac{n^k}{n^l} = \begin{cases} 0, & l > k \\ 1, & l = k \\ \text{ne obstaja}, & l < k \end{cases} \qquad \lim_{n\to\infty} q^n = \begin{cases} 0, & q \in (-1, 1) \\ 1, & q = 1 \\ \text{ne obstaja}, & \text{sicer} \end{cases}$$

### $\displaystyle\lim_{n\to\infty} \sqrt[n]{n} = 1$

Naj bo $a_n = n^{1/n}$ in $x_n = n^{1/n} - 1 \ge 0$. Potem je $n^{1/n} = 1 + x_n$ in
$$n = (1 + x_n)^n \ge \frac{n(n-1)}{2}\, x_n^2$$
(iz binomske formule obdržimo samo člen z $x_n^2$, ostali so pozitivni). Od tod:
$$\frac{2}{n-1} \ge x_n^2 \;\Rightarrow\; 0 \le x_n \le \sqrt{\frac{2}{n-1}}$$
Desna stran gre proti $0$, zato po izreku o sendviču $\lim x_n = 0$. Ker je $x_n = a_n - 1$:
$$0 = \lim_{n\to\infty} (a_n - 1) \;\Rightarrow\; \lim_{n\to\infty} a_n = 1$$

## Ali velja $f\left(\lim a_n\right) = \lim f(a_n)$?

Ne vedno. Protiprimer:
$$f(x) = \begin{cases} 1, & x = 0 \\ 0, & x \ne 0 \end{cases} \qquad a_n = \frac1n$$
$$f\left(\lim_{n\to\infty} \frac1n\right) = f(0) = 1, \qquad \lim_{n\to\infty} f\left(\frac1n\right) = \lim_{n\to\infty} 0 = 0$$
Členi $\frac1n$ nikoli niso enaki $0$, zato je $f\left(\frac1n\right)$ vedno $0$. Funkcija pa ima ravno v točki $0$ skok na vrednost $1$, zato dobimo različna rezultata.

## Zadnji komentar na limite: kje je treba paziti

**a) $\dfrac{a_n}{b_n}$, kdaj je limita $0$:** če je $a_n$ konstanta, $b_n$ pa raste čez vse meje, je limita vedno $0$:
$$\frac{\text{konstanta}}{\text{nekaj, kar raste}} \to 0$$
Primer: $\frac5n \to 0$.

**b) $\dfrac{\infty}{\infty}$:** lahko je limita, lahko ni.

- $\dfrac{n^2}{n^2+1}$ ima limito ($1$)
- $\dfrac{n^3}{n^2+1}$ nima limite:
$$\frac{n^3}{n^2+1} = \frac{n^3}{n^2}\cdot\frac{1}{1+\frac{1}{n^2}} = \frac{n}{1+\frac{1}{n^2}}$$
Števec $n$ narašča, imenovalec $1+\frac{1}{n^2}$ pa je omejen (manjši kot $2$), zato ulomek raste čez vse meje.

**c) $\dfrac00$:** lahko je limita, lahko ni. Primer, ko limita je:
$$\frac{\frac{1}{n^2}}{\frac1n} = \frac{n}{n^2} = \frac1n \to 0$$
Primer, ko limite ni (števec in imenovalec gresta oba proti $0$):
$$\frac{\frac{(-1)^n}{n}}{\frac1n} = (-1)^n = -1, 1, -1, 1, \dots$$

**d) $a_n^{b_n}$, kjer $a_n \to \infty$ in $b_n \to \infty$:** $a_n^{b_n} \to \infty$, torej nikoli ni (končne) limite.

**e) $a_n^{b_n}$, kjer $\lim_{n\to\infty} a_n = 0$ in $b_n \to \infty$:** limita je ($0$). Če je $\lim a_n = 0$, bodo od nekega trenutka naprej vsi $a_n$ manjši od $1$, potence pa bodo vedno večje, zato gre $a_n^{b_n} \to 0$.

**f) $a_n^{b_n}$, kjer $a_n \to \infty$ in $\lim_{n\to\infty} b_n = 0$ ($\infty^0$):** limita je ali pa je ni, rezultat je odvisen od tega, kako hitro gresta $a_n$ in $b_n$. Primera, ko limita je, a je vsakič drugačna:

- $a_n = n$, $b_n = \frac1n$: $\;n^{1/n} \to 1$ (dokaz zgoraj)
- $a_n = 2^n$, $b_n = \frac1n$: $\;(2^n)^{1/n} = 2 \to 2$

# Vaje

## Naloga 1: $a_n = \dfrac{2n-1}{n+3}$

**a)** Izračunaj nekaj členov in nariši graf, pomagaj si s funkcijo $y = \frac{2x-1}{x+3}$.
$$a_1 = \frac{2\cdot1-1}{1+3} = \frac14, \qquad a_2 = \frac{2\cdot2-1}{2+3} = \frac35, \qquad a_3 = \frac{2\cdot3-1}{3+3} = \frac56$$

- **Ničla:** $2x - 1 = 0 \Rightarrow x = \frac12$
- **Pol:** $x + 3 = 0 \Rightarrow x = -3$
- **Začetna vrednost:** $y(0) = -\frac13$
- **Asimptota:** $y = 2$

```desmos-graph
left=-10; right=8;
bottom=-6; top=8;
---
y=\frac{2x-1}{x+3}
y=2|dashed
x=-3|dashed
(1,0.25)|label:a₁
(2,0.6)|label:a₂
(3,0.833)|label:a₃
```

**b)** Ali je zaporedje padajoče ali naraščajoče? Preveri z računom.

Zaporedje je naraščajoče, dokazati moramo $a_n \le a_{n+1}$ za vse $n$:
$$a_{n+1} - a_n = \frac{2(n+1)-1}{n+1+3} - \frac{2n-1}{n+3} = \frac{2n+1}{n+4} - \frac{2n-1}{n+3} = \frac{(2n+1)(n+3) - (2n-1)(n+4)}{(n+4)(n+3)}$$
$$= \frac{2n^2+7n+3 - (2n^2+7n-4)}{(n+4)(n+3)} = \frac{7}{(n+4)(n+3)} > 0$$
Torej $a_{n+1} > a_n$.

**c)** Prepričaj se, da je zaporedje monotono in izračunaj limito. Od katerega $n$ naprej ležijo členi v intervalu $\left(L - \frac14, L + \frac14\right)$?

**Dokaz, da limita obstaja:** iz b) vemo, da je zaporedje monotono. Pokažimo še, da je omejeno:

- spodnja meja: $a_1 = \frac14$ (zaporedje narašča, zato so vsi členi $\ge a_1$)
- zgornja meja: $2$ (glej graf). Z računom: $a_n = \frac{2n-1}{n+3} = \frac{2(n+3) - 7}{n+3} = 2 - \frac{7}{n+3} < 2$, ker je $\frac{7}{n+3} > 0$

Po izreku je zaporedje konvergentno, limita obstaja:
$$L = \lim_{n\to\infty} \frac{2n-1}{n+3} = 2$$

Za $\varepsilon = \frac14$ iščemo $n_0$:
$$|a_{n_0} - 2| < \frac14 \;\Rightarrow\; \left|\frac{2n_0-1}{n_0+3} - 2\right| < \frac14 \;\Rightarrow\; \left|\frac{2n_0-1-2(n_0+3)}{n_0+3}\right| < \frac14$$
$$\left|\frac{-7}{n_0+3}\right| < \frac14 \;\Rightarrow\; \frac{7}{n_0+3} < \frac14 \;\Rightarrow\; 28 < n_0 + 3 \;\Rightarrow\; n_0 > 25$$
Torej $n_0 = 26$: od $26.$ člena naprej so vsi členi v intervalu $\left(2 - \frac14, 2 + \frac14\right)$.

## Naloga 2: rekurzivno zaporedje

Rekurzivno zaporedje podamo z začetnim členom in pravilom: $a_0 = a$, $a_{n+1} = f(a_n)$.

Dano je zaporedje $a_0 = 3$, $a_{n+1} = \sqrt{2 + a_n}$.

**a)** Preveri in dokaži, da je zaporedje padajoče in da je $a_n \ge 2$ za vse $n$.
$$a_1 = \sqrt{2 + a_0} = \sqrt{2+3} = \sqrt5, \qquad a_2 = \sqrt{2 + a_1} = \sqrt{2+\sqrt5}$$

**Zaporedje je padajoče** ($a_n \ge a_{n+1}$ za vse $n$), dokaz z indukcijo:

- **Baza** ($n = 0$): $a_0 \ge a_1$, torej $3 \ge \sqrt5$ ✓
- **Indukcijska predpostavka:** $a_n \ge a_{n+1}$
- **Dokazujemo:** $a_{n+1} \ge a_{n+2}$
$$a_n \ge a_{n+1} \quad / +2$$
$$a_n + 2 \ge a_{n+1} + 2 \quad / \sqrt{\ }$$
$$\sqrt{a_n + 2} \ge \sqrt{a_{n+1} + 2} \;\Rightarrow\; a_{n+1} \ge a_{n+2}$$
Korenimo lahko, ker sta obe strani pozitivni in koren ohrani neenakost. Zadnji korak je samo definicija: $\sqrt{a_n + 2} = a_{n+1}$ in $\sqrt{a_{n+1} + 2} = a_{n+2}$.

**Dokažimo $a_n \ge 2$** za vse $n$, z indukcijo:

- **Baza** ($n = 0$): $a_0 \ge 2$, torej $3 \ge 2$ ✓
- **Predpostavka:** $a_n \ge 2$
- **Dokazujemo:** $a_{n+1} \ge 2$
$$a_{n+1} = \sqrt{2 + a_n} \ge \sqrt{2+2} = \sqrt4 = 2$$

**b)** Izračunaj limito, če obstaja.

Ker je zaporedje monotono (padajoče) in omejeno (navzdol z $2$, navzgor z $a_0 = 3$), je konvergentno, torej limita obstaja. Naj bo $L = \lim_{n\to\infty} a_n$. Potem je tudi $\lim a_{n+1} = L$:
$$L = \lim_{n\to\infty} a_{n+1} = \lim_{n\to\infty} \sqrt{2 + a_n} = \sqrt{2 + L}$$
$$L^2 = 2 + L \;\Rightarrow\; L^2 - L - 2 = 0 \;\Rightarrow\; (L-2)(L+1) = 0$$
Rešitvi sta $L_1 = 2$ in $L_2 = -1$. Ker so vsi členi $\ge 2$, $L_2 = -1$ ne pride v poštev, torej je $L = 2$.

## Naloga 3: izračunaj limite

**a)**
$$\lim_{n\to\infty} \frac{n+1}{2n-1} = \lim_{n\to\infty} \frac{n\left(1+\frac1n\right)}{n\left(2-\frac1n\right)} = \frac12$$

**b)**
$$\lim_{n\to\infty} \frac{n^2+2n+2}{1-2n^2} = \lim_{n\to\infty} \frac{n^2\left(1+\frac2n+\frac{2}{n^2}\right)}{n^2\left(\frac{1}{n^2}-2\right)} = \frac{1}{-2} = -\frac12$$

**c)** Razširimo z $\sqrt{n+1} + \sqrt n$:
$$\lim_{n\to\infty} \left(\sqrt{n+1} - \sqrt n\right) = \lim_{n\to\infty} \frac{\left(\sqrt{n+1} - \sqrt n\right)\left(\sqrt{n+1} + \sqrt n\right)}{\sqrt{n+1} + \sqrt n} = \lim_{n\to\infty} \frac{n+1-n}{\sqrt{n+1} + \sqrt n} = \lim_{n\to\infty} \frac{1}{\sqrt{n+1} + \sqrt n} = 0$$

**d)** Izpostavimo $3^n$ zgoraj in $3^{n-1}$ spodaj:
$$\lim_{n\to\infty} \frac{2^{n+1}+3^n}{2^n+3^{n-1}} = \lim_{n\to\infty} \frac{3^n\left(\frac{2^{n+1}}{3^n}+1\right)}{3^{n-1}\left(\frac{2^n}{3^{n-1}}+1\right)} = \lim_{n\to\infty} \frac{3\left(2\left(\frac23\right)^n+1\right)}{3\left(\frac23\right)^n+1} = \frac{3(0+1)}{0+1} = 3$$
