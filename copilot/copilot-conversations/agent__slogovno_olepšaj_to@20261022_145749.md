---
epoch: 1792673869559
mode: agent
backendId: claude
sessionId: "a5b83aa6-7f34-401d-a027-b78c885d9a89"
agentLabel: "slogovno olepšaj to"
usage: '{"usedTokens":133255,"contextWindow":1000000,"inputTokens":2,"outputTokens":8,"cacheReadTokens":130950,"cacheWriteTokens":2295,"updatedAt":1792680458542}'
tags:
  - copilot-conversation
---

**user**: slogovno olepšaj to
[Timestamp: 2026/10/22 14:57:49]

**ai**: Vrstico sem olepšal (155. vrstica v [[nastanek računalništva 2]]):

- **Prednost:** omogoča preprost prehod iz pozitivnega v negativno število (in obratno) v dvojiškem komplementu – negiramo vse bite in prištejemo 1. Primer: $+3 = 011 \rightarrow 100 + 1 = 101 = -3$.

Popravil sem tipkarske napake in razpisal okrajšave. Ker je bil stavek nedokončan („primer:“), sem dodal še primer, ki se ujema s krožnico pod njim.
[Timestamp: 2026/10/22 14:57:49]

**user**: dopolni to tabelo
[Timestamp: 2026/10/22 15:23:16]

**ai**: Tabela v [[zapis realnih števil]] je dopolnjena za vse števke števila 374,6895, od $10^2$ do $10^{-4}$.

- **Popravek:** 3 je na mestu stotic, zato je njena vrednost $3\cdot10^2$, ne $3\cdot10^0$. $10^0$ pripada števki 4.
- Dodal sem stolpec za decimalno vejico in vrstico z vrednostmi (300, 70, 4, 0,6 …).
- Pod tabelo je še celoten zapis: $374,6895 = 3\cdot10^2 + 7\cdot10^1 + 4\cdot10^0 + 6\cdot10^{-1} + 8\cdot10^{-2} + 9\cdot10^{-3} + 5\cdot10^{-4}$
[Timestamp: 2026/10/22 15:23:16]

**user**: naredi isto za binarno število 1011,00101
[Timestamp: 2026/10/22 15:24:01]

**ai**: Pod desetiško tabelo v [[zapis realnih števil]] sem dodal enako tabelo za binarno število $1011,00101_2$. Uteži so tu potence števila 2, od $2^3$ do $2^{-5}$.

- **Celi del:** $8 + 0 + 2 + 1 = 11$
- **Decimalni del:** $0,125 + 0,03125 = 0,15625$
- **Rezultat:** $1011,00101_2 = 11,15625_{10}$
[Timestamp: 2026/10/22 15:24:01]

**user**: naredi sedaj še za ta primir bk in pred vejco bk - bk+1 .. bn-1 in pred bk je bk-1
[Timestamp: 2026/10/22 15:27:33]

**ai**: Pod binarni primer v [[zapis realnih števil]] sem dodal še splošni primer. Število ima $n$ bitov, $b_k$ je zadnji bit pred vejico, levo od njega so $b_{k+1} \dots b_{n-1}$, desno za vejico pa $b_{k-1} \dots b_0$.

- **Uteži:** $b_k$ ima utež $2^0$. Proti levi uteži rastejo do $2^{n-1-k}$, proti desni padajo do $2^{-k}$.
- **Formula:** $v = \sum_{i=0}^{n-1} b_i \cdot 2^{\,i-k}$
- **Preverjanje:** za $1011,00101_2$ je $n = 9$ in $k = 5$, kar spet da $11,15625$.

**Opomba:** napisal si „pred $b_k$ je $b_{k-1}$“. Postavil sem ga takoj za vejico, ker ima tam utež $2^{-1}$. Če ste v razredu uporabljali drugačno oštevilčenje, mi povej in popravim.
[Timestamp: 2026/10/22 15:27:33]

**user**: tako naj bo to kakor sem sedaj naredil
[Timestamp: 2026/10/22 15:28:45]

