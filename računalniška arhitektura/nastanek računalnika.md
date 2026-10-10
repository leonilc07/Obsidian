# Volume 1: kaj se da izračunati?
- majhne probleme – **da**
- velike probleme – **ne**

# Volume 2: življenjska vprašanja
Kakšen naj bo stroj, s katerim se da izračunati vse, kar je izračunljivo?

# Volume 3: the chosen one
Turing je pogruntal **Turingov stroj** – matematični zapis takega stroja, ne pa dejanske izvedbe (predpostavil je, da ima stroj neskončen trak).

# Volume 4: ugibanje realnosti
Ali lahko tak stroj tudi zares naredimo?

Von Neumann je predlagal računalnik, ki je v osnovi Turingov stroj, vendar prilagojen realnosti.

Danes so skoraj vsi računalniki von Neumannovi računalniki – pravimo, da imajo **von Neumannovo arhitekturo**.

# Volume 5: in the words of a genius
Vprašanja, na katera je bilo treba odgovoriti:
- Kako lahko computing machine (= **računalnik**) dobi navodila za računanje (= **ukaze**)?
- Kje naj bodo ukazi shranjeni?
- Kako naj bodo zapisani?
- V kakšnem vrstnem redu naj računalnik jemlje ukaze?
- Kje naj bodo podatki za računanje (= **operandi**)?
- Kako naj bo v ukazih zapisan podatek o lokaciji (mestu, kjer so shranjeni operandi)?
- Kako naj bodo ukazi in operandi zapisani (= **kodirani**) v računalniku razumljivi obliki?
- Kako naj bo računalnik povezan z okolico?

> [!important]
> Podatek o lokaciji operandov mora biti del ukaza.

# Volume 6: too smart to exit
Von Neumannova arhitektura odgovori na zgornja vprašanja:
1. Računalnik deluje izključno na osnovi ukazov – internega ožičenja računalnika ne spreminjamo. Temu pravimo **računalnik s shranjenim programom**.
2. Ukazi naj bodo shranjeni v enem delu računalnika, ki mu rečemo **pomnilnik**.
3. Tudi operandi naj bodo shranjeni v pomnilniku.
4. Ukazi naj bodo shranjeni eden za drugim; takemu zaporedju ukazov rečemo **program**.
5. V računalniku potrebujemo nekaj, kar bo na osnovi ukazov in operandov računalo, torej izvajalo ukaze in zahtevane operacije. To je **centralna procesna enota** (CPE, angl. *central processing unit*, CPU).
6. Kako naj CPE ve, kje je naslednji ukaz? CPE naj ima nekaj, kamor ob zagonu računalnika zapišemo, kje se nahaja prvi ukaz. Ker so ukazi shranjeni zaporedno, CPE to vrednost po vsakem izvedenem ukazu samodejno poveča za 1. Temu rečemo **programski števec** (angl. *program counter*, PC): hrani **naslov** (angl. *address*, lokacija ukaza v pomnilniku) naslednjega ukaza.
7. Vzemimo ukaz »seštej A in B ter rezultat shrani v C«. A, B in C so operandi. Operandi so v pomnilniku, ukaz pa vsebuje le njihove naslove. CPE mora zato A in B prebrati iz pomnilnika, ju shraniti pri sebi, sešteti in rezultat shraniti v pomnilnik na naslov C. CPE torej potrebuje **majhen lasten pomnilnik** za začasno shranjevanje operandov.
8. CPE mora imeti enoto, ki dejansko računa, torej izvaja aritmetične in logične operacije. To je **aritmetično-logična enota** (ALE).
9. Računalnik mora imeti možnost, da podatke dobi iz zunanjega sveta in jih v zunanji svet tudi pošlje. Za to skrbijo **vhodno-izhodne enote**.
10. Kaj sme CPE spreminjati v pomnilniku? Operande **da**, ukazov **ne**.

# Volume 7: IQ too high
## Amdahlov zakon

Amdahl se je vprašal: ali lahko z $N$ von Neumannovimi računalniki nek program izvedemo $N$-krat hitreje?

Naj bo $f$ delež programa, ki ga lahko pohitrimo, $1 - f$ pa delež, ki ostane nespremenjen. Čas izvajanja na enem računalniku naj bo $1$:

$$
\underbrace{\;f\;}_{\text{se pohitri}} + \underbrace{\;1 - f\;}_{\text{ostane}} = 1
$$

Z $N$ računalniki se prvi del izvede $N$-krat hitreje, drugi del pa traja enako dolgo:

$$
\underbrace{\;\frac{f}{N}\;}_{N\text{-krat hitreje}} + \underbrace{\;1 - f\;}_{\text{ostane}} < 1
$$

Pohitritev $S(N)$ je razmerje med starim in novim časom izvajanja:

$$
S(N) = \frac{1}{\dfrac{f}{N} + (1 - f)}
$$

> [!important] Amdahlov zakon
> Pohitritev je omejena z delom programa, ki ga ne moremo pohitriti:
> $$
> \lim_{N \to \infty} S(N) = \frac{1}{1 - f}
> $$

### Zgled 1: $f = 0{,}5$, $N = 1000$

$$
\begin{align}
S(1000) &= \frac{1}{\dfrac{0{,}5}{1000} + (1 - 0{,}5)} \\
&= \frac{1}{0{,}0005 + 0{,}5} \\
&= \frac{1}{0{,}5005} \approx 1{,}998
\end{align}
$$

S 1000 računalniki je program komaj $2$-krat hitrejši. Zgornja meja je $\dfrac{1}{1 - 0{,}5} = 2$.

### Zgled 2: $f = 0{,}9$, $N = 1000$

$$
\begin{align}
S(1000) &= \frac{1}{\dfrac{0{,}9}{1000} + (1 - 0{,}9)} \\
&= \frac{1}{0{,}0009 + 0{,}1} \\
&= \frac{1}{0{,}1009} \approx 9{,}91
\end{align}
$$

Čeprav lahko pohitrimo kar $90\,\%$ programa, je s 1000 računalniki le slabih $10$-krat hitrejši. Zgornja meja je $\dfrac{1}{1 - 0{,}9} = 10$.

### Ugotovitev

| $f$ | $N$ | $S(N)$ | zgornja meja $\frac{1}{1-f}$ |
|-|-|-|-|
| $0{,}5$ | $1000$ | $\approx 1{,}998$ | $2$ |
| $0{,}9$ | $1000$ | $\approx 9{,}91$ | $10$ |

- Z $N$ računalniki programa **ne** izvedemo $N$-krat hitreje: s 1000 računalniki smo dobili le $2$-kratno oziroma $10$-kratno pohitritev.
- Pohitritev določa predvsem delež $f$, ne število računalnikov. Omejuje jo del programa $1 - f$, ki ga ne moremo pohitriti.
- V obeh zgledih smo že skoraj na zgornji meji, zato dodajanje računalnikov ne pomaga več.

> [!important] Ugotovitev
> Bolj se splača povečati delež programa, ki ga lahko pohitrimo ($f$), kot dodajati računalnike ($N$).
