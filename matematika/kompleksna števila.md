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

### Iz $a + bi$ v polarni zapis

Postopek v treh korakih:

**1. Dolžina:** po Pitagori, $|z| = \sqrt{a^2 + b^2}$.

**2. Kvadrant:** narišeš točko (ali pogledaš predznaka $a$ in $b$) in vidiš, v katerem kvadrantu je. To je pomembno, ker $\tan$ sam ne loči npr. $1 + i$ od $-1 - i$ (v obeh primerih je $\frac{b}{a} = 1$), ti dve števili pa kažeta v nasprotni smeri.

**3. Kot:** najprej poiščeš **ostri kot $\alpha$** v trikotniku, z dolžinama $|a|$ in $|b|$ (brez predznakov):
$$\tan\alpha = \frac{|b|}{|a|}$$
Nato ga glede na kvadrant prestaviš na pravo mesto:
- 1. kvadrant ($a > 0$, $b > 0$): $\varphi = \alpha$
- 2. kvadrant ($a < 0$, $b > 0$): $\varphi = 180^\circ - \alpha$
- 3. kvadrant ($a < 0$, $b < 0$): $\varphi = 180^\circ + \alpha$
- 4. kvadrant ($a > 0$, $b < 0$): $\varphi = 360^\circ - \alpha$ (ali $-\alpha$)

Zakaj to prestavljanje: $\alpha$ iz $\tan$ je kot v trikotniku, merjen od **najbližjega dela realne osi** (lahko tudi od negativnega). $\varphi$ pa se vedno meri od **pozitivne realne osi** v nasprotni smeri urinega kazalca. V 1. kvadrantu sta ista, drugje pa moraš $\alpha$ prišteti ali odšteti od $180^\circ$ oz. $360^\circ$.

**Bližnjica za lepe kote:** v nalogah sta $|a|$ in $|b|$ skoraj vedno v enem od teh razmerij:
- $|a| = |b|$, npr. $1 + i$: $\alpha = 45^\circ$
- večji je $\sqrt{3}$-krat večji od manjšega, npr. $\sqrt{3} + i$ ali $1 + \sqrt{3}i$:
  - če je večji $|a|$ (točka je bolj "ležeča", bližje realni osi): $\alpha = 30^\circ$
  - če je večji $|b|$ (točka je bolj "pokončna", bližje imaginarni osi): $\alpha = 60^\circ$

To izhaja iz $\tan 30^\circ = \frac{1}{\sqrt{3}}$, $\tan 45^\circ = 1$, $\tan 60^\circ = \sqrt{3}$.

**Na oseh** ni treba nič računati: pozitivna realna os je $0^\circ$, pozitivna imaginarna $90^\circ$, negativna realna $180^\circ$, negativna imaginarna $270^\circ$. Npr. $-5 = 5\,e^{i\pi}$, $3i = 3\,e^{i\pi/2}$.

**Primer 1:** $\sqrt{3} + i$
- dolžina: $\sqrt{3 + 1} = 2$
- kvadrant: $a > 0$, $b > 0$, prvi
- kot: $|a| = \sqrt{3}$ je večji, torej $\alpha = 30^\circ$, in $\varphi = 30^\circ$

$$\sqrt{3} + i = 2\,e^{i\pi/6}$$

**Primer 2:** $-1 + \sqrt{3}i$
- dolžina: $\sqrt{1 + 3} = 2$
- kvadrant: $a < 0$, $b > 0$, drugi
- kot: $|b| = \sqrt{3}$ je večji, torej $\alpha = 60^\circ$, in $\varphi = 180^\circ - 60^\circ = 120^\circ$

$$-1 + \sqrt{3}i = 2\,e^{i\,2\pi/3}$$

```desmos-graph
width=300; height=250;
left=-2; right=1.5;
bottom=-0.5; top=2.5;
xAxisLabel=Re; yAxisLabel=Im;
---
(-1,1.732)|label:-1 + √3 i
y=-1.732x|-1<x<0
x=-1|0<y<1.732
y=0|-1<x<0
x^2+y^2=0.25|y>=0|y>=-1.732x
(0.35,0.55)|label:φ = 120°
(-0.55,0.3)|label:α = 60°
```

