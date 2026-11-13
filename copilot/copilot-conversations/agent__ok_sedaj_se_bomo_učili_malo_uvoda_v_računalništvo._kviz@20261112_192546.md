---
epoch: 1794507946025
mode: agent
backendId: claude
sessionId: "f98c2496-2d0e-4e17-a918-f9b372478e06"
topic: "ok sedaj se bomo učili malo uvoda v računalništvo. kviz ia č…"
tags:
  - copilot-conversation
usage: '{"usedTokens":84046,"contextWindow":1000000,"inputTokens":4,"outputTokens":3,"cacheReadTokens":82723,"cacheWriteTokens":1316,"updatedAt":1794512117566}'
---

**user**: ok sedaj se bomo učili malo uvoda v računalništvo. kviz ia časovno omejitev taok da de či kaj nebo ratalo ti bom poslal sem slike ali jh dal na to datoteok. nato boš malo pogledal kaj sem ndaredil in kaok. dobro zanem
[Timestamp: 2026/11/12 19:25:46]

**ai**: Pripravil sem kviz iz vseh dosedanjih tem ([[Glavno UR]], tedni 1–5 in vaje 6). **Časovna omejitev je 60 minut.** Nastavi si štoparico, piši na papir ali v [[Drawing 2026-11-09 16.26.43.excalidraw|risbo]] in ne glej v zapiske. Ob vsaki nalogi je okviren čas. Kar ti ne uspe, preskoči in pojdi naprej.

# Kviz: Uvod v računalništvo (60 min)

**1. Zahteve in diagram primerov uporabe (8 min)**
- Za vsako zahtevo za bankomat povej, ali je funkcijska ali nefunkcijska: a) uporabnik lahko dvigne gotovino, b) dvig se zaključi v manj kot 5 s, c) PIN je shranjen šifriran.
- Napiši eno uporabniško zgodbo za bankomat v pravilni obliki.
- Nariši diagram primerov uporabe za spletno trgovino. Akter **Kupec** lahko poišče izdelek, doda izdelek v košarico in plača. Akter **Skrbnik** doda izdelek. Plačilo **vedno** vključuje preverjanje kartice, kupon pa se uporabi le **včasih**. Pravilno označi «include» in «extend» ter smer puščic.

**2. Diagram razredov (4 min)**
Katero povezavo bi narisal in kje je romb ali trikotnik?
- a) Hiša in Soba
- b) Ekipa in Igralec (igralec obstaja tudi brez ekipe)
- c) Žival in Pes
- d) Profesor uporabi Projektor kot parameter metode `predavaj(p: Projektor)`

Pri a) dopiši še kratnosti.

**3. Pomnilnik (5 min)**
- a) Najmanj koliko bitov potrebuje naslovni register za pomnilnik velikosti $32 \cdot 2^{20}$ B?
- b) Pomnilnik s kvadratno organizacijo hrani $4 \cdot 2^{20}$ B. Kakšne so mere, koliko bitov ima naslovni register, koliko bitov dobi vsak dekodirnik in koliko izhodov ima vsak?

**4. Predpomnilnik (4 min)**
Dostop do RAM traja 40 ns, do predpomnilnika 8 ns, verjetnost zadetka je 90 %.
- a) Kolikšen je povprečni čas dostopa?
- b) Kolikšna mora biti verjetnost zadetka za povprečni čas 10 ns?

**5. Trdi disk (7 min)**
Disk ima 6000 obr/min, 2 površini (glavi se pomikata skupaj), 400 sledi na površino, 50 sektorjev na sled in 512 B na sektor. Premik glave traja 1 ms + 0,1 ms za vsako sled.
- a) Kakšna je kapaciteta diska?
- b) Izračunaj čas dostopa do enega sektorja v najboljšem, najslabšem in srednjem primeru (v srednjem se glava premakne čez 100 sledi).

**6. Strojni ukazi (6 min)**
V zbirnem jeziku (LOAD, COMPARE, JUMPGT … iz [[Strojni ukazi|tabele]]) napiši program, ki prebere $X$ in $Y$ ter izpiše **večjega** od njiju. Pazi, kaj točno primerja `COMPARE X`.

