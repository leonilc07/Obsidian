---
epoch: 1794816919188
mode: agent
backendId: claude
sessionId: "166e59b1-97f4-4ac9-a56c-76ec6235e29c"
topic: "te zapiske iz vaj dodaj na file funkcjie, definicije, kako s…"
tags:
  - copilot-conversation
usage: '{"usedTokens":237895,"contextWindow":1000000,"inputTokens":2,"outputTokens":895,"cacheReadTokens":236435,"cacheWriteTokens":563,"updatedAt":1794828949087}'
---

**user**: te zapiske iz vaj dodaj na file funkcjie, definicije, kako se izračuna vse  tiste primere, dodatne razlage in vse podobne stvari in nato preimenuj ta ročni zapisek in ga shrani v mapo stvari
[Timestamp: 2026/11/16 09:15:19]

**ai**: Berem ročni zapisek po delih (povečane izreze), da lahko natančno prepišem vse primere.Zdaj dopolnjujem `funkcije.md` z vsemi primeri iz vaj.Vse zapiske z vaj sem prepisal v [[funkcije]], ročni zapisek pa preimenoval v **`Funkcije - vaje.excalidraw.md`** in ga premaknil v mapo `stvari`. Na koncu `funkcije.md` je povezava nanj.

**Kaj je novega v [[funkcije]]:**
- **Definicijsko območje:** pravila za ulomek, sodi in lihi koren, logaritem in presek pogojev. Zraven so vsi primeri 1a–1h s postopkom.
- **Injektivnost, surjektivnost, bijektivnost:** definicije, kaj pomenijo na grafu (vodoravnica) in kako injektivnost dokažeš.
- **Inverzna funkcija:** definicija, $D_{f^{-1}} = Z_f$, zrcaljenje čez $y = x$ in postopek v treh korakih. Primeri so $\frac{x+1}{2x-3}$ (z dokazom injektivnosti, ničlami, polom in asimptoto), $\ln(2x-1)$ ter $3 - 2x^2$ na zoženem območju.
- **Soda in liha:** postopek preverjanja in primeri 3a–3d. K logaritmom sem dodal pravilo $r \log_a x = \log_a x^r$.
- **Kompozitum:** definicija in primer $f(x) = e^x$, $g(x) = -\frac{1}{x^2}$.
- **Kvadratna funkcija:** formule za ničle, diskriminanto in teme ter primer $3 - 2x^2$.
- **Signum:** definicija in primer $\operatorname{sign}(3 - 2x^2)$.
- Grafe (desmos) sem dodal pri primerih, kjer pomagajo: 1b, oba inverza, parabola in signum.

**Popravki pri prepisu:**
- **Primer 1f:** v zapisku piše $D_f = [-4, 0]$, pravilno je $(-4, 0]$, ker je pogoj pri logaritmu strog ($x > -4$).
- **Primer 3b:** med računom je v zapisku vmesna vrstica napačna ($-x^2 - 2 + x + 1$). Zapisal sem pravilen račun, rezultat (soda) ostane enak.

Če je bil zapisek odprt v zavihku, ga po premiku ponovno odpri iz mape `stvari`.
[Timestamp: 2026/11/16 09:15:19]

**user**: ok sedaj imaš tukaj še vaje iz diskretnih struktur. prebrskaj datoteke v diskretnih strukturah in če je treba kje kaj dopolni z tem kar je zapisano tukaj v teh vaja. ni treba vseh primirov prepisavati samo kakšne osnutke lli kakšen trik ki ga mogoče pokaži na kakem primiru ali kaj takega. ta zadnja naloga je profesor ni uspel rešiti tako da jo daj sedaj ti sem v komentar(5 naloga). nato preimenuj in daj ta zapisek v stvari.

<!-- copilot-image:99cba50c32fee9b9c397ca637c6be573a399b8d4c890f091112ec4adb40b050f -->
![[copilot-image-99cba50c32fee9b9c397ca637c6be573a399b8d4c890f091112ec4adb40b050f.png]]
<!-- /copilot-image -->
[Timestamp: 2026/11/16 12:05:55]