**Primer 3:** $-2 - 2i$
- dolžina: $\sqrt{4 + 4} = 2\sqrt{2}$
- kvadrant: $a < 0$, $b < 0$, tretji
- kot: $|a| = |b|$, torej $\alpha = 45^\circ$, in $\varphi = 180^\circ + 45^\circ = 225^\circ$

$$-2 - 2i = 2\sqrt{2}\,e^{i\,5\pi/4}$$
Na grafu: od pozitivne realne osi gremo najprej $180^\circ$ do negativne realne osi, nato še $45^\circ$ navzdol, skupaj $225^\circ$. Kalkulator bi pri $\arctan\frac{-2}{-2} = \arctan 1$ vrnil $45^\circ$, kar je **1. kvadrant**, torej narobe. Zato je treba vedno preveriti kvadrant.

```desmos-graph
width=280; height=280;
left=-2.5; right=1;
bottom=-2.5; top=1;
xAxisLabel=Re; yAxisLabel=Im;
---
(-2,-2)|label:-2 - 2i
y=x|-2<x<0
x=-2|-2<y<0
y=0|-2<x<0
x^2+y^2=0.25|y>=0
x^2+y^2=0.25|y<=0|x<=0|y>=x
(0.35,0.5)|label:φ = 225°
(-1.3,-0.45)|label:α = 45°
```

**Primer 4:** $1 - i$
- dolžina: $\sqrt{2}$
- kvadrant: $a > 0$, $b < 0$, četrti
- kot: $|a| = |b|$, torej $\alpha = 45^\circ$, in $\varphi = -45^\circ$ (ali $315^\circ$)

$$1 - i = \sqrt{2}\,e^{-i\pi/4}$$

### Konjugirano število v polarnem zapisu

Če konjugiramo vse skupaj, se samo pri $i$ zamenja predznak:
$$\bar{z} = \overline{|z|(\cos\varphi + i\sin\varphi)} = |z|(\cos\varphi - i\sin\varphi)$$
Ker je $\cos(-\varphi) = \cos\varphi$ in $\sin(-\varphi) = -\sin\varphi$, je to isto, kot če vzamemo kot $-\varphi$:
$$|z|(\cos\varphi - i\sin\varphi) = |z|\big(\cos(-\varphi) + i\sin(-\varphi)\big) = |z|\,e^{-i\varphi}$$
$$\boldsymbol{\bar{z} = |z|\,e^{-i\varphi}}$$
Dolžina ostane enaka, kot pa zamenja predznak. To se ujema z grafom: $\bar{z}$ je zrcalna slika $z$ čez realno os, torej je za kot $\varphi$ **pod** realno osjo namesto nad njo.

### Množenje v polarnem zapisu

Pri množenju v polarnem zapisu se **dolžini zmnožita**, **kota pa seštejeta**:
$$z = |z|\,e^{i\varphi}, \quad w = |w|\,e^{i\psi} \quad \Rightarrow \quad \boldsymbol{z \cdot w = |z||w|\,e^{i(\varphi + \psi)}}$$
Z $\cos$ in $\sin$ zapisano isto:
$$z \cdot w = |z||w|\big(\cos(\varphi + \psi) + i\sin(\varphi + \psi)\big)$$
Množenje z $w$ si lahko predstavljamo kot dva koraka: $z$ **raztegnemo** za faktor $|w|$ in ga **zasukamo** za kot $\psi$.

Primer: $z = 1 + i$ in $w = 2i$.
- $z = 1 + i$: dolžina $\sqrt{2}$, kot $45^\circ$
- $w = 2i$: dolžina $2$, kot $90^\circ$
- $z \cdot w$: dolžina $\sqrt{2} \cdot 2 = 2\sqrt{2}$, kot $45^\circ + 90^\circ = 135^\circ$

