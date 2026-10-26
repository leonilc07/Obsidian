# Binarna števila

## Nepredznačena cela števila

**Binarno → desetiško:** vsak bit pomnožiš z $2^{\text{mesto}}$ (mesta štejemo od desne, od 0) in sešteješ.

$$10011_2 = 1\cdot2^4 + 0\cdot2^3 + 0\cdot2^2 + 1\cdot2^1 + 1\cdot2^0 = 16 + 2 + 1 = 19$$

**Desetiško → binarno:**
- razstaviš na potence števila 2: $19 = 16 + 2 + 1 = 2^4 + 2^1 + 2^0 \to 10011$
- ali deliš z 2 in pišeš ostanke, nato jih bereš **od spodaj navzgor**:

```
19 / 2 = 9   ostanek 1   ↑
 9 / 2 = 4   ostanek 1   |
 4 / 2 = 2   ostanek 0   |
 2 / 2 = 1   ostanek 0   |
 1 / 2 = 0   ostanek 1   |
```
→ $10011$

## Predznak in velikost

**Prvi bit je predznak:** 0 pomeni pozitivno, 1 negativno. Ostali biti so velikost.

- $010011 \to +19$
- $110011 \to -19$

Primer: zapiši $-6$ s 5 biti → $6 = 110$, dopolniš na 4 bite $0110$, dodaš predznak 1 → $10110$.

Slabosti: **dve ničli** ($00000 = +0$ in $10000 = -0$), seštevanje se ne da narediti kar navadno.

## Dvojiški komplement

- **Pozitivna** števila pretvorimo normalno.
- **Negativna**: absolutno vrednost zapišemo binarno, **invertiramo bite** ($0 \to 1$, $1 \to 0$) in **prištejemo 1**.
- Prvi bit je še vedno 1 pri negativnih, ampak **samo ena ničla**, seštevanje deluje normalno.
- Z $n$ biti zapišemo od $-2^{n-1}$ do $2^{n-1}-1$ (s 3 biti od $-4$ do $3$, s 4 biti od $-8$ do $7$).

Krog za 3 bite: $000 = 0$, $001 = 1$, $010 = 2$, $011 = 3$, $100 = -4$, $101 = -3$, $110 = -2$, $111 = -1$.

### Naloga
Kako izgledata $+6$ in $-3$ s 4 biti v dvojiškem komplementu?

**+6:** pozitivno, pretvorimo normalno → $6 = 4 + 2$ → $\mathbf{0110}$

**−3:**
1. $3 \to 0011$
2. invertiramo → $1100$
3. prištejemo 1 → $1100 + 1 = \mathbf{1101}$

Preverjanje: $0011 + 1101 = 1\,0000$ → odrežemo 5. bit → $0000$, torej $3 + (-3) = 0$ ✓

## Znanstveni zapis (mantisa in eksponent)

Oblika: $\pm M \times B^{\pm E}$ ($M$ mantisa, $B$ osnova, pri nas 2, $E$ eksponent)

Decimalke v binarnem: $2^{-1} = \frac12$, $2^{-2} = \frac14$, $2^{-3} = \frac18$, $2^{-4} = \frac1{16}$ …

**Postopek:**
1. pretvorimo v binarno
2. **normaliziramo**: vejico premaknemo levo od prve enice → $0{,}1\ldots \times 2^E$
3. mantisa = predznak + biti za vejico (od desne dopolnimo z 0), eksponent = predznak + $E$ (od leve dopolnimo z 0)

**Primer:** 4,75; 8 bitov za mantiso, 6 za eksponent
1. $4{,}75 = 2^2 + 2^{-1} + 2^{-2} = 100{,}11$
2. $0{,}10011 \times 2^3$, $3 \to 11$
- mantisa: $0\,1001100$
- eksponent: $0\,00011$

### Naloga 7
Notranja predstavitev, mantisa 10 bitov in eksponent 6 bitov (oba v zapisu predznak in velikost). Najmanj koliko bitov potrebujemo, da ne izgubimo natančnosti?

