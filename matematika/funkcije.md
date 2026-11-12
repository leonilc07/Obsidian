# Funkcije

**Številska funkcija** $f$ (druga je običajno $g$) vsakemu številu iz definicijskega območja priredi realno število:
$$f: D_f \to \mathbb{R}, \qquad x \mapsto f(x)$$

- $x$ je **neodvisna spremenljivka**
- $D_f$ je **definicijsko območje** (domena): vsi $x$, za katere lahko $f(x)$ izračunamo

**Definicija funkcije:** za vsak $x \in D_f$ mora $f(x)$ imeti **točno eno** vrednost.

Na grafu to pomeni: vsaka navpična premica $x = \text{konst.}$ seka graf največ enkrat. Krožnica $x^2 + y^2 = 1$ zato ni graf funkcije, saj sta npr. pri $x = 0$ dve vrednosti, $y = 1$ in $y = -1$.

## Zaloga vrednosti

**Zaloga vrednosti** (slika, ang. range, image) so vse vrednosti, ki jih funkcija zavzame:
$$Z_f = \{\, f(x) \mid x \in D_f \,\}$$

Primer: $f(x) = \frac12 x^2 + 1$

- $D_f = \mathbb{R}$, ker lahko vsako število kvadriramo
- $Z_f = [1, \infty)$, ker je $x^2 \ge 0$, torej $\frac12 x^2 + 1 \ge 1$. Najmanjšo vrednost $1$ dobimo pri $x = 0$, navzgor pa funkcija raste čez vse meje

```desmos-graph
left=-4; right=4;
bottom=-1; top=6;
---
y=\frac{1}{2}x^2+1
(0,1)|label:1
```

Primer: $f(x) = \sqrt{x-1}$

- $D_f = [1, \infty)$, saj koren negativnega števila ni definiran: $x - 1 \ge 0 \Rightarrow x \ge 1$
- $Z_f = [0, \infty)$, ker je koren vedno $\ge 0$. Vrednost $0$ dobimo pri $x = 1$, z večanjem $x$ pa koren zavzame vse pozitivne vrednosti

```desmos-graph
left=-1; right=8;
bottom=-1; top=3;
---
y=\sqrt{x-1}
(1,0)|label:1
```

## Graf funkcije

**Graf funkcije** je množica točk v ravnini, kjer $x$ teče po vseh točkah iz $D_f$:
$$\Gamma(f) = \{\, (x, f(x)) \mid x \in D_f \,\}$$

Primer: za $f(x) = \frac12 x^2 + 1$ je $f(2) = 3$, zato točka $(2, 3)$ leži na grafu. Točka $(2, 5)$ pa ne, ker $f(2) \ne 5$.

## Logaritem

Logaritem je obratna operacija potenciranja:
$$a^x = b \quad \Leftrightarrow \quad \log_a b = x$$
Logaritem odgovori na vprašanje: na katero potenco moramo dvigniti $a$, da dobimo $b$?

- $\log_2 8 = 3$, ker je $2^3 = 8$
- $\log_3 \frac19 = -2$, ker je $3^{-2} = \frac19$

Če osnove ne napišemo, je osnova $10$: $\log b = x \Rightarrow 10^x = b$. Npr. $\log 100 = 2$, ker je $10^2 = 100$.

$f(x) = \log_e(x) = \ln x$ (osnova je $e \approx 2{,}718$)

- $D_f = (0, \infty)$, ker lahko logaritem izračunamo samo iz pozitivnih števil. Potenca $e^x$ je vedno pozitivna, zato ni nobenega $x$, za katerega bi bilo $e^x = 0$ ali $e^x = -1$

```desmos-graph
left=-1; right=6;
bottom=-3; top=3;
---
y=\ln(x)
(1,0)|label:1
```

## Naraščanje in padanje

**Funkcija narašča**, če:
$$x_1 \le x_2 \;\Rightarrow\; f(x_1) \le f(x_2)$$

**Funkcija pada**, če:
$$x_1 \le x_2 \;\Rightarrow\; f(x_1) \ge f(x_2)$$

Funkcija narašča, če se z večanjem $x$ vrednost $f(x)$ ne zmanjša (graf gre od leve proti desni navzgor). Funkcija pada, če se z večanjem $x$ vrednost ne poveča (graf gre navzdol). Npr. $f(x) = x + 0{,}5$ narašča, $f(x) = -x$ pada.

Konstantna funkcija $f(x) = 1$ po teh definicijah hkrati narašča in pada, ker je $f(x_1) = f(x_2)$, kar izpolni tako $\le$ kot $\ge$.

```desmos-graph
left=-3; right=3;
bottom=-3; top=3;
---
y=x+0.5
(-1.5,-1)|label:f(x₁)
(1.5,2)|label:f(x₂)
x=-1.5|-1<y<0|dashed
x=1.5|0<y<2|dashed
```

## Soda in liha funkcija

**Liha funkcija:** za vsak $x \in D_f$ velja $f(-x) = -f(x)$. Graf je simetričen glede na izhodišče.

- Primera: $f(x) = x$, $f(x) = x^3$
- Preverba za $x^3$: $f(-x) = (-x)^3 = -x^3 = -f(x)$ ✓
- Če točka $(x, y)$ leži na grafu, leži na njem tudi $(-x, -y)$, npr. pri $x^3$ točki $(2, 8)$ in $(-2, -8)$

```desmos-graph
left=-2; right=2;
bottom=-2; top=2;
---
y=x
y=x^3|dashed
```

**Soda funkcija:** za vsak $x \in D_f$ velja $f(-x) = f(x)$. Graf je simetričen glede na $y$ os.

- Primeri: $f(x) = |x|$, $f(x) = x^2$, $f(x) = \cos(x)$
- Preverba za $x^2$: $f(-x) = (-x)^2 = x^2 = f(x)$ ✓, enako $|-x| = |x|$
- Če točka $(x, y)$ leži na grafu, leži na njem tudi $(-x, y)$, npr. pri $x^2$ točki $(2, 4)$ in $(-2, 4)$

Funkcija je lahko tudi **ne soda ne liha**, npr. $f(x) = x + 1$: $f(-1) = 0$, $f(1) = 2$, kar ni niti enako niti nasprotno.

```desmos-graph
left=-3; right=3;
bottom=-1.5; top=3;
---
y=|x|
y=x^2|dashed
y=\cos(x)|dotted
```
