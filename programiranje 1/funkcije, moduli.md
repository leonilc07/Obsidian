# Funkcije in moduli

## Moduli

**Modul** je datoteka s kodo (npr. `math`), ki jo uvozimo, da uporabimo njene funkcije.

- `from math import sin` – uvozi samo `sin`, kličeš `sin(0)`
- `from math import *` – uvozi vse, a **ni priporočeno** (lahko povozi tvoja imena)
- `import math` – kličeš s predpono `math.sin(0)`, **najbolj pregledno**
- tudi svojo datoteko lahko uvoziš: `from funkcije import delitelji`

## Funkcije

- definiramo z `def ime(parametri):`, rezultat vrnemo z `return`
- **namigi tipov**: `def f(n: int) -> list[int]` pove, kaj funkcija sprejme in vrne
  - Python jih ne preverja, program se izvede, a urejevalnik opozori (npr. če podaš niz)
- funkcije lahko **kličejo druga drugo** (npr. `popolno` uporabi `delitelji` in `vsota`)

## Primeri, ki smo jih delali

- **delitelji(n)** – z zanko čez `range(1, n+1)` in pogojem `n % i == 0` zbere delitelje v seznam z `append`
- **vsota(a)** – sešteje seznam (isto kot vgrajeni `sum`)
- **popolno(n)** – število je popolno, če je vsota deliteljev brez njega enaka njemu, npr. $1+2+3=6$
  - `d[:-1]` odstrani zadnji element (število samo)
- **dan_v_tednu(dan)** – vrne ime dneva z `if/elif/else`

**Pozor:** `if` mora biti **znotraj** funkcije, ne okoli `def`, in nizi morajo biti v narekovajih (`"ponedeljek"`).