**7. Binarna števila (6 min)**
- a) $45$ zapiši v dvojiškem sistemu.
- b) $1101101_2$ zapiši v desetiškem sistemu.
- c) $-5$ zapiši s 6 biti v zapisu predznak in velikost ter v dvojiškem komplementu.
- d) Katera števila lahko zapišemo s 6 biti v dvojiškem komplementu?

**8. Mantisa in eksponent (5 min)**
Mantisa ima 8 bitov, eksponent 5 bitov (oba v zapisu predznak in velikost). Zapiši:
- a) $6{,}625$
- b) $-0{,}375$

**9. Leksemi in BNF (7 min)**
- a) Po tabeli leksemov iz vaj 6 razdeli `while (x == 10) x = x - 1;` na lekseme in vsakemu pripiši številko. Koliko leksemov je?
- b) Napiši BNF za nize `1`, `10`, `100`, `1000` … (enica, nato poljubno mnogo ničel).
- c) Po gramatiki
```
<izraz> ::= <clen> | <izraz> * <clen>
<clen>  ::= a|b|c
```
nariši sintaksno drevo za `a * b * c`.

**10. Turingov stroj (6 min)**
- a) Program `1 0 1 1 R`, `1 1 0 1 R`, `1 b 1 2 L` izvedi na začetni konfiguraciji $b\,1_{(1)}\,0\,1\,b$. Zapiši vse korake in končno konfiguracijo.
- b) Napiši program, ki nizu enic doda še eno enico na konec (npr. $b\,1\,1\,1\,b \Rightarrow b\,1\,1\,1\,1\,b$).

---

Ko se čas izteče ali končaš, mi pošlji slike ali nariši v risbo in mi napiši, da si končal. Nato bom pregledal vsako nalogo: kaj je prav, kje je napaka in zakaj. Srečno, **čas teče od zdaj**.
[Timestamp: 2026/11/12 19:25:46]

**user**: nene jaz bom reševal kviz. od profesorjev.  ok zakaj to ni pravokotnik ?

<!-- copilot-image:004252c1f1bd002d16defc91357497cafa953701e6adfc0b1ba64062b5a37f25 -->
![[copilot-image-004252c1f1bd002d16defc91357497cafa953701e6adfc0b1ba64062b5a37f25.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 19:36:46]

**ai**: Pravilen odgovor je **akter**, torej lutka (človeška figura), ne pravokotnik.

Diagram je narejen **za banko**, zato je sistem, ki ga modeliramo, bankin sistem (bankomat). Bankart je **zunanje podjetje** in njegov sistem ni del bankinega sistema, ampak z njim samo komunicira od zunaj. V UML je **akter oseba ali zunanji sistem**, ki sodeluje z našim sistemom. To piše tudi v tvojih zapiskih v [[02 UML - pregled#Sekvenčni diagram|UML - pregled]]: »Akter: lutka na vrhu, uporabnik ali zunanji sistem«.

- **Pravokotnik** (udeleženec, *participant*) uporabimo za dele **našega** sistema, npr. Bankomat ali bankino bazo podatkov.
- **Lutka** (akter) je za vse, kar je **zunaj** našega sistema: Komitent (oseba) in Bankart (zunanji sistem).

**Akter ni nujno človek.** Lutko narišeš za vsakega, ki je zunaj meje sistema, tudi če je to računalniški sistem drugega podjetja.

Na sliki zato manjka piktogram nad Bankartom. Tja spada lutka, enaka kot pri Komitentu.
[Timestamp: 2026/11/12 19:36:46]

**user**: raylo\i malo to

<!-- copilot-image:2dbf7125b1e1405d99a1dc19dca14c7e6ab37fdafb62e94d3f445f5e83d383db -->
![[copilot-image-2dbf7125b1e1405d99a1dc19dca14c7e6ab37fdafb62e94d3f445f5e83d383db.png]]
<!-- /copilot-image -->

<!-- copilot-image:d330e7347d8d970eac1d77d3ab3c0ab79be4ae915d814d92ed20fa5a78754c08 -->
![[copilot-image-d330e7347d8d970eac1d77d3ab3c0ab79be4ae915d814d92ed20fa5a78754c08.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 19:37:51]

**ai**: a) in b) si **zamenjal**. Prav je:

- **a) Komitent** (zgornji akter)
- **b) Imetnik zlate kartice** (spodnji levi akter)

