# Funkcije

**Funkcija** je predpis, ki vsakemu $x \in D_f \subseteq \mathbb{R}$ priredi natanko eno število $f(x) \in \mathbb{R}$.

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

## Kako izračunamo definicijsko območje

Iščemo vse $x$, pri katerih je predpis smiseln. Pogoji, na katere pazimo:

- **Polinom** (npr. $x^2 - 2x + 1$): ni omejitev, $D_f = \mathbb{R}$
- **Ulomek** $\frac{p(x)}{q(x)}$: imenovalec ne sme biti $0$, torej $q(x) \ne 0$
- **Sodi koren** $\sqrt[2n]{g(x)}$ ($\sqrt{\ }$, $\sqrt[4]{\ }$, ...): pod korenom mora biti **nenegativno**, $g(x) \ge 0$
- **Lihi koren** $\sqrt[3]{g(x)}$, $\sqrt[5]{g(x)}$, ...: definiran za **vsa** realna števila (npr. $\sqrt[3]{-8} = -2$), paziti moramo le na to, kar je znotraj
- **Logaritem** $\log_a g(x)$: argument mora biti **strogo pozitiven**, $g(x) > 0$
- **Vsota ali produkt** več izrazov: $D_f$ je **presek** območij posameznih delov (veljati morajo vsi pogoji hkrati)

Pri logaritmih si pomagamo z zvezo $\log_a x = b \Leftrightarrow x = a^b$.

### Primeri iz vaj

**a)** $f(x) = x^2 - 2x + 1$

- Polinom, zato $D_f = \mathbb{R}$

**b)** $f(x) = \sqrt{-x^2 - x + 2}$

- Sodi koren, zato mora biti $-x^2 - x + 2 \ge 0$
- Pomnožimo z $-1$ (obrne se neenačaj): $x^2 + x - 2 \le 0$
- Razstavimo: $(x - 1)(x + 2) \le 0$, ničli sta $x = 1$ in $x = -2$
- Parabola je obrnjena navzgor, zato je $\le 0$ med ničlama
- $D_f = [-2, 1]$

```desmos-graph
left=-4; right=3;
bottom=-3; top=3;
---
y=x^2+x-2|dashed
y=\sqrt{-x^2-x+2}
(-2,0)|label:-2
(1,0)|label:1
```

**c)** $f(x) = \dfrac{x}{2x^2 - 8}$

- Imenovalec ne sme biti $0$: $2x^2 - 8 = 0 \Rightarrow 2(x^2 - 4) = 0 \Rightarrow 2(x-2)(x+2) = 0$
- Prepovedani sta $x = 2$ in $x = -2$
- $D_f = \mathbb{R} \setminus \{-2, 2\}$

**d)** $f(x) = \log_2\big(\log_3(\log_4 x)\big)$

Pogoje rešujemo od znotraj navzven, vsak logaritem mora imeti pozitiven argument:

- $\log_4 x$: $x > 0$
- $\log_3(\log_4 x)$: $\log_4 x > 0 \Rightarrow x > 4^0 \Rightarrow x > 1$
- $\log_2(\log_3(\log_4 x))$: $\log_3(\log_4 x) > 0 \Rightarrow \log_4 x > 3^0 = 1 \Rightarrow x > 4^1 \Rightarrow x > 4$
- Presek pogojev $x > 0$, $x > 1$, $x > 4$ je $D_f = (4, \infty)$

**f)** $f(x) = \sqrt{-x} + \log(4 + x)$

- Koren: $-x \ge 0 \;/\cdot(-1) \Rightarrow x \le 0$
- Logaritem: $4 + x > 0 \Rightarrow x > -4$
- Presek obeh pogojev: $D_f = (-4, 0]$ (pri $-4$ okrogel oklepaj, ker je pogoj strog, pri $0$ oglat)

**g)** $f(x) = \log\left(\dfrac{2 + x}{2 - x}\right)$

- Pogoj $\frac{2+x}{2-x} > 0$. Ulomek je pozitiven, če sta števec in imenovalec **istega predznaka**, zato ločimo dva primera:
- Oba pozitivna: $2 + x > 0$ **in** $2 - x > 0 \Rightarrow x > -2$ in $x < 2 \Rightarrow x \in (-2, 2)$
- Oba negativna: $2 + x < 0$ **in** $2 - x < 0 \Rightarrow x < -2$ in $x > 2$, kar nima preseka (ni rešitve)
- $D_f = (-2, 2)$

**h)** $f(x) = \sqrt[3]{\dfrac{2}{x - 3}}$

- Lihi koren je definiran povsod, paziti moramo le na ulomek: $x - 3 \ne 0 \Rightarrow x \ne 3$
- $D_f = \mathbb{R} \setminus \{3\}$

## Graf funkcije

