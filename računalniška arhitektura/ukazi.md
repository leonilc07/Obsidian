# Ukazi

Tudi ukazi so, tako kot operandi, **bitni zapisi fiksne dolžine**.

Ukaz (niz bitov) kodira **dve informaciji**:
1. **kaj naj CPE naredi** = operacija
2. **kaj in kje so operandi**

V splošnem je ukaz sestavljen tako (biti od $n-1$ do $0$):

```
| operand1 | o2 | operacija | o3 | ... | om |
```

Delu, ki določa operacijo, pogosto rečemo **operacijska koda (OpCode)**.

## Koliko operandov imajo ukazi

Arhitekture razlikujemo tudi glede na **število operandov v ukazu**.

Kje se operandi sploh nahajajo (hranijo)?
- **v pomnilniku** – glavni pomnilnik je velik in lahko hrani zelo veliko operandov, a je dostop do njega počasen. Vsak operand v pomnilniku ima svoj **naslov**, ki ga mora ukaz vsebovati ali iz njega izračunati, zato so taki ukazi daljši.
- **v CPE** – manjše število operandov, ki jih CPE v nekem trenutku potrebuje. V CPE je vgrajen zelo majhen pomnilnik, vsaki pomnilniški besedi v njem pravimo **register**. Tipično ima CPE **16 ali 32 registrov**.

Naivno bi rekli, naj ima ukaz čim več operandov, nad katerimi izvede isto operacijo. Tak ukaz pa bi bil izjemno dolg (**VLIW – Very Long Instruction Word**), zato:
- bi ga zelo dolgo brali iz pomnilnika
- bi CPE potrebovala nekakšen interni pomnilnik, v katerem bi hranila tako dolg ukaz
- bi bila CPE zelo kompleksna, ker bi morala tako dolg ukaz razumeti

Danes je tipično število operandov v ukazu **$\le 3$**.

## Enooperandni računalniki

Ukaz ima en **ekspliciten operand** (zapisan v ukazu):

```
| operacija | operand |
```

Taki računalniki imajo natanko **en register – akumulator (ACC)**, ki je **impliciten operand** (ni zapisan v ukazu, a se vedno uporabi).

Tipičen ukaz:

$$ACC \leftarrow ACC \text{ op } OPERAND$$

Primeri arhitektur: **Z80** (ZX Spectrum), **6502** (Commodore 64).

## Enooperandni računalniki z več registri

Primer: **Motorola 6800**
- dva 8-bitna akumulatorja: **A** in **B**
- dva 16-bitna registra za delo z naslovi:
	- **indeksni register (X)**
	- **skladovni kazalec (SP)** – kaže na vrh sklada v pomnilniku

En bit operacijske kode pove, **kateri akumulator** (A ali B) ukaz uporablja.

Tipičen ukaz:

$$A \leftarrow A \text{ op } OPERAND \quad \text{ali} \quad B \leftarrow B \text{ op } OPERAND$$

Primer: `ADDA $20` – vsebini akumulatorja A prišteje vsebino pomnilniške lokacije 20 (hex): $A \leftarrow A + M[20]$. Isti ukaz za drugi akumulator je `ADDB $20`, razlikujeta se le v enem bitu operacijske kode.

## Dvooperandni računalniki

Ti računalniki imajo več registrov, npr. 8.

```
| operacija | operand1 | operand2 |
```

Tipičen ukaz:

$$operand1 \leftarrow operand1 \text{ op } operand2$$

Primer: **Intel x86** (32-bitni) – ima 8 registrov:
- **EAX, EBX, ECX, EDX** – za aritmetične in logične operacije
- **ESI, EDI, EBP, ESP** – za računanje z naslovi (ne za aritmetične/logične operacije)

Primera ukazov:
- `MOV EAX, EBX` – $EAX \leftarrow EBX$
- `ADD EAX, EBX` – $EAX \leftarrow EAX + EBX$

## Trioperandni računalniki

```
| operacija | operand1 | operand2 | operand3 |
```

Tipičen ukaz:

$$operand1 \leftarrow operand2 \text{ op } operand3$$

Registrski niz je velik, tipično **16–64 registrov**.

Zgled: **ARMv7** – 16 registrov, sodobna arhitektura, uporabljajo jo praktično vsi (npr. procesorji **ARM Cortex-M**).
- registri **r0, r1, …, r15**
- **r15** se uporablja kot **programski števec (PC)**

Primer ukaza: `SUB r1, r2, r3` – $r1 \leftarrow r2 - r3$

Primer 2: **RISC-V** – 32 registrov (**x0–x31**), trioperandni ukazi.

### Kje so lahko operandi

Operandi so lahko **v pomnilniku**, **v registrih** ali **mešano**. Glede na to poznamo 3 arhitekture:

1. **Pomnilniški računalniki** – računalniki, ki niso imeli registrov; vsi operandi so v pomnilniku.
2. **Pomnilniško-registrski računalniki** – operandi v ukazu so lahko v pomnilniku ali v registru (npr. **Intel**).
	- `ADD AX, [BX]` – $AX \leftarrow AX + M[BX]$
	- `[BX]` pomeni vsebino pomnilniške besede, katere naslov hrani register BX
3. **Registrsko-registrski računalniki** (najnovejša arhitektura)
	- vsi operandi v **aritmetičnih in logičnih ukazih** morajo biti v registrih – **brez izjeme**
	- tudi pri t. i. **pogojnih ukazih** morajo biti operandi v registrih
	- edini ukazi, pri katerih je dovoljen **natanko en pomnilniški operand**, so ukazi za dostop do pomnilnika, s katerimi beremo iz pomnilnika ali pišemo vanj – **load/store ukazi**

S temi računalniki bomo imeli opravka pri tem predmetu.

## Kako CPE povemo, kje v pomnilniku je pomnilniški operand

**Načini naslavljanja (addressing modes)**

Centralni procesni enoti moramo nekako podati naslov pomnilniške besede, v kateri je operand. To lahko storimo na dva načina:

1. **Neposredno pomnilniško naslavljanje** – naslov je zapisan v ukazu.
	- tipičen ukaz: `LOAD reg, naslov` – $reg \leftarrow M[naslov]$
	- $M[naslov]$ je vsebina pomnilniške besede, katere naslov je *naslov*
	- **problem:** danes je pomnilnik ogromen, npr. za 32 GB pomnilnika potrebujemo **35 bitov** za zapis naslova ($2^{35}$ B = 32 GB), zato bi bili ukazi predolgi
2. **Posredno naslavljanje** – naslov (ali del naslova) je zapisan v registru.
	- tipičen ukaz: `LOAD reg1, reg2` – $reg1 \leftarrow M[reg2]$
	- v reg1 zapišemo vsebino pomnilniške besede, katere naslov je v reg2
	- **zakaj je to bolje:** če ima CPE 16 registrov, potrebujemo le **4 bite** ($2^4 = 16$), da povemo, kateri register hočemo, zato naslov operanda v ukazu zapišemo s samo 4 biti
	- vrsti posrednega naslavljanja:
		- **bazno** – naslov (ali del naslova) je zapisan v **enem** registru
		- **indeksno** – naslov (ali del naslova) je zapisan v **več** registrih