$$z \cdot w = 2\sqrt{2}\,(\cos 135^\circ + i\sin 135^\circ) = 2\sqrt{2}\left(-\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = -2 + 2i$$
Preizkus z navadnim množenjem: $(1 + i) \cdot 2i = 2i + 2i^2 = -2 + 2i$ ✓

```desmos-graph
width=300; height=250;
left=-3; right=2;
bottom=-0.5; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
(1,1)|label:z = 1 + i
(0,2)|label:w = 2i
(-2,2)|label:z · w = -2 + 2i
y=x|0<x<1
x=0|0<y<2
y=-x|-2<x<0
```

#### Utemeljitev

Zakaj se dolžini zmnožita in kota seštejeta? Pravilo $e^x \cdot e^y = e^{x+y}$ je hitra bližnjica, ampak da dobimo pravi razlog, pomnožimo $z$ in $w$ v zapisu s $\cos$ in $\sin$, čisto navadno, oklepaj krat oklepaj:
$$z \cdot w = |z|(\cos\varphi + i\sin\varphi) \cdot |w|(\cos\psi + i\sin\psi)$$
Dolžini sta navadni realni števili, zato ju damo naprej. Oklepaja zmnožimo člen s členom:
$$= |z||w|\big(\cos\varphi\cos\psi + i\cos\varphi\sin\psi + i\sin\varphi\cos\psi + i^2\sin\varphi\sin\psi\big)$$
Namesto $i^2$ napišemo $-1$ ter zložimo realne člene skupaj in člene z $i$ skupaj:
$$= |z||w|\Big(\underbrace{(\cos\varphi\cos\psi - \sin\varphi\sin\psi)}_{\text{realni del}} + i\,\underbrace{(\sin\varphi\cos\psi + \cos\varphi\sin\psi)}_{\text{imaginarni del}}\Big)$$
Zdaj uporabimo **adicijska izreka** za $\cos$ in $\sin$:
$$\cos(\varphi + \psi) = \cos\varphi\cos\psi - \sin\varphi\sin\psi$$
$$\sin(\varphi + \psi) = \sin\varphi\cos\psi + \cos\varphi\sin\psi$$
Realni del je točno $\cos(\varphi + \psi)$, imaginarni pa točno $\sin(\varphi + \psi)$. Torej:
$$\boldsymbol{z \cdot w = |z||w|\big(\cos(\varphi + \psi) + i\sin(\varphi + \psi)\big)}$$
To je število z dolžino $|z||w|$ in kotom $\varphi + \psi$. ∎

Ključni korak je, da se izraza, ki nastaneta pri množenju oklepajev, **ujemata z adicijskima izrekoma**. Prav zato se kota seštejeta. To je tudi razlog, zakaj lahko $\cos\varphi + i\sin\varphi$ pišemo kot $e^{i\varphi}$: obnaša se kot potenca, pri množenju se "eksponenta" (kota) seštejeta.

**Konjugirano število produkta v polarnem zapisu** (lastnost 4, samo drugače dokazana). Konjugiramo produkt, torej obrnemo predznak kota:
$$\overline{z \cdot w} = \overline{|z||w|\,e^{i(\varphi + \psi)}} = |z||w|\,e^{-i(\varphi + \psi)}$$
Razbijemo nazaj na dva faktorja:
$$|z||w|\,e^{-i(\varphi + \psi)} = |z|\,e^{-i\varphi} \cdot |w|\,e^{-i\psi} = \bar{z} \cdot \bar{w}$$
Torej spet $\overline{z \cdot w} = \bar{z} \cdot \bar{w}$, le da je račun v polarnem zapisu krajši kot z $a$, $b$, $c$, $d$.

### Deljenje v polarnem zapisu

Deljenje je obratno od množenja: **dolžini delimo**, **kota odštejemo** ($w \neq 0$):
$$\boldsymbol{\frac{z}{w} = \frac{|z|}{|w|}\,e^{i(\varphi - \psi)}} = \frac{|z|}{|w|}\big(\cos(\varphi - \psi) + i\sin(\varphi - \psi)\big)$$
#### Utemeljitev

**1. korak: koliko je $\frac{1}{w}$?** Ulomek razširimo s konjugiranim številom $\bar{w}$, kot pri navadnem deljenju. V imenovalcu dobimo $w \cdot \bar{w} = |w|^2$ (lastnost 2):
$$\frac{1}{w} = \frac{\bar{w}}{w \cdot \bar{w}} = \frac{\bar{w}}{|w|^2}$$
Zdaj vstavimo konjugirano število v polarnem zapisu, $\bar{w} = |w|\,e^{-i\psi}$, in en $|w|$ pokrajšamo:
$$\frac{1}{w} = \frac{|w|\,e^{-i\psi}}{|w|^2} = \boldsymbol{\frac{1}{|w|}\,e^{-i\psi}}$$
Število $\frac{1}{w}$ ima torej dolžino $\frac{1}{|w|}$ in kot $-\psi$.

Na grafu za $w = 1 + i$: $\bar{w} = 1 - i$ je zrcalna slika $w$ čez realno os (kot $-45^\circ$). $\frac{1}{w}$ leži na **istem poltraku** kot $\bar{w}$, le da je $|w|^2 = 2$-krat krajši: $\frac{1}{w} = \frac{1 - i}{2} = \frac{1}{2} - \frac{1}{2}i$. Njegova dolžina je $\frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} = \frac{1}{|w|}$.

