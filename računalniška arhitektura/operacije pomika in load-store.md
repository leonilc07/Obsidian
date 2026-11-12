# Operacije pomika
Pri pomiku se vsi biti v registru premaknejo za določeno število mest v levo ali v desno. Pomike uporabljamo predvsem za hitro **množenje in deljenje s potencami števila 2**, ker je pomik veliko hitrejši od pravega množenja ali deljenja.

## Logični pomik v levo – LSL
**LSL** (*Logical Shift Left*): vsi biti se premaknejo za eno mesto v levo. Najvišji bit izpade, na najnižje mesto pa pride $0$.

**Zgled:** `0111` → `1110` ($7 \to 14$)
- en pomik v levo je množenje z $2$
- $n$ pomikov v levo je **množenje z $2^n$**

## Logični pomik v desno – LSR
**LSR** (*Logical Shift Right*): vsi biti se premaknejo za eno mesto v desno. Najnižji bit izpade, na najvišje mesto pa pride $0$.

**Zgled:** `1101` → `0110` ($13 \to 6$)
- $n$ logičnih pomikov v desno je **celoštevilsko deljenje z $2^n$** (oziroma množenje z $2^{-n}$)
- biti, ki izpadejo, predstavljajo **ostanek** pri deljenju: $13 = 2 \cdot 6 + 1$, izpadel je bit $1$
- ker na najvišje mesto vedno pride $0$, to deluje le za nepredznačena števila

## Aritmetični pomik v desno – ASR
**ASR** (*Arithmetic Shift Right*): vsi biti se premaknejo za eno mesto v desno, najvišji bit (predznak) pa se **ohrani** in se prepiše na najvišje mesto. Tako število ostane pozitivno oziroma negativno.

**Zgleda:**
- `0110` → `0011` ($6 \to 3$)
- `1100` → `1110` ($-4 \to -2$, v dvojiškem komplementu)

ASR uporabljamo za **deljenje predznačenih števil** z $2^n$.

## Rotacija v desno – ROR
**ROR** (*Rotate Right*): vsi biti se premaknejo za eno mesto v desno, najnižji bit pa se vrne na najvišje mesto. Noben bit ne izpade, samo krožijo.

**Zgled:** `1001` → `1100`

# Ukaz za pomik
Pomik je v FRI ARMv7 Lite ukaz iz skupine splošnih aritmetično-logičnih ukazov (glej [[načini naslavljanja in CISC-RISC]]). Ima kodo operacije `11010`, prvi izvorni operand $R_n$ se ne uporablja (`0000`). Pomaknjena vsebina registra $R_m$ se zapiše v $R_d$.

```
31–28 | 27–25 | 24–20 | 19–16 | 15–12 | 11–0
1110  |  000  | 11010 | 0000  |  Rd   | operand pomika
```

Spodnjih 12 bitov (operand pomika) ima dve obliki. Razlikujeta se po **bitu 4**, ki pove, kje je zapisano, za koliko mest se pomika:
- bit 4 = $0$ → število mest je zapisano **v ukazu**
- bit 4 = $1$ → število mest je zapisano **v registru** $R_s$

## Število mest v ukazu (bit 4 = 0)
```
11–7 | 6–5 | 4 | 3–0
Imm  | sh  | 0 | Rm
```
- **Imm**: za koliko mest se pomika; ima 5 bitov, zato je največ $2^5 - 1 = 31$
- **sh**: vrsta pomika
- **Rm**: register, katerega vsebino pomikamo

## Število mest v registru (bit 4 = 1)
```
11–8 | 7 | 6–5 | 4 | 3–0
Rs   | 0 | sh  | 1 | Rm
```
- **Rs**: register, v katerem je zapisano, za koliko mest se pomika
- **sh**: vrsta pomika
- **Rm**: register, katerega vsebino pomikamo

## Vrsta pomika (sh)
- `00` – LSL
- `01` – LSR
- `10` – ASR
- `11` – ROR

## Zgled
V pomnilniku sta od naslova `0x0000000C` naprej shranjena dva ukaza. Vsak zaseda 4 zaporedne pomnilniške besede (bajte):
```
naslov | vsebina
0x0C   | E1  ┐
0x0D   | A0  │ 1. ukaz: E1A07971
0x0E   | 79  │
0x0F   | 71  ┘
0x10   | E1  ┐
0x11   | A0  │ 2. ukaz: E1A088CD
0x12   | 88  │
0x13   | CD  ┘
```

Ukaz razberemo tako, da vsako šestnajstiško števko zapišemo s 4 biti in bite razdelimo na polja.

**1. ukaz** `E1A07971`:
```
1110 | 000 | 11010 | 0000 | 0111 | 1001 | 0 | 11 | 1 | 0001
cond | 00I | pomik |  Rn  |  Rd  |  Rs  |   | sh |   |  Rm
```
- $R_d$ = `0111` = $R_7$
- bit 4 = $1$ → število mest je v registru $R_s$ = `1001` = $R_9$
- sh = `11` → **ROR**
- $R_m$ = `0001` = $R_1$

Ukaz je `ROR R7, R1, R9`: $R_7 \leftarrow R_1$, rotiran v desno za toliko mest, kot je zapisano v $R_9$.

**2. ukaz** `E1A088CD`:
```
1110 | 000 | 11010 | 0000 | 1000 | 10001 | 10 | 0 | 1101
cond | 00I | pomik |  Rn  |  Rd  |  Imm  | sh |   |  Rm
```
- $R_d$ = `1000` = $R_8$
- bit 4 = $0$ → število mest je v ukazu: Imm = `10001` = $17$
- sh = `10` → **ASR**
- $R_m$ = `1101` = $R_{13}$

Ukaz je `ASR R8, R13, #17`: $R_8 \leftarrow R_{13}$, aritmetično pomaknjen v desno za $17$ mest.

# Ukazi za dostop do pomnilnika (load/store)
S temi ukazi prenašamo podatke med pomnilnikom in registri CPE:
- **load**: podatek preberemo iz pomnilnika v enega od registrov CPE
- **store**: podatek iz registra zapišemo v pomnilnik

## Operandi
Ukaz ima **tri operande**:
1. **register**: v kateri register prenašamo iz pomnilnika (load) oziroma iz katerega registra pišemo v pomnilnik (store)
2. **pomnilniška beseda**: iz katere besede beremo v register (load) oziroma v katero besedo pišemo iz registra (store)

Pomnilniško besedo podamo z naslovom, ki je sestavljen iz dveh delov:

$$\text{naslov} = \text{bazni register} + \text{odmik}$$

- **bazni register**: del naslova je v registru
- **odmik**: drugi del naslova je takojšnji operand, zapisan neposredno v ukazu

Za zapis naslova torej potrebujemo dva operanda, enega registrskega in enega takojšnjega. Skupaj z registrom iz točke 1 so to trije operandi. Takemu načinu pravimo **bazno naslavljanje z odmikom**.

## Format ukaza
```
31–28 | 27–25 | 24 | 23 | 22 | 21 | 20 | 19–16 | 15–12 | 11–0
1110  |  010  | 1  | 1  | B  | 0  | L  |  Rn   |  Rt   | Imm12
```
- **L**: vrsta prenosa
	- $L = 0$ → store
	- $L = 1$ → load
- **B**: velikost podatka
	- $B = 0$ → prenašamo 32 bitov
	- $B = 1$ → prenašamo 8 bitov
- **Rn**: bazni register
- **Rt**: ponorni register (pri load) oziroma izvorni register (pri store)
- **Imm12**: odmik; ima 12 bitov, zato je največ $2^{12} - 1 = 4095$
