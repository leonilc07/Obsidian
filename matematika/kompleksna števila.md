Realna števila ležijo na eni premici, na **realni osi** ($x$ os). Kompleksna števila to razširijo v ravnino: dodamo še **imaginarno os** ($y$ os), ki je pravokotna na realno. Kompleksno število je zato **dvodimenzionalno število**, ena točka v ravnini, ki ima realni in imaginarni del.

Množico kompleksnih števil označimo z $\mathbb{C}$. Vsebuje vsa realna števila, $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$.
$$\mathbb{C} = \{\, a + bi \mid a, b \in \mathbb{R} \,\}$$

$z$ – kompleksno število
$$z = a + bi \in \mathbb{C}, \quad a, b \in \mathbb{R} \qquad \text{Re}(z) = a, \quad \text{Im}(z) = b$$
Seštevamo po delih, realno z realnim in imaginarno z imaginarnim:
$$(a + ib) + (c + id) = (a + c) + i(b + d)$$

Zakaj je $i^2 = -1$? Na navadnem $x$–$y$ grafu množenje z $-1$ število "obrne" na drugo stran: $1 \cdot (-1) = -1$, kar je **zasuk za $180^\circ$**. Število $i$ pa je zasuk samo za **$90^\circ$**, iz $1$ na realni osi pridemo na $i$ na imaginarni osi. Če z $i$ pomnožimo dvakrat, se zasukamo za $90^\circ + 90^\circ = 180^\circ$, torej pristanemo na $-1$:
$$i \cdot i = i^2 = -1 \quad \Rightarrow \quad i = \sqrt{-1}$$

```desmos-graph
left=-2; right=2;
bottom=-1.5; top=1.5;
xAxisLabel=Re; yAxisLabel=Im;
---
(1,0)|label:1
(0,1)|label:i
(-1,0)|label:-1
(0,-1)|label:-i
x^2+y^2=1|dashed
```

## Konjugirano število

**Konjugirano število** $\bar{z}$ (konj $z$) je isto število, samo z obrnjenim predznakom pred $i$. Realni del ostane, imaginarni del zamenja predznak:
$$z = a + bi \quad \Rightarrow \quad \bar{z} = a - bi$$
Primer: $z = 3 + 2i \Rightarrow \bar{z} = 3 - 2i$

Na grafu je $\bar{z}$ **zrcalna slika** $z$ čez realno os:

```desmos-graph
left=-1; right=5;
bottom=-3; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
(3,2)|label:z = 3 + 2i
(3,-2)|label:konj z = 3 - 2i
x=3|-2<y<2|dashed
```

## Množenje

Množimo kot pri navadnih oklepajih: vsak člen iz prvega oklepaja zmnožimo z vsakim členom iz drugega. Na koncu povsod, kjer dobimo $i^2$, napišemo $-1$, in zložimo skupaj realne člene ter skupaj člene z $i$:
$$(a + bi)(c + di) = ac + adi + bci + bd\,i^2 = (ac - bd) + i(ad + bc)$$
Primer:
$$(2 + 3i)(1 + 4i) = 2 + 8i + 3i + 12i^2 = 2 + 11i - 12 = -10 + 11i$$

Če $z$ pomnožimo z $\bar{z}$, se člena z $i$ pokrajšata ($-abi + abi = 0$) in ostane samo realno število:
$$z \cdot \bar{z} = (a + bi)(a - bi) = a^2 - abi + abi - b^2 i^2 = a^2 + b^2$$
$$(3 + 2i)(3 - 2i) = 9 - 6i + 6i - 4i^2 = 9 + 4 = 13$$

## Deljenje

Z $i$ v imenovalcu ne znamo deliti, zato ulomek razširimo s **konjugiranim imenovalcem**. V imenovalcu se $i$ pokrajša in ostane realno število:
$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + i(bc - ad)}{c^2 + d^2}$$
Primer:
$$\frac{5 + 5i}{1 + 2i} = \frac{(5 + 5i)(1 - 2i)}{(1 + 2i)(1 - 2i)} = \frac{5 - 10i + 5i - 10i^2}{1 + 4} = \frac{15 - 5i}{5} = 3 - i$$

