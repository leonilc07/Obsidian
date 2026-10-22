# Pomnilnik (*kot si ga je zamislil von Neumann*)
- Pomnilnik hrani ukaze in operande.
- Pomnilnik naj bo zaporedje enako velikih pomnilniških besed (angl. *memory word*).

| Beseda   | Naslov | Naslov (*ni treba, da se začne z 0*) |
| -------- | ------ | ------------------------------------ |
| word 0   | 0      | k+0                                  |
| word 1   | 1      | k+1                                  |
| ...      | ...    | ...                                  |
| word n-2 | n-2    | k+n-2                                |
| word n-1 | n-1    | k+n-1                                |

- Vsaka beseda naj bo »enolično naslovljiva«: vsaka beseda ima svoj naslov (indeks), po katerem jo ločimo od ostalih besed.
- Vsaka beseda hrani enako količino informacije.
- Torej vsaka beseda hrani enako število bitov (je dolga enako število bitov).

## Najmanjša količina informacije v sodobnih računalniških sistemih
Zaradi narave tehnologije izdelave računalnikov lahko v najmanjših gradnikih hranimo oziroma merimo napetost približno 0 V (je **0**) ali približno 1,1 V (je **1**). Tej najmanjši količini informacije, ki ima vrednost 0 ali 1, rečemo **bit** (b): $b \in \{0, 1\}$.

## Pomnilniška beseda
*M*-bitna beseda:

| $b_{M-1}$ | $b_{M-2}$ | $b_{M-3}$ | ... | $b_3$ | $b_2$ | $b_1$ | $b_0$ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |

- $b_0$ – bit z najmanjšo težo (najmanj pomemben bit, angl. *least significant bit*, LSB)
- $b_{M-1}$ – bit z največjo težo (najbolj pomemben bit, angl. *most significant bit*, MSB)

V praksi je najpogosteje $M = 8$, torej je beseda dolga 8 bitov. Zato so ji dali ime **bajt** (angl. *byte*).

## informacija
- **Pomnilnik:** $N$ pomnilniških besed, dolgih $M$ bitov (angl. *N × M bit memory*).
- **Informacija** (predstavljena z biti) je sestavljena iz ukazov in operandov.
	- Kako so operandi in ukazi predstavljeni z biti? Najprej si pogledamo operande.
- **Operandi** so števila, znaki in znakovni nizi, barve, zvok … Vse to je predstavljeno z biti.

`10010110` – kaj je to? Zvok? Barva? Število?
→ **Iz bitnega zapisa ne moremo prepoznati tipa informacije.** Mi kot programerji se odločimo, kako bomo interpretirali vsebino neke pomnilniške besede.

Omejimo se na:
# Cela nepredznačena števila
- Kako z biti zapišemo cela nepredznačena števila? 
- Najprej poglejmo, kako jih zapišemo s števili, ki jih poznamo → **desetiškimi**.

Primer: $347$
- $3 \to 3 \cdot 10^2 = 300$
- $4 \to 4 \cdot 10^1 = 40$
- $7 \to 7 \cdot 10^0 = 7$

$$
347 = 3 \cdot 10^2 + 4 \cdot 10^1 + 7 \cdot 10^0
$$

Vrednost števila je določena s pomočjo posameznih števk in njihovega mesta v zapisu.

Vrednost $n$-mestnega števila:

$$
\text{vrednost} = \sum_{i=0}^{n-1} x_i \cdot B^i
$$

- **Desetiški sistem:** $B = 10$, $x_i \in \{0, 1, \dots, 9\}$
- **V računalniku (dvojiški sistem):** $B = 2$, $x_i \in \{0, 1\}$

Najbolj naraven način za zapis celih nepredznačenih števil je **pozicijski zapis**.

Primer: $n = 4$, `1011`
$$
1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 2 + 1 = 11
$$

Primer: $n = 8$, `10011100`
$$
1 \cdot 2^7 + 0 \cdot 2^6 + 0 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0 = 128 + 16 + 8 + 4 = 156
$$

# Cela predznačena števila
Kako bitnemu zapisu dodati predznak (+, −)?

1. **Predznak in velikost:** najbolj pomemben bit naj bo predznak: 0 = +, 1 = −. Vrednost določimo iz pozicijskega zapisa preostalih bitov.
	- `0011` → $+3$ (pozicijski zapis `011` = 3)
	- `1011` → $-3$
	- Seštejemo $+3$ in $-3$:

	```
	  0011   (+3)
	+ 1011   (-3)
	------
	  1110   (-6)
	```

	- Dobimo `1110` → $-6$, pravilno pa bi bilo $+3 + (-3) = 0$ (`0000`). → **Pri zapisu s predznakom in velikostjo navadno seštevanje bitov ne da pravilnega rezultata.**