**Kako to prebereš:** pri posplošitvi (generalizaciji) je **prazen trikotnik vedno pri splošnem** akterju, isto kot pri dedovanju v diagramu razredov. Na sliki je trikotnik pod zgornjim akterjem, zato je zgornji splošen. Spodnja dva (Kreditojemalec in b) sta njegovi posebni vrsti.

Smiselno je tudi po vsebini:
- **Komitent** je vsak bančni stranka. Vsak komitent lahko dvigne gotovino, zato je Dvig gotovine povezan z zgornjim akterjem.
- **Kreditojemalec** je komitent, ki lahko še dodatno naredi informativni izračun kredita.
- **Imetnik zlate kartice** je komitent, ki lahko še dodatno pregleda popuste.

Posebni akter **podeduje** vse primere uporabe splošnega akterja. Imetnik zlate kartice in kreditojemalec torej lahko tudi dvigneta gotovino, čeprav nimata svoje črte do Dviga gotovine.

c), d) in vprašanje o relaciji med akterji imaš prav.
[Timestamp: 2026/11/12 19:37:51]

**user**: a ups nisem vidil pu[;ice. sepravi kaj je definicija komitenta_ a tako se re;e splo[nemu clenu.  sedaj sem opayil da imam tipkovnico nastimano na anglesko. kako jo dam na slovensko ce jo upas jo daj ti y ukaiy.
[Timestamp: 2026/11/12 19:41:30]

**ai**: Na računalniku je nameščena samo slovenska tipkovnica, a Windows je začasno naložil še angleško (US) in ta je zdaj vklopljena. Preklopil jo bom na slovensko in angleško odstranil.Tipkovnico sem preklopil na **slovensko** in začasno angleško odstranil. Zdaj bi morali delati č, š in ž, z in y pa bi morala biti spet na svojih mestih. Če se angleška kdaj spet pojavi, med tipkovnicami preklopiš z **Win + preslednica** ali **levi Alt + Shift**.

**Komitent** ni izraz iz UML. To je bančna beseda za **stranko banke**, torej osebo, ki ima pri banki račun. V tem diagramu je pač akter, ki je slučajno splošen.

Splošnemu členu v UML rečemo:
- **splošni akter** (tudi nadrejeni akter, angl. *parent* ali *general actor*), od njega gre posplošitev, trikotnik je pri njem
- **posebni (specializirani) akter** (angl. *child*), to sta tukaj Kreditojemalec in Imetnik zlate kartice

Pri razredih velja isto: splošni razred je **nadrazred**, posebni je **podrazred**.
[Timestamp: 2026/11/12 19:41:30]

**user**: ok sedaj poglej zapiske če je to noter
[Timestamp: 2026/11/12 19:43:15]

**ai**: Delno je v zapiskih.

**Akter kot zunanji sistem (vprašanje z Bankartom): je noter.** V [[02 UML - pregled]] piše na dveh mestih:
- v gradnikih diagrama primerov uporabe: »oseba ali zunanji sistem, ki uporablja sistem«
- v gradnikih sekvenčnega diagrama: »lutka na vrhu, uporabnik ali zunanji sistem«

Ni pa izrecno napisano, da zunanji sistem **ne** narišeš kot pravokotnik, zato je bilo to vprašanje lahko zavajajoče.

**Posplošitev med akterji (vprašanje s Komitentom): ni noter.** Posplošitev s praznim trikotnikom je opisana samo pri diagramu razredov (»Clan je Oseba«). Da lahko z njo povežeš tudi **akterje** in da posebni akter podeduje primere uporabe splošnega, v zapiskih ne piše.

Če želiš, bom oboje dopisal v obstoječo tabelo gradnikov diagrama primerov uporabe, brez novega razdelka.
[Timestamp: 2026/11/12 19:43:15]

**user**: <!-- copilot-image:962413e5d07f432763d161f2b4f1a8167ba60b2d669ac640fc54174bf1957ec9 -->
![[copilot-image-962413e5d07f432763d161f2b4f1a8167ba60b2d669ac640fc54174bf1957ec9.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 19:47:08]

**ai**: **Rezultat:** $2^{34}$ B $= 16$ GB.

**Postopek:**
- **Vhodi** dekodirnika so **biti naslova**, ki jih dekodirnik dobi. Dekodirnik stolpcev dobi 24 bitov, dekodirnik vrstic pa 10 bitov.
- Naslovni register ima skupaj $24 + 10 = 34$ bitov.
- S 34 biti naslovimo $2^{34}$ različnih celic. Ena celica je 1 bajt, zato:

$$2^{10} \cdot 2^{24}\,\text{B} = 2^{34}\,\text{B} = 2^4 \cdot 2^{30}\,\text{B} = 16\,\text{GB} = 17\,179\,869\,184\,\text{B}$$

Mere pomnilnika so $2^{10}$ vrstic $\times$ $2^{24}$ stolpcev $= 1024 \times 16\,777\,216$.

**Pazi:** ne zamenjaj vhodov in izhodov. Dekodirnik z $n$ **vhodi** ima $2^n$ **izhodov**: dekodirnik vrstic ima tukaj $2^{10} = 1024$ izhodov, dekodirnik stolpcev pa $2^{24}$.

To je ista snov kot nalogi 2 in 3 v [[racualniska arhitektura]], le obrnjena. Tudi 34 bitov za 16 GB že imaš v nalogi 8.
[Timestamp: 2026/11/12 19:47:08]

**user**: <!-- copilot-image:44ec3e4cc987e6e67fc2090a7d189719effb1c95512754d971f56d800df8bc81 -->
![[copilot-image-44ec3e4cc987e6e67fc2090a7d189719effb1c95512754d971f56d800df8bc81.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 19:50:02]

**ai**: **Rezultat:** verjetnost zadetka je $50\,\%$.

**Postopek** (isti kot naloga 4 v [[racualniska arhitektura]]):
- **zadetek**: podatek je v predpomnilniku, dostop traja $10$ ns
- **zgrešitev**: najprej pogledamo v predpomnilnik ($10$ ns), nato še v pomnilnik ($30$ ns), skupaj $40$ ns

Z $x$ označimo verjetnost zadetka:

$$x \cdot 10 + (1-x) \cdot 40 = 25$$
$$40 - 30x = 25 \Rightarrow x = \frac{15}{30} = 0{,}5$$

Če kviz $50\,\%$ označi kot napačno, profesor računa brez časa predpomnilnika pri zgrešitvi: $10x + 30(1-x) = 25 \Rightarrow x = 0{,}25$, torej $25\,\%$. Na vajah ste računali z $10 + 30$, zato najprej poskusi z $50\,\%$.
[Timestamp: 2026/11/12 19:50:02]

**user**: <!-- copilot-image:214026dccb1adea2fdbc48915089719a54069a3a8ffedb524211c289dc69838a -->
![[copilot-image-214026dccb1adea2fdbc48915089719a54069a3a8ffedb524211c289dc69838a.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 19:59:16]

**ai**: Odgovor a) je **napačen**, ker ima zamenjana z in w. Program naredi:

```
if (y < x)
    x = w
else
    x = z
```

**Korak za korakom:**
1. `LOAD X`: v register R naloži $x$, torej $R = x$.
2. `COMPARE Y`: po tabeli v [[Strojni ukazi]] primerja **CON(Y) z R**, torej $y$ z $x$. LT = 1, če je $y < x$.
3. `JUMPLT SIX`: če je $y < x$, skoči na SIX.
   - **da** ($y < x$): `LOAD W`, nato `STORE X`, torej $x = w$
   - **ne** ($y \geq x$): `LOAD Z`, `JUMP SEVEN` preskoči LOAD W, nato `STORE X`, torej $x = z$

**Past je v ukazu COMPARE:** `COMPARE Y` ne primerja »x z y«, ampak **y z registrom**. Pogoj se zato bere kot $y < x$, kar je isto kot $x > y$. Med ponujenimi odgovori je pravilen lahko tudi zapisan kot `if (x > y) x = w else x = z`, ker pomeni isto.
[Timestamp: 2026/11/12 19:59:16]

**user**: <!-- copilot-image:b57d11afbe49839f35da0c51c4969353ed7992b1b935386fe811dd63d4150902 -->
![[copilot-image-b57d11afbe49839f35da0c51c4969353ed7992b1b935386fe811dd63d4150902.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 20:01:51]

**ai**: Celoten ukaz ima $4 + 10 = 14$ bitov: najprej operacijska koda iz tabele v [[Strojni ukazi]], nato naslov v dvojiškem zapisu, dopolnjen z ničlami na 10 bitov.

- **ADD 32**: ADD = `0011`, $32 = 2^5$ → `0000100000`
  → **`00110000100000`**
- **DECREMENT 64**: DECREMENT = `0110`, $64 = 2^6$ → `0001000000`
  → **`01100001000000`**
- **INCREMENT 65**: INCREMENT = `0100`, $65 = 2^6 + 2^0$ → `0001000001`
  → **`01000001000001`**

Vpiši jih brez presledkov. Če kviz pravilnega odgovora ne sprejme, poskusi s presledkom med kodo in naslovom (npr. `0011 0000100000`), ker je to odvisno od tega, kako je profesor nastavil vprašanje.
[Timestamp: 2026/11/12 20:01:51]

**user**: ok sedaj kako dela compare v asembliju
[Timestamp: 2026/11/12 20:05:16]

**ai**: `COMPARE X` primerja **vrednost v pomnilniku X** z **vrednostjo v registru R** in ne spremeni nobenega od njiju. Samo nastavi tri bite, imenovane **pogojne kode**:

- **GT = 1**, če je $\text{CON}(X) > R$
- **EQ = 1**, če je $\text{CON}(X) = R$
- **LT = 1**, če je $\text{CON}(X) < R$

Vedno je nastavljena natanko ena od treh, drugi dve sta 0.

**Najpomembneje je vrstni red.** Na levi strani je vedno X (tisto, kar piše za COMPARE), na desni je R (tisto, kar si prej naložil z LOAD):

$$\texttt{LOAD A} \;\; \texttt{COMPARE B} \;\Rightarrow\; \text{primerja } B \text{ z } A$$

GT torej pomeni $B > A$, **ne** $A > B$.

**Primer:** $A = 5$, $B = 8$
```
LOAD    A      ; R = 5
COMPARE B      ; 8 > 5, zato GT = 1, EQ = 0, LT = 0
JUMPGT  NAPREJ ; GT je 1, zato skoči
```

**COMPARE sam ne naredi ničesar vidnega.** Pomemben je šele skupaj z ukazom za skok, ki prebere pogojne kode:
- `JUMPGT X` skoči, če je GT = 1
- `JUMPEQ X` skoči, če je EQ = 1
- `JUMPLT X` skoči, če je LT = 1
- `JUMPNEQ X` skoči, če je EQ = 0
- `JUMP X` skoči vedno

**Kako to prevedeš v if:** pri `LOAD A`, `COMPARE B`, `JUMPLT L` zapišeš pogoj kot »B < A«. Skok se zgodi, ko pogoj velja, zato je koda na oznaki L del »če«, koda takoj za skokom pa del »sicer«. Točno tako je bila sestavljena prejšnja naloga.

**Pazi v zapiskih:** v [[Strojni ukazi]] je pri razdelku »3. Primerjanje« primer `COMPARE X, Y`, ki primerja dve pomnilniški lokaciji. Na kvizih in v tabeli ukazov pa se uporablja različica z enim naslovom, ki primerja z registrom R.
[Timestamp: 2026/11/12 20:05:16]

**user**: <!-- copilot-image:6628ed1d6706cf5d5937732f551bbaab8e1409a271d33a1af8e82785a22699a1 -->
![[copilot-image-6628ed1d6706cf5d5937732f551bbaab8e1409a271d33a1af8e82785a22699a1.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 20:18:51]

**ai**: **Pravilen je e) `01010000`.**

$80$ je **pozitivno** število, zato ga v dvojiškem komplementu zapišeš čisto navadno. Invertiranje in prištevanje 1 uporabiš samo pri negativnih številih.

$$80 = 64 + 16 = 2^6 + 2^4 \to 1010000 \to \mathbf{01010000}\ \text{(8 bitov)}$$

**Hitro preverjanje:** pozitivno število se v dvojiškem komplementu vedno začne z **0**. Zato a), b) in d) že na prvi pogled odpadejo, c) pa je $64 + 32 = 96$.

b) `11010000` je zvijača: to je $80$, zapisan v **predznaku in velikosti** kot $-80$. V dvojiškem komplementu bi bil $-80$ enak `10110000`.
[Timestamp: 2026/11/12 20:18:51]