**ai**: The user edited the file; I need to read it.Tvoja različica ostane taka, kot si jo uredil. Ničesar nisem spremenil.

Na mestu, kjer si zapisal **ne znam zapisati vejce**: vejica nima uteži, ker ni bit, zato je ta celica lahko prazna ali pa vanjo napišeš samo $,$ (tako kot v glavi tabele). Če želiš, ta tekst zamenjam z vejico.
[Timestamp: 2026/10/22 15:28:45]

**user**: naredi ta zgled in izračunaj velikost
[Timestamp: 2026/10/22 15:30:13]

**ai**: Zgled je rešen in dodan v [[zapis realnih števil]], pod vrstico z nalogo: $x = 11011001$ predstavlja število **27,125**.

- Ker je $k = 3$, so zadnji trije biti za vejico: $x = 11011,001_2$.
- **Celi del:** $16 + 8 + 0 + 2 + 1 = 27$
- **Decimalni del:** $0 + 0 + 0,125 = 0,125$
- **Vrednost:** $v(x) = 27,125$

Tabela ima enako obliko kot prejšnje: biti, uteži $2^i$ in vrednosti. Če si z „velikostjo“ mislil kaj drugega, na primer razpon števil, ki jih lahko zapišemo z $n = 8$ in $k = 3$, mi povej in dodam še to.
[Timestamp: 2026/10/22 15:30:13]

**user**: še splošno enačbo odpodaj. vsota je bi * 2na i in ta ji je ubistvu k
[Timestamp: 2026/10/22 15:31:43]

**ai**: Splošno enačbo sem dodal v [[zapis realnih števil]], takoj pod zgled:

$$v(x) = \sum_{i=0}^{n-1} b_i \cdot 2^{\,i-k} = \frac{1}{2^k}\sum_{i=0}^{n-1} b_i \cdot 2^{\,i}$$

- **Kaj naredi $k$:** vsako utež $2^i$ zamakne za $k$ mest. Celoten $x$ torej preberemo kot celo število in ga delimo z $2^k$.
- **Preverjanje na zgledu:** $11011001_2 = 217$ in $\frac{217}{8} = 27,125$, kar se ujema s tabelo.
[Timestamp: 2026/10/22 15:31:43]

**user**: ne i ' k ampak samo 2nai
[Timestamp: 2026/10/22 15:32:44]

**ai**: V vsoti je zdaj samo še $2^i$, brez $-k$:

$$v(x) = \frac{1}{2^k}\sum_{i=0}^{n-1} b_i \cdot 2^{i}$$

Zamik za $k$ je v celoti v ulomku $\frac{1}{2^k}$ spredaj, zato zgled še vedno da $\frac{217}{8} = 27,125$.

Če si želel vsoto čisto brez $k$, se ga ne da odstraniti, ne da bi spremenil oštevilčenje bitov. Bite za vejico bi moral označiti z negativnimi indeksi ($b_{-1}, b_{-2}, \dots$), potem pa bi bila enačba $v(x) = \sum_{i=-k}^{n-k-1} b_i \cdot 2^{i}$. Povej, če raje uporabiš to različico.
[Timestamp: 2026/10/22 15:32:44]

**user**: uredi in daj še dva primira z vejco 0 in 1
[Timestamp: 2026/10/22 15:37:28]

**ai**: Del o težavah v [[zapis realnih števil]] sem uredil in dodal zgled s številoma, ki se razlikujeta samo v zadnjem bitu (0 ali 1).

- **Urejeno:** popravil sem tipkarske napake, $2^{-1}$ je zapisan kot formula, ključne besede pa so poudarjene.
- **Zgled:** ($n = 4$, $k = 1$)
  - $010,0_2 = 2$
  - $010,1_2 = 2,5$
- **Sklep:** sosednji števili se razlikujeta za $0,5$, zato vmesnih vrednosti, na primer $2,3$, ne moremo zapisati natančno.