## Absolutna vrednost

**Absolutna vrednost** $|z|$ je razdalja točke $z$ od izhodišča $(0, 0)$. Točka $z = a + bi$ leži $a$ v desno po realni osi in $b$ gor po imaginarni osi, zato z izhodiščem tvori **pravokotni trikotnik** s katetama $a$ in $b$. Razdalja $|z|$ je hipotenuza, torej jo izračunamo s **Pitagorovim izrekom**:
$$|z|^2 = a^2 + b^2 \quad \Rightarrow \quad |z| = \sqrt{a^2 + b^2}$$
Primer: $z = 3 + 4i$, $|z| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$

```desmos-graph
left=-1; right=6;
bottom=-1; top=5;
xAxisLabel=Re; yAxisLabel=Im;
---
(3,4)|label:z = 3 + 4i
y=(4/3)x|0<x<3
y=0|0<x<3
x=3|0<y<4
(1.5,0)|label:a = 3
(3,2)|label:b = 4
(1.5,2)|label:razdalja = 5
```

Iz množenja s konjugiranim številom smo dobili isto: $z \cdot \bar{z} = a^2 + b^2 = |z|^2$.

Vsa števila z enako absolutno vrednostjo ležijo na **krožnici** s središčem v $0$ in polmerom $r$:
$$\{\, z \in \mathbb{C} \mid |z| = r \,\}$$
Za $r = 5$ so na tej krožnici npr. $3 + 4i$, $-3 - 4i$, $4 + 3i$, $5i$, $-5$:

```desmos-graph
left=-7; right=7;
bottom=-6; top=6;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2=25|dashed
(3,4)|label:3 + 4i
(-3,-4)|label:-3 - 4i
(4,3)|label:4 + 3i
(0,5)|label:5i
(-5,0)|label:-5
```

## Lastnosti kompleksnih števil

1. $\boldsymbol{\overline{\overline{z}} = z}$ – če število dvakrat konjugiramo, dobimo nazaj isto število. Konjugiranje obrne predznak pred $i$, dvakrat obrnjen predznak pa je spet prvoten:
$$z = a + bi \;\rightarrow\; \bar{z} = a - bi \;\rightarrow\; \overline{\overline{z}} = a + bi = z$$
2. $\boldsymbol{z \cdot \bar{z} = |z|^2}$ – število, pomnoženo s svojim konjugiranim, da kvadrat absolutne vrednosti (vedno realno število):
$$z \cdot \bar{z} = (a + bi)(a - bi) = a^2 + b^2 = |z|^2$$
3. $\boldsymbol{\overline{z + w} = \bar{z} + \bar{w}}$ – konjugirano število vsote je enako vsoti konjugiranih. Vseeno je, ali najprej seštejemo in potem konjugiramo, ali obratno:
$$\overline{z + w} = \overline{(a + ib) + (c + id)} = (a - ib) + (c - id) = \bar{z} + \bar{w}$$
4. $\boldsymbol{\overline{z \cdot w} = \bar{z} \cdot \bar{w}}$ – enako velja za množenje: konjugirano število produkta je enako produktu konjugiranih:
$$\overline{z \cdot w} = \overline{(a + ib)(c + id)} = (a - ib)(c - id) = \bar{z} \cdot \bar{w}$$
5. $\boldsymbol{z + \bar{z} = 2a = 2\,\text{Re}(z)}$ – vsota števila in njegovega konjugiranega je realno število, imaginarna dela se pokrajšata:
$$z + \bar{z} = (a + ib) + (a - ib) = 2a = 2\,\text{Re}(z)$$
   $\boldsymbol{z - \bar{z} = 2ib = 2i\,\text{Im}(z)}$ – razlika je samo imaginarna, realna dela se pokrajšata:
