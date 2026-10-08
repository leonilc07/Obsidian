---
tags:
  - cheatsheet
---

# Obsidian: bližnjice in snippeti

Hitra pomoč za **Obsidian**, **Latex Suite** in **Calctex**. Snippeti so privzeti iz Latex Suite (stanje oktober 2026). Če jih v nastavitvah plugina spremeniš ali dodaš svoje, se tvoji razlikujejo od teh.

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

---

## Obsidian: privzete bližnjice

> [!note] Opomba
> Uradna dokumentacija navaja samo bližnjice za urejanje besedila. Bližnjice ukazov (Command palette, Quick switcher …) so preverjene v več virih, lahko pa se med verzijami razlikujejo. Če katera ne dela, jo poišči v **Settings → Hotkeys**.

### Ukazi in navigacija

| Bližnjica | Kaj naredi |
|-|-|
| `Ctrl+P` | Command palette: zaženi poljuben ukaz |
| `Ctrl+O` | Quick switcher: odpri zapisek po imenu |
| `Ctrl+N` | Nov zapisek |
| `Ctrl+Shift+F` | Iskanje po vseh zapiskih |
| `Ctrl+F` | Iskanje v zapisku |
| `Ctrl+H` | Najdi in zamenjaj v zapisku |
| `Ctrl+E` | Preklop med urejanjem in branjem |
| `Ctrl+G` | Graf povezav (graph view) |
| `Ctrl+,` | Nastavitve |
| `Ctrl+W` | Zapri zavihek |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Naslednji / prejšnji zavihek |
| `Ctrl+1` … `Ctrl+8` | Skoči na zavihek 1–8 |
| `Ctrl+Alt+←` / `Ctrl+Alt+→` | Nazaj / naprej po zgodovini odprtih zapiskov |
| `Alt+Enter` | Sledi povezavi pod kurzorjem |
| `Ctrl` + klik na povezavo | Odpri v novem zavihku |

### Oblikovanje in urejanje

| Bližnjica | Kaj naredi |
|-|-|
| `Ctrl+B` | Krepko |
| `Ctrl+I` | Ležeče |
| `Ctrl+K` | Vstavi povezavo |
| `Ctrl+Enter` | Preklopi checkbox (`- [ ]` ↔ `- [x]`) |
| `Tab` / `Shift+Tab` | Zamik / zmanjšaj zamik elementa seznama |
| `Ctrl+]` / `Ctrl+[` | Zamik / zmanjšaj zamik |
| `Ctrl+Shift+K` | Izbriši trenutno vrstico (brez izbire) |
| `Ctrl+D` | Izbriši odstavek |
| `Ctrl+C` / `Ctrl+X` brez izbire | Kopiraj / izreži celo vrstico (odstavek) |
| `Ctrl+Shift+V` | Prilepi brez oblikovanja |
| `Ctrl+Z` / `Ctrl+Y` | Razveljavi / uveljavi (uveljavi tudi `Ctrl+Shift+Z`) |

### Premikanje in izbiranje

| Bližnjica | Kaj naredi |
|-|-|
| `Ctrl+←` / `Ctrl+→` | Beseda levo / desno |
| `Home` / `End` | Začetek / konec vrstice |
| `Ctrl+Home` / `Ctrl+End` | Začetek / konec zapiska |
| `Page Up` / `Page Down` | Stran gor / dol |
| `Ctrl+Backspace` / `Ctrl+Delete` | Izbriši prejšnjo / naslednjo besedo |
| `Shift` + premik | Razširi izbiro (`Ctrl+Shift+←/→` po besedah, `Shift+Home/End` do roba vrstice) |
| `Ctrl+A` | Izberi vse |
| `Escape` | Poenostavi izbiro |

Na Macu je premikanje drugačno: `Option+←/→` po besedah, `Cmd+←/→` začetek/konec vrstice, `Cmd+↑/↓` začetek/konec zapiska.

---

## Latex Suite

### Kako deluje

- **Sprožilec → zamenjava.** Vtipkaš sprožilec (npr. `sr`) in plugin ga zamenja s kodo (`^{2}`).
- **`Tab` skače.** Če snippet pusti več mest za kurzor, `Tab` skoči na naslednje. Na koncu formule `Tab` izstopi za `$`.
- **Snippete urejaš** v **Settings → Latex Suite** (tam dodaš tudi svoje).
- **Past:** besede v formuli brez `\text` lahko sprožijo snippete. Npr. `pi` v besedi `spin` postane `s\pi n`, samostojna beseda `and` pa $\cap$. Besedilo piši po `text` ali `"`.

