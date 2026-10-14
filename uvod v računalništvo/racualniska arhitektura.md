*Glej [[Vaje 2.pdf]]*

## Von Neumannova arhitektura
- 4 glavni podsistemi:
	- pomnilnik
	- vhodno/izhodne enote
	- aritmetično-logična enota (ALE)
	- krmilna enota
- program je shranjen v pomnilniku
- zaporedno izvajanje ukazov

## Pomnilnik
- funkcijska enota za shranjevanje in branje podatkov in programov
- pomnilnik z naključnim dostopom (RAM)
	- MAR – *memory address register* (naslovni register)
	- MDR – *memory data register* (podatkovni register)

![[Pasted image 20261014201733.png|364]]

---

## Naloga 1
> Najmanj koliko bitov je potrebnih za naslovni register pri velikosti pomnilnika:
> a) 1 MB,
> b) 10 MB,
> c) 100 MB in
> d) 1 GB?

**a) 1 MB**
$1\,\text{MB} = 1\,000\,000\,\text{B}$
$2^N \geq 1\,000\,000 \Rightarrow N = 20$

**b) 10 MB**
$10\,\text{MB} = 10\,000\,000\,\text{B}$
$2^N \geq 10\,000\,000 \Rightarrow N = 24$

**c) 100 MB**
$100\,\text{MB} = 100\,000\,000\,\text{B}$
$2^N \geq 100\,000\,000 \Rightarrow N = 27$

**d) 1 GB**
$1\,\text{GB} = 1\,000\,000\,000\,\text{B}$
$2^N \geq 1\,000\,000\,000 \Rightarrow N = 30$

### Tabela potenc števila 2

| Potenca  | Rezultat      |
| -------- | ------------- |
| $2^{10}$ | 1 024         |
| $2^{16}$ | 65 536        |
| $2^{20}$ | 1 048 576     |
| $2^{21}$ | 2 097 152     |
| $2^{22}$ | 4 194 304     |
| $2^{23}$ | 8 388 608     |
| $2^{24}$ | 16 777 216    |
| $2^{25}$ | 33 554 432    |
| $2^{26}$ | 67 108 864    |
| $2^{27}$ | 134 217 728   |
| $2^{28}$ | 268 435 456   |
| $2^{29}$ | 536 870 912   |
| $2^{30}$ | 1 073 741 824 |

---

## Naloga 2
> Pomnilnik naj ima dvorazsežno, kvadratno organizacijo. Kakšne so mere pomnilnika vzdolž vsake izmed obeh razsežnosti, če lahko vanj shranimo 1 MB podatkov? Kako velik bo naslovni register? Koliko bitov se pošlje v dekodirnik vrstice in koliko v dekodirnik stolpca? Koliko izhodov imata vsak izmed obeh dekodirnikov?

$x \cdot x\,\text{B} = 1\,\text{MB} = 2^{20}\,\text{B} \Rightarrow x = 2^{10} = 1024$

- **Mere:** $1024 \times 1024$
- **Naslovni register:** 20 bitov
- **Dekodirnik vrstice:** 10 bitov, **dekodirnik stolpca:** 10 bitov
- **Izhodi:** vsak dekodirnik ima $2^{10} = 1024$ izhodov

---

## Naloga 3
> Recimo, da ima pomnilnik 24-bitni naslovni register, prvih 16 bitov je pri tem namenjenih naslovu vrstice, preostalih 8 bitov pa naslovu stolpca. Koliko bajtov podatkov lahko shranimo v ta pomnilnik? Kakšne so mere pomnilnika vzdolž vsake izmed obeh razsežnosti, če predpostavimo, da ima pomnilnik največjo možno velikost?

$2^{16} \cdot 2^{8}\,\text{B} = 2^{24}\,\text{B} = 2^4 \cdot 2^{20}\,\text{B} = 16\,\text{MB}$

- **Velikost:** $16\,\text{MB} = 16\,777\,216\,\text{B}$
- **Mere:** $2^{16} \times 2^{8} = 65\,536 \times 256$


---

## Predpomnilnik
- ozko grlo in princip lokalnosti
- uporaba:
	- poglej v predpomnilnik in uporabi podatek, če je tam
	- če ga ni, dostopaj do pomnilnika RAM
	- kopiraj še $k$ naslednjih podatkov

