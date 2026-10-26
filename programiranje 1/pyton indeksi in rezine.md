---
tags:
  - python
  - programiranje
---
# Indeksi in rezine

## Indeksiranje – od kje se šteje

- **Indeksi se začnejo z 0.** Prvi element je `s[0]`, zadnji je `s[len(s) - 1]`.
- **Negativni indeksi štejejo od konca:** `s[-1]` je zadnji, `s[-2]` predzadnji (ni `-0`).
- Prevelik indeks vrne `IndexError`.
- Enako deluje za **sezname, nize in terke**.
- Dvojni indeks za sezname seznamov: `M[vrstica][stolpec]`.

```python
imena = ["Anze", "Benjamin", "Cilka", "Dani"]
imena[0]    # 'Anze'
imena[-1]   # 'Dani'
"Benjamin"[2]  # 'n'
```

**Pravilo za `range` in rezine je isto:** začetek je **vključen**, konec **ni vključen**. Zato `range(2, 5)` → `2, 3, 4`, število elementov pa je kar `5 - 2 = 3`.

## Rezanje (slicing)

Oblika: `s[začetek:konec:korak]`

- `začetek` je vključen, `konec` ni.
- Če izpustiš začetek, se začne na začetku; če izpustiš konec, gre do konca.
- Korak je privzeto 1, lahko je tudi negativen (takrat mora biti začetek večji od konca).
- Rezina **nikoli ne vrne napake**, tudi če so meje prevelike.

```python
b = "Benjamin"
b[2:5]     # 'nja'
b[:5]      # 'Benja'   prvih 5
b[5:]      # 'min'     vse razen prvih 5
b[-3:]     # 'min'     zadnji 3
b[:-3]     # 'Benja'   vse razen zadnjih 3
b[3:-2]    # 'jam'     odbij prve 3 in zadnja 2
b[::2]     # 'Bnai'    vsak drugi
b[::-1]    # 'nimajneB' obrnjen
```

Zakaj je štetje od 0 praktično: `s[:k] + s[k:]` je vedno cel `s`, nič se ne podvoji. Zato je vrivanje preprosto:

```python
b[:5] + "X" + b[5:]   # 'BenjaXmin'
```

### Spreminjanje z rezinami (samo seznami)

```python
s = [1, 2, 3, 4, 5]
s[1:3] = ["a", "b", "c"]   # zamenjaš 2 elementa s 3 → [1, 'a', 'b', 'c', 4, 5]
s[1:1] = [9]               # vrineš na mesto 1
s[1:3] = []                # izbrišeš
del s[0]                   # izbriše en element
```

**Nizov in terk ne moreš spreminjati** (`b[2] = "a"` → `TypeError`), lahko pa sestaviš nov niz: `b = b[:2] + "a" + b[3:]`.

## `enumerate` – oštevilči elemente

Vrača pare `(indeks, element)`. Namesto `for i in range(len(s))` raje uporabi `enumerate`.

```python
imena = ["Ana", "Bor", "Cene"]
for i, ime in enumerate(imena):
    print(i, ime)
# 0 Ana
# 1 Bor
# 2 Cene

for i, ime in enumerate(imena, 1):   # štetje od 1
    print(f"{i}. {ime}")
```

## `zip` – združi sezname

Vzame več seznamov in vrača terke istoležnih elementov. **Ustavi se pri najkrajšem.**

```python
imena = ["Ana", "Bor", "Cene"]
ocene = [9, 7, 10]
for ime, ocena in zip(imena, ocene):
    print(ime, ocena)

list(zip(imena, ocene))   # [('Ana', 9), ('Bor', 7), ('Cene', 10)]
dict(zip(imena, ocene))   # {'Ana': 9, 'Bor': 7, 'Cene': 10}
```

## Sinergije

**zip + rezina → pari zaporednih elementov** (najpogostejši trik):

```python
s = [5, 3, 8, 2, 1]
razlike = [a - b for a, b in zip(s, s[1:])]   # [2, -5, 6, 1]
narasca = all(a < b for a, b in zip(s, s[1:]))   # ali je seznam naraščajoč
```

**enumerate + zip → indeks in več seznamov hkrati:**

```python
for i, (ime, ocena) in enumerate(zip(imena, ocene), 1):
    print(f"{i}. {ime}: {ocena}")
```

**enumerate za iskanje mesta:**

```python
pozicije = [i for i, x in enumerate(s) if x > 4]   # indeksi elementov > 4
```

**zip za primerjavo dveh nizov po znakih:**

```python
razlik = sum(a != b for a, b in zip("kolo", "kino"))   # 2
```