Če si z „vejco 0 in 1“ mislil primera s $k = 0$ in $k = 1$, mi povej in ju dodam namesto tega.
[Timestamp: 2026/10/22 15:37:28]

**user**: uredi še to in tisto odzgorej skrajšaj
[Timestamp: 2026/10/22 15:40:05]

**ai**: Razdelek o težavah v [[zapis realnih števil]] je zdaj krajši in razdeljen na dva dela:

- **a) Natančnost** ($n = 4$, $k = 1$): najmanjša razlika je $2^{-1} = 0,5$. Zgled $010,0_2 = 2$ in $010,1_2 = 2,5$ je zdaj v eni vrstici namesto tabele, dodal pa sem še obseg od $0$ do $7,5$.
- **b) Popravek** ($k = 3$): $1011 \to 1,011_2 = 1,375$, najmanjša razlika je $2^{-3} = 0,125$. **Ampak se zmanjša obseg:** največje število je samo še $1,875$ namesto $7,5$.

Odstranil sem še podvojeni stavek „ne moremo zapisati vseh realnih števil“.

**Opomba:** v splošni enačbi nad tem razdelkom je zdaj $v(x) = \sum b_i \cdot 2^{i}$, brez $\frac{1}{2^k}$. Tako da cela števila, na primer $217$ namesto $27,125$, ne pa vrednosti z vejico. Tega nisem spreminjal, ker si enačbo spremenil sam. Če želiš, vrnem $\frac{1}{2^k}$.
[Timestamp: 2026/10/22 15:40:05]

**user**: še to uredi
[Timestamp: 2026/10/22 15:42:03]

**ai**: Zadnja dva stavka v [[zapis realnih števil]] sta urejena in ločena od točke b) kot poseben sklep:

**Sklep:** v računalništvu ne moremo biti absolutno natančni.
- Najmanjša razlika med dvema sosednjima številoma se imenuje **ULP** (*Unit in the Last Place* oz. *Unit of Least Precision*).
- Pri fiksni vejici je $\text{ULP} = 2^{-k}$.

Popravil sem tipkarske napake („aboslutno“, „nemoremo“, „dvemi“). Dodal sem polno angleško ime, ki ga za ULP najpogosteje srečaš, in formulo $2^{-k}$, ki se ujema s tvojima primeroma ($0,5$ in $0,125$).
[Timestamp: 2026/10/22 15:42:03]

**user**: to dokončaj in daj v tabelo
[Timestamp: 2026/10/22 15:45:00]

**ai**: Seznam v [[zapis realnih števil]] je zdaj tabela z vsemi osmimi kombinacijami treh bitov za vejico. Vsaka vrstica ima bite, izračun s potencami števila 2 in vrednost.

**Popravek:** zadnje štiri vrednosti so bile v zapisu napačne. Pravilne so:
- $,100 = 0,5$
- $,101 = 0,625$
- $,110 = 0,75$
- $,111 = 0,875$

Pod tabelo sem dodal še opombo, da si vrednosti sledijo v korakih po $\text{ULP} = 2^{-3} = 0,125$.
[Timestamp: 2026/10/22 15:45:00]

**user**: uredi sedaj to
[Timestamp: 2026/10/22 15:48:12]

**ai**: Razdelek „vejica ni fiksna“ v [[zapis realnih števil]] je urejen:

- **Naslov:** dodal sem izraz *plavajoča vejica* (*floating point*).
- **Dopolnjeni eksponenti:** v zapisu so manjkali, zdaj so vsi štirje zapisi pravilni:
  - $983 = 98,3 \cdot 10^{1}$
  - $983 = 9,83 \cdot 10^{2}$
  - $983 = 0,983 \cdot 10^{3}$
  - $983 = 9830 \cdot 10^{-1}$

Ko vejico premaknemo v levo, se eksponent poveča, ko jo premaknemo v desno, pa zmanjša.
[Timestamp: 2026/10/22 15:48:12]

**user**: vredi in daj v tabelo
[Timestamp: 2026/10/22 15:50:24]

