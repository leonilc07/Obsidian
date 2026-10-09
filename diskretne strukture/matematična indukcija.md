velja samo za $\mathbb{N}$ 
  
# poteka v dveh korakih
## 1.  BAZA
n = 0
## 2. INDUKCJISKI KORAK
n -> n + 1
predpostavimo da lastnost velja za poljubno število **n**
lastnost velja za **n + 1**

če te dva koraka veljata potem lastost velja za vsa ${}\mathbb{N}{}$

### 1. primer: 

enačba:
$$
2 + 4 + 6 \dots 2n = n(n+1)
$$
želimo dokazati da je leva stran enaka desni.

BAZA:

Uzamemo bazo ki je v tem primiru 1 in jo preverimo.
$$
 n = 1\\
2 = 1 (1 + 1)\\
2 = 2\\
$$
INDUKCJISKI KORAK:

PREDPOSTAVIMO: ${}2 + 4 + 6 \dots 2n = n(n+1) {}$
RADI BI VIDELI: ${}2 + 4 + 6 \dots 2(n + 1) = (n+1)(n+2) {}$
RAČUNAMO: ${}2 + 4 + 6 \dots 2(n + 1) = n(n+1) +2 (n+1) = (n+1)(n+2){}$

*splošni člen povečaš za n+1 in potem prišteješ prejšni člen(n(n+1)) in nato dobiš isto kakor če bi tisti drugi člen povečal za n+1*

### 2. primer:

enačba:

$$
1 \cdot 2^1 + 2 \cdot 2^2 + \dots + n \cdot 2^n = (n-1) \cdot 2^{n+1} + 2
$$

BAZA:

$$
\begin{align}
n &= 1 \\
1 \cdot 2^1 &= (1-1) \cdot 2^{1+1} + 2 \\
2 &= 0 + 2 \\
2 &= 2
\end{align}
$$

INDUKCIJSKI KORAK:

PREDPOSTAVIMO: $1 \cdot 2^1 + 2 \cdot 2^2 + \dots + n \cdot 2^n = (n-1) \cdot 2^{n+1} + 2$
RADI BI VIDELI: $1 \cdot 2^1 + 2 \cdot 2^2 + \dots + n \cdot 2^n + (n+1) \cdot 2^{n+1} = n \cdot 2^{n+2} + 2$
RAČUNAMO:

$$
\begin{align}
1 \cdot 2^1 + \dots + n \cdot 2^n + (n+1) \cdot 2^{n+1} &= (n-1) \cdot 2^{n+1} + 2 + (n+1) \cdot 2^{n+1} \\
&= 2^{n+1} \, (n - 1 + n + 1) + 2 \\
&= 2n \cdot 2^{n+1} + 2 \\
&= n \cdot 2^{n+2} + 2
\end{align}
$$
### 3. Primer: Fibonaccijevo zaporedje

Fibonaccijevo zaporedje je zaporedje, v katerem je vsak člen vsota prejšnjih dveh:

$$
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad (n \geq 2)
$$

Prvi členi:

| $n$   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $F_n$ | 0   | 1   | 1   | 2   | 3   | 5   | 8   | 13  | 21  | 34  | 55  |

- Rekurzivna formula $F_n = F_{n-1} + F_{n-2}$ nam omogoča, da vsak člen izrazimo z manjšimi. To uporabljamo v indukcijskem koraku.
- Nekateri avtorji začnejo z $F_1 = F_2 = 1$ in izpustijo $F_0$. Zaporedje je isto, razlikuje se samo začetek oštevilčenja.

---

#### Naloga

Pokazati moramo, da je za vsak $n \in \mathbb{N}$ število $F_{4n}$ deljivo s 3.

BAZA:

Za $n = 1$ je $F_4 = 3 = 3 \cdot 1$, kar je deljivo s 3.

INDUKCIJSKI KORAK

