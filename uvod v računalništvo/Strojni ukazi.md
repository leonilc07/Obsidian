# Aritmetično-logična enota

**ALE** je del procesorja (skupaj s krmilno enoto).

Vsebuje **vezja**:
- za aritmetiko: `+`, `-`, `*`, `/`
- za primerjanje in logiko: `=`, IN, ALI, NE

Vsebuje **registre**:
- izjemno hitre namenske pomnilniške enote, povezane z vezjem ALE

**Podatkovna pot** (data path) – kako potuje informacija v ALE:
- iz registrov na vezja
- iz vezij nazaj v registre

# Strojni ukazi

**Format ukaza** v strojnem jeziku:
- koda operacije (op code)
- naslovi pomnilniških lokacij z operandi

**Primer:**
- op code: 9
- naslov X: 99
- naslov Y: 100
- `ADD X, Y` sešteje števili in zapiše rezultat nazaj na lokacijo Y
- binarno: `00001001 0000000001100011 0000000001100100`

## 1. Prenos podatkov

- pomnilniška lokacija → register ALE
- register ALE → pomnilniška lokacija
- ena pomnilniška lokacija → druga pomnilniška lokacija
- en register ALE → drug register ALE

**Primeri:**
- `LOAD X` – naloži vsebino pomnilniške lokacije X v register
- `STORE X` – shrani vsebino registra R na pomnilniško lokacijo X
- `MOVE X, Y` – kopira vsebino pomnilniške lokacije X na lokacijo Y

## 2. Aritmetika

Aritmetične in logične operacije v ALE: `+`, `-`, `*`, `/`, IN, ALI, NE

**Primeri:**
- `ADD X, Y, Z` – v Z shrani vsoto X in Y
- `ADD X, Y` – v Y shrani vsoto X in Y
- `ADD X` – v register shrani vsoto X in registra

## 3. Primerjanje

Rezultat primerjanja nastavi vrednosti bitov **pogojnih kod** (GT, EQ, LT).

**Primer:** `COMPARE X, Y` primerja vrednosti pomnilniških lokacij X in Y ter nastavi pogojne kode:
- vr(X) > vr(Y) → GT = 1, EQ = 0, LT = 0
- vr(X) = vr(Y) → GT = 0, EQ = 1, LT = 0
- vr(X) < vr(Y) → GT = 0, EQ = 0, LT = 1

## 4. Vejitve

Spreminjajo normalni zaporedni tok izvajanja ukazov, tipično **po ukazu za primerjanje**.

**Primeri:**
- `JUMP X` – vzemi naslednji ukaz s pomnilniške lokacije X
- `JUMPGT X` – skoči samo, če je indikator GT nastavljen na 1
- `JUMPGE X` – skoči, če je GT ali EQ nastavljen na 1
- `HALT` – ustavi izvajanje programa

## 5. Nabor strojnih ukazov

| Binarna koda | Operacija   | Pomen                                                                                                    |
| ------------ | ----------- | -------------------------------------------------------------------------------------------------------- |
| 0000         | LOAD X      | CON(X) → R                                                                                               |
| 0001         | STORE X     | R → CON(X)                                                                                               |
| 0010         | CLEAR X     | 0 → CON(X)                                                                                               |
| 0011         | ADD X       | R + CON(X) → R                                                                                           |
| 0100         | INCREMENT X | CON(X) + 1 → CON(X)                                                                                      |
| 0101         | SUBTRACT X  | R − CON(X) → R                                                                                           |
| 0110         | DECREMENT X | CON(X) − 1 → CON(X)                                                                                      |
| 0111         | COMPARE X   | if CON(X) > R then GT = 1 else 0<br>if CON(X) = R then EQ = 1 else 0<br>if CON(X) < R then LT = 1 else 0 |
| 1000         | JUMP X      | Get the next instruction from memory location X.                                                         |
| 1001         | JUMPGT X    | Get the next instruction from memory location X if GT = 1.                                               |
| 1010         | JUMPEQ X    | Get the next instruction from memory location X if EQ = 1.                                               |
| 1011         | JUMPLT X    | Get the next instruction from memory location X if LT = 1.                                               |
| 1100         | JUMPNEQ X   | Get the next instruction from memory location X if EQ = 0.                                               |
| 1101         | IN X        | Input an integer value from the standard input device and store into memory cell X.                      |
| 1110         | OUT X       | Output, in decimal notation, the value stored in memory cell X.                                          |
| 1111         | HALT        | Stop program execution.                                                                                  |
