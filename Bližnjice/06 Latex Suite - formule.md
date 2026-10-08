---
tags:
  - cheatsheet
---

# Latex Suite: formule

Nazaj na [[00 Kazalo|Kazalo]]. Prej: [[04 Latex Suite - osnove|osnove]], [[05 Latex Suite - simboli|simboli]].

> [!info] Kako brati
> - Snippeti delujejo **samo znotraj formule** (`$...$` ali `$$...$$`), razen če piše drugače.
> - Snippet z oznako **⇥** se razširi šele s tipko `Tab`. Vsi ostali se razširijo takoj, ko vtipkaš sprožilec.

## Potence, indeksi, ulomki, koreni

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

## Naglasi in pisave

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

## Vsote, limite, odvodi, integrali

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

## Trigonometrija

`sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `csc`, `sec`, `cot`: backslash se doda sam, npr. `sin @t` → `\sin \theta`. Za `arccsc`, `arcsec`, `arccot` se uporabi `\operatorname{ }`.

## Matrike in okolja

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

## Oklepaji

- `(`, `[`, `{`: vstavijo par oklepajev s kurzorjem znotraj, `Tab` skoči čez zaključni oklepaj. Pri označenem besedilu ga obdajo.
- `lr(`, `lr[`, `lr{`, `lr|`, `lra`: velikostno prilagojeni oklepaji `\left … \right`.
- `avg` → `\langle  \rangle`, `ceil` → `\lceil  \rceil`, `floor` → `\lfloor  \rfloor`.
- `norm` → `\lvert  \rvert` (absolutna vrednost), `Norm` → `\lVert  \rVert` (norma).
- `mod` → navpični črti okoli izraza.

## Ostalo

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