**ai**: Primeri s plavajočo vejico v [[zapis realnih števil]] so zdaj v tabeli, desetiški in dvojiški zapisi pa stojijo drug ob drugem. Vrstice so urejene po eksponentu, od $-3$ do $3$.

Popravil sem dve stvari:
- **$101100$ ima eksponent $2^{-2}$**, ne $2^{-3}$. Za $2^{-3}$ je pravilno $1011000 \cdot 2^{-3}$, kar sem dodal kot svojo vrstico.
- **Vrstico „1011 23“ sem razumel kot $10,11 \cdot 2^{2}$.** Tako se zaporedje pravilno nadaljuje: $1011 \to 101,1 \to 10,11 \to 1,011$.

Pod tabelo je pravilo: vejica v levo → eksponent $+1$, vejica v desno → eksponent $-1$. Stavek, da baza ostane ista, sem prestavil v uvodni stavek nad tabelo.
[Timestamp: 2026/10/22 15:50:24]

**user**: šte to
[Timestamp: 2026/10/22 15:52:23]

**ai**: Del z idejo v [[zapis realnih števil]] je urejen:

**Ideja:** število zapišemo z **velikostjo** (mantiso) in **eksponentom** → potrebujemo dve ločeni števili.

Zgled $10,101110_2$:
- **velikost:** $10101110_2$ (vejico odstranimo)
- **eksponent:** $-6$ (6 bitov je bilo za vejico)
- **zapis:** $10101110_2 \cdot 2^{-6} = \frac{174}{64} = 2,71875$

Tvoj eksponent $-6$ je bil pravilen. Dodal sem izraz *mantisa*, ki je strokovno ime za velikost, in desetiško vrednost za preverjanje.
[Timestamp: 2026/10/22 15:52:23]

**user**: kaj je problem pri tisti enačbi prej?
[Timestamp: 2026/10/22 15:55:14]

**ai**: Enačba v 40. vrstici, $v(x) = \sum_{i=0}^{n-1} b_i \cdot 2^{i}$, ne upošteva vejice. Bite prebere, kot da je vejica čisto na koncu, torej izračuna celo število.

Na tvojem zgledu ($x = 11011001$, $k = 3$):
- **Ta enačba da:** $128 + 64 + 16 + 8 + 1 = 217$
- **Pravilno je:** $11011,001_2 = 27,125$

Rezultat je $2^k = 8$-krat prevelik, ker vsak bit dobi utež $2^i$ namesto $2^{i-k}$. Bit $b_0$ bi moral biti vreden $2^{-3} = 0,125$, enačba pa mu da $2^0 = 1$.

Popravek je, da delimo z $2^k$:

$$v(x) = \frac{1}{2^k}\sum_{i=0}^{n-1} b_i \cdot 2^{i}$$

Tako dobimo $\frac{217}{8} = 27,125$. To je ista ideja kot v tvojem razdelku o mantisi: $10101110_2 \cdot 2^{-6}$, kjer je $2^{-6}$ ravno $\frac{1}{2^k}$ za $k = 6$.

Če želiš, enačbo v zapisku popravim.
[Timestamp: 2026/10/22 15:55:14]

**user**: uredi
[Timestamp: 2026/10/22 16:27:30]

**ai**: Razdelek o IEEE 754 v [[zapis realnih števil]] je urejen in razdeljen na dele: dogovor, IEEE 754, normalizacija, primeri in skrita enica.

**Popravek:** $0,01101_2 = 1,101 \cdot 2^{-2}$, ne $2^{-1}$. Vejico moraš premakniti za dve mesti v desno, zato je eksponent $-2$.

Ostale spremembe:
- popravljene tipkarske napake („vejco“, „torek“, „vednoj“, „vdako“ …),
- eksponenti so zapisani kot formule (prej npr. „2na-1“, „krat 21“),
- dodana angleška imena natančnosti (*single*, *double*, *quadruple precision*),
- pravilo za zadnjo vrstico sem poimenoval **skrita enica**, ker je to ustaljeno ime zanj.
[Timestamp: 2026/10/22 16:27:30]

