Kako podamo naslove pomnilniških operandov?

# Načini naslavljanja pomnilniških operandov
## Neposredno
## Posredno
Del naslova je v enem od registrov, drugi del naslova pa je lahko neposredno v ukazu ali v drugem registru.

1. **Bazno**
	- celoten naslov je v registru
	- $\text{naslov} = \text{reg}$
2. **Bazno z odmikom**
	- en del naslova je v registru, drugi je neposredno v ukazu
	- $\text{naslov} = \text{reg} + \text{odmik}$
3. **Indeksno**
	- naslov je v dveh registrih, končni naslov se tvori kot seštevek obeh
	- $\text{naslov} = \text{reg}_1 + \text{reg}_2$
4. **Indeksno z odmikom**
	- naslov je v dveh registrih, tretji del pa neposredno v ukazu
	- $\text{naslov} = \text{reg}_1 + \text{reg}_2 + \text{odmik}$

# Načini naslavljanja nepomnilniških operandov
## Registrsko
Operand je v registru CPE.
## Takojšnje
Operand je del ukaza.

# Število in vrsta operacij
Naivno bi si želeli, da zna CPE izvajati čim več operacij nad različnimi vrstami operandov:
- npr. seštevanje, odštevanje, množenje, deljenje, morda tudi $\sin$, $\cos$, $\tan$, $\log$, …
- nad celimi števili, števili s plavajočo vejico, pa tudi nad neštevilskimi operandi

V praksi je to nepotrebno in zelo drago, zato je danes trend: **čim manj operacij**.

## Dilema CISC – RISC
### CISC
**Complex Instruction Set Computer** – veliko operacij in veliko načinov naslavljanja pomnilniških operandov (npr. Intel).
- ukazi so lahko pom–pom, reg–reg, pom–reg
### RISC
**Reduced Instruction Set Computer** – malo operacij in samo en način naslavljanja pomnilniških operandov.
- ukazi so reg–reg

# Fri ARMv7 Lite
## Shranjevanje operandov v CPE
V CPE je **16 splošnonamenskih registrov**, vsi so 32-bitni. Splošnonamenski pomeni:
- vsi se lahko uporabljajo za shranjevanje operandov
- vsi se lahko uporabljajo v vseh ukazih
- dolžina in način kodiranja ukazov nista odvisna od uporabljenih registrov

Registri $r_0, \dots, r_{15}$ imajo binarne kode $0000, 0001, \dots, 1111$. Register $r_{15}$ je programski števec (PC).

## Vrste operacij
- **aritmetično-logične**
- **dostop do operandov v pomnilniku**
	- *load*: branje iz pomnilnika v enega izmed registrov CPE
	- *store*: pisanje operanda iz registra CPE v pomnilnik
- **skočne (kontrolne)**
	- spreminjajo vrstni red izvajanja ukazov

## Vrste operandov
Samo celoštevilski operandi:
- 8-bitni
- 16-bitni
- 32-bitni

## Načini naslavljanja
Operandi so lahko na treh mestih:
- v registru CPE – **registrsko** naslavljanje
- v ukazu – **takojšnje** naslavljanje
- v pomnilniku – dovolimo le **bazno z odmikom**

Prva dva načina sta namenjena samo aritmetično-logičnim in skočnim ukazom. Tretji način se uporablja samo v ukazih za dostop do pomnilnika (load/store).

## Število operandov v ukazu
Ukazi imajo **3 operande**.

## Pojasnilo glede spreminjanja PC
Po vsakem prebranem ukazu iz pomnilnika se PC samodejno spremeni tako, da kaže na naslednji ukaz v pomnilniku. Običajno to zapišemo kot $PC = PC + 1$.

Tipična dolžina pomnilniške besede je **8 bitov** (1 bajt), ukazi pa so dolgi **32 bitov**, torej vsak ukaz zasede 4 zaporedne pomnilniške besede. Zato mora PC po vsakem ukazu preskočiti 4 naslove: $PC = PC + 4$.


## 1. Splošni aritmetično-logični ukazi
**Data processing instructions**

Ukaz ima 32 bitov (biti $0 \dots 31$):
- **31–28**: za to vrsto ukazov vedno `1110`
- **27–25**: `00I`
	- $I = 0$ → drugi operand je register $R_m$
	- $I = 1$ → drugi operand je takojšnji $Imm8$
- **24–20**: koda operacije (*Op Code*)
- **19–16**: $R_n$ – prvi izvorni operand (vedno v registru)
- **15–12**: $R_d$ – ponorni operand (kamor gre rezultat, vedno v registru)
- **11–0**: drugi izvorni operand, odvisno od bita $I$:
	- $I = 0$: biti 11–4 so same ničle, biti 3–0 so $R_m$ → $R_d \leftarrow R_n \text{ op } R_m$
	- $I = 1$: biti 11–8 so same ničle, biti 7–0 so $Imm8$ (*immediate 8*) → $R_d \leftarrow R_n \text{ op } Imm8$
	- to je število, ki ga zapišemo neposredno v ukaz; ker ima 8 bitov, je njegova največja vrednost $2^8 - 1 = 255$

| Op Code | Ukaz                       |
| ------- | -------------------------- |
| 00000   | AND                        |
| 00010   | EOR                        |
| 00100   | SUB                        |
| 01000   | ADD                        |
| 01010   | ADC (*add with carry*)     |
| 01100   | SBC (*subtract with carry*) |
| 10001   | TST                        |
| 10101   | CMP                        |
| 11000   | ORR                        |
| 11010   | MOV                        |
| 11110   | MVN                        |

**Zgled:** `SUB R4, R7, R1` → $R_4 \leftarrow R_7 - R_1$

Koda ukaza:
```
1110 | 000 | 00100 | 0111 | 0100 | 00000000 | 0001
cond | 00I | opcode|  Rn  |  Rd  |  ničle   |  Rm
     |     |  SUB  |  R7  |  R4  |          |  R1
```