PREDPOSTAVIMO: $F_{4n} = 3k$, $k \in \mathbb{Z}$
RADI BI VIDELI: $F_{4(n+1)} = 3l$, $l \in \mathbb{Z}$
RAČUNAMO: $F_{4(n+1)}$ razpišemo z rekurzivno formulo, dokler ne pridemo do členov $F_{4n+1}$ in $F_{4n}$:

$$
\begin{align}
F_{4n+4} &= F_{4n+3} + F_{4n+2} \\
&= (F_{4n+2} + F_{4n+1}) + F_{4n+2} \\
&= 2F_{4n+2} + F_{4n+1} \\
&= 2(F_{4n+1} + F_{4n}) + F_{4n+1} \\
&= 3F_{4n+1} + 2F_{4n}
\end{align}
$$

Zdaj uporabimo predpostavko $F_{4n} = 3k$:

$$
\begin{align}
F_{4n+4} &= 3F_{4n+1} + 2 \cdot 3k \\
&= 3F_{4n+1} + 6k \\
&= 3 \, (F_{4n+1} + 2k)
\end{align}
$$

Ker sta $F_{4n+1}$ in $k$ celi števili, je tudi $l = F_{4n+1} + 2k$ celo število. Torej je $F_{4(n+1)} = 3l$, kar je deljivo s 3. $\blacksquare$
### 4. Primer:
enačba:

$$
3 \mid 5^n + 2 \cdot 11^n
$$

želimo dokazati da je izraz $5^n + 2 \cdot 11^n$ deljiv s 3 za vsak $n \in \mathbb{N}$.

BAZA:

$$
\begin{align}
n &= 1 \\
5^1 + 2 \cdot 11^1 &= 5 + 22 \\
&= 27 = 3 \cdot 9
\end{align}
$$

INDUKCIJSKI KORAK

PREDPOSTAVIMO: $5^n + 2 \cdot 11^n = 3k$, $k \in \mathbb{Z}$
RADI BI VIDELI: $5^{n+1} + 2 \cdot 11^{n+1} = 3l$, $l \in \mathbb{Z}$
RAČUNAMO: koeficiente razbijemo tako, da se pojavi predpostavka $5^n + 2 \cdot 11^n$ (pomnožena z 2):

$$
\begin{align}
5^{n+1} + 2 \cdot 11^{n+1} &= 5 \cdot 5^n + 22 \cdot 11^n \\
&= (2 + 3) \cdot 5^n + (4 + 18) \cdot 11^n \\
&= 2 \cdot 5^n + 4 \cdot 11^n + 3 \cdot 5^n + 18 \cdot 11^n \\
&= 2 \, (5^n + 2 \cdot 11^n) + 3 \cdot 5^n + 18 \cdot 11^n \\
&= 2 \cdot 3k + 3 \cdot 5^n + 18 \cdot 11^n \\
&= 3 \, (2k + 5^n + 6 \cdot 11^n)
\end{align}
$$

Ker so $k$, $5^n$ in $11^n$ cela števila, je tudi $l = 2k + 5^n + 6 \cdot 11^n \in \mathbb{Z}$. Torej je $5^{n+1} + 2 \cdot 11^{n+1} = 3l$, kar je deljivo s 3. $\blacksquare$
### 5. Primer:
enačba:

$$
n! < n^{n-1}, \quad n \geq 3
$$

želimo dokazati da to velja za vsak $\mathbb{N} \geq 3$.

BAZA:

$$
\begin{align}
n &= 3 \\
3! &< 3^{3-1} \\
6 &< 9
\end{align}
$$

INDUKCIJSKI KORAK

PREDPOSTAVIMO: $n! < n^{n-1}$
RADI BI VIDELI: $(n+1)! < (n+1)^n$
RAČUNAMO: $$ \begin{align} (n+1)! = (n+1) \cdot n! &< (n+1) \cdot n^{n-1} \\ &< (n+1) \cdot (n+1)^{n-1} \\ &= (n+1)^n \end{align} $$ Torej je $(n+1)! < (n+1)^n$. $\blacksquare$
### 6. primer:

#### Pojmi

**Konveksen mnogokotnik:** mnogokotnik je konveksen, če za poljubni dve točki v njem tudi cela daljica med njima leži v mnogokotniku. Enakovredno: vsi notranji koti so manjši od $180°$, vse diagonale pa ležijo znotraj mnogokotnika.

**Diagonala:** daljica, ki povezuje dve nesosednji oglišči mnogokotnika.

**Triangulacija:** razdelitev mnogokotnika na trikotnike z diagonalami, ki se v notranjosti ne sekajo. Trikotniki pokrijejo cel mnogokotnik in se prekrivajo samo po stranicah ali ogliščih. "Brez dodatnih oglišč" pomeni, da so oglišča trikotnikov samo oglišča mnogokotnika.

#### Trditev

Vsaka triangulacija konveksnega $n$-kotnika ($n \geq 3$) ima natanko $n-2$ trikotnikov.

BAZA:

$$
\begin{align}
n &= 3 \\
n - 2 &= 1
\end{align}
$$

Trikotnik se ne da razdeliti naprej, zato je njegova edina triangulacija on sam, to pa je 1 trikotnik.

INDUKCIJSKI KORAK

PREDPOSTAVIMO: vsaka triangulacija konveksnega $n$-kotnika ima $n-2$ trikotnikov.
RADI BI VIDELI: vsaka triangulacija konveksnega $(n+1)$-kotnika ima $(n+1)-2 = n-1$ trikotnikov.
RAČUNAMO:

Vzamemo poljubno triangulacijo konveksnega $(n+1)$-kotnika. Ker je $n+1 \geq 4$, v njej obstaja trikotnik, ki ima dve stranici na robu mnogokotnika (dokaz je v dodatku). Imenujmo ga $\Delta$ in naj bo $A$ oglišče, kjer se ti dve stranici stikata.

Ko trikotnik $\Delta$ odrežemo, ostane konveksen $n$-kotnik (oglišče $A$ izgine). Ostali trikotniki so triangulacija tega $n$-kotnika, saj se nobeden drug trikotnik ne dotika oglišča $A$ (kot pri $A$ je v celoti zapolnjen z $\Delta$). Po predpostavki ima ta triangulacija $n-2$ trikotnikov. Skupaj z odrezanim trikotnikom:

$$
(n-2) + 1 = n-1 = (n+1) - 2
$$

Torej ima vsaka triangulacija konveksnega $(n+1)$-kotnika $(n+1)-2$ trikotnikov. $\blacksquare$

#### Dodatek: zakaj obstaja trikotnik z dvema stranicama na robu

Trditev: v vsaki triangulaciji konveksnega $m$-kotnika, $m \geq 4$, obstaja trikotnik z dvema stranicama na robu mnogokotnika (imenujemo ga "ušesce").

Dokaz:
1. Triangulacija vsebuje vsaj eno diagonalo. Če je ne bi, bi imel vsak trikotnik vse tri stranice na robu mnogokotnika, to pa je mogoče samo za $m = 3$.
2. Vsaka diagonala razdeli mnogokotnik na dva manjša konveksna mnogokotnika. Izmed vseh diagonal triangulacije in njunih strani izberemo tisto stran z najmanj oglišči. Naj bo to mnogokotnik $Q$.
3. Če bi imel $Q$ več kot 3 oglišča, bi ga triangulacija morala deliti naprej z novo diagonalo (po koraku 1). Ta bi imela na eni strani še manj oglišč, kar je protislovje.
4. Torej je $Q$ trikotnik. Ima eno stranico (diagonalo) in dve stranici, ki sta na robu mnogokotnika, ker med krajiščema diagonale leži natanko eno oglišče. $\square$