**user**: <!-- copilot-image:fbab29145caa967689500614c7278522b1bb2f5a1cbc16cefdbc95a12d305c5b -->
![[copilot-image-fbab29145caa967689500614c7278522b1bb2f5a1cbc16cefdbc95a12d305c5b.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 20:20:38]

**ai**: **Odgovor:** `1101010101 000111` (mantisa `1101010101`, eksponent `000111`)

**Postopek** (kot naloga 7 v [[binarna števila]]):

1. **Celi del:** $85 = 64 + 16 + 4 + 1 \to 1010101$
2. **Decimalni del:** $0{,}375 = \frac14 + \frac18 = 2^{-2} + 2^{-3} \to 0{,}011$
3. Skupaj: $85{,}375 = 1010101{,}011$
4. **Normaliziraš:** vejico premakneš za 7 mest levo, pred prvo enico:
$$0{,}1010101011 \times 2^7$$
5. **Mantisa:** predznak 1 (negativno) in biti za vejico. Za vejico je **10 bitov**, prostora pa je samo za 9 (en bit je predznak), zato zadnja enica ($2^{-3} = 0{,}125$) **se izgubi**:
$$\mathbf{1}\,101010101$$
6. **Eksponent:** predznak 0 (pozitiven) in $7 = 111$, od leve dopolnjeno na 5 bitov:
$$\mathbf{0}\,00111$$

**Pazi:** zaradi izgube bita se v resnici shrani $-85{,}25$, ne $-85{,}375$. Za natančen zapis bi mantisa potrebovala 11 bitov.

Vpiši najprej s presledkom med mantiso in eksponentom. Če kviz tega ne sprejme, poskusi brez presledka: `1101010101000111`.
[Timestamp: 2026/11/12 20:20:38]

**user**: Kakšna je desetiška vrednost zapisa 0110 1101 0010 1000, če ga tolmačimo kot znanstveni zapis (11 bitov mantisa, 5 bitov eksponent)?


Uporabite decimalno vejico.
[Timestamp: 2026/11/12 20:26:33]

**ai**: **Odgovor:** $218{,}25$

**Postopek:**

1. Razdeliš 16 bitov: prvih 11 je mantisa, zadnjih 5 eksponent.
$$\underbrace{01101101001}_{\text{mantisa}}\ \underbrace{01000}_{\text{eksponent}}$$
2. **Mantisa:** prvi bit 0 pomeni pozitivno, ostali biti so za vejico:
$$+0{,}1101101001$$
3. **Eksponent:** prvi bit 0 pomeni pozitiven, $1000 = 8$, torej $2^{8}$.
4. Vejico premakneš za 8 mest desno:
$$0{,}1101101001 \times 2^8 = 11011010{,}01$$
5. Pretvoriš v desetiško:
$$11011010 = 128 + 64 + 16 + 8 + 2 = 218, \qquad 0{,}01 = 2^{-2} = 0{,}25$$

Skupaj $218{,}25$.

**Pazi pri razdelitvi:** presledki v zapisu `0110 1101 0010 1000` so le za lažje branje po 4 bite in **ne** kažejo, kje se mantisa konča. Mejo vedno odšteješ sam: 11 bitov, nato 5.
[Timestamp: 2026/11/12 20:26:33]

**user**: <!-- copilot-image:14c702e3189a877f496d3adade32d734be21c48b3424df29e50ac73eb25e4c83 -->
![[copilot-image-14c702e3189a877f496d3adade32d734be21c48b3424df29e50ac73eb25e4c83.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/12 20:28:27]

**ai**: **Pravilen je c) `11011111`.**

**Postopek:**
1. $33 = 32 + 1 \to \mathbf{00100001}$ (8 bitov)
2. Invertiraš bite: $\mathbf{11011110}$
3. Prišteješ 1: $11011110 + 1 = \mathbf{11011111}$

**Preverjanje:** $00100001 + 11011111 = 1\,00000000$, odrežeš 9. bit in dobiš $0$, torej $33 + (-33) = 0$ ✓

Drugi odgovori so pasti:
- a) `11100001` je $-33$ v **predznaku in velikosti** (na 7 bitov dopolnjen)
- b) `11011110` bi bil samo invertiran, brez $+1$, tu pa je še drugačen
- d) se začne z 0, zato je pozitivno število
- e) `11011101` je $-35$
[Timestamp: 2026/11/12 20:28:27]