**ai**: Ročni zapisek z vaj DS sem prebral. Zdaj rišem Vennov diagram za 5. nalogo in dopolnjujem `Množice.md` ter `Kartezični produkt, moč množic in relacije.md`.Zdaj še preimenujem in premaknem ročni zapisek.Rešil sem 5. nalogo: **natanko en predmet zanima 48 dijakov**. Rešitev je spodaj, zapisal sem jo tudi v [[Kartezični produkt, moč množic in relacije]] kot nalogo 3, skupaj z Vennovim diagramom.

## 5. naloga: rešitev

Oznake: $M$ = matematika, $F$ = fizika, $B$ = biologija.

1. **Unija prek komplementa:** tisti, ki jih ne zanima nič, so $(M \cup F \cup B)^c$ (De Morgan). Zato je $|M \cup F \cup B| = 100 - 30 = 70$.
2. **Presek vseh treh** dobiš iz načela vključitev in izključitev, kjer je to edina neznanka:
$$70 = 32 + 20 + 45 - 15 - 7 - 10 + |M \cap F \cap B| \Rightarrow |M \cap F \cap B| = 5$$
3. **Vsako območje "samo ena množica" posebej:** od množice odšteješ oba preseka parov. Presek vseh treh si s tem odštel dvakrat, zato ga enkrat prišteješ:
   - samo M: $32 - 7 - 15 + 5 = 15$
   - samo F: $20 - 7 - 10 + 5 = 8$
   - samo B: $45 - 15 - 10 + 5 = 25$

**Rezultat:** $15 + 8 + 25 = 48$

**Preverba:** natanko dva predmeta zanimata $2 + 10 + 5 = 17$ dijakov, vse tri pa 5. Skupaj $48 + 17 + 5 = 70$ ✓

**Krajša pot:** natanko ena $= S_1 - 2S_2 + 3S_3 = 97 - 64 + 15 = 48$. Pri tem je $S_1$ vsota moči vseh treh množic, $S_2$ vsota presekov parov in $S_3$ presek vseh treh.

Profesor je na tabli z rdečo začel izražati območje $M \cap F^c \cap B^c$ prek komplementov, kar je zelo dolga pot. Ključ je v tem, da najprej izračunaš $|M \cap F \cap B| = 5$. Po tem je vsako območje en sam odštevek.

## Spremembe v zapiskih

**[[Množice]]:** nov razdelek "triki pri reševanju (vaje)" pod enakostmi. Vsak trik je pokazan na enem primeru z vaj:
- izpostavljanje skupne množice, npr. $(A \cup B) \cap (A \cup B^c) = A$
- dvojna razlika $X \setminus (X \setminus Y) = X \cap Y$, gnezdene razlike razpakiraš od znotraj
- razlika se razdeli čez unijo, primer $(A + B) \setminus A = B \setminus A$
- dokaz vsebovanosti po elementih
- iskanje protiprimera z Vennovim diagramom in majhnimi množicami
- pri simetrični razliki se enaki členi pokrajšajo: $(A + B) + (A + C) = B + C$
- 8 območij Vennovega diagrama treh množic in zapis "natanko ena"

**[[Kartezični produkt, moč množic in relacije]]:**
- pri formuli za $|A \cup B|$ je dodana obrnjena oblika $|A \cap B| = |A| + |B| - |A \cup B|$
- nova naloga 3 (dijaki) z diagramom ![[Naloga dijaki.excalidraw]]

**Datoteke:** ročni zapisek je zdaj `stvari/Množice - vaje.excalidraw.md`, povezava nanj je na koncu razdelka s triki. Diagram za nalogo je v `stvari/Naloga dijaki.excalidraw.md`.
[Timestamp: 2026/11/16 12:05:55]

**user**: koliko ročnih zapiskov je seda v mapi stvari?
[Timestamp: 2026/11/16 12:15:52]

**ai**: V mapi `stvari` sta **2 ročna zapiska** v Excalidrawu, oba sem premaknil danes:
- `Funkcije - vaje.excalidraw.md`
- `Množice - vaje.excalidraw.md`

Ročno pisanje je tudi v mapi `stvari/Ink`, ki jo naredi vtičnik Ink: **14 datotek SVG**, 13 v `Ink/Writing` in 1 v `Ink/Drawing`.