**Graf funkcije** je množica točk v ravnini, kjer $x$ teče po vseh točkah iz $D_f$:
$$\Gamma(f) = \{\, (x, f(x)) \mid x \in D_f \,\}$$

Primer: za $f(x) = \frac12 x^2 + 1$ je $f(2) = 3$, zato točka $(2, 3)$ leži na grafu. Točka $(2, 5)$ pa ne, ker $f(2) \ne 5$.

Pri risanju grafa si pomagamo z:

- **ničlami**: $f(x) = 0$ (kje graf seka os $x$)
- **začetno vrednostjo**: $f(0)$ (kje graf seka os $y$)
- **poli**: točke, kjer je imenovalec $0$ (navpične asimptote)
- **vodoravno asimptoto**: $\lim_{x \to \infty} f(x)$

## Logaritem

Logaritem je obratna operacija potenciranja:
$$a^x = b \quad \Leftrightarrow \quad \log_a b = x$$
Logaritem odgovori na vprašanje: na katero potenco moramo dvigniti $a$, da dobimo $b$?

- $\log_2 8 = 3$, ker je $2^3 = 8$
- $\log_3 \frac19 = -2$, ker je $3^{-2} = \frac19$

Če osnove ne napišemo, je osnova $10$: $\log b = x \Rightarrow 10^x = b$. Npr. $\log 100 = 2$, ker je $10^2 = 100$.

$f(x) = \log_e(x) = \ln x$ (osnova je $e \approx 2{,}718$)

- $D_f = (0, \infty)$, ker lahko logaritem izračunamo samo iz pozitivnih števil. Potenca $e^x$ je vedno pozitivna, zato ni nobenega $x$, za katerega bi bilo $e^x = 0$ ali $e^x = -1$

**Pravilo za potenco:** $r \cdot \log_a x = \log_a (x^r)$. Npr. $-\log(2 - x) = \log\big((2-x)^{-1}\big) = \log\frac{1}{2-x}$.

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

## Injektivnost, surjektivnost, bijektivnost

**Injektivna funkcija:** $f: D_f \to \mathbb{R}$ je injektivna, če za vsaka $x_1, x_2 \in D_f$ velja:
$$x_1 \ne x_2 \;\Rightarrow\; f(x_1) \ne f(x_2)$$
oziroma enakovredno (to obliko uporabljamo pri dokazovanju):
$$f(x_1) = f(x_2) \;\Rightarrow\; x_1 = x_2$$

- Različni $x$ dajo različne vrednosti, nobena vrednost se ne ponovi
- **Na grafu:** graf injektivne funkcije seka vsako vodoravnico v **največ eni** točki
- **Kako preverimo:** nastavimo $f(x_1) = f(x_2)$ in računamo. Če pridemo do $x_1 = x_2$, je injektivna. Če dobimo še kakšno drugo možnost (npr. $x_1 = -x_2$), ni

**Surjektivna funkcija:** $f: D_f \to \mathbb{R}$ je surjektivna, če je $Z_f = \mathbb{R}$ (zaloga vrednosti, torej množica vseh slik, je cela kodomena).

- **Na grafu:** graf surjektivne funkcije seka vsako vodoravnico v **vsaj eni** točki

**Bijektivna funkcija:** je hkrati injektivna in surjektivna.

- **Na grafu:** graf bijektivne funkcije seka vsako vodoravnico v **natanko eni** točki

## Inverzna funkcija

**Inverzna funkcija** funkcije $f: D_f \to \mathbb{R}$ je taka funkcija $f^{-1}$, da za vsak $x \in D_f$ velja:
$$(f^{-1} \circ f)(x) = x$$

- $f^{-1}$ "razveljavi" to, kar naredi $f$: če $f$ pošlje $x$ v $y$, $f^{-1}$ pošlje $y$ nazaj v $x$
- Inverz **obstaja le za injektivne funkcije** (če bi dva $x$ šla v isti $y$, ne bi vedeli, kam $y$ vrniti)
- Definicijsko območje in zaloga vrednosti zamenjata vlogi:
$$D_{f^{-1}} = Z_f, \qquad Z_{f^{-1}} = D_f$$
- **Graf** $f^{-1}$ dobimo tako, da graf $f$ **prezrcalimo čez simetralo lihih kvadrantov** $y = x$

**Postopek računanja inverza:**

1. Zapišemo $y = f(x)$
2. **Zamenjamo** $x$ in $y$
3. Iz dobljene enačbe **izrazimo** $y$; to je $f^{-1}(x)$

### Primer: $f(x) = \dfrac{x+1}{2x-3}$

**Definicijsko območje:** $2x - 3 \ne 0 \Rightarrow x \ne \frac32$, torej $D_f = \mathbb{R} \setminus \{\frac32\}$