2. **Zapis z odmikom:** recimo, da je $n = 3$, da nam bo lažje. Zapišemo ta števila na premico:

	```
	 000   001   010   011   100   101   110   111
	──┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──▶
	 -4    -3    -2    -1     0     1     2     3
	```
	**Lepo:** najvišji bit določa predznak: 0 = −, 1 = +.

	Kako pa določimo vrednost (velikost) v takem zapisu? Pozicijsko vrednost »sredine« (**odmik**, angl. *offset*) odštejemo od pozicijske vrednosti števila.
	- V našem primeru je sredina `100`: $v(100) = 4$ → odmik je 4.
	- Primera: $v(110) = 6 - 4 = 2$, $v(011) = 3 - 4 = -1$
	- Splošno (odmik je $2^{n-1}$):

	$$
	v = \sum_{i=0}^{n-1} x_i \cdot 2^i - 2^{n-1}
	$$

	- Seštejemo $0$ in $-3$:

	```
	  100   (0)
	+ 001   (-3)
	-----
	  101   (1)
	```

	- Dobimo `101` → $5 - 4 = 1$, pravilno pa bi bilo $0 + (-3) = -3$ (`001`). → **Tudi pri zapisu z odmikom navadno seštevanje bitov ne da pravilnega rezultata.**

	**Ampak dobro:** števila so **leksikografsko** razvrščena: če bite primerjamo od leve proti desni, nam prvi bit, v katerem se števili razlikujeta, pove, katero je večje.
3. **Enični komplement:** predpostavimo $n = 3$. Pozitivna števila zapišemo pozicijsko, negativno število dobimo tako, da **obrnemo vse bite** pozitivnega ($+2 =$ `010` → $-2 =$ `101`).

	```
	              000 (+0)
	     111 (−0)          001 (+1)
	 110 (−1)                  010 (+2)
	     101 (−2)          011 (+3)
	              100 (−3)
	```

	- Najvišji bit spet določa predznak: 0 = +, 1 = −.
	- Seštejemo $+3$ in $-3$:

	```
	  011   (+3)
	+ 100   (-3)
	-----
	  111   (-0)
	```

	- Dobimo `111` → $-0$. Rezultat je sicer nič, ampak **imamo dve ničli** ($+0$ = `000` in $-0$ = `111`).
	- Seštejemo $+2$ in $-3$:

	```
	  010   (+2)
	+ 100   (-3)
	-----
	  110   (-1)
	```

	- Dobimo `110` → $-1$, kar je pravilno.
	- **Rešitev:** če negativna števila na krožnici zamaknemo za eno mesto (`111` = $-1$, `110` = $-2$, `101` = $-3$, `100` = $-4$), se znebimo dvojne ničle → dvojiški komplement.
	- **Prednost:** omogoča preprost prehod iz pozitivnega v negativno število (in obratno) v dvojiškem komplementu – negiramo vse bite in prištejemo 1. Primer: $+3 = 011 \rightarrow 100 + 1 = 101 = -3$.
4. **Dvojiški komplement:** ($n = 3$)

	```
	              000 (0)
	     111 (−1)          001 (+1)
	 110 (−2)                  010 (+2)
	     101 (−3)          011 (+3)
	              100 (−4)
	```

	Ali znamo izračunati vrednost?
	- **Pozitivna** števila (najvišji bit 0): vrednost je kar pozicijski zapis.
	- **Negativna** števila (najvišji bit 1): vrednost = pozicijski zapis $- 2^n$, npr. $v(101) = 5 - 8 = -3$.
	- Splošno:

	$$
	v = -x_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} x_i \cdot 2^i
	$$

	- Seštejemo $+3$ in $-3$:

	```
	   011   (+3)
	+  101   (-3)
	------
	  1000   (0)
	```

	- Najvišja `1` je **prenos** (angl. *carry*), ki ga zavržemo → `000` = $0$, kar je pravilno.
	- Seštejemo $+2$ in $-3$:

	```
	  010   (+2)
	+ 101   (-3)
	-----
	  111   (-1)
	```

	- Dobimo `111` → $-1$, kar je pravilno.
	- Seštejemo $+3$ in $+1$:

	```
	  011   (+3)
	+ 001   (+1)
	-----
	  100   (-4)
	```

	- Dobimo `100` → $-4$, pravilno pa bi bilo $+4$. Rezultat se je prelil čez mejo med `011` in `100` – v napačen predznak. Temu rečemo **preliv** (angl. *overflow*).

	**Ugotovitev:** če seštevamo števili z **nasprotnim predznakom**, vedno dobimo pravilen rezultat. Če seštevamo števili z **enakim predznakom**, se lahko zgodi preliv. Preliv ne pomeni, da ne znamo računati, ampak le, da imamo **premalo bitov** za zapis rezultata.