**a) +0,25**
1. $0{,}25 = 2^{-2} = 0{,}01$
2. $0{,}1 \times 2^{-1}$
- mantisa: $\mathbf{0\,100000000}$
- eksponent: $\mathbf{1\,00001}$ ($-1$)
- **najmanj:** mantisa 2 bita ($0\,1$), eksponent 2 bita ($1\,1$)

**b) $-32\frac1{16}$**
1. $32\frac1{16} = 2^5 + 2^{-4} = 100000{,}0001$
2. $0{,}1000000001 \times 2^6$, $6 \to 110$
- za vejico je **10 bitov**, z predznakom bi mantisa rabila 11 → v 10 bitov gre samo 9, zadnja enica ($\frac1{16}$) **se izgubi**
- mantisa: $\mathbf{1\,100000000}$ (shrani se $-32$)
- eksponent: $\mathbf{0\,00110}$
- **najmanj:** mantisa 11 bitov ($1\,1000000001$), eksponent 4 biti ($0\,110$)

## Shranjevanje drugih podatkov

**Tekst:** vsakemu simbolu pripada koda, ki se pretvori v binarni zapis.
- **ASCII**: 7 bitov (razširjen 8 bitov), samo 128 (256) znakov, angleška abeceda, števke, ločila. `A` = 65, `a` = 97, `0` = 48.
- **UNICODE**: skoraj vsi znaki vseh jezikov in emojiji. Prvih 128 kod je enakih kot v ASCII. Pogosto kodiranje UTF-16 (16 bitov na znak) ali UTF-8 (1–4 bajti, ASCII znaki ostanejo 1 bajt).
- velikost = število znakov × bitov na znak

**Zvok:** na določene intervale **vzorčimo amplitudo** (analogni val pretvorimo v zaporedje števil).
- **frekvenca vzorčenja** (Hz): kolikokrat na sekundo izmerimo amplitudo (CD: 44.100 Hz)
- **bitna globina**: s koliko biti zapišemo en vzorec (CD: 16 bitov)
- velikost = čas [s] × frekvenca × bitna globina (× število kanalov, npr. 2 za stereo)

**Slika:** dvodimenzionalna **matrika točk (pikslov)**, kjer izmerimo intenziteto svetlobe.
- črno-bela: 1 bit na piksel, sivinska: 8 bitov
- **RGB**: vsak piksel ima 3 barve (rdeča, zelena, modra) po 8 bitov → **24 bitov na piksel**
- velikost = širina × višina × bitov na piksel

**Stiskanje:** stopnja stiskanja = originalna velikost : stisnjena velikost. Brez izgub (ZIP, PNG) ali z izgubami (MP3, JPEG).

### Naloga: niz "X+Y"

ASCII kode: `X` = 88, `+` = 43, `Y` = 89

**8-bitni ASCII** (24 bitov):
$$01011000\ \ 00101011\ \ 01011001$$

**16-bitni UNICODE** (U+0058, U+002B, U+0059, 48 bitov): spredaj dodamo 8 ničel
$$00000000\,01011000\ \ 00000000\,00101011\ \ 00000000\,01011001$$

### Naloga: triminutna pesem

$3\text{ min} = 180\text{ s}$

$$180 \cdot 40\,000 \cdot 16 = \mathbf{115\,200\,000\text{ bitov}} \approx 115{,}2\text{ Mb}$$

S stiskanjem 5:1:
$$\frac{115\,200\,000}{5} = \mathbf{23\,040\,000\text{ bitov}} \approx 23\text{ Mb}$$

### Naloga: RGB slika 1200 × 800

$$1200 \cdot 800 \cdot 24 = \mathbf{23\,040\,000\text{ bitov}} \approx 23\text{ Mb}$$

Stisnjeno na 2,4 Mb = 2 400 000 bitov:
$$\frac{23\,040\,000}{2\,400\,000} = 9{,}6 \Rightarrow \textbf{stopnja stiskanja } \mathbf{9{,}6 : 1}$$