## Naloga 4
> Povprečni čas dostopa do pomnilnika je 25 ns, povprečni čas dostopa do predpomnilnika pa 10 ns. Kakšen je skupni povprečni čas dostopa, če je verjetnost zadetka v predpomnilniku enaka 80 %? Kakšna pa bi morala biti verjetnost zadetka, če želimo skupni povprečni čas dostopa znižati na 12 ns?

**Povprečni čas pri 80 %**
$0{,}8 \cdot 10\,\text{ns} + 0{,}2 \cdot (10\,\text{ns} + 25\,\text{ns}) = 8\,\text{ns} + 7\,\text{ns} = 15\,\text{ns}$

**Verjetnost zadetka za 12 ns**
$x \cdot 10 + (1-x) \cdot 35 = 12$
$35 - 25x = 12 \Rightarrow x = \frac{23}{25} = 0{,}92$

- **Skupni povprečni čas:** 15 ns
- **Potrebna verjetnost zadetka:** 92 %

---

## Trdi disk
- zunanji pomnilnik (trajni)
- vhodno-izhodne naprave

![[Pasted image 20261014203141.png]]

## Naloga 5
> Recimo, da ima trdi disk naslednje lastnosti:
> - hitrost vrtenja: 7200 obratov / min
> - čas premika glave: 0,5 ms (fiksni začetni čas) + 0,05 ms za vsako sled
> - število površin: 2 (glavi obeh površin se pomikata sočasno)
> - število sledi na površino: 500
> - število sektorjev na sled: 20
> - število bajtov na sektor: 1024
>
> a) Koliko bajtov podatkov lahko shranimo na ta disk?
> b) Kakšni so časi dostopa do enega sektorja v najboljšem, najslabšem in srednjem primeru? Predpostavi, da se v srednjem glava premakne preko 150 sledi.

**a) Kapaciteta**
$2 \cdot 500 \cdot 20 \cdot 1024\,\text{B} = 20\,480\,000\,\text{B}$

**b) Časi dostopa**
$7200\,\text{obr/min} = 120\,\text{obr/s} \Rightarrow \frac{1}{120}\,\text{s} = 8{,}33\,\text{ms/obr}$

**1. Čas iskanja (seek time)**
- najslabši: $0{,}5 + 499 \cdot 0{,}05 = 25{,}45\,\text{ms}$
- srednji: $0{,}5 + 150 \cdot 0{,}05 = 8\,\text{ms}$
- najboljši: $0{,}5\,\text{ms}$

**2. Rotacijska latenca (rotation time)**
- najslabši: cel obrat $= 8{,}33\,\text{ms}$
- srednji: pol obrata $= 4{,}165\,\text{ms}$
- najboljši: $0\,\text{ms}$

**3. Čas prenosa (transfer time)**
$\frac{8{,}33\,\text{ms}}{20} = 0{,}4165\,\text{ms}$ (enak v vseh primerih)

|                | Najslabši     | Srednji       | Najboljši    |
| -------------- | ------------- | ------------- | ------------ |
| Čas iskanja    | 25,45 ms      | 8 ms          | 0,5 ms       |
| Latenca        | 8,33 ms       | 4,165 ms      | 0 ms         |
| Čas prenosa    | 0,4165 ms     | 0,4165 ms     | 0,4165 ms    |
| **Skupaj**     | **34,1965 ms** | **12,5815 ms** | **0,9165 ms** |

## Naloga 6
> V splošnem podatki na disku niso shranjeni povsem naključno, temveč se običajno shranjujejo tako, da je čas, ki je potreben za dostop do podatkov kar najkrajši. Če bi imeli disk iz naloge 5, kam bi shranili 50 KB podatkov, da bi bil poznejši dostop do njih kar najhitrejši?

- **Latenca:** je ne moremo izboljšati.
- **Čas iskanja:** zmanjšamo ga tako, da podatke shranimo blizu **sledi 250** (sredina diska → najkrajši povprečni premik glave).
- **Razporeditev 50 KB** (1 sled = $20 \cdot 1024\,\text{B} = 20\,\text{KB}$):
	1. $20\,\text{KB}$ → sled 250, površina 1
	2. $20\,\text{KB}$ → sled 250, površina 2 (glavi se pomikata sočasno, zato ni dodatnega premika)
	3. $10\,\text{KB}$ → sosednja sled (npr. 251)