```desmos-graph
width=300; height=300;
left=-1.5; right=2;
bottom=-1.5; top=1.5;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2=1|dashed
(1,1)|label:w = 1 + i
(1,-1)|label:konj w = 1 - i
(0.5,-0.5)|label:1/w
y=x|0<x<1
y=-x|0<x<1|dashed
y=-x|0<x<0.5
```

**2. korak: deljenje zapišemo kot množenje.** Deliti z $w$ je isto kot množiti z $\frac{1}{w}$:
$$\frac{z}{w} = z \cdot \frac{1}{w} = |z|\,e^{i\varphi} \cdot \frac{1}{|w|}\,e^{-i\psi}$$
Po pravilu za množenje se dolžini zmnožita in kota seštejeta:
$$\frac{z}{w} = \frac{|z|}{|w|}\,e^{i(\varphi + (-\psi))} = \boldsymbol{\frac{|z|}{|w|}\,e^{i(\varphi - \psi)}} \quad ∎$$

Druga, krajša možnost: količnik označimo s $q = \frac{z}{w}$ (dolžina $|q|$, kot $\theta$). Potem je $q \cdot w = z$, po pravilu za množenje pa velja:
$$|q| \cdot |w| = |z| \;\Rightarrow\; |q| = \frac{|z|}{|w|} \qquad \theta + \psi = \varphi \;\Rightarrow\; \theta = \varphi - \psi$$

Primer: obrnemo primer od množenja, $z = -2 + 2i$ delimo z $w = 1 + i$.
- $z = -2 + 2i$: dolžina $2\sqrt{2}$, kot $135^\circ$
- $w = 1 + i$: dolžina $\sqrt{2}$, kot $45^\circ$
- $\frac{z}{w}$: dolžina $\frac{2\sqrt{2}}{\sqrt{2}} = 2$, kot $135^\circ - 45^\circ = 90^\circ$

$$\frac{z}{w} = 2(\cos 90^\circ + i\sin 90^\circ) = 2(0 + i) = 2i$$
Na grafu: $z$ zasukamo **nazaj** za kot $w$ ($45^\circ$, iz $135^\circ$ na $90^\circ$) in ga **skrčimo** za $|w| = \sqrt{2}$ (iz $2\sqrt{2}$ na $2$). Prav obratno kot pri množenju, kjer smo iz $1 + i$ prišli do $-2 + 2i$.

