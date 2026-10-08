---
tags:
  - cheatsheet
---

# Latex Suite: osnove

Nazaj na [[00 Kazalo|Kazalo]]. Snippeti: [[05 Latex Suite - simboli|simboli]], [[06 Latex Suite - formule|formule]].

> [!info] Kako brati
> - Snippeti delujejo **samo znotraj formule** (`$...$` ali `$$...$$`), razen če piše drugače.
> - Snippet z oznako **⇥** se razširi šele s tipko `Tab`. Vsi ostali se razširijo takoj, ko vtipkaš sprožilec.

## Kako deluje

- **Sprožilec → zamenjava.** Vtipkaš sprožilec (npr. `sr`) in plugin ga zamenja s kodo (`^{2}`).
- **`Tab` skače.** Če snippet pusti več mest za kurzor, `Tab` skoči na naslednje. Na koncu formule `Tab` izstopi za `$`.
- **Snippete urejaš** v **Settings → Latex Suite** (tam dodaš tudi svoje).
- **Past:** besede v formuli brez `\text` lahko sprožijo snippete. Npr. `pi` v besedi `spin` postane `s\pi n`, samostojna beseda `and` pa $\cap$. Besedilo piši po `text` ali `"`.

## Vstop v matematiko

| Vpiši | Kaj naredi |
|-|-|
| `mk` | Formula v vrstici `$ $` (v besedilu) |
| `dm` | Formula v svojem bloku `$$ $$` (na prazni vrstici ali za besedilom v vrstici) |
| `beg` | Poljubno okolje `\begin{ } … \end{ }` |

## Funkcije plugina

| Funkcija | Kako deluje |
|-|-|
| **Auto-fraction** | `x/` → `\frac{x}{ }`, kurzor je v imenovalcu, `Tab` izstopi iz ulomka. Deluje tudi z oklepaji: `(a + b)/` |
| **Tabout** | `Tab` na koncu formule te premakne iz `$`. Znotraj `\left … \right` skoči za `\right`, sicer na naslednji zaključni oklepaj `)`, `]`, `}`, `\rangle`, `\rvert` |
| **Matrične bližnjice** | V okoljih matrix, array, align, cases: `Tab` → `&`, `Enter` → `\\` in nova vrstica, `Shift+Enter` → konec naslednje vrstice (izhod iz matrike) |
| **Vizualni snippeti** | Označi del formule in pritisni eno črko (tabela spodaj) |
| **Auto-enlarge brackets** | Ko se razširi snippet z `\sum`, `\int` ali `\frac`, se okoliški oklepaji povečajo z `\left` in `\right` |
| **Conceal** | Skrije LaTeX kodo in prikaže lepšo obliko (ẋ², √…). Kodo vidiš, ko kurzor pride nanjo. **Vklopiš v nastavitvah plugina**, mono pisava pa mora podpirati simbole (npr. JuliaMono) |
| **Preview inline math** | Ko je kurzor v formuli v vrstici, se prikaže okno z izrisano formulo |
| **Barvni oklepaji** | Pari oklepajev imajo enako barvo, ob kurzorju se par označi |

Ukaza v Command palette (`Ctrl+P`): **Box current equation** (formulo obda z `\boxed{ }`) in **Select current equation** (izbere formulo). Bližnjico jima dodeliš sam v Settings → Hotkeys.

## Vizualni snippeti (najprej označi, potem pritisni)

| Pritisni | Koda |
|-|-|
| `U` | `\underbrace{ }_{ }` |
| `O` | `\overbrace{ }^{ }` |
| `B` | `\underset{ }{ }` |
| `C` | `\cancel{ }` |
| `K` | `\cancelto{ }{ }` |
| `S` | `\sqrt{ }` |
| `(`, `[`, `{` | Obda izbiro z oklepaji |
