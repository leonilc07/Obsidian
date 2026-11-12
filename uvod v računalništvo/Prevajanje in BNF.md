# Programski jeziki
Jezike razvrstimo po tem, kako blizu so strojni opremi:
- **nizkonivojski jeziki**: strojni jezik in zbirni jezik (*assembly*), **zelo povezani** s strojno opremo
- **visokonivojski jeziki**: npr. C++, Java, Python in psevdokoda, **manj povezani** s strojem
- **naravni jeziki**: angleščina, španščina, japonščina …, **niso povezani** s strojno opremo

Primer zbirnega jezika (program bere $x$ in $y$ ter izpisuje $x$, dokler $x \leq y$, nato izpiše $y$):
```
LOOP:   IN      X
        IN      Y
        LOAD    X
        COMPARE Y
        JUMPGT  DONE
        OUT     X
        JUMP    LOOP
DONE:   OUT     Y
        HALT
X:      .DATA   0
Y:      .DATA   0
```

Vrst programskih jezikov je več sto, med njimi so:
- deklarativni in proceduralni jeziki
- skriptni jeziki (awk …)
- simbolični jeziki (Mathematica …)
- jeziki na podlagi seznamov
- jeziki za opisovanje pomena (XML, OWL2, Linked Data …)
- jeziki za generiranje formul (LagraMge)

# Proces prevajanja
Prevajalnik (*compiler*) izvorni program prevede v strojni (objektni) program v štirih fazah:
1. **Leksikalna analiza** (*scanner*): združevanje znakov v **lekseme** (tokene). Vsak leksem dobi oznako, kaj je (spremenljivka, število, operator …). Če znaka ali besede ni na seznamu dovoljenih, javi napako.
2. **Sintaksna analiza** (*parser*): preverjanje sintakse, torej ali so leksemi v pravilnem **vrstnem redu**, in gradnja notranje predstavitve programa (sintaksno drevo).
3. **Semantična analiza in generiranje kode**: analiza pomena in generiranje strojnih ukazov (npr. v zbirni jezik).
4. **Optimizacija kode**: izboljševanje časovne in prostorske učinkovitosti kode. Boljši prevajalniki znajo kodo tudi pohitriti.

$$\text{izvorni program} \to \text{scanner} \to \text{parser} \to \text{generator kode} \to \text{optimizator} \to \text{objektni program}$$

# Proces izvajanja programa
1. Programer napiše **izvorni program** v visokonivojskem jeziku.
2. **Prevajalnik** ga prevede v **strojni (objektni) program**.
3. **Nalagalnik** (*loader*) naloži strojni program v pomnilnik.
4. **Strojna oprema** program izvede in vrne rezultate.

Primer: Java `a = b + c - d;` v zbirnem jeziku
```
LOAD     B
ADD      C
SUBTRACT D
STORE    A
```

## primer z vaj
`A = (B + C) - (D + E)` razdelimo na tri dele: I je $(B + C)$, II je $(D + E)$, III je razlika obeh.
```
LOAD     B      ; I:   T1 = B + C
ADD      C
STORE    T1
LOAD     D      ; II:  T2 = D + E
ADD      E
STORE    T2
LOAD     T1     ; III: A = T1 - T2
SUBTRACT T2
STORE    A
```
Vmesna rezultata shranimo v **začasni spremenljivki** $T1$ in $T2$. Če bi ju shranili kar v $B$ in $D$, bi prepisali vrednosti teh spremenljivk, ki jih program morda še potrebuje.

# Leksikalna analiza
## naloga 6.1
Jezik v imenih spremenljivk dovoljuje podčrtaje (`_`). Koliko leksemov sta `AB_CD` in `A_B CD`?
- `AB_CD` je **1 leksem**, ker je podčrtaj del imena
- `A_B CD` sta **2 leksema**, `A_B` in `CD`, ker presledek loči lekseme

## tabela leksemov
Pri nalogah 6.2, 6.3 in dodatni nalogi 1 uporabljamo to tabelo (tip leksema in klasifikacijska številka):
- symbol (ime, npr. spremenljivka): **1**
- number (število): **2**
- `=`: **3**, `+`: **4**, `-`: **5**, `;`: **6**, `==`: **7**
- `if`: **8**, `else`: **9**
- `(`: **10**, `)`: **11**

## naloga 6.2
`delta = epsilon + sqrt(alpha);`
- `delta` 1, `=` 3, `epsilon` 1, `+` 4, `sqrt` 1, `(` 10, `alpha` 1, `)` 11, `;` 6