```desmos-graph
width=300; height=250;
left=-3; right=2;
bottom=-0.5; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
(-2,2)|label:z = -2 + 2i
(1,1)|label:w = 1 + i
(0,2)|label:z / w = 2i
y=-x|-2<x<0
y=x|0<x<1
x=0|0<y<2
x^2+y^2=1|x<0|y>-x
(-0.45,1.3)|label:-45°
```
Preizkus s konjugiranim imenovalcem:
$$\frac{-2 + 2i}{1 + i} = \frac{(-2 + 2i)(1 - i)}{(1 + i)(1 - i)} = \frac{-2 + 2i + 2i - 2i^2}{2} = \frac{4i}{2} = 2i \;✓$$
V polarnem zapisu je deljenje veliko krajše, ni treba širiti s konjugiranim številom.

### Množica v polarnem zapisu

V polarnem zapisu lahko množico točk opišemo z **dolžino** $r$ in **kotom** $\varphi$ namesto z $a$ in $b$. Primer:
$$\{\, r\,e^{i\varphi} \mid \tfrac{1}{2} \le r \le 1,\; 0 \le \varphi \le \tfrac{\pi}{2} \,\}$$
Pogoja pogledamo vsakega posebej:
- $\boldsymbol{\frac{1}{2} \le r \le 1}$: točka je od izhodišča oddaljena vsaj $\frac{1}{2}$ in največ $1$. To je **kolobar** med krožnico s polmerom $\frac{1}{2}$ in krožnico s polmerom $1$.
- $\boldsymbol{0 \le \varphi \le \frac{\pi}{2}}$: kot je med $0^\circ$ (smer realne osi) in $90^\circ$ (smer imaginarne osi). To je **prvi kvadrant**.

Veljati morata oba pogoja hkrati, zato je množica presek obeh: **četrtina kolobarja** v prvem kvadrantu. Robovi so:
- zunanji lok od $1$ do $i$ (to je $r = 1$, kot gre od $0$ do $\frac{\pi}{2}$)
- notranji lok od $\frac{1}{2}$ do $\frac{1}{2}i$ (to je $r = \frac{1}{2}$)
- daljica od $\frac{1}{2}$ do $1$ na realni osi ($\varphi = 0$)
- daljica od $\frac{1}{2}i$ do $i$ na imaginarni osi ($\varphi = \frac{\pi}{2}$)

```desmos-graph
width=300; height=300;
left=-0.5; right=1.5;
bottom=-0.5; top=1.5;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2<=1|x^2+y^2>=0.25|x>=0|y>=0
x^2+y^2=1|x>=0|y>=0
x^2+y^2=0.25|x>=0|y>=0
(1,0)|label:1
(0,1)|label:i
(0.5,0)|label:1/2
(0,0.5)|label:1/2 i
```

Z $a$ in $b$ bi bilo isto območje težje zapisati, $\frac{1}{4} \le a^2 + b^2 \le 1$, $a \ge 0$, $b \ge 0$. V polarnem zapisu pa je takoj vidno: $r$ pove, **kako daleč** je točka, $\varphi$ pa **v katero smer**.

## Potence

Potenca je večkratno množenje samega s sabo:
$$z^n = \underbrace{z \cdot z \cdot \ldots \cdot z}_{n\text{-krat}}$$
Z $a + bi$ je to hitro zelo zamudno. Že $(1 + i)^8$ bi pomenilo osemkrat množiti oklepaje. V polarnem zapisu pa je preprosto: pri vsakem množenju se **dolžini zmnožita** in **kota seštejeta**. Če $z$ množimo samega s sabo $n$-krat, se dolžina $n$-krat zmnoži sama s sabo, kot pa se $n$-krat prišteje:
$$z = |z|\,e^{i\varphi} \quad \Rightarrow \quad \boldsymbol{z^n = |z|^n\,e^{in\varphi}} = |z|^n\big(\cos(n\varphi) + i\sin(n\varphi)\big)$$
Dolžino **potenciramo**, kot pa **pomnožimo z $n$**.

### Utemeljitev

Uporabimo pravilo za množenje, korak za korakom:
$$z^2 = z \cdot z = |z| \cdot |z|\,e^{i(\varphi + \varphi)} = |z|^2\,e^{i\,2\varphi}$$
$$z^3 = z^2 \cdot z = |z|^2 \cdot |z|\,e^{i(2\varphi + \varphi)} = |z|^3\,e^{i\,3\varphi}$$
$$z^4 = z^3 \cdot z = |z|^3 \cdot |z|\,e^{i(3\varphi + \varphi)} = |z|^4\,e^{i\,4\varphi}$$
Vsakič, ko pomnožimo še z enim $z$, se dolžina pomnoži z $|z|$, kotu pa se prišteje $\varphi$. Po $n$ korakih imamo $|z|^n$ in $n\varphi$. ∎