**Ali je injektivna?** Vzamemo $x_1, x_2 \in D_f$ in nastavimo $f(x_1) = f(x_2)$:
$$\frac{x_1+1}{2x_1-3} = \frac{x_2+1}{2x_2-3}$$
$$(x_1+1)(2x_2-3) = (x_2+1)(2x_1-3)$$
$$2x_1x_2 - 3x_1 + 2x_2 - 3 = 2x_1x_2 - 3x_2 + 2x_1 - 3$$
$$-3x_1 + 2x_2 = -3x_2 + 2x_1$$
$$5x_2 = 5x_1 \;\Rightarrow\; x_1 = x_2$$
Funkcija **je injektivna**, zato inverz obstaja.

**Inverz:** $y = \frac{x+1}{2x-3}$, zamenjamo $x$ in $y$ ter izrazimo $y$:
$$x = \frac{y+1}{2y-3} \;/\cdot(2y-3)$$
$$x(2y-3) = y+1$$
$$2xy - 3x = y + 1$$
$$2xy - y = 3x + 1$$
$$y(2x-1) = 3x + 1$$
$$f^{-1}(x) = \frac{3x+1}{2x-1}$$

**Podatki za graf:**

- Ničla: $x + 1 = 0 \Rightarrow x = -1$
- Pol: $x = \frac32$ (navpična asimptota)
- Začetna vrednost: $f(0) = \frac{0+1}{0-3} = -\frac13$
- Vodoravna asimptota: $\lim_{x\to\infty} \frac{x+1}{2x-3} = \lim_{x\to\infty} \frac{1 + \frac1x}{2 - \frac3x} = \frac12$, torej $y = \frac12$
- Zato $Z_f = \mathbb{R} \setminus \{\frac12\}$ in $D_{f^{-1}} = \mathbb{R} \setminus \{\frac12\}$ (pol inverza je pri $x = \frac12$, asimptota pri $y = \frac32$)

```desmos-graph
left=-5; right=6;
bottom=-5; top=6;
---
y=\frac{x+1}{2x-3}
y=\frac{3x+1}{2x-1}|dashed
y=x|dotted
x=1.5|dotted
y=0.5|dotted
```

### Primer: $f(x) = \ln(2x - 1)$

- **Definicijsko območje:** $2x - 1 > 0 \Rightarrow x > \frac12$, $D_f = (\frac12, \infty)$
- **Ničla:** $\ln(2x-1) = 0 \Rightarrow 2x - 1 = e^0 = 1 \Rightarrow 2x = 2 \Rightarrow x = 1$
- Funkcija **je injektivna** (logaritem ves čas narašča, vsako vodoravnico seka enkrat)

**Inverz:**
$$y = \ln(2x-1) \;\to\; x = \ln(2y-1)$$
$$e^x = 2y - 1$$
$$2y = e^x + 1$$
$$f^{-1}(x) = \frac{e^x + 1}{2}$$

```desmos-graph
left=-3; right=5;
bottom=-3; top=5;
---
y=\ln(2x-1)
y=\frac{e^x+1}{2}|dashed
y=x|dotted
(1,0)|label:1
```

### Primer: $f(x) = 3 - 2x^2$ (inverz na zoženem območju)

Ta funkcija na $\mathbb{R}$ ni injektivna (glej spodaj pri kvadratni funkciji), zato ji **zožimo definicijsko območje** na del, kjer je injektivna:

- $f: [0, \infty) \to \mathbb{R}$: $y = 3 - 2x^2 \to x = 3 - 2y^2 \Rightarrow 2y^2 = 3 - x \Rightarrow y^2 = \frac{3-x}{2} \Rightarrow f^{-1}(x) = \sqrt{\frac{3-x}{2}}$
- $f: (-\infty, 0] \to \mathbb{R}$: enak račun, le da vzamemo negativni koren, $f^{-1}(x) = -\sqrt{\frac{3-x}{2}}$

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

**Kako preverimo:** izračunamo $f(-x)$ (povsod namesto $x$ vstavimo $-x$) in ga primerjamo z $f(x)$ in $-f(x)$.

### Primeri iz vaj

**a)** $f(x) = \sqrt{1 - x^2}$
$$f(-x) = \sqrt{1 - (-x)^2} = \sqrt{1 - x^2} = f(x)$$
Funkcija je **soda** (to je zgornja polovica krožnice, simetrična glede na os $y$).

**b)** $f(x) = -x^2 - 2|x| + 1$
$$f(-x) = -(-x)^2 - 2|-x| + 1 = -x^2 - 2|x| + 1 = f(x)$$
Funkcija je **soda**, ker je $(-x)^2 = x^2$ in $|-x| = |x|$.

