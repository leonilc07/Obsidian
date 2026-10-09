---
tags:
  - racunalnistvo
  - zahteve
---

# Zahteve in uporabniške zgodbe

Naprej: [[02 UML - pregled|UML - pregled]].

Preden narišemo kakršen koli diagram, moramo vedeti, **kaj naj sistem sploh počne**. To zapišemo kot *zahteve*, pogosto v obliki *uporabniških zgodb*.

## Zahteve (Requirements)

| Vrsta | Angleško | Na kaj odgovarja | Primer (knjižnica) |
|-|-|-|-|
| Funkcijske zahteve | Functional requirements | **Kaj** sistem naredi? | Član lahko izposodi knjigo. |
| Nefunkcijske zahteve | Non-functional requirements | **Kako dobro** (hitro, varno, zanesljivo ...) to naredi? | Iskanje knjige traja manj kot 2 sekundi. |

Tipične nefunkcijske zahteve: zmogljivost (performance), varnost (security), uporabnost (usability), zanesljivost (reliability), vzdrževanost (maintainability).

> [!warning] Preveri v gradivu predmeta
> V zapiskih s predavanj piše »neformalne/formalne zahteve = funkcijske in nefunkcijske zahteve«. V splošni literaturi sta to **dve različni delitvi**:
> - *neformalne* ali *formalne* pove, **kako je zahteva zapisana** (v navadnem jeziku ali v strogo določeni, npr. matematični obliki),
> - *funkcijske* ali *nefunkcijske* pove, **kaj zahteva opisuje** (funkcijo ali kakovost in omejitev sistema).
>
> Če ju predmet izenači, se drži razlage predmeta.

## Uporabniška zgodba (User Story)

Ena zahteva, zapisana z **vidika uporabnika**, v enem stavku:

> **Kot** *vloga* **želim** *cilj*, **da** *korist*.

Primer: *Kot član knjižnice želim poiskati knjigo po naslovu, da vidim, ali je prosta.*

## Od zgodbe do diagrama

Iz zgodbe preberemo gradnike [[03 UML - diagram primerov uporabe|diagrama primerov uporabe]]:

| Del zgodbe | Postane | Primer |
|-|-|-|
| vloga (»kot ...«) | akter | Član |
| cilj (»želim ...«) | primer uporabe | Poišči knjigo |
| korist (»da ...«) | ni v diagramu, pove le, zakaj zgodba obstaja | da vidim, ali je prosta |

> [!question] Vaja
> Za bankomat napiši tri uporabniške zgodbe, eno funkcijsko in eno nefunkcijsko zahtevo. Isti primer uporabljaj pri vajah v naslednjih zapiskih.

*Primer »knjižnica« je izmišljen, za lažje razumevanje.*