`sqrt` je ime funkcije, zato je **symbol** (1), ker ga v tabeli ni kot posebne besede.

## naloga 6.3
`thenelse == error -`
- `thenelse` 1, `==` 7, `error` 1, `-` 5

`thenelse` je **en** leksem (symbol), čeprav vsebuje besedo `else`. Analizator bere čim daljši niz črk, zato `else` tu ni posebna beseda. Tudi `==` je en leksem (7), ne dva `=`.

## dodatna naloga 1
`if (a == 15) x = 10; else b = x + 25;`
- `if` 8, `(` 10, `a` 1, `==` 7, `15` 2, `)` 11
- `x` 1, `=` 3, `10` 2, `;` 6
- `else` 9, `b` 1, `=` 3, `x` 1, `+` 4, `25` 2, `;` 6

# BNF gramatika
**BNF** (*Backus-Naur Form*) je zapis pravil, ki opisujejo, kateri nizi so v jeziku pravilni.
- `<ime>` je **vmesni simbol** (pojem, ki ga še razčlenimo)
- `::=` beremo „je definiran kot“
- `|` pomeni „ali“ (ena od možnosti)
- znaki brez `< >` so **končni simboli**, ki se dejansko pojavijo v nizu

**Sintaksno drevo** pokaže, kako iz pravil dobimo dani niz: na vrhu so znaki niza, vsak vmesni simbol združi svoje dele, na dnu je začetni simbol.

## naloga 6.4
`<stevilo>` je lahko znak `+`, ki mu sledita natanko dve števki, prva pa ni 0. Veljavna sta npr. `15` in `+72`, neveljavna pa `+05` in `123`.
```
<stevilo> ::= <cifra1><cifra2> | <znak><cifra1><cifra2>
<cifra1>  ::= 1|2|3|4|5|6|7|8|9
<cifra2>  ::= 0|<cifra1>
<znak>    ::= +
```
- `<cifra1>` so števke brez 0, zato prva števka ne more biti 0
- `<cifra2>` je katerakoli števka: 0 ali `<cifra1>`
- dve možnosti za `<stevilo>` pomenita, da je `+` neobvezen

Sintaksno drevo za `+35`:

![[Vaje 6 - sintaksno drevo 6.4.excalidraw]]

## naloga 6.5
Poljubno dolgi nizi črk in števk, kjer je prvi znak črka.
```
<niz>    ::= <crka> | <crka><naprej>
<naprej> ::= <cifra> | <crka> | <cifra><naprej> | <crka><naprej>
<cifra>  ::= 0|...|9
<crka>   ::= A|...|Z
```
- `<niz>` se vedno začne s `<crka>`
- `<naprej>` je **rekurziven**: se sklicuje sam nase, zato je niz lahko poljubno dolg. Ustavi se, ko izberemo možnost brez `<naprej>`.

Sintaksno drevo za `AB5C8`:

![[Vaje 6 - sintaksno drevo 6.5.excalidraw]]

## naloga 6.6
Izrazi oblike `var AND var` ali `var OR var`, kjer je `var` eden od `w`, `x`, `y`, `z`.

1. način:
```
<izraz> ::= <var> AND <var> | <var> OR <var>
<var>   ::= w|x|y|z
```

2. način, z ločenim pravilom za operator:
```
<izraz>    ::= <var><operator><var>
<operator> ::= AND | OR
<var>      ::= w|x|y|z
```
Oba načina opisujeta iste nize. Drugi je krajši in ga je lažje razširiti z novim operatorjem.

## naloga 6.7
Sintaksno drevo za `x = x + y` po gramatiki:
```
<statement>  ::= <variable> = <expression>
<expression> ::= <variable> | <expression> + <variable>
<variable>   ::= x|y|z
```

![[Vaje 6 - sintaksno drevo 6.7.excalidraw]]

- desni `x` je najprej `<variable>`, nato `<expression>` (prva možnost)
- `<expression> + <variable>` (`x + y`) je spet `<expression>` (druga možnost)
- `<variable> = <expression>` je `<statement>`

## dodatna naloga 2
Ista gramatika, stavek `x = x + y + z`. Pravilo `<expression> + <variable>` uporabimo dvakrat: najprej za `x + y`, nato za `(x + y) + z`.

![[Vaje 6 - sintaksno drevo dodatna 2.excalidraw]]