$$z - \bar{z} = (a + ib) - (a - ib) = 2ib = 2i\,\text{Im}(z)$$
6. $\boldsymbol{|z + w| \leq |z| + |w|}$ – **trikotniška neenakost**. Na grafu $z$, $w$ in $z + w$ tvorijo trikotnik: najprej gremo od $0$ do $z$, nato še za $w$ naprej in pridemo do $z + w$. Ena stranica trikotnika ($|z + w|$, naravnost od $0$ do $z + w$) ne more biti daljša od drugih dveh skupaj ($|z| + |w|$, ovinek čez $z$). Enako velja samo, ko $z$ in $w$ kažeta v isto smer in trikotnik "splošči" v daljico.

```desmos-graph
width=360; height=300;
left=-1; right=5;
bottom=-1; top=4;
xAxisLabel=Re; yAxisLabel=Im;
---
(3,1)|label:z
(4,3)|label:z + w
y=x/3|0<x<3
y=2x-5|3<x<4
y=0.75x|0<x<4|dashed
```

## Enačbe

Enačbo s kompleksno neznanko $z$ rešujemo enako kot navadno enačbo z $x$. Število $i$ se obnaša kot navadna črka, rešitev pa je kompleksno število.

**Primer 1:**
$$2z + 6i = 8 \quad \Big|\; -6i$$
$$2z = 8 - 6i \quad \Big|\; :2$$
$$z = 4 - 3i$$
Preizkus: $2(4 - 3i) + 6i = 8 - 6i + 6i = 8$ ✓

**Primer 2:** rešitev je lahko tudi **množica** števil.
$$\{\, z \in \mathbb{C} \mid z + \bar{z} = 5 \,\}$$
Po lastnosti 5 je $z + \bar{z} = 2a$, zato:
$$2a = 5 \quad \Rightarrow \quad a = \frac{5}{2}$$
O $b$ enačba ne pove nič, zato je $b$ lahko karkoli. Rešitve so vsa števila $z = \frac{5}{2} + bi$, $b \in \mathbb{R}$. Na grafu je to **navpična premica** $\text{Re}(z) = \frac{5}{2}$:

```desmos-graph
width=240; height=200;
left=-1; right=5;
bottom=-2.5; top=2.5;
xAxisLabel=Re; yAxisLabel=Im;
---
x=2.5
(2.5,0)|label:5/2
(2.5,1.5)|label:5/2 + 1.5i
(2.5,-1)|label:5/2 - i
```

**Primer 3:**
$$\{\, z \in \mathbb{C} \mid |z - 1 - i|^2 = 2 \,\}$$
Vstavimo $z = a + bi$ in zložimo realni del skupaj ter imaginarni del skupaj:
$$z - 1 - i = (a - 1) + i(b - 1)$$
Absolutna vrednost na kvadrat je po Pitagori realni del na kvadrat plus imaginarni del na kvadrat:
$$|z - 1 - i|^2 = (a - 1)^2 + (b - 1)^2 = 2$$
To je enačba **krožnice** s središčem v $(1, 1)$, torej v točki $1 + i$, in polmerom $\sqrt{2}$. Enako se vidi brez računanja: $|z - (1 + i)|$ je razdalja med $z$ in $1 + i$, ta pa mora biti $\sqrt{2}$. Rešitve so vse točke, ki so od $1 + i$ oddaljene za $\sqrt{2}$.

```desmos-graph
width=240; height=240;
left=-1; right=3;
bottom=-1; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
(x-1)^2+(y-1)^2=2
(1,1)|label:1 + i
(0,0)|label:0
(2,2)|label:2 + 2i
```

## Polarni zapis

Spet narišemo $z = a + bi$ kot hipotenuzo pravokotnega trikotnika. Kot med realno osjo in $z$ označimo s $\varphi$. Hipotenuza je dolga $|z|$, kateti pa sta $a$ in $b$.

