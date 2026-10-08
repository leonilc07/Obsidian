---
tags:
  - cheatsheet
---

# Markdown: osnove

Nazaj na [[00 Kazalo|Kazalo]]. Naprej: [[03 Markdown - povezave in struktura|povezave in struktura]].

> [!tip] Če ne veš sintakse
> Pritisni `Ctrl+P` in vpiši `toggle` ali `insert`. Obsidian ima ukaze za oblikovanje (seznam, citat, tabela, črta …).

## Odstavki, prelomi vrstic in črte

- **Nov odstavek:** med besedilom pusti prazno vrstico.
- **Prelom vrstice v odstavku:** `Shift+Enter` ali dva presledka na koncu vrstice in `Enter`. Če imaš v Settings → Editor vklopljeno *Strict line breaks*, se samo `Enter` v prikazu zlije v isto vrstico.
- **Vodoravna črta:** tri ali več znakov `---`, `***` ali `___` (tudi `* * *`) na svoji vrstici.

```md
Prvi odstavek.

---

Drugi odstavek.
```

> [!warning] Pasti pri `---`
> - `---` takoj pod vrstico besedila naredi iz nje naslov. Pred črto vedno pusti prazno vrstico.
> - `---` na samem začetku zapiska ni črta, ampak začetek bloka lastnosti (glej [[03 Markdown - povezave in struktura#Oznake in lastnosti|Oznake in lastnosti]]).

## Naslovi

```md
# Naslov 1
## Naslov 2
### Naslov 3
#### Naslov 4
##### Naslov 5
###### Naslov 6
```

Za `#` mora biti **presledek**. Brez njega (`#naslov`) je to oznaka (tag).

## Poudarki

| Pišem | Dobim |
|-|-|
| `**krepko**` ali `__krepko__` | **krepko** |
| `*ležeče*` ali `_ležeče_` | *ležeče* |
| `***krepko ležeče***` | ***krepko ležeče*** |
| `~~prečrtano~~` | ~~prečrtano~~ |
| `==označeno==` | ==označeno== |
| `` `koda` `` | `koda` |
| `\*ni ležeče\*` | \*ni ležeče\* |

Backslash `\` pred znakom prepreči oblikovanje (več v naslednjem razdelku).

## Posebni znaki

Backslash pred znakom izklopi njegov poseben pomen.

- `\*`, `\_`, `\#`, `\|`, `\~`: znak se izpiše, oblikovanje se ne zgodi.
- `\$`: znak za dolar v besedilu (npr. cena). Brez backslasha lahko Obsidian dva `$` v istem odstavku vzame za formulo.
- `1\.`: številka s piko ne naredi seznama.

## Seznami in številčenje

```md
- alineja
- druga alineja
    - podalineja (Tab)
    - še ena

1. prvi korak
2. drugi korak
    1. podkorak
3. tretji korak

- [ ] odprta naloga
- [x] opravljena naloga
```

- **Alineje:** `-`, `*` ali `+` in presledek.
- **Številčenje:** `1.` ali `1)` in presledek. `Enter` nadaljuje seznam (naslednja številka se vstavi sama), `Enter` na prazni alineji seznam zaključi.
- **Zamik:** `Tab` naredi podalinejo, `Shift+Tab` jo vrne nazaj. Tipe seznamov lahko mešaš (številke z alinejami znotraj).
- **Začetek številčenja:** prva številka določa začetek (`5.` začne pri 5). Črkovnega številčenja (a, b, c) Markdown nima.
- **Prelom vrstice v alineji:** `Shift+Enter` doda prelom, ne da bi se številčenje spremenilo.
- **Naloge:** `- [ ]` in `- [x]`, `Ctrl+Enter` preklopi stanje.
- **Besedilo, ki se začne s številko in piko, brez seznama:** backslash pred piko, npr. `1\. besedilo`.

## Citati, narekovaji in okvirji

Citat naredi `>` na začetku vsake vrstice, dodaten `>` pa citat v citatu:

```md
> To je citat.
> Nadaljuje se v naslednji vrstici.
>
> > Citat v citatu.
```

**Narekovaji:** navadni `"narekovaji"` so samo znaki, Markdown jih ne spremeni. Slovenske narekovaje „ in “ kopiraj od tu: „besedilo“. Pozor: v formuli (`$...$`) Latex Suite znak `"` spremeni v `\text{ }`.

**Okvirji (callouts)** so citati z oznako tipa:

```md
> [!note] Naslov (neobvezen)
> Besedilo okvirja. Deluje tudi **oblikovanje**, [[povezave]] in $formule$.

> [!tip]- Zložen okvir (klik ga odpre)
> Skrito besedilo.

> [!question] Zunanji
> > [!todo] Notranji
```

- `-` za tipom: okvir je privzeto zložen. `+`: privzeto razprt.
- Neznan tip se prikaže kot `note`.
- Za matematiko se obnesejo npr. `info` (definicija), `tip` (izrek), `example` (primer), `warning` (pozor).

| Tip | Drugi nazivi |
|-|-|
| `note` | privzeti |
| `abstract` | `summary`, `tldr` |
| `info` |  |
| `todo` |  |
| `tip` | `hint`, `important` |
| `success` | `check`, `done` |
| `question` | `help`, `faq` |
| `warning` | `caution`, `attention` |
| `failure` | `fail`, `missing` |
| `danger` | `error` |
| `bug` |  |
| `example` |  |
| `quote` | `cite` |