**c)** $f(x) = \log(2 - x)$
$$f(-x) = \log(2 - (-x)) = \log(2 + x) \ne f(x) \quad \Rightarrow \text{ni soda}$$
$$-f(x) = -\log(2 - x) = \log\frac{1}{2 - x} \ne f(-x) \quad \Rightarrow \text{ni liha}$$
Funkcija **ni ne soda ne liha**. Tu nam pride prav pravilo $r \cdot \log_a x = \log_a(x^r)$ z $r = -1$.

**d)** $f(x) = \log\left(\dfrac{1+x}{1-x}\right)$
$$f(-x) = \log\left(\frac{1-x}{1+x}\right) \ne f(x) \quad \Rightarrow \text{ni soda}$$
$$-f(x) = -\log\left(\frac{1+x}{1-x}\right) = \log\left(\frac{1+x}{1-x}\right)^{-1} = \log\left(\frac{1-x}{1+x}\right) = f(-x)$$
Funkcija je **liha**.

## Kompozitum funkcij

**Kompozitum** $f \circ g$ pomeni, da najprej uporabimo $g$, nato na rezultatu še $f$:
$$(f \circ g)(x) = f\big(g(x)\big)$$

- Vrstni red je pomemben: v splošnem je $f \circ g \ne g \circ f$
- Računamo tako, da v zunanjo funkcijo namesto $x$ vstavimo celotno notranjo funkcijo

### Primer: $f(x) = e^x$, $g(x) = -\dfrac{1}{x^2}$

$$(f \circ g)(x) = f\big(g(x)\big) = e^{g(x)} = e^{-\frac{1}{x^2}}$$
$$(g \circ f)(x) = g\big(f(x)\big) = -\frac{1}{(f(x))^2} = -\frac{1}{(e^x)^2} = -\frac{1}{e^{2x}}$$

Rezultata sta različna, kar pokaže, da vrstni red šteje.

## Kvadratna funkcija

$$f(x) = ax^2 + bx + c$$

- **Ničle:** $x_{1,2} = \dfrac{-b \pm \sqrt{D}}{2a}$, kjer je **diskriminanta** $D = b^2 - 4ac$
- **Teme:** $T(p, q)$, kjer je $p = -\dfrac{b}{2a}$ in $q = -\dfrac{D}{4a}$
- Če je $a > 0$, je parabola obrnjena navzgor, če je $a < 0$, navzdol

### Primer: $f(x) = 3 - 2x^2$

- **Ničle:** $3 - 2x^2 = 0 \Rightarrow -2x^2 = -3 \;/:(-2) \Rightarrow x^2 = \frac32 \Rightarrow x_{1,2} = \pm\sqrt{\frac32} \approx \pm 1{,}22$
- **Teme:** $f(0) = 3 - 2 \cdot 0^2 = 3$, torej $T(0, 3)$ (ker je $b = 0$, je $p = 0$)
- $a = -2 < 0$, parabola je obrnjena navzdol
- $D_f = \mathbb{R}$, $Z_f = (-\infty, 3]$ (najvišja vrednost je v temenu)
- **Ni injektivna:** $3 - 2x_1^2 = 3 - 2x_2^2 \Rightarrow x_1^2 = x_2^2 \Rightarrow x_1 = \pm x_2$, npr. $f(-1) = f(1) = 1$
- **Ni surjektivna:** $Z_f \ne \mathbb{R}$ (vrednosti nad $3$ nikoli ne zavzame)

```desmos-graph
left=-3; right=3;
bottom=-3; top=4;
---
y=3-2x^2
(0,3)|label:T(0,3)
(-1.2247,0)|label:-√(3/2)
(1.2247,0)|label:√(3/2)
```

## Funkcija signum

**Signum** (predznak) vrne samo predznak števila:
$$\operatorname{sign}(x) = \begin{cases} 1, & x > 0 \\ 0, & x = 0 \\ -1, & x < 0 \end{cases}$$

### Primer: $f(x) = \operatorname{sign}(3 - 2x^2)$

Pogledamo, kje je $3 - 2x^2$ pozitiven, ničeln ali negativen (iz zgornjega primera):

- med ničlama, $|x| < \sqrt{\frac32}$: $3 - 2x^2 > 0$, zato $f(x) = 1$
- v ničlah, $x = \pm\sqrt{\frac32}$: $f(x) = 0$
- zunaj ničel, $|x| > \sqrt{\frac32}$: $3 - 2x^2 < 0$, zato $f(x) = -1$

Lastnosti:

- $D_f = \mathbb{R}$, $Z_f = \{-1, 0, 1\}$
- **Ni injektivna** (npr. vsi $x$ med ničlama dajo vrednost $1$)
- **Ni surjektivna** ($Z_f \ne \mathbb{R}$)

```desmos-graph
left=-3; right=3;
bottom=-2; top=2;
---
y=\operatorname{sign}(3-2x^2)
y=3-2x^2|dashed
```

Ročni zapiski z vaj: [[M - Funkcije - vaje.excalidraw]]