```desmos-graph
width=300; height=250;
left=-1; right=5;
bottom=-1; top=5;
xAxisLabel=Re; yAxisLabel=Im;
---
(3,4)|label:z
y=(4/3)x|0<x<3
y=0|0<x<3
x=3|0<y<4
x^2+y^2=1|y>0|y<(4/3)x
(1.4,0.5)|label:φ
```

Iz trikotnika s kotnima funkcijama ($\cos = \frac{\text{priležna}}{\text{hipotenuza}}$, $\sin = \frac{\text{nasprotna}}{\text{hipotenuza}}$):
$$\cos\varphi = \frac{a}{|z|} \;\Rightarrow\; a = |z|\cos\varphi \qquad \sin\varphi = \frac{b}{|z|} \;\Rightarrow\; b = |z|\sin\varphi$$
Vstavimo v $z = a + bi$:
$$z = |z|\cos\varphi + i\,|z|\sin\varphi = |z|(\cos\varphi + i\sin\varphi)$$
Po **Eulerjevi formuli** je $\cos\varphi + i\sin\varphi = e^{i\varphi}$, zato:
$$\boldsymbol{z = |z|\,e^{i\varphi}}$$
Število tako ne opišemo z $a$ in $b$ (koliko desno, koliko gor), ampak z **dolžino** $|z|$ in **kotom** $\varphi$ (kako daleč in v katero smer).

Primer: $z = 1 + i$, $|z| = \sqrt{2}$, $\varphi = 45^\circ = \frac{\pi}{4}$, torej $1 + i = \sqrt{2}\,e^{i\pi/4}$.

To se poveže z uvodom: $i$ ima dolžino $1$ in kot $90^\circ$, torej $i = e^{i\pi/2}$. Množenje z $i$ je zato res zasuk za $90^\circ$.

**Konjugirano število v polarnem zapisu:** če konjugiramo vse skupaj, se samo pri $i$ zamenja predznak:
$$\bar{z} = \overline{|z|(\cos\varphi + i\sin\varphi)} = |z|(\cos\varphi - i\sin\varphi)$$
Ker je $\cos(-\varphi) = \cos\varphi$ in $\sin(-\varphi) = -\sin\varphi$, je to isto, kot če vzamemo kot $-\varphi$:
$$|z|(\cos\varphi - i\sin\varphi) = |z|\big(\cos(-\varphi) + i\sin(-\varphi)\big) = |z|\,e^{-i\varphi}$$
$$\boldsymbol{\bar{z} = |z|\,e^{-i\varphi}}$$
Dolžina ostane enaka, kot pa zamenja predznak. To se ujema z grafom: $\bar{z}$ je zrcalna slika $z$ čez realno os, torej je za kot $\varphi$ **pod** realno osjo namesto nad njo.

**Množenje v polarnem zapisu:** po pravilu za potence ($e^x \cdot e^y = e^{x+y}$) se dolžini zmnožita, kota pa seštejeta:
$$z = |z|\,e^{i\varphi}, \quad w = |w|\,e^{i\psi} \quad \Rightarrow \quad \boldsymbol{z \cdot w = |z||w|\,e^{i(\varphi + \psi)}}$$

**Konjugirano število produkta v polarnem zapisu** (lastnost 4, samo drugače dokazana). Konjugiramo produkt, torej obrnemo predznak kota:
$$\overline{z \cdot w} = \overline{|z||w|\,e^{i(\varphi + \psi)}} = |z||w|\,e^{-i(\varphi + \psi)}$$
Razbijemo nazaj na dva faktorja:
$$|z||w|\,e^{-i(\varphi + \psi)} = |z|\,e^{-i\varphi} \cdot |w|\,e^{-i\psi} = \bar{z} \cdot \bar{w}$$
Torej spet $\overline{z \cdot w} = \bar{z} \cdot \bar{w}$, le da je račun v polarnem zapisu krajši kot z $a$, $b$, $c$, $d$.