Za števila z dolžino $1$ (na enotski krožnici) je $|z|^n = 1$ in ostane samo **Moivrova formula**:
$$\boldsymbol{(\cos\varphi + i\sin\varphi)^n = \cos(n\varphi) + i\sin(n\varphi)}$$

**Pomembno:** če je $n\varphi$ večji od $360^\circ$ ($2\pi$), odštejemo toliko polnih krogov, kolikor jih gre. Kot $360^\circ$ je isto kot $0^\circ$, kot $405^\circ$ pa isto kot $45^\circ$.

### Primeri

**Primer 1:** $(1 + i)^8$
- $1 + i$: dolžina $\sqrt{2}$, kot $45^\circ$
- dolžina: $(\sqrt{2})^8 = 2^4 = 16$
- kot: $8 \cdot 45^\circ = 360^\circ$, kar je isto kot $0^\circ$

$$(1 + i)^8 = 16(\cos 0^\circ + i\sin 0^\circ) = 16$$

**Primer 2:** $(\sqrt{3} + i)^5$
- $\sqrt{3} + i$: dolžina $\sqrt{3 + 1} = 2$, kot $30^\circ$ (ker je $\tan\varphi = \frac{1}{\sqrt{3}}$)
- dolžina: $2^5 = 32$
- kot: $5 \cdot 30^\circ = 150^\circ$

$$(\sqrt{3} + i)^5 = 32(\cos 150^\circ + i\sin 150^\circ) = 32\left(-\frac{\sqrt{3}}{2} + \frac{1}{2}i\right) = -16\sqrt{3} + 16i$$

### Na grafu

Potence $1 + i$ ena za drugo: vsaka naslednja je za $45^\circ$ bolj zasukana in $\sqrt{2}$-krat daljša. Točke se zato vrtijo okoli izhodišča in se oddaljujejo, kot **spirala**:
- $(1 + i)^0 = 1$
- $(1 + i)^1 = 1 + i$
- $(1 + i)^2 = 2i$ (dolžina $2$, kot $90^\circ$)
- $(1 + i)^3 = -2 + 2i$ (dolžina $2\sqrt{2}$, kot $135^\circ$)
- $(1 + i)^4 = -4$ (dolžina $4$, kot $180^\circ$)

```desmos-graph
width=350; height=250;
left=-5; right=2;
bottom=-1; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
(1,0)|label:1
(1,1)|label:(1+i)^1
(0,2)|label:(1+i)^2
(-2,2)|label:(1+i)^3
(-4,0)|label:(1+i)^4
y=x|0<x<1
x=0|0<y<2
y=-x|-2<x<0
y=0|-4<x<0
```

Ali se potence oddaljujejo ali približujejo, je odvisno od dolžine $|z|$:
- $|z| > 1$: $|z|^n$ raste, točke gredo **navzven** (kot pri $1 + i$)
- $|z| = 1$: $|z|^n = 1$, točke se samo **vrtijo po enotski krožnici**
- $|z| < 1$: $|z|^n$ pada, točke gredo **navznoter** proti $0$

### Potence števila $i$

$i$ ima dolžino $1$ in kot $90^\circ$, zato je vsaka potenca samo še en zasuk za $90^\circ$ po enotski krožnici:
$$i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1, \quad i^5 = i, \ldots$$
Po štirih korakih ($4 \cdot 90^\circ = 360^\circ$) smo spet na začetku, zato se potence ponavljajo **na vsake 4**. Za velik $n$ zato pogledamo samo **ostanek pri deljenju s 4**.

Primer: $i^{2026}$. Ker je $2026 = 4 \cdot 506 + 2$, je ostanek $2$:
$$i^{2026} = (i^4)^{506} \cdot i^2 = 1 \cdot (-1) = -1$$

