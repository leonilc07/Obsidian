---
tags:
  - python
  - programiranje
---
# Python osnove

## 1. Kaj je Python in malo ozadja

- Ustvaril ga je **Guido van Rossum**, prva verzija leta **1991**. Ime je dobil po skupini *Monty Python*, ne po kači.
- Danes se uporablja **Python 3** (Python 2 je mrtev od 2020).
- Filozofija: **berljivost kode je pomembnejša od kratkosti**. V Pythonu napiši `import this` in dobiš "Zen of Python".
- Uporablja se za: znanstveno računanje, analizo podatkov, strojno učenje, avtomatizacijo, spletne strežnike, skripte.

### Kako se razlikuje od drugih jezikov

| Lastnost | Python | C / C++ | Java |
|---|---|---|---|
| Izvajanje | interpretiran (prevede v bytecode, ki ga izvaja virtualni stroj) | prevajan v strojno kodo | prevajan v bytecode za JVM |
| Tipi | **dinamični** (tip ima vrednost, ne spremenljivka) | statični | statični |
| Pomnilnik | samodejni (garbage collector) | ročno (`malloc`/`free`, `new`/`delete`) | garbage collector |
| Bloki kode | **zamik (indentacija)** | `{ }` | `{ }` |
| Hitrost | počasnejši | zelo hiter | hiter |
| Dolžina kode | kratka | dolga | dolga |

**Pomembno:** Python je počasen sam po sebi, ampak knjižnice kot `numpy` so napisane v C-ju, zato je težko računanje v praksi hitro.

## 2. Namestitev in okolja s Condo

### Namestitev