V mapi je še **15 drugih risb Excalidraw**, ki niso ročni zapiski. To so diagrami za zapiske (Vennovi diagrami, Turingov stroj, sintaksna drevesa ipd.). Odprl sem le `Naloga programerji`, ki je sestavljena iz oblik in natipkanega besedila. Druge so prav tako majhne datoteke, ročna zapiska pa imata vsak okoli 1 MB, ker sta narisana s prosto roko.
[Timestamp: 2026/11/16 12:15:52]

**user**: daj jih iz stvari v mapo Excalidraw in vsakemu daj pred njega črko za določen predmet recimo DS ali M ali ...
[Timestamp: 2026/11/16 12:17:18]

**ai**: Vse risbe pripadajo trem predmetom: DS, M in uvod v računalništvo (zanj uporabim **UR**). Premikam jih in nato popravim povezave v zapiskih.Zdaj popravljam povezave v zapiskih.
[Timestamp: 2026/11/16 12:17:18]

**user**: ne samo zapiske.
[Timestamp: 2026/11/16 12:18:09]

**ai**: Razumem: v mapo Excalidraw gresta samo ročna zapiska, diagrame vračam v `stvari` z njihovimi prvotnimi imeni.Diagrami so spet na mestu. Popravljam še povezavi na oba ročna zapiska.Oba ročna zapiska sta zdaj v mapi `Excalidraw` in imata pred imenom oznako predmeta:
- `M - Funkcije - vaje.excalidraw.md`
- `DS - Množice - vaje.excalidraw.md`

Povezavi nanju v [[funkcije]] in [[Množice]] sem popravil na nova imena.

Na začetku sem po pomoti premaknil in preimenoval tudi 15 diagramov. Vse sem vrnil v `stvari` s prvotnimi imeni, zato vgrajene slike v zapiskih delujejo kot prej.

V mapi `Excalidraw` je bil že prej ročni zapisek `diskretne strukture vaje 4.md`, ki še nima oznake. Če želiš, ga preimenujem v `DS - vaje 4.excalidraw.md`.
[Timestamp: 2026/11/16 12:18:09]

**user**: preimenuj še tisto drugo ki je v elixsdraw
[Timestamp: 2026/11/16 12:19:37]

**ai**: I renamed the note in the Excalidraw folder: it is now **`DS - vaje 4.excalidraw.md`**. I changed the link to it in [[DS glavno]] (under "vaje") to the new name.

The `Excalidraw` folder now holds:
- `DS - Množice - vaje.excalidraw.md`
- `DS - vaje 4.excalidraw.md`
- `M - Funkcije - vaje.excalidraw.md`
[Timestamp: 2026/11/16 12:19:37]

**user**: sedaj je tukaj zapisek še o indukciji ki smo jo malo ponovili. preberi že narejeno datoteko matematična indukcija in dodaj noter če je kaj novega. nato ta zapisek izbriši in vse datoteke povezane nanj
[Timestamp: 2026/11/16 12:21:05]

**ai**: Preberem nove zapiske z indukcije (tri slike Ink). Novo je: vsota lihih števil, $F_{3n}$ je sodo in tlakovanje s triomini. Zdaj to dodajam v `matematična indukcija.md`.Diagram je v redu. Zdaj dopolnjujem zapisek.Brišem stari zapisek in njegove tri slike Ink.I added the new material from the review session to [[matematična indukcija]] and deleted the old note together with its linked files.

**Added to [[matematična indukcija]]:**
- **Precise wording of both steps:** the base is always the *smallest* number for which the claim is stated (0, 1 or e.g. 3), and the inductive step is "if it holds for $k$, it also holds for the successor $k+1$".
- **Example 7, sum of the odd numbers:** $1 + 3 + \dots + (2n-1) = n^2$. In the step you get $n^2 + (2n+1) = (n+1)^2$.
- **Example 8, $F_{3n}$ is even:** the same trick as for $F_{4n}$. Expand until you get $2F_{3n+1} + F_{3n}$, which is even plus even.
- **Example 9, tiling with triominoes:** the $2^n \times 2^n$ board with one square removed. The base is $n = 0$, where nothing is left to tile. In the step you split the board into 4 quadrants and place one triomino in the middle. A diagram is included: ![[Indukcija triomino.excalidraw]]
- **Trick for the triominoes:** the assumption has to hold for *any* position of the removed square.