```desmos-graph
width=240; height=240;
left=-1.5; right=1.5;
bottom=-1.5; top=1.5;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2=1|dashed
(1,0)|label:i^0 = i^4 = 1
(0,1)|label:i^1 = i
(-1,0)|label:i^2 = -1
(0,-1)|label:i^3 = -i
```

## Koreni

$n$-ti koren števila $w$ so **vsa** števila $z$, za katera velja:
$$z^n = w$$
Pri realnih številih ima $\sqrt{4}$ en rezultat ($2$), pri kompleksnih pa je drugače: vsako število $w \neq 0$ ima **natanko $n$ različnih $n$-tih korenov**. Kvadratni koren ima 2 rešitvi, kubični 3, četrti 4, ...

### Ideja: obratno od potenciranja

Pri potenciranju dolžino **potenciramo**, kot pa **pomnožimo z $n$**. Pri korenjenju gremo nazaj: dolžino **korenimo**, kot pa **delimo z $n$**.

Ampak tu je zanka. Kot števila ni enoličen: če naredimo poln krog ($360^\circ$), pridemo na isto mesto. Število $-1$ ima kot $180^\circ$, ampak tudi $180^\circ + 360^\circ = 540^\circ$, $180^\circ + 720^\circ = 900^\circ$, ... Vse to je **ista točka**.

Ko pa te kote delimo z $n$, dobimo **različne** točke. Za kubični koren iz $-1$ ($n = 3$):
$$\frac{180^\circ}{3} = 60^\circ, \qquad \frac{540^\circ}{3} = 180^\circ, \qquad \frac{900^\circ}{3} = 300^\circ$$
To so tri različna števila, vsa pa na tretjo dajo $-1$ (kot $\cdot\, 3$ da $180^\circ$, $540^\circ$, $900^\circ$, kar je vse $180^\circ$). Naslednji, $\frac{1260^\circ}{3} = 420^\circ$, je spet isto kot $60^\circ$, zato več novih rešitev ni.

### Formula in izpeljava

Iščemo $z = r\,e^{i\varphi}$, za katerega je $z^n = w$, pri čemer je $w = |w|\,e^{i\psi}$. Po pravilu za potence:
$$z^n = r^n\,e^{in\varphi} = |w|\,e^{i\psi}$$
Dve števili sta enaki, če imata enako dolžino in enak kot (do polnih krogov natančno):
- **dolžina:** $r^n = |w| \;\Rightarrow\; r = \sqrt[n]{|w|}$ (navaden realni koren pozitivnega števila)
- **kot:** $n\varphi = \psi + k \cdot 360^\circ \;\Rightarrow\; \varphi_k = \dfrac{\psi + k \cdot 360^\circ}{n}$

Za $k = 0, 1, \ldots, n - 1$ dobimo $n$ različnih rešitev, za $k = n$ pa se začnejo ponavljati:
$$\boldsymbol{z_k = \sqrt[n]{|w|}\;e^{\,i\frac{\psi + 2\pi k}{n}}, \qquad k = 0, 1, \ldots, n - 1}$$

### Zakaj pravilni $n$-kotnik

- Vse rešitve imajo **isto dolžino** $\sqrt[n]{|w|}$, torej ležijo na **krožnici** s središčem v $0$ in polmerom $\sqrt[n]{|w|}$.
- Kota sosednjih rešitev se razlikujeta za $\dfrac{360^\circ}{n}$ (ker se $k$ poveča za $1$), torej so rešitve po krožnici **enakomerno razporejene**.

$n$ enakomerno razporejenih točk na krožnici so ravno oglišča **pravilnega $n$-kotnika** s središčem v izhodišču. Kvadratni koreni so 2 nasprotni točki, kubični enakostranični trikotnik, četrti kvadrat, peti pravilni petkotnik, ...

### Postopek