- Najlažje: namesti **Miniconda** (lahka verzija) ali **Anaconda** (pride z veliko knjižnicami že vnaprej). 
- Alternativa: navaden Python s [python.org](https://www.python.org) + `pip`.
- Urejevalnik: **VS Code** (z razširitvijo Python), **PyCharm** ali **Jupyter Notebook**.

### Zakaj okolja (environments)

Vsak projekt lahko potrebuje drugačne verzije knjižnic. Okolje je **ločena mapa s svojim Pythonom in svojimi knjižnicami**, da se projekti med seboj ne kregajo.

### Osnovni conda ukazi

```bash
conda create -n prog1 python=3.12      # ustvari okolje "prog1"
conda activate prog1                    # vklopi okolje
conda install numpy matplotlib          # namesti knjižnice v okolje
pip install nekaj                       # tudi pip deluje znotraj okolja
conda list                              # kaj je nameščeno
conda env list                          # seznam vseh okolij
conda deactivate                        # izklopi okolje
conda env export > environment.yml      # shrani okolje v datoteko
conda env create -f environment.yml     # ustvari okolje iz datoteke
conda remove -n prog1 --all             # izbriše okolje
```

**Nasvet:** za vsak predmet ali projekt naredi svoje okolje, `base` okolja ne smetiti.

### Zagon programa

```bash
python moj_program.py     # zažene datoteko
python                    # interaktivni način (REPL), izhod z exit()
```

## 3. Knjižnice (moduli in paketi)

- **Modul** = ena `.py` datoteka s funkcijami. **Paket** = mapa z več moduli.
- **Standardna knjižnica** pride s Pythonom: `math`, `random`, `os`, `sys`, `datetime`, `collections`, `itertools`, `json`.
- **Zunanje knjižnice** namestiš s `conda install` ali `pip install`.

```python
import math
print(math.sqrt(16))        # 4.0

import numpy as np          # vzdevek
from random import randint  # uvoziš samo eno funkcijo
print(randint(1, 6))
```

Najbolj uporabne zunanje knjižnice:
- **numpy** – hitre tabele (matrike) in matematika
- **pandas** – tabelarični podatki (kot Excel)
- **matplotlib** – grafi
- **scipy**, **sympy** – znanstveno in simbolno računanje
- **requests** – delo s spletom

## 4. Osnove jezika

### Spremenljivke in tipi

```python
x = 5           # int (celo število, poljubno veliko!)
y = 3.14        # float
ime = "Ana"     # str
je_res = True   # bool
nic = None      # "ni vrednosti"

type(x)         # <class 'int'>
x = "zdaj sem niz"   # dovoljeno, tip se spremeni
```

**Posebnost:** `int` v Pythonu nima omejitve velikosti, `2**1000` deluje brez težav.

### Operatorji

```python
7 / 2    # 3.5   navadno deljenje (vedno float)
7 // 2   # 3     celoštevilsko deljenje
7 % 2    # 1     ostanek
2 ** 10  # 1024  potenca
a == b, a != b, a < b      # primerjave
and, or, not               # logični operatorji
```

### Pogoji in zanke

```python
if x > 0:
    print("pozitivno")
elif x == 0:
    print("nič")
else:
    print("negativno")

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i)

while x > 0:
    x -= 1
    if x == 3:
        break             # prekine zanko
```

**Zamik je del sintakse.** Napačen zamik = napaka (`IndentationError`). Uporabljaj 4 presledke.

### Funkcije

```python
def ploscina(a, b=1):      # b ima privzeto vrednost
    """Vrne ploščino pravokotnika."""
    return a * b

ploscina(3, 4)   # 12
ploscina(3)      # 3
ploscina(b=2, a=5)  # poimenovani argumenti

kvadrat = lambda x: x ** 2   # kratka anonimna funkcija
```

### Vhod in izhod

```python
ime = input("Kako ti je ime? ")   # vedno vrne str!
n = int(input("Število: "))       # pretvorba v int
print(f"Živjo {ime}, n^2 = {n**2}")  # f-string
```

## 5. Podatkovne strukture ("tabele")

Python nima klasičnih "arrayev" kot C, ima pa več vgrajenih zbirk:

| Struktura | Primer | Spremenljiva? | Urejena? | Duplikati? |
|---|---|---|---|---|
| **list** (seznam) | `[1, 2, 3]` | da | da | da |
| **tuple** (terka) | `(1, 2, 3)` | ne | da | da |
| **set** (množica) | `{1, 2, 3}` | da | ne | ne |
| **dict** (slovar) | `{"a": 1}` | da | da (vrstni red vstavljanja) | ključi ne |
| **str** (niz) | `"abc"` | ne | da | da |

### Seznam (list)

```python
s = [3, 1, 4, 1, 5]
s[0]        # 3   (indeksi od 0)
s[-1]       # 5   (zadnji)
s[1:3]      # [1, 4]  rezina (slice), konec ni vključen
s[::-1]     # obrnjen seznam
s.append(9) # doda na konec
s.pop()     # odstrani in vrne zadnjega
s.sort()    # uredi na mestu
len(s)      # dolžina
5 in s      # True

# list comprehension – zelo "pythonovsko"
kvadrati = [x**2 for x in range(10) if x % 2 == 0]   # [0, 4, 16, 36, 64]
```

### Slovar (dict)

```python
ocene = {"Ana": 9, "Bor": 7}
ocene["Ana"]          # 9
ocene["Cene"] = 10    # doda
ocene.get("Dan", 0)   # 0, če ključa ni
for ime, ocena in ocene.items():
    print(ime, ocena)
```

### Množica (set)

```python
A = {1, 2, 3}; B = {2, 3, 4}
A | B   # unija      {1, 2, 3, 4}
A & B   # presek     {2, 3}
A - B   # razlika    {1}
```

### 2D tabela (matrika)

```python
M = [[0] * 3 for _ in range(3)]   # pravilno
M[1][2] = 5

# NAPAČNO: M = [[0] * 3] * 3 – vse tri vrstice so ISTI objekt!
```

## 6. Bolj tehnično: kako Python deluje

### Vse je objekt, spremenljivke so imena (reference)

Spremenljivka v Pythonu **ni škatla z vrednostjo**, ampak **ime, ki kaže na objekt** v pomnilniku.

```python
a = [1, 2, 3]
b = a          # b kaže na ISTI seznam
b.append(4)
print(a)       # [1, 2, 3, 4]  ← a se je tudi spremenil!

c = a.copy()   # nova kopija (plitva)
import copy
d = copy.deepcopy(M)   # globoka kopija (tudi notranji seznami)

a is b   # True  – isti objekt
a == c   # True  – enaka vsebina
id(a)    # "naslov" objekta
```

### Spremenljivi in nespremenljivi tipi (mutable / immutable)

- **Nespremenljivi:** `int`, `float`, `str`, `tuple`, `bool`, `frozenset`. Ob "spremembi" nastane nov objekt.
- **Spremenljivi:** `list`, `dict`, `set`. Spreminjajo se na mestu.

```python
def dodaj(s):
    s.append(1)    # spremeni originalni seznam!

def povecaj(x):
    x += 1         # ne spremeni originala, nastane nov int
```

**Past:** nikoli ne piši `def f(s=[])`, ker se privzeti seznam deli med vsemi klici. Uporabi `s=None`.

### Časovna zahtevnost osnovnih operacij

| Operacija | list | dict / set |
|---|---|---|
| dostop po indeksu / ključu | $O(1)$ | $O(1)$ povprečno |
| `x in ...` | $O(n)$ | $O(1)$ povprečno |
| dodajanje na konec | $O(1)$ amortizirano | $O(1)$ |
| vstavljanje na začetek | $O(n)$ | – |
| `sort()` | $O(n \log n)$ | – |

- `list` je v ozadju **dinamična tabela** kazalcev (ko se napolni, se poveča za ~12,5 % in prepiše).
- `dict` in `set` sta **zgoščevalni tabeli (hash table)**, zato morajo biti ključi nespremenljivi (hashable).

**Nasvet:** če veliko preverjaš `x in zbirka`, uporabi `set`, ne `list`.

### Kako se koda izvede

1. Izvorna koda `.py` → prevede se v **bytecode** (`.pyc` v mapi `__pycache__`).
2. Bytecode izvaja **CPython virtualni stroj**, ukaz za ukazom.
3. Pomnilnik se sprošča s **štetjem referenc** + občasnim zbiralnikom smeti za cikle.
4. **GIL** (Global Interpreter Lock) pomeni, da v enem procesu naenkrat teče le ena nit Python kode (v novejših verzijah obstaja eksperimentalna različica brez GIL).

```python
import dis
dis.dis(lambda x: x + 1)   # pokaže bytecode
```

### numpy tabele vs. seznami

```python
import numpy as np
a = np.array([1, 2, 3])
a * 2            # array([2, 4, 6])  – operacija na vseh elementih
[1, 2, 3] * 2    # [1, 2, 3, 1, 2, 3] – seznam se podvoji!

M = np.zeros((3, 3))
M.shape          # (3, 3)
M @ M            # matrično množenje
```

numpy tabela ima **en sam tip** in je shranjena **zvezno v pomnilniku** (kot v C-ju), zato je 10–100× hitrejša od seznama.

## 7. Napake in izjeme

```python
try:
    x = int("abc")
except ValueError as e:
    print("Napaka:", e)
finally:
    print("to se vedno izvede")
```

Pogoste napake: `SyntaxError`, `IndentationError`, `NameError` (neznano ime), `TypeError` (napačen tip), `IndexError`, `KeyError`, `ZeroDivisionError`.

## 8. Delo z datotekami

```python
with open("podatki.txt", "r", encoding="utf-8") as f:
    for vrstica in f:
        print(vrstica.strip())

with open("izhod.txt", "w", encoding="utf-8") as f:
    f.write("Živjo\n")
```

`with` samodejno zapre datoteko.

## 9. Razredi (na kratko)

```python
class Ulomek:
    def __init__(self, st, im):
        self.st = st
        self.im = im

    def __str__(self):
        return f"{self.st}/{self.im}"

    def __add__(self, other):
        return Ulomek(self.st * other.im + other.st * self.im, self.im * other.im)

print(Ulomek(1, 2) + Ulomek(1, 3))   # 5/6
```

Metode z dvojnimi podčrtaji (`__add__`, `__len__`, `__eq__`...) določajo, kako se objekt obnaša z operatorji.