### Vstop v matematiko

| Vpiši | Kaj naredi |
|-|-|
| `mk` | Formula v vrstici `$ $` (v besedilu) |
| `dm` | Formula v svojem bloku `$$ $$` (na prazni vrstici ali za besedilom v vrstici) |
| `beg` | Poljubno okolje `\begin{ } … \end{ }` |

### Funkcije plugina

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

### Vizualni snippeti (najprej označi, potem pritisni)

| Pritisni | Koda |
|-|-|
| `U` | `\underbrace{ }_{ }` |
| `O` | `\overbrace{ }^{ }` |
| `B` | `\underset{ }{ }` |
| `C` | `\cancel{ }` |
| `K` | `\cancelto{ }{ }` |
| `S` | `\sqrt{ }` |
| `(`, `[`, `{` | Obda izbiro z oklepaji |

### Grške črke

| Vpiši | Videz | Vpiši | Videz |
|-|-|-|-|
| `@a` | $\alpha$ | `@s` | $\sigma$ |
| `@b` | $\beta$ | `@S` | $\Sigma$ |
| `@g` | $\gamma$ | `@u` | $\upsilon$ |
| `@G` | $\Gamma$ | `@U` | $\Upsilon$ |
| `@d` | $\delta$ | `@o`, `ome` | $\omega$ |
| `@D` | $\Delta$ | `@O`, `Ome` | $\Omega$ |
| `@e` | $\epsilon$ | `@i` | $\iota$ |
| `:e` | $\varepsilon$ | `@k` | $\kappa$ |
| `@z` | $\zeta$ | `@l` | $\lambda$ |
| `@t` | $\theta$ | `@L` | $\Lambda$ |
| `@T` | $\Theta$ | `:t` | $\vartheta$ |

Črke s kratkim imenom samo vtipkaš (backslash se doda sam): `eta`, `mu`, `nu`, `xi`, `Xi`, `pi`, `Pi`, `rho`, `tau`, `phi`, `Phi`, `chi`, `psi`, `Psi`.

### Potence, indeksi, ulomki, koreni

| Vpiši | Koda | Videz |
|-|-|-|
| `sr` | `^{2}` | $x^{2}$ |
| `cb` | `^{3}` | $x^{3}$ |
| `rd` | `^{ }` | $x^{n}$ |
| `_` | `_{ }` | $x_{n}$ |
| `x3` | `x_{3}` | $x_{3}$ |
| `x34` | `x_{34}` | $x_{34}$ |
| `xnn`, `xii`, `xjj` | `x_{n}`, `x_{i}`, `x_{j}` | $x_{n}$ |
| `xp1` | `x_{n+1}` | $x_{n+1}$ |
| `sts` | `_\text{ }` | $x_\text{max}$ |
| `//` | `\frac{ }{ }` | $\frac{a}{b}$ |
| `a/` | `\frac{a}{ }` | $\frac{a}{b}$ |
| `sq` | `\sqrt{ }` | $\sqrt{x}$ |
| `3rt` | `\sqrt[3]{ }` | $\sqrt[3]{x}$ |
| `ee` | `e^{ }` | $e^{x}$ |
| `invs` | `^{-1}` | $A^{-1}$ |
| `conj` | `^{*}` | $z^{*}$ |
| `bf` | `\mathbf{ }` | $\mathbf{v}$ |
| `rm` | `\mathrm{ }` | $\mathrm{d}$ |
| `text` ali `"` | `\text{ }` | $\text{beseda}$ |
| `Re`, `Im` | `\mathrm{Re}`, `\mathrm{Im}` | $\mathrm{Re}$, $\mathrm{Im}$ |
| `det`, `trace` | `\det`, `\mathrm{Tr}` | $\det$, $\mathrm{Tr}$ |
| `exp`, `log`, `ln` | `\exp`, `\log`, `\ln` | $\exp$, $\log$, $\ln$ |
| `pmod` | `\pmod{n}` | $a \equiv b \pmod{n}$ |

### Naglasi in pisave

Pred končnico napišeš črko, npr. `xhat`.

| Vpiši | Koda | Videz |
|-|-|-|
| `xhat` | `\hat{x}` | $\hat{x}$ |
| `xbar` | `\bar{x}` | $\bar{x}$ |
| `xdot`, `xddot` | `\dot{x}`, `\ddot{x}` | $\dot{x}$, $\ddot{x}$ |
| `xtilde` | `\tilde{x}` | $\tilde{x}$ |
| `xvec` | `\vec{x}` | $\vec{x}$ |
| `xund` | `\underline{x}` | $\underline{x}$ |
| `x,.` ali `x.,` | `\mathbf{x}` | $\mathbf{x}$ |