1. $w$ zapišeš v polarnem zapisu: $|w|$ in $\psi$.
2. **Polmer:** $r = \sqrt[n]{|w|}$.
3. **Prvi kot:** $\varphi_0 = \dfrac{\psi}{n}$.
4. **Ostali koti:** vsakič prišteješ $\dfrac{360^\circ}{n}$, dokler nimaš $n$ rešitev.
5. Po potrebi rešitve pretvoriš nazaj v $a + bi$.

### Primeri

**Primer 1:** $z^2 = -1$
- $w = -1$: dolžina $1$, kot $180^\circ$
- polmer: $\sqrt{1} = 1$
- prvi kot: $\frac{180^\circ}{2} = 90^\circ$, drugi: $90^\circ + \frac{360^\circ}{2} = 270^\circ$

$$z_0 = e^{i\pi/2} = i, \qquad z_1 = e^{i\,3\pi/2} = -i$$
Torej ima $-1$ dva kvadratna korena, $i$ in $-i$. Obe sta na enotski krožnici, nasprotni si.

**Primer 2:** $z^3 = 8$
- $w = 8$: dolžina $8$, kot $0^\circ$
- polmer: $\sqrt[3]{8} = 2$
- koti: $0^\circ$, $0^\circ + 120^\circ = 120^\circ$, $120^\circ + 120^\circ = 240^\circ$

$$z_0 = 2, \qquad z_1 = 2(\cos 120^\circ + i\sin 120^\circ) = -1 + \sqrt{3}i, \qquad z_2 = 2(\cos 240^\circ + i\sin 240^\circ) = -1 - \sqrt{3}i$$
Preizkus za $z_1$: dolžina $2^3 = 8$, kot $3 \cdot 120^\circ = 360^\circ = 0^\circ$, torej $z_1^3 = 8$ ✓

Rešitve so oglišča **enakostraničnega trikotnika** na krožnici s polmerom $2$:

```desmos-graph
width=280; height=280;
left=-3; right=3;
bottom=-3; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2=4|dashed
(2,0)|label:z0 = 2
(-1,1.732)|label:z1 = -1 + √3 i
(-1,-1.732)|label:z2 = -1 - √3 i
y=-0.577(x-2)|-1<x<2
x=-1|-1.732<y<1.732
y=0.577(x-2)|-1<x<2
```

**Primer 3:** $z^4 = -16$
- $w = -16$: dolžina $16$, kot $180^\circ$
- polmer: $\sqrt[4]{16} = 2$
- prvi kot: $\frac{180^\circ}{4} = 45^\circ$, nato vsakič $+\frac{360^\circ}{4} = +90^\circ$: $45^\circ$, $135^\circ$, $225^\circ$, $315^\circ$

$$z_0 = 2(\cos 45^\circ + i\sin 45^\circ) = \sqrt{2} + \sqrt{2}i, \qquad z_1 = -\sqrt{2} + \sqrt{2}i$$
$$z_2 = -\sqrt{2} - \sqrt{2}i, \qquad z_3 = \sqrt{2} - \sqrt{2}i$$
Preizkus za $z_0$: dolžina $2^4 = 16$, kot $4 \cdot 45^\circ = 180^\circ$, torej $z_0^4 = -16$ ✓

Tu prvi kot ni $0^\circ$, zato je **kvadrat zasukan** za $45^\circ$ (oglišča niso na oseh):

```desmos-graph
width=280; height=280;
left=-3; right=3;
bottom=-3; top=3;
xAxisLabel=Re; yAxisLabel=Im;
---
x^2+y^2=4|dashed
(1.414,1.414)|label:z0
(-1.414,1.414)|label:z1
(-1.414,-1.414)|label:z2
(1.414,-1.414)|label:z3
x=1.414|-1.414<y<1.414
x=-1.414|-1.414<y<1.414
y=1.414|-1.414<x<1.414
y=-1.414|-1.414<x<1.414
```

**Pogosta napaka:** najdeš samo prvo rešitev ($k = 0$) in pozabiš na ostale. Ker vedno nastane pravilni $n$-kotnik, je dovolj najti prvo oglišče, ostala pa dobiš z zasuki za $\frac{360^\circ}{n}$.