**user**: sepravi če je decimalka 0,01. a bi se dalo to še nekako drugače prevediti kakor samo z 2 na -2
[Timestamp: 2026/11/12 20:31:18]

**ai**: Da, dve priročni poti.

**1. Kot ulomek:** bite za vejico prebereš kot navadno dvojiško število in ga deliš z $2^{\text{število mest za vejico}}$.
- $0{,}01_2 = \frac{01_2}{2^2} = \frac{1}{4} = 0{,}25$
- $0{,}011_2 = \frac{011_2}{2^3} = \frac{3}{8} = 0{,}375$
- $0{,}1011_2 = \frac{1011_2}{2^4} = \frac{11}{16} = 0{,}6875$

To je najhitrejše, ko je za vejico veliko enic.

**2. Vsako mesto je pol prejšnjega:** mesta za vejico so vredna $0{,}5$, $0{,}25$, $0{,}125$, $0{,}0625$ … Seštej tista, kjer je enica. To je isto kot $2^{-1}, 2^{-2} \dots$, le brez potenc.

**V obratni smeri** (desetiško v dvojiško) decimalni del **množiš z 2** in zapisuješ cele dele **od zgoraj navzdol**:
```
0,375 · 2 = 0,75   → 0   ↓
0,75  · 2 = 1,5    → 1   |
0,5   · 2 = 1,0    → 1   |   (ostane 0, konec)
```
→ $0{,}011$. To je zrcalno deljenju z 2 pri celih številih, le da tam ostanke bereš od spodaj navzgor.