**Deleted:**
- `diskretne strukture/12. 11 - indukcija dopolnjevanje.md`
- the three Ink images it embedded (`stvari/Ink/Writing/2026.11.12 - 11.32am.svg`, `11.35am.svg`, `11.47am.svg`)

Before deleting I checked that no other note links to them. The new diagram is saved as `stvari/Indukcija triomino.excalidraw.md`.
[Timestamp: 2026/11/16 12:21:05]

**user**: saj si napisal po sloensko
[Timestamp: 2026/11/16 12:26:32]

**ai**: Oprosti, zadnji odgovor sem po pomoti napisal v angleščini. Tukaj je v slovenščini.

V [[matematična indukcija]] sem dodal snov s ponavljanja, stari zapisek pa sem izbrisal skupaj z datotekami, ki so bile povezane nanj.

**Dodano v [[matematična indukcija]]:**
- **Natančnejša formulacija obeh korakov:** baza je vedno *najmanjše* število, za katero trditev trdimo (0, 1 ali npr. 3). Indukcijski korak pravi: če trditev velja pri $k$, velja tudi pri nasledniku $k+1$.
- **7. primer, vsota lihih števil:** $1 + 3 + \dots + (2n-1) = n^2$. V koraku dobiš $n^2 + (2n+1) = (n+1)^2$.
- **8. primer, $F_{3n}$ je sodo:** isti trik kot pri $F_{4n}$. Razpisuješ, dokler ne dobiš $2F_{3n+1} + F_{3n}$, kar je sodo plus sodo.
- **9. primer, tlakovanje s triominami:** plošča $2^n \times 2^n$ z enim odstranjenim poljem. Baza je $n = 0$, kjer ne ostane nič za tlakovati. V koraku ploščo razdeliš na 4 kvadrante in en triomino položiš v sredino. Zraven je diagram: ![[Indukcija triomino.excalidraw]]
- **Trik pri triominih:** predpostavka mora veljati za *katerokoli* lokacijo odstranjenega polja.

**Izbrisano:**
- `diskretne strukture/12. 11 - indukcija dopolnjevanje.md`
- tri slike Ink, ki jih je zapisek vseboval (`stvari/Ink/Writing/2026.11.12 - 11.32am.svg`, `11.35am.svg`, `11.47am.svg`)

Pred brisanjem sem preveril, da nanje ne kaže noben drug zapisek. Novi diagram je shranjen kot `stvari/Indukcija triomino.excalidraw.md`.
[Timestamp: 2026/11/16 12:26:32]

**user**: in sedaj so tukaj še ene vaje iz diskretnih struktur. naredi isto kot prej
[Timestamp: 2026/11/16 12:27:24]

**ai**: Novi ročni zapisek je `diskretne strukture/9.11.md` (predikatni račun in množice). Berem ga po delih.Nove vaje so bile v datoteki `diskretne strukture/9.11.md`. Kot prej sem v zapiske dodal samo trike, vsakega pokazanega na enem primeru. Ročni zapisek sem preimenoval v **`DS - Predikati in množice - vaje.excalidraw.md`** in ga premaknil v mapo `Excalidraw`. Na koncu novega razdelka v predikatih je povezava nanj, drugih povezav na staro ime ni bilo.

**V [[področje pogovora in predikati]] je nov razdelek "triki pri PNO (vaje)":**
- **Kvantifikator na levi strani implikacije se obrne:** iz $\forall x\, P(x) \Rightarrow \forall x\, Q(x)$ dobiš $\exists x\, \forall y\, (P(x) \Rightarrow Q(y))$. Dodal sem opozorilo na pogosto napako $\forall x\, \forall y$.
- **Na desni strani implikacije ostane kvantifikator enak**, implikacijo lahko pustiš.
- **PNO ni enolična:** kvantifikatorje iz ločenih delov formule lahko izvlečeš v poljubnem vrstnem redu.
- **Preimenovanje pred izvlečenjem:** potrebno je, ker $\exists$ ne gre čez $\land$, sicer bi moral isti $y$ ustrezati obema predikatoma.
- **Protiprimer za neenakovrednost:** pri $\neg \forall x\, \exists y$ in $\forall y\, \exists x$ je kvantifikatorja zamenjana, kar pokaže protiprimer na $D = \{a, b\}$ s tabelo iz zapiska. Izid je 0 proti 1, zato formuli nista enakovredni.