**user**: uredi to v tabelo
[Timestamp: 2026/10/22 16:29:19]

**ai**: Razporeditev bitov za 32-bitni IEEE 754 v [[zapis realnih števil]] je zdaj tabela s tremi vrsticami: biti, pomen in število bitov.

Popravil sem dve napaki:
- **Eksponent je v bitih 30 – 23**, ne 30 – 28. To je 8 bitov in se stakne z mantiso, ki se začne pri bitu 22.
- **Standard je IEEE 754**, ne 745.

Skupaj je $1 + 8 + 23 = 32$ bitov.
[Timestamp: 2026/10/22 16:29:19]

**user**: še to
[Timestamp: 2026/10/22 16:30:55]

**ai**: Formula v [[zapis realnih števil]] je zdaj zapisana kot enačba, pod njo pa so razloženi simboli:

$$v = (-1)^{p} \cdot 1,m \cdot 2^{E}$$

- $p$ – predznak (0 = pozitivno, 1 = negativno)
- $1,m$ – skrita enica + mantisa
- $E$ – eksponent

Besedo „velikost“ sem zamenjal z **vrednost**, ker formula da celo število s predznakom, ne samo velikosti.

V standardu IEEE 754 se eksponent v bite ne zapiše neposredno, ampak s prištetim odmikom 127. To boste verjetno obravnavali v nadaljevanju, zato tega nisem dodal.
[Timestamp: 2026/10/22 16:30:55]

**user**: kaj je skrita enica
[Timestamp: 2026/10/22 16:33:25]

**ai**: Skrita enica je bit 1 pred vejico, ki ga v pomnilnik ne zapišemo, ker vemo, da je vedno tam.

Po normalizaciji ima vsako število obliko $1,\text{xxx} \cdot 2^E$, kar si zapisal v svojem dogovoru: pred vejico je vedno samo en bit in ta bit je vedno 1. Ker je to vedno enako, bi bilo shranjevanje te enice zapravljen bit.

**Primer:** $1110_2 = 1,110 \cdot 2^3$
- v 23 bitov za mantiso shranimo samo $110000\dots0$, torej bite za vejico,
- enice pred vejico ne shranimo, računalnik jo pri računanju doda sam.

**Prednost:** z 23 shranjenimi biti dobimo dejansko 24 bitov natančnosti, ker je 24. bit (enica) „zastonj“.

Zato je v formuli $1,m$: enica je skrita, $m$ pa so shranjeni biti mantise.
[Timestamp: 2026/10/22 16:33:25]

**user**: za E daj še -127
[Timestamp: 2026/10/22 16:34:13]

**ai**: V formulo v [[zapis realnih števil]] sem dodal $-127$:

$$v = (-1)^{p} \cdot 1,m \cdot 2^{E-127}$$

Pri $E$ sem dopisal še razlago: v 8 bitov se shrani število od 0 do 255, pravi eksponent pa je $E - 127$. Tako lahko zapišemo tudi negativne eksponente, približno od $-127$ do $+128$.

**Primer:** za $1,110 \cdot 2^{3}$ se shrani $E = 3 + 127 = 130$.
[Timestamp: 2026/10/22 16:34:13]

**user**: naredi primer z 0101101001110 ... 0 in izračunaj vrednost
[Timestamp: 2026/10/22 16:35:34]

**ai**: Primer je na koncu zapiska [[zapis realnih števil]]: bitni vzorec $0\,10110100\,1110\dots0$ ima vrednost **$1,875 \cdot 2^{53} = 16\,888\,498\,602\,639\,360 \approx 1,69 \cdot 10^{16}$**.

Prvih 13 bitov sem razdelil po tabeli za 32-bitni zapis, ostale bite mantise pa sem dopolnil z ničlami.

