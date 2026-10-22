374,6895

| 3           | 7           | 4           | ,   | 6              | 8              | 9              | 5              |
| ----------- | ----------- | ----------- | --- | -------------- | -------------- | -------------- | -------------- |
| $3\cdot10^2$ | $7\cdot10^1$ | $4\cdot10^0$ |     | $6\cdot10^{-1}$ | $8\cdot10^{-2}$ | $9\cdot10^{-3}$ | $5\cdot10^{-4}$ |
| 300         | 70          | 4           |     | 0,6            | 0,08           | 0,009          | 0,0005         |

$374,6895 = 3\cdot10^2 + 7\cdot10^1 + 4\cdot10^0 + 6\cdot10^{-1} + 8\cdot10^{-2} + 9\cdot10^{-3} + 5\cdot10^{-4}$

$1011,00101_2$

| 1           | 0           | 1           | 1           | ,                          | 0              | 0              | 1              | 0              | 1              |
| ----------- | ----------- | ----------- | ----------- | -------------------------- | -------------- | -------------- | -------------- | -------------- | -------------- |
| $1\cdot2^3$ | $0\cdot2^2$ | $1\cdot2^1$ | $1\cdot2^0$ | **ne znam zapisati vejce** | $0\cdot2^{-1}$ | $0\cdot2^{-2}$ | $1\cdot2^{-3}$ | $0\cdot2^{-4}$ | $1\cdot2^{-5}$ |
| 8           | 0           | 2           | 1           |                            | 0              | 0              | 0,125          | 0              | 0,03125        |

$1011,00101_2 = 1\cdot2^3 + 0\cdot2^2 + 1\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} + 1\cdot2^{-3} + 0\cdot2^{-4} + 1\cdot2^{-5} = 11,15625_{10}$

## bodi vejca vedno na istem mestu(fiksna vejca fixet point)
recimo postavimo vejco vedno med bit bk-1 in bk
Splošno: $b_{n-1} \dots b_{k+1}\, b_k\, ,\, b_{k-1} \dots b_1\, b_0$ ($n$ bitov, od tega $k$ za vejico)

| $b_{n-1}$               | …   | $b_{k+1}$         | $b_k$         | ,   | $b_{k-1}$            | …   | $b_1$                | $b_0$            |
| ----------------------- | --- | ----------------- | ------------- | --- | -------------------- | --- | -------------------- | ---------------- |
| $b_{n-1}\cdot2^{n-1-k}$ | …   | $b_{k+1}\cdot2^1$ | $b_k\cdot2^0$ |     | $b_{k-1}\cdot2^{-1}$ | …   | $b_1\cdot2^{-(k-1)}$ | $b_0\cdot2^{-k}$ |
zgled: 
n=8, k=3, x= 11011001

Vejica je med $b_3$ in $b_2$ → $x = 11011,001_2$

| $b_7$       | $b_6$       | $b_5$       | $b_4$       | $b_3$       | ,   | $b_2$          | $b_1$          | $b_0$          |
| ----------- | ----------- | ----------- | ----------- | ----------- | --- | -------------- | -------------- | -------------- |
| 1           | 1           | 0           | 1           | 1           | ,   | 0              | 0              | 1              |
| $1\cdot2^4$ | $1\cdot2^3$ | $0\cdot2^2$ | $1\cdot2^1$ | $1\cdot2^0$ |     | $0\cdot2^{-1}$ | $0\cdot2^{-2}$ | $1\cdot2^{-3}$ |
| 16          | 8           | 0           | 2           | 1           |     | 0              | 0              | 0,125          |

$v(x) = 16 + 8 + 2 + 1 + 0,125 = 27,125$

Splošna enačba:
$$v(x) = \sum_{i=0}^{n-1} b_i \cdot 2^{i}$$
**Težave:** ($n = 4$, $k = 1$)

a) **Natančnost:** najmanjša razlika med sosednjima številoma je najbolj desni bit: $2^{-k} = 2^{-1} = 0,5$
- $010,0_2 = 2$ in $010,1_2 = 2,5$ → vmesnih števil (npr. $2,3$) ne moremo zapisati
- obseg: od $0$ do $111,1_2 = 7,5$

b) **Popravek:** vejico premaknemo v levo, npr. na $k = 3$
- $1011 \to 1,011_2 = 1,375$
- najmanjša razlika je zdaj $2^{-3} = 0,125$ → večja natančnost
- **ampak se zmanjša obseg:** največje število je $1,111_2 = 1,875$ (prej $7,5$)

**Sklep:** v računalništvu ne moremo biti absolutno natančni.
- Najmanjša razlika med dvema sosednjima številoma se imenuje **ULP** (*Unit in the Last Place* oz. *Unit of Least Precision*).
- Pri fiksni vejici je $\text{ULP} = 2^{-k}$.
Recimo, da imamo 3 bite za vejico. Potem lahko za vejico predstavimo le te vrednosti:

| biti za vejico | izračun                       | vrednost |
| -------------- | ----------------------------- | -------- |
| ,000           | $0$                           | 0,0      |
| ,001           | $2^{-3}$                      | 0,125    |
| ,010           | $2^{-2}$                      | 0,25     |
| ,011           | $2^{-2} + 2^{-3}$             | 0,375    |
| ,100           | $2^{-1}$                      | 0,5      |
| ,101           | $2^{-1} + 2^{-3}$             | 0,625    |
| ,110           | $2^{-1} + 2^{-2}$             | 0,75     |
| ,111           | $2^{-1} + 2^{-2} + 2^{-3}$    | 0,875    |