Če končnico vtipkaš sam (`hat`, `bar`, `dot`, `ddot`, `tilde`, `vec`, `und`), dobiš prazen ovoj s kurzorjem znotraj.

### Simboli, relacije, puščice

| Vpiši | Koda | Videz |
|-|-|-|
| `ooo` | `\infty` | $\infty$ |
| `+-`, `-+` | `\pm`, `\mp` | $\pm$, $\mp$ |
| `...` | `\dots` | $\dots$ |
| `xx` | `\times` | $\times$ |
| `**` | `\cdot` | $\cdot$ |
| `nabl` | `\nabla` | $\nabla$ |
| `para` | `\parallel` | $\parallel$ |
| `deg` | `\degree` | $90\degree$ |
| `!=` | `\neq` | $\neq$ |
| `>=`, `<=` | `\geq`, `\leq` | $\geq$, $\leq$ |
| `>>`, `<<` | `\gg`, `\ll` | $\gg$, $\ll$ |
| `===` | `\equiv` | $\equiv$ |
| `simm`, `sim=` | `\sim`, `\simeq` | $\sim$, $\simeq$ |
| `prop` | `\propto` | $\propto$ |
| `->` | `\to` | $\to$ |
| `<->` | `\leftrightarrow` | $\leftrightarrow$ |
| `!>` | `\mapsto` | $\mapsto$ |
| `=>` | `\implies` | $\implies$ |
| `=<` | `\impliedby` | $\impliedby$ |

### Množice in številski sistemi

| Vpiši | Koda | Videz |
|-|-|-|
| `inn` | `\in` | $\in$ |
| `notin` | `\not\in` | $\not\in$ |
| `and` | `\cap` (samostojna beseda) | $\cap$ |
| `orr` | `\cup` | $\cup$ |
| `\\\` | `\setminus` | $\setminus$ |
| `sub=`, `sup=` | `\subseteq`, `\supseteq` | $\subseteq$, $\supseteq$ |
| `eset` | `\emptyset` | $\emptyset$ |
| `set` | `\{ \}` | $\{ x \}$ |
| `RR`, `NN`, `ZZ`, `QQ`, `CC` | `\mathbb{R}` … | $\mathbb{R}$, $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{C}$ |
| `LL`, `HH` | `\mathcal{L}`, `\mathcal{H}` | $\mathcal{L}$, $\mathcal{H}$ |

### Vsote, limite, odvodi, integrali

| Vpiši | Koda | Videz |
|-|-|-|
| `sum`, nato ⇥ | `\sum_{i=1}^{N}` | $\sum_{i=1}^{N}$ |
| `prod`, nato ⇥ | `\prod_{i=1}^{N}` | $\prod_{i=1}^{N}$ |
| `lim` | `\lim_{ n \to \infty }` | $\lim_{n \to \infty}$ |
| `par` ⇥ | `\frac{ \partial y }{ \partial x }` | $\frac{\partial y}{\partial x}$ |
| `par2` | drugi parcialni odvod | $\frac{\partial^{2} y}{\partial x^{2}}$ |
| `ddt` | `\frac{d}{dt}` | $\frac{d}{dt}$ |
| `int`, nato ⇥ | `\int \, dx` | $\int f \, dx$ |
| `dint` | `\int_{0}^{1} \, dx` | $\int_{0}^{1} f \, dx$ |
| `oint`, `iint`, `iiint` | `\oint`, `\iint`, `\iiint` | $\oint$, $\iint$, $\iiint$ |
| `oinf` | `\int_{0}^{\infty} \, dx` | $\int_{0}^{\infty} f \, dx$ |
| `infi` | `\int_{-\infty}^{\infty} \, dx` | $\int_{-\infty}^{\infty} f \, dx$ |

Pri `par` in `dint` `Tab` skače po mestih: `par` ⇥ → števec → ⇥ → spremenljivka → ⇥. Pri `dint`: spodnja meja → ⇥ → zgornja meja → ⇥ → integrand → ⇥ → spremenljivka → ⇥. Primer: `dint` ⇥ `2pi` ⇥ `sin @t` ⇥ `@t` ⇥ daje $\int_{0}^{2\pi} \sin \theta \, d\theta$.

### Trigonometrija

`sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `csc`, `sec`, `cot`: backslash se doda sam, npr. `sin @t` → `\sin \theta`. Za `arccsc`, `arcsec`, `arccot` se uporabi `\operatorname{ }`.