**V [[Množice]] so trije novi triki:**
- **Simetrična razlika s podmnožico:** $C + (A \cup C) = A \setminus C$.
- **Potenčna množica minus množica števil:** nič se ne odšteje, ker so elementi $\mathcal{P}X$ množice. Tudi $\emptyset$ se pri $+$ izniči.
- **$\emptyset$ in $\{\emptyset\}$:** pri potenčni množici so dodani trije primeri iz 4. naloge.

**Napake v ročnem zapisku, ki jih nisem prepisal:**
- **Pri 1a** je podčrtana oblika $\forall x\, \forall y\, (P(x) \Rightarrow Q(y))$ napačna. Pravilno je $\exists x\, \forall y$.
- **Pri 3e** je v $\mathcal{P}\{2, 3\}$ zapisano $\{0\}$ namesto $\emptyset$. Končni rezultat je kljub temu pravilen.

V mapi `Excalidraw` je še `DS - vaje 4.excalidraw.md`, ki ga v zapiske še nisem vključil. Če želiš, ga obdelam na enak način.
[Timestamp: 2026/11/16 12:27:24]

**user**: ok daj še tistega
[Timestamp: 2026/11/16 12:34:10]

**ai**: Vaje 4 so iz predikatnega računa: resničnost formul v $\mathbb{N}$, iskanje interpretacij in (ne)enakovrednost formul. Dopolnjujem `področje pogovora in predikati.md`.Vaje 4 so obdelane. Vse iz njih je šlo v [[področje pogovora in predikati]], ker so v celoti iz predikatnega računa. Ročni zapisek sem preimenoval v **`DS - Predikati - vaje 4.excalidraw.md`**, da je iz imena razvidna snov. Povezavo v [[DS glavno]] sem popravil na novo ime, nova povezava pa je tudi na koncu trikov pri PNO.

**Dodano v [[področje pogovora in predikati]]:**
- **Triki pri določanju resničnosti:**
  - $\forall$ ovržeš z enim protiprimerom, $\exists$ potrdiš z enim primerom.
  - Pri $\forall x\, (W \Rightarrow V)$ gledaš samo tiste $x$, pri katerih $W$ velja.
  - Pazi na robna elementa $0$ in $1$ v $\mathbb{N}$.
  - Vse je pokazano na 1. nalogi (praštevila in deljivost), npr. $x = 1$ nima praštevilskega delitelja, $x = 1$ deli vse, $x = 10$ pri $\exists x\, \forall y$.
- **Triki pri (ne)enakovrednosti:**
  - Neenakovrednost pokažeš z eno interpretacijo na $\{a\}$ ali $\{a, b\}$ s tabelo. Primeri iz 2. naloge so $\forall$ proti $\exists$, $\Leftrightarrow$ proti $\Rightarrow$ in $\forall x\, \forall y\, (P(x) \Rightarrow P(y))$.
  - Enakovrednost pokažeš s preoblikovanjem, kjer $\exists$ združiš čez $\lor$ in prepoznaš $P \Leftrightarrow Q$. To je 4. naloga, skupaj s protiprimerom $Q = \neg P$ za tretjo formulo.
- **Negacija čez več kvantifikatorjev:** pri zakonih je dodan primer iz 3. naloge, $\neg \forall x\, \exists y\, (P(x) \land \neg Q(y)) \sim \exists x\, \forall y\, (P(x) \Rightarrow Q(y))$.

Dve stvari iz zapiska nisem prepisal:
- **Seznam zakonov** na levi strani lista, ker je že v zapiskih.
- **Naloga 2d**, ker je na listu le "-11-" in en primer, zato iz zapiska ne razberem, kaj se je točno reševalo.
[Timestamp: 2026/11/16 12:34:10]