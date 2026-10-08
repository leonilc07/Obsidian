---
tags:
  - cheatsheet
---

# Obsidian: bližnjice in snippeti

Hitra pomoč za **Obsidian**, **Latex Suite** in **Calctex**. Snippeti so privzeti iz Latex Suite (stanje oktober 2026). Če jih v nastavitvah plugina spremeniš ali dodaš svoje, se tvoji razlikujejo od teh.

## Zapiski

- [[01 Obsidian - bližnjice|Obsidian: bližnjice]]: privzete bližnjice za ukaze, urejanje in premikanje
- [[02 Markdown - osnove|Markdown: osnove]]: odstavki, črte, naslovi, poudarki, seznami, citati, okvirji
- [[03 Markdown - povezave in struktura|Markdown: povezave in struktura]]: povezave, slike, tabele, koda, opombe, oznake, lastnosti
- [[04 Latex Suite - osnove|Latex Suite: osnove]]: kako deluje, funkcije plugina, vizualni snippeti
- [[05 Latex Suite - simboli|Latex Suite: simboli]]: grške črke, relacije, puščice, množice
- [[06 Latex Suite - formule|Latex Suite: formule]]: potence, ulomki, integrali, matrike, oklepaji
- [[07 Calctex|Calctex]]: samodejni izračun formul
- [[08 Moje bližnjice|Moje bližnjice]]: tvoje bližnjice in Git plugin

> [!info] Kako brati
> - Bližnjice veljajo za **Windows/Linux**. Na **Macu** zamenjaj `Ctrl` → `Cmd` in `Alt` → `Option` (izjema: za zavihke ostane `Ctrl+Tab`).
> - Snippeti Latex Suite delujejo **samo znotraj formule** (`$...$` ali `$$...$$`), razen če piše drugače.
> - Snippet z oznako **⇥** se razširi šele s tipko `Tab`. Vsi ostali se razširijo takoj, ko vtipkaš sprožilec.
> - Če bližnjica ne dela: `Ctrl+P`, poišči ukaz (tam se izpiše njegova bližnjica) ali pojdi v **Settings → Hotkeys**.

## Najprej se nauči

| Želim | Vpiši |
|-|-|
| formulo v vrstici | `mk` |
| formulo v svojem bloku | `dm` |
| ulomek | `a/` ali `//` |
| kvadrat, kub, poljubno potenco | `sr`, `cb`, `rd` |
| indeks | `x3` → $x_{3}$ |
| koren | `sq` |
| grško črko | `@a` $\alpha$, `@t` $\theta$, `pi` $\pi$ |
| neskončnost, $\leq$, $\geq$, $\neq$ | `ooo`, `<=`, `>=`, `!=` |
| množice $\mathbb{R}$, $\mathbb{N}$ | `RR`, `NN` |
| vsoto, integral | `sum` ⇥, `dint` |
| matriko | `pmat` |
| izstopiti iz formule ali oklepaja | `Tab` |
| preveriti račun | `=` na koncu formule (Calctex) |

## Viri

- Latex Suite: [GitHub](https://github.com/artisticat1/obsidian-latex-suite), [privzeti snippeti](https://github.com/artisticat1/obsidian-latex-suite/blob/main/src/default_snippets.js)
- Calctex: [GitHub](https://github.com/Developer-Mike/obsidian-calctex)
- Obsidian: [bližnjice za urejanje](https://obsidian.md/help/editing-shortcuts), [hotkeys](https://obsidian.md/help/hotkeys)