### Matrike in okolja

| Vpiši | Kaj dobiš |
|-|-|
| `pmat` | `pmatrix`: okrogli oklepaji |
| `bmat` | `bmatrix`: oglati oklepaji |
| `Bmat` | `Bmatrix`: zaviti oklepaji |
| `vmat` | `vmatrix`: ravne črte (determinanta) |
| `Vmat` | `Vmatrix`: dvojne črte |
| `matrix`, `cases`, `align`, `array` | Okolje s tem imenom |
| `iden3` | Enotska matrika 3×3 (tudi `iden2`, `iden4` …) |

V bloku `$$` snippeti okolja dodajo nove vrstice, v formuli v vrstici ostanejo v eni vrstici. Znotraj matrike veljajo matrične bližnjice (`Tab` → `&`, `Enter` → `\\`).

### Oklepaji

- `(`, `[`, `{`: vstavijo par oklepajev s kurzorjem znotraj, `Tab` skoči čez zaključni oklepaj. Pri označenem besedilu ga obdajo.
- `lr(`, `lr[`, `lr{`, `lr|`, `lra`: velikostno prilagojeni oklepaji `\left … \right`.
- `avg` → `\langle  \rangle`, `ceil` → `\lceil  \rceil`, `floor` → `\lfloor  \rfloor`.
- `norm` → `\lvert  \rvert` (absolutna vrednost), `Norm` → `\lVert  \rVert` (norma).
- `mod` → navpični črti okoli izraza.

### Ostalo

| Vpiši | Koda |
|-|-|
| `tayl` | Taylorjev razvoj `f(x + h) = f(x) + f'(x)h + …` s prostori za izpolnitev |
| `kbt`, `msun` | `k_{B}T`, `M_{\odot}` |
| `dag` | `^{\dagger}` |
| `o+`, `ox` | `\oplus`, `\otimes` |
| `bra`, `ket`, `brk`, `outer` | Dirac: `\bra{ }`, `\ket{ }`, `\braket{ }`, `\ket{\psi} \bra{\psi}` |
| `cee` | `\ce{ }` (kemijske formule) |
| `pu` | `\pu{ }` (enote) |
| `he4`, `he3`, `iso` | Zapis izotopov |

---

## Calctex

Plugin sam izračuna rešitev formule (uporablja CortexJS Compute Engine).

| Dejanje | Kaj se zgodi |
|-|-|
| Na konec formule dodaš `=` | Rešitev se samodejno izračuna in prikaže |
| Klik na rešitev ali `Tab` | Rešitev se zapiše v zapisek |

Primer: v formuli `$2+3=$` se po `=` prikaže rešitev. Formulo najhitreje napišeš z Latex Suite snippeti, na koncu dodaš `=` in preveriš rezultat.

---

## Markdown: hitro pisanje

| Pišem | Dobim |
|-|-|
| `# ` … `###### ` | Naslovi 1–6 |
| `- ` ali `* ` | Seznam |
| `1. ` | Oštevilčen seznam |
| `- [ ] ` | Naloga (checkbox), `Ctrl+Enter` jo označi |
| `> ` | Citat |
| `> [!note]` | Okvir (callout), še `tip`, `info`, `warning` … |
| `**besedilo**` | Krepko |
| `*besedilo*` | Ležeče |
| `==besedilo==` | Označeno |
| `` ` `` | Koda v vrstici (okoli besede) |
| `[[` | Povezava na zapisek (sproži iskanje po zapiskih) |
| `![[` | Vgradi zapisek ali sliko |
| `#oznaka` | Oznaka (tag) |

Blok kode narediš s tremi backticks in imenom jezika (npr. python).

---

## Git plugin

Ukaze najdeš z `Ctrl+P` → `Git`. Bližnjico jim dodeliš sam v **Settings → Hotkeys** (poišči `Git`), npr. ukazu **Commit-and-sync**.

---

## Moje bližnjice

Sem si zapisuj bližnjice, ki jih dodaš ali spremeniš.

| Bližnjica | Kaj naredi |
|-|-|
|  |  |
|  |  |
|  |  |

---

## Viri

- Latex Suite: [GitHub](https://github.com/artisticat1/obsidian-latex-suite), [privzeti snippeti](https://github.com/artisticat1/obsidian-latex-suite/blob/main/src/default_snippets.js)
- Calctex: [GitHub](https://github.com/Developer-Mike/obsidian-calctex)
- Obsidian: [bližnjice za urejanje](https://obsidian.md/help/editing-shortcuts), [hotkeys](https://obsidian.md/help/hotkeys)
