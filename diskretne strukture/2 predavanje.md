# Reševanje ukazov
Kako pokazati, da sta dva izraza enakovredna?
- s pravilnostno tabelo
- s preoblikovanjem

Kako pokazati, da nista enakovredna?
- dovolj je ena sama vrstica

Primer: napiši izraz za to pravilnostno tabelo:

| p   | q   | r   | A   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |
Rešitev 1: za vsako vrstico, kjer je vrednost 1, napišemo izjavo s konjunkcijami med členi. Nato vse konjunkcije združimo z disjunkcijo in dobimo **disjunktivno normalno obliko (DNO)** $A_{DNO}$.

| p   | q   | r   | konjunkcija                       |
| --- | --- | --- | --------------------------------- |
| 0   | 0   | 1   | $\neg p \land \neg q \land r$      |
| 0   | 1   | 1   | $\neg p \land q \land r$           |
| 1   | 0   | 0   | $p \land \neg q \land \neg r$      |
| 1   | 0   | 1   | $p \land \neg q \land r$           |
| 1   | 1   | 1   | $p \land q \land r$                |

$$
A_{DNO} = (\neg p \land \neg q \land r) \lor (\neg p \land q \land r) \lor (p \land \neg q \land \neg r) \lor (p \land \neg q \land r) \lor (p \land q \land r)
$$

Rešitev 2: za vsako vrstico, kjer je vrednost 0, napišemo izjavo z disjunkcijami med členi. Spremenljivko z vrednostjo 0 zapišemo tako, kot je, spremenljivko z vrednostjo 1 pa negiramo (disjunkcija je tako v tej vrstici 0). Nato vse disjunkcije združimo s konjunkcijo in dobimo **konjunktivno normalno obliko (KNO)** $A_{KNO}$.

| p   | q   | r   | disjunkcija                    |
| --- | --- | --- | ------------------------------ |
| 0   | 0   | 0   | $p \lor q \lor r$              |
| 0   | 1   | 0   | $p \lor \neg q \lor r$         |
| 1   | 1   | 0   | $\neg p \lor \neg q \lor r$    |

$$
A_{KNO} = (p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor r)
$$

Poenostavitev KNO:

$$
\begin{aligned}
A_{KNO} &= (p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor r) \\
&\sim ((p \lor r) \lor q) \land ((p \lor r) \lor \neg q) \land (\neg p \lor \neg q \lor r) && \text{komutativnost, asociativnost} \\
&\sim ((p \lor r) \lor (q \land \neg q)) \land (\neg p \lor \neg q \lor r) && \text{distributivnost} \\
&\sim ((p \lor r) \lor 0) \land (\neg p \lor \neg q \lor r) && A \land \neg A \sim 0 \\
&\sim (p \lor r) \land ((\neg p \lor \neg q) \lor r) && A \lor 0 \sim A \\
&\sim (p \land (\neg p \lor \neg q)) \lor r && \text{distributivnost} \\
&\sim ((p \land \neg p) \lor (p \land \neg q)) \lor r && \text{distributivnost} \\
&\sim (0 \lor (p \land \neg q)) \lor r && A \land \neg A \sim 0 \\
&\sim p \land \neg q \lor r && A \lor 0 \sim A
\end{aligned}
$$

Če poenostavimo DNO, dobimo isti rezultat: $A_{DNO} \sim p \land \neg q \lor r$.

Rezultat lahko zapišemo še z implikacijami:

$$
\begin{aligned}
p \land \neg q \lor r &\sim \neg(\neg p \lor q) \lor r && \text{De Morgan, dvojna negacija} \\
&\sim \neg(p \implies q) \lor r && A \implies B \sim \neg A \lor B \\
&\sim (p \implies q) \implies r && A \implies B \sim \neg A \lor B \\
&\sim p \implies q \implies r && \text{opuščanje oklepajev (od leve proti desni)}
\end{aligned}
$$
## Nabori veznikov
$\{\neg, \lor\}$ je poln nabor, kar pomeni, da lahko vsak izjavni izraz zapišemo samo z vezniki iz tega nabora.

Dokažemo ga tako, da vzamemo drug poln nabor, recimo $\{\neg, \lor, \land\}$ (poln je, ker lahko vsak izraz zapišemo v DNO), in pokažemo, da lahko $\land$ izrazimo z vezniki iz prvega nabora:

$$
\begin{aligned}
A \land B &\sim \neg\neg(A \land B) && \text{dvojna negacija} \\
&\sim \neg(\neg A \lor \neg B) && \text{De Morgan}
\end{aligned}
$$

Torej $A \land B \sim \neg(\neg A \lor \neg B)$, kar vsebuje samo $\neg$ in $\lor$. Vsak $\land$ v izrazu lahko tako zamenjamo, zato je $\{\neg, \lor\}$ poln nabor. $\blacksquare$

### Nabor $\{0, \implies\}$
Trdimo, da je $\{0, \implies\}$ poln nabor. Vzamemo poln nabor $\{\neg, \lor\}$ in pokažemo, da lahko $\neg$ in $\lor$ izrazimo samo z $0$ in $\implies$:

$$
\neg A \sim A \implies 0 \qquad \text{(lastnosti 0 in 1)}
$$

$$
\begin{aligned}
A \lor B &\sim \neg\neg A \lor B && \text{dvojna negacija} \\
&\sim \neg A \implies B && A \implies B \sim \neg A \lor B \\
&\sim (A \implies 0) \implies B && \neg A \sim A \implies 0
\end{aligned}
$$

Oba veznika iz $\{\neg, \lor\}$ smo izrazili z $0$ in $\implies$, zato je $\{0, \implies\}$ poln nabor. $\blacksquare$

### Zakaj $\{1, \implies\}$ ni poln nabor
Vsak izraz, ki ga sestavimo samo iz $1$, $\implies$ in spremenljivk, je resničen, ko so vse spremenljivke enake 1:
- konstanta $1$ je vedno 1,
- spremenljivka $p$ je pri $p = 1$ enaka 1,
- če sta $A$ in $B$ enaka 1, je tudi $A \implies B$ enako $1 \implies 1 = 1$.

Takemu izrazu pravimo, da **ohranja enico**. Zato z $\{1, \implies\}$ ne moremo zapisati izraza, ki je pri vseh spremenljivkah 1 enak 0, npr. $\neg p$ (pri $p = 1$ je $\neg p = 0$) ali konstante $0$. Nabor torej ni poln.