---

## Naloga 7
> Na spletu najdite računalniško konfiguracijo in kategorizirajte komponente po Von Neumannovi arhitekturi.

**Konfiguracija:** Prenosnik ACER Nitro V 15, 39,62 cm (15,6"), FHD, IPS, 165 Hz, Ryzen 7 170, 16 GB RAM, 512 GB SSD, RTX 5050, W11H

| Komponenta                         | Podsistem                                  |
| ---------------------------------- | ------------------------------------------ |
| Ryzen 7 170 (procesor)             | ALE + krmilna enota                        |
| 16 GB RAM                          | pomnilnik                                  |
| 512 GB SSD                         | vhod/izhod (zunanji, trajni pomnilnik)     |
| zaslon 15,6" FHD, IPS, 165 Hz      | vhod/izhod                                 |
| W11H (Windows 11 Home)             | programska oprema – ni del strojne arhitekture |

> [!note] Grafična kartica (RTX 5050)
> Grafične kartice ne uvrščamo v nobenega od štirih podsistemov, saj je sama po sebi **svoj računalnik** – ima lasten procesor (GPU) in lasten pomnilnik (VRAM).

---

## Naloga 8
> Imamo glavni pomnilnik velikosti 16 GB, z dostopnim časom 24 ns.
> a) Kako velik je naslovni register?
> b) Povprečni dostopni čas želimo z uporabo predpomnilnika zmanjšati na 18 ns. Kakšen dostopni čas mora imeti predpomnilnik, če vemo, da je verjetnost zadetka enaka 75 %?

**a) Naslovni register**
$16\,\text{GB} = 16 \cdot 2^{30}\,\text{B} = 2^4 \cdot 2^{30}\,\text{B} = 2^{34}\,\text{B} \Rightarrow N = 34$

**b) Dostopni čas predpomnilnika**
$0{,}75 \cdot x + 0{,}25 \cdot (x + 24) = 18$
$x + 6 = 18 \Rightarrow x = 12\,\text{ns}$

- **Naslovni register:** 34 bitov
- **Dostopni čas predpomnilnika:** 12 ns

---

## Naloga 9
> Na trdem disku z naslednjimi lastnostmi:
> - velikost: 5 palcev
> - hitrost vrtenja: 6000 obr./min
> - št. sledi: 500
> - št. sektorjev na sled: 200
> - velikost sektorja: 1024 B
> - št. površin na ploščo: 2
>
> je shranjenih 10000 slik, ki jih želimo prenesti v pomnilnik.
> a) Kolikšna je velikost slike (v bajtih), če slika zasede natanko eno sled na disku?
> b) Kolikšen je čas prenosa ene slike z diska?
> c) Kako velik je pomnilnik, ki lahko hrani natanko 1000 slik? Kolikšna je najmanjša možna velikost naslovnega prostora za tak pomnilnik? Koliko je velik naslovni register?

**a) Velikost slike**
$200 \cdot 1024\,\text{B} = 204\,800\,\text{B} = 200\,\text{KB}$

**b) Čas prenosa ene slike**
$6000\,\text{obr/min} = 100\,\text{obr/s} \Rightarrow 0{,}01\,\text{s/obr} = 10\,\text{ms/obr}$
Slika zasede natanko eno sled → en obrat → $10\,\text{ms}$

**c) Pomnilnik za 1000 slik**
$1000 \cdot 200\,\text{KB} = 200\,000\,\text{KB} = 204\,800\,000\,\text{B}$
$2^{17} \cdot 2^{10}\,\text{B} < 200\,000\,\text{KB} < 2^{18} \cdot 2^{10}\,\text{B} \Rightarrow 2^{28}$

- **Velikost slike:** 204 800 B (200 KB)
- **Čas prenosa:** 10 ms
- **Velikost pomnilnika:** 204 800 000 B (200 000 KB)
- **Najmanjši naslovni prostor:** $2^{28}$
- **Naslovni register:** 28 bitov