## Vejica ni fiksna (plavajoča vejica – *floating point*)
Vejico premikamo z **eksponentom**, **baza pa ostane ista**. Isto število lahko zapišemo na več načinov:

| desetiško (baza 10)       | dvojiško (baza 2)           |
| ------------------------- | --------------------------- |
| $9830 \cdot 10^{-1}$      | $1011000 \cdot 2^{-3}$      |
|                           | $101100 \cdot 2^{-2}$       |
|                           | $10110 \cdot 2^{-1}$        |
| $983 \cdot 10^{0}$        | $1011 \cdot 2^{0}$          |
| $98,3 \cdot 10^{1}$       | $101,1 \cdot 2^{1}$         |
| $9,83 \cdot 10^{2}$       | $10,11 \cdot 2^{2}$         |
| $0,983 \cdot 10^{3}$      | $1,011 \cdot 2^{3}$         |

Vejica v levo → eksponent $+1$, vejica v desno → eksponent $-1$.

**Ideja:** število zapišemo z **velikostjo** (mantiso) in **eksponentom** → potrebujemo dve ločeni števili.

Zgled: $10,101110_2$
- velikost: $10101110_2$ (vejico odstranimo)
- eksponent: $-110$ (6 bitov je bilo za vejico)
- zapis: $10,101110_2 = 10101110_2 \cdot 2^{-110} = \dfrac{174}{64} = 2,71875$
Dogovoriti se moramo:
- koliko bitov za velikost,
- koliko bitov za eksponent,
- kako bomo kodirali velikost in eksponent.

To je določila organizacija **IEEE** s standardom **IEEE 754**.

### IEEE 754
Število v plavajoči vejici lahko zapišemo z 32, 64 ali 128 biti:
- **32 bitov** – enojna natančnost (*single precision*) → omejili se bomo samo na to
- **64 bitov** – dvojna natančnost (*double precision*)
- **128 bitov** – četvorna natančnost (*quadruple precision*)

**Normalizacija:** isto število lahko zapišemo na več načinov, npr. $1001_2$:
- $1001 \cdot 2^0 = 100,1 \cdot 2^1 = 10,01 \cdot 2^2 = 1,001 \cdot 2^3 = 0,1001 \cdot 2^4 = \dots$

Ker moramo vedno vedeti, kje je vejica, se dogovorimo:
1. pred vejico je vedno **samo en bit**,
2. ta bit je vedno **1**.

Eksponent torej vedno nastavimo tako, da je pred vejico 1:
- $1110_2 = 1,110 \cdot 2^{3}$
- $0010_2 = 1,0 \cdot 2^{1}$
- $0,01101_2 = 1,101 \cdot 2^{-2}$

**Skrita enica:** ker se vsako število začne z 1, te enice ni treba zapisati. Shranimo samo bite za vejico → to je **mantisa**.
### 32-bitni zapis IEEE 754

| biti     | 31        | 30 – 23   | 22 – 0  |
| -------- | --------- | --------- | ------- |
| pomen    | predznak  | eksponent | mantisa |
| št. bitov | 1        | 8         | 23      |
**Vrednost:**

#### Normalizirana števila
$$v = (-1)^{p} \cdot 1,m \cdot 2^{E-127}$$
- $p$ – predznak (0 = pozitivno, 1 = negativno)
- $1,m$ – skrita enica + mantisa
- $E$ – shranjeni eksponent (8 bitov, 0 – 255); pravi eksponent je $E - 127$ (odmik 127), da lahko zapišemo tudi negativne eksponente

**Primer:** $x = 0\,10110100\,11100000000000000000000$

| del       | biti                      | vrednost                          |
| --------- | ------------------------- | --------------------------------- |
| predznak  | $0$                       | $p = 0$ → pozitivno               |
| eksponent | $10110100$                | $E = 128 + 32 + 16 + 4 = 180$     |
| mantisa   | $1110\,0000\dots0$        | $1,m = 1,111_2 = 1,875$           |

- pravi eksponent: $E - 127 = 180 - 127 = 53$
- $1,111_2 = 1 + 0,5 + 0,25 + 0,125 = 1,875$

$$v = (-1)^0 \cdot 1,111_2 \cdot 2^{53} = +(1 + 2^{-1} + 2^{-2} + 2^{-3}) \cdot 2^{53}$$
$$v = +(2^{53} + 2^{52} + 2^{51} + 2^{50})$$
**Vprašanje:** ali lahko vsa števila zapišemo tako, da je spredaj vedno 1?

Poskusimo na številih, kjer za eksponent uporabimo samo **3 bite**:
- $0,00001_2 = 0,00001 \cdot 2^{0} = 0,0001 \cdot 2^{-1} = \dots = 1,0 \cdot 2^{-5}$

**Težava:** eksponent s 3 biti je zapisan z odmikom, zato je **najmanjši eksponent $-3$**, potrebujemo pa $-5$.
- Vejico lahko premaknemo največ do $0,00001_2 = 0,01 \cdot 2^{-3}$ → spredaj ni 1.
- Odgovor: **ne**, vseh števil ne moremo zapisati tako, da je spredaj 1.

**Rešitev – denormalizirana števila:** dogovorimo se, da kadar so v eksponentu **same ničle**, se število ne začne z 1, ampak z **0**.
- Takim številom rečemo **denormalizirana števila**.