**Popravek prejšnjega odgovora:** pri $-33$ sem dve pasti narobe razložil. Pravilni odgovor c) ostaja.
- a) `11100001` ni predznak in velikost (to bi bilo `10100001`), ampak $-31$ v dvojiškem komplementu.
- b) `11010111` je $-41$.
[Timestamp: 2026/11/12 20:31:18]

**user**: kaj pa v obratnem vrstnem redu. sepravi iz ..1010,01101. tisto kar je za vejico daš samo /2 ubistvu za vsak bit po vrsti in nato samo prišteješ. ali pa daš povsod samo 2 na -n po vrsti in prišteješ
[Timestamp: 2026/11/12 20:35:07]

**ai**: Da, oboje deluje in je v resnici **isto**: $2^{-n}$ je samo vrednost, ki jo dobiš, če $n$-krat deliš z 2. Izberi, kar ti je hitreje.

**Primer:** $1010{,}01101_2$

Celi del: $1010 = 8 + 2 = 10$

Del za vejico, mesto za mestom:
- 1. mesto: bit 0, vrednost $2^{-1} = 0{,}5$
- 2. mesto: bit **1**, vrednost $2^{-2} = 0{,}25$
- 3. mesto: bit **1**, vrednost $2^{-3} = 0{,}125$
- 4. mesto: bit 0, vrednost $2^{-4} = 0{,}0625$
- 5. mesto: bit **1**, vrednost $2^{-5} = 0{,}03125$

Sešteješ tam, kjer je enica: $0{,}25 + 0{,}125 + 0{,}03125 = 0{,}40625$

Skupaj: $\mathbf{10{,}40625}$

**Preverjanje z ulomkom:** $\frac{01101_2}{2^5} = \frac{13}{32} = 0{,}40625$ ✓

**Še tretja možnost, od desne proti levi:** začneš pri zadnjem bitu, na vsakem koraku prišteješ bit in deliš z 2:
```
bit 1:  (0 + 1) / 2 = 0,5
bit 0:  (0,5 + 0) / 2 = 0,25
bit 1:  (0,25 + 1) / 2 = 0,625
bit 1:  (0,625 + 1) / 2 = 0,8125
bit 0:  (0,8125 + 0) / 2 = 0,40625
```
Tako se izogneš majhnim številom, kot je $0{,}03125$, in nikoli ne rabiš potenc. Na kvizu je najvarneje prvo, tretje pa uporabi za preverjanje.
[Timestamp: 2026/11/12 20:35:07]