- **Predznak:** $0$ → pozitivno
- **Eksponent:** $10110100_2 = 180$, pravi eksponent je $180 - 127 = 53$
- **Mantisa:** $1110\,0\dots0$, s skrito enico $1,111_2 = 1 + 0,5 + 0,25 + 0,125 = 1,875$

Rezultat sem preveril tudi z računalnikom.
[Timestamp: 2026/10/22 16:35:34]

**user**: daj raje da prideš do +(2na53+252+251+250)
[Timestamp: 2026/10/22 16:37:58]

**ai**: Končni izračun v [[zapis realnih števil]] se zdaj konča z vsoto potenc:

$$v = (-1)^0 \cdot 1,111_2 \cdot 2^{53} = +(1 + 2^{-1} + 2^{-2} + 2^{-3}) \cdot 2^{53}$$
$$v = +(2^{53} + 2^{52} + 2^{51} + 2^{50})$$

Vsak bit mantise pomnožimo z $2^{53}$, zato $2^{-1}$ postane $2^{52}$, $2^{-2}$ postane $2^{51}$ in tako naprej. Desetiško število $16\,888\,498\,602\,639\,360$ sem odstranil.
[Timestamp: 2026/10/22 16:37:58]

**user**: ureddi
[Timestamp: 2026/10/22 16:40:40]

**ai**: Vprašanje in primer v [[zapis realnih števil]] sta urejena:

**Vprašanje:** ali lahko vsa števila zapišemo tako, da je spredaj vedno 1?

Poskusimo na številih, kjer za eksponent uporabimo samo **3 bite**:
- $0,00001_2 = 0,00001 \cdot 2^{0} = 0,0001 \cdot 2^{-1} = \dots = 1,0 \cdot 2^{-5}$

Odgovor je verjetno **ne**: s 3 biti in odmikom 3 gre pravi eksponent samo od $-3$ do $4$, zato $2^{-5}$ ne gre v zapis. Tega sklepa nisem dodal v zapisek, ker ga boste verjetno izpeljali sami pri predavanjih. Če želiš, ga dopišem.
[Timestamp: 2026/10/22 16:40:40]

**user**: uredi
[Timestamp: 2026/10/22 16:44:28]

**ai**: Del s 3-bitnim eksponentom v [[zapis realnih števil]] je urejen.

- **Težava:** eksponent s 3 biti je zapisan z odmikom, zato je najmanjši eksponent $-3$, potrebujemo pa $-5$.
- **Najdlje:** vejico lahko premaknemo samo do $0,00001_2 = 0,01 \cdot 2^{-3}$, spredaj pa takrat ni 1.
- **Odgovor:** ne, vseh števil ne moremo zapisati tako, da je spredaj 1.

Popravil sem še tipkarske napake („eksoopnejt“, „najmanši“, „njdlje“) in manjkajoči „P“ v besedi „Poskusimo“.
[Timestamp: 2026/10/22 16:44:28]

**user**: sedaj to še uredi kar sem dodal
[Timestamp: 2026/10/22 16:46:57]

**ai**: Tvoj dodatek v [[zapis realnih števil]] sem uredil kot rešitev prejšnje težave:

**Rešitev – denormalizirana števila:** dogovorimo se, da kadar so v eksponentu **same ničle**, se število ne začne z 1, ampak z **0**.
- Takim številom rečemo **denormalizirana števila**.

Popravil sem okrajšave („št“ → „število“) in stavek razdelil na dva dela.
[Timestamp: 2026/10/22 16:46:57]

**user**: še to
[Timestamp: 2026/10/22 16:47:26]

**ai**: „NORMALIZIRANA ŠTEVILA“ je zdaj podnaslov **Normalizirana števila** (`####`, eno raven pod „32-bitni zapis IEEE 754“). Pred njim sem dodal prazno vrstico, da ga Obsidian ne prilepi na tabelo.

Če želiš, naredim enak podnaslov še za **Denormalizirana števila** spodaj, da bosta oba dela enako označena.
[Timestamp: 2026/10/22 16:47:26]