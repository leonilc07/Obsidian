---
epoch: 1791624598975
mode: agent
backendId: claude
sessionId: "5cae816a-b77c-4417-8a9b-b1366ff13662"
agentLabel: "tukaj sem sedaj napisal snov. sedaj popravi slogovne in razn…"
usage: '{"usedTokens":194907,"contextWindow":1000000,"inputTokens":2,"outputTokens":281,"cacheReadTokens":194065,"cacheWriteTokens":559,"updatedAt":1792074787978}'
tags:
  - copilot-conversation
---

**user**: tukaj sem sedaj napisal snov.  sedaj popravi slogovne in razne napake.  in lahko spremniš še kaj da bo bolj berljivo.
[Timestamp: 2026/10/10 11:29:58]

**ai**: Zapisek [[nastanek računalnika]] je popravljen: tipkarske in pravopisne napake, vejice, velike začetnice in nezaključene krepke oznake (`**operandi`, `**pomnilnik`, `**program`).

Na treh mestih sem posegel v vsebino oziroma ugibal, kaj si mislil, zato jih preveri:

- **Točka 2 v Volume 6:** pisalo je »naj bodo *računalniki* shranjeni v enem delu računalnika«. Spremenil sem v »*ukazi* naj bodo shranjeni …«, ker je to edino smiselno glede na točko 3.
- **Točka 1 v Volume 6:** »ođičwnja« sem prebral kot »ožičenja«.
- **Naslovi:** »in a word of a genius« sem spremenil v »in the words of a genius«, »to smart to exit« v »too smart to exit«, pri Volume 1 pa sem odstranil odvečni »da« na koncu.

Za boljšo berljivost sem spremenil še to:

- Vprašanja v Volume 5 so zdaj cele povedi z vprašaji, z uvodno vrstico nad seznamom.
- Poudarek z velikimi črkami (»TOREJ PODATEK O LOKACIJI …«) je zdaj callout `[!important]` pod seznamom.
- Puščice `<-` v Volume 6 sem prepisal v običajne stavke.
- Pri centralni procesni enoti sem dodal kratici CPE in CPU.
- Med razdelki so prazne vrstice, naslovi »Volume« pa so ostali.
[Timestamp: 2026/10/10 11:30:00]

**user**: sedaj naredi isto in za zadnji volume uporabi plugine ki jih imam nameščene/aktivirane  lahko pogledaš zapsike od matematike ali DS
[Timestamp: 2026/10/10 12:02:09]

**ai**: Novi del zapiska [[nastanek računalnika]] je popravljen: točke 6–10 v Volume 6 in celoten Volume 7, ki je zdaj zapisan v LaTeXu v enakem slogu kot [[množice števil]] (bločne formule, `align`, decimalna vejica `0{,}5`).

Od vtičnikov imaš aktivirane samo Latex Suite, CalcTeX, Git in Copilot, zato sem uporabil LaTeX. Excalidraw, Desmos in ostali so nameščeni, a izklopljeni, zato jih nisem uporabil. V [[predavanje 1]] pri DS je samo naslov, tako da sem se zgledoval le po matematiki.

Preveri ta mesta, kjer sem ugibal ali kaj dodal:

- **Zgleda 1 in 2:** bila sta prazna, zato sem ju izračunal sam: $S(1000) \approx 1{,}998$ pri $f = 0{,}5$ in $S(1000) \approx 9{,}91$ pri $f = 0{,}9$.
- **Limita:** dodal sem callout z zgornjo mejo $\frac{1}{1-f}$, ki je v tvojem zapisku ni bilo. Če je na predavanju niste omenili, ga izbriši.
- **Skica programa:** tvoji črtni skici `|--f--|--1-f--|` sem zamenjal z dvema formulama z oznakami pod členi (»se pohitri«, »ostane«).
- **Ime:** »Ahmdol« sem popravil v Amdahl.
- **Točka 9:** pisalo je »dobi *operacijo* iz zunanjega sveta«; zapisal sem »podatke dobi iz zunanjega sveta in jih v zunanji svet tudi pošlje«.
- **Naslov Volume 7:** »na IQ to high« sem spremenil v »IQ too high«, ker besede »na« nisem razumel.
- **Kratice:** dodal sem PC pri programskem števcu in ALE pri aritmetično-logični enoti.
[Timestamp: 2026/10/10 12:02:11]

**user**: za izgleda izlušči še ugotovitev
[Timestamp: 2026/10/10 12:02:47]

**ai**: Na konec zapiska [[nastanek računalnika]] sem dodal razdelek »Ugotovitev«, ki povzame oba zgleda:

- **Tabela:** za vsak zgled primerja $f$, $N$, dobljeno pohitritev $S(N)$ in zgornjo mejo $\frac{1}{1-f}$.
- **Ne dobimo $N$-kratne pohitritve:** s 1000 računalniki je program le $2$-krat oziroma $10$-krat hitrejši.
- **Odloča $f$, ne $N$:** pohitritev omejuje del programa $1 - f$, ki ga ne moremo pohitriti.
- **Smo že skoraj na meji:** v obeh zgledih dodajanje računalnikov ne pomaga več.
- **Sklep v calloutu:** bolj se splača povečati delež programa, ki ga lahko pohitrimo, kot dodajati računalnike.

Ugotovitev sem izpeljal sam iz obeh izračunov, zato jo primerjaj s tem, kar ste zapisali na predavanju.

Popravil sem tudi svojo napako iz prejšnjega koraka: v izračunih obeh zgledov je bil na koncu vrstic en sam `\` namesto `\\`, zato se enačbe niso prelomile v vrstice. Zdaj je prav.
[Timestamp: 2026/10/10 12:02:50]

**user**: povej mi kako dobim ta znak za negacijo in vse ostale za te stvari in dodaj to odzadi še drugim
[Timestamp: 2026/10/10 13:20:31]

**ai**: Preveril sem, katere bližnjice ima tvoj Latex Suite; zdaj dodajam znake še ostalim veznikom v zapisku.Znake pišeš v matematičnem načinu (med `$ … $`) z ukazi LaTeX; v [[izjave in izjavni vezniki]] sem jih dodal na konec vsake vrstice z vezniki.

| Veznik | Znak | Ukaz | Bližnjica v Latex Suite |
|-|-|-|-|
| negacija | $\neg p$ | `\neg p` | ni |
| konjunkcija | $p \land q$ | `p \land q` | ni |
| disjunkcija | $p \lor q$ | `p \lor q` | ni |
| ekskluzivna disjunkcija | $p \oplus q$ | `p \oplus q` | `o+` |
| implikacija | $p \implies q$ | `p \implies q` | `=>` |
| ekvivalenca | $p \iff q$ | `p \iff q` | ni |

Bližnjice sem preveril v privzetih nastavitvah tvojega Latex Suite: obstajata samo `o+` in `=>`, ostale ukaze moraš vpisati v celoti. Pazi, bližnjici `and` in `orr` dasta množična znaka $\cap$ in $\cup$, ne logičnih $\land$ in $\lor$.

V zapisku preveri dvoje:

- **Črki:** tvoj »¬f« sem zamenjal z $\neg p$ in povsod uporabil $p$ in $q$. Če na predavanjih uporabljate druge črke, jih zamenjaj.
- **Znaki:** za ekskluzivno disjunkcijo sem izbral $\oplus$, nekateri profesorji pišejo $\veebar$ (`\veebar`). Za implikacijo in ekvivalenco sem uporabil dvojni puščici; če pišete enojni, sta ukaza `\to` (bližnjica `->`) in `\leftrightarrow` (bližnjica `<->`).

Lastne bližnjice za `\neg`, `\land`, `\lor` in `\iff` se da dodati v nastavitvah Latex Suite pod »Snippets«.
[Timestamp: 2026/10/10 13:20:42]

**user**: dodaj to v bljižnice
[Timestamp: 2026/10/10 13:27:13]

**user**: [Request interrupted by user]
[Timestamp: 2026/10/10 13:27:16]

**ai**: No response requested.
[Timestamp: 2026/10/10 13:27:27]

**user**: tisto tabelo v mapo bljižnice
[Timestamp: 2026/10/10 13:27:27]

**ai**: Tabelo sem dodal v mapo Bližnjice, na konec zapiska [[05 Latex Suite - simboli]], kot nov razdelek »Logika: izjavni vezniki«.

- **Oblika:** stolpci so veznik, kaj vpišeš, koda in videz, tako kot v ostalih tabelah tam.
- **Ekskluzivna disjunkcija:** vpisal sem oba zapisa, `\veebar` (ki ga zdaj uporabljaš v zapisku) in `\oplus` z bližnjico `o+`.
- **Opozorilo:** pod tabelo je callout, da `and` in `orr` dasta $\cap$ in $\cup$, ne $\land$ in $\lor$.
- **Kazalo:** v [[00 Kazalo]] sem pri opisu tega zapiska dodal besedo »logika«.
[Timestamp: 2026/10/10 13:27:29]

**user**: naredi pod negacijo pravilnostno tabelo v tej datoteki
[Timestamp: 2026/10/10 13:29:10]

**ai**: Pravilnostna tabela je dodana pod razdelek »negacija« v [[izjave in izjavni vezniki]]:

| $A$ | $\neg A$ |
|:-:|:-:|
| $0$ | $1$ |
| $1$ | $0$ |

Uporabil sem $1$ za resnično in $0$ za neresnično, kot imaš zapisano zgoraj v zapisku.

Pri tem sem opazil napako v 6. vrstici, ki je nisem popravljal: piše »*resnične (1)* in *neresnične(1)*«, pri neresničnih bi morala biti (0).
[Timestamp: 2026/10/10 13:29:12]

**user**: ali je kakšna bljižnica za dati tabelo v dat
[Timestamp: 2026/10/10 13:29:50]

**ai**: Privzete bližnjice za tabelo Obsidian nima, lahko pa jo vstaviš z ukazom in si bližnjico nastaviš sam.

- **Ukaz:** pritisni `Ctrl+P`, vpiši `Insert table` in potrdi z `Enter`. Vstavi se prazna tabela 2×2, s `Tab` skačeš v naslednjo celico, z `Enter` v naslednjo vrstico.
- **Lastna bližnjica:** v **Settings → Hotkeys** poišči `Insert table` in ji dodeli kombinacijo, npr. `Ctrl+Shift+T`.
- **Desni klik:** v zapisku izberi **Insert → Table**. Z desnim klikom na obstoječo tabelo dodajaš in brišeš vrstice ter stolpce.

Imaš tudi nameščen, a izklopljen vtičnik Advanced Tables (`table-editor-obsidian`). Če ga vklopiš, napišeš samo `| A | ¬A` in pritisneš `Tab`, pa se tabela sama naredi in poravna.
[Timestamp: 2026/10/10 13:29:57]

**user**: tisto z | ne dela
[Timestamp: 2026/10/10 13:47:32]

**ai**: Vtičnik Advanced Tables imaš zdaj vklopljen in `Tab` je v njegovih nastavitvah vezan na tabele, tako da bi moralo delati. Kaj točno si vtipkal, ne vidim, zato so to najverjetnejši vzroki:

1. **Kazalec je v formuli.** Če napišeš `| $A$ | $\neg A$` in pritisneš `Tab`, ko je kazalec še med `$ … $`, ga prestreže Latex Suite in te samo vrže iz formule. Pritisni `Tab` še enkrat, ko si zunaj formule, ali pa najprej naredi tabelo z navadnim besedilom in formule vpiši potem.
2. **Vrstica se ne začne z `|`.** Pred prvim `|` ne sme biti besedila ali alineje (`-`), nad vrstico pa naj bo prazna vrstica.
3. **Vtičnik se še ni naložil.** Če si ga vklopil tik pred tem, zapri in ponovno odpri Obsidian (ali `Ctrl+P` → `Reload app without saving`).

Preizkusi v prazni vrstici brez formul:

```md
| A | B
```

S kazalcem na koncu vrstice pritisni `Tab`. Dobiti moraš glavo tabele z ločilno vrstico pod njo.

Če še vedno ne dela, uporabi `Ctrl+P` → `Insert table`, ki dela neodvisno od vtičnika. Povej mi, kaj točno si vtipkal in kaj se je zgodilo ob `Tab`, pa bom pogledal naprej.
[Timestamp: 2026/10/10 13:47:35]

**user**: napiši hirearhijo z > znaki in nato še vsako z svojimi znaki in oklepaji
[Timestamp: 2026/10/10 13:54:38]

**ai**: V razdelek »dogovorno opuščanje oklepajev« v [[izjave in izjavni vezniki]] sem dopisal hierarhijo in primere z oklepaji za vsa tri pravila.

Hierarhija je zapisana tako (levo veže najmočneje):

$$
\neg \;>\; \land \;>\; \lor,\ \veebar \;>\; \implies \;>\; \iff
$$

- **Pravilo 1 (hierarhija):** en dolg primer z vsemi vezniki in tabela, ki za vsak par sosednjih ravni pokaže, kam gredo oklepaji, npr. $A \land B \lor C = (A \land B) \lor C$.
- **Pravilo 2 (ista vrsta):** tabela za vsak veznik posebej, npr. $A \implies B \implies C = (A \implies B) \implies C$.
- **Pravilo 3 (disjunkciji):** $\lor$ in $\veebar$ sta na isti ravni, npr. $A \lor B \veebar C = (A \lor B) \veebar C$.

Vrstni red hierarhije sem zapisal po spominu na običajni dogovor, ker je bila tvoja vrstica prazna, zato ga primerjaj s tablo. Posebej preveri dvoje:

- **Raven $\veebar$:** dal sem jo na isto raven kot $\lor$, kar sem sklepal iz tvojega tretjega pravila.
- **Implikacija od leve proti desni:** $A \implies B \implies C$ sem po tvojem drugem pravilu zapisal kot $(A \implies B) \implies C$. Nekateri učbeniki jo združujejo z desne.
[Timestamp: 2026/10/10 13:54:40]

**user**: naredi tukaj konstrukcisko drevo tako da rata spodnji izraz
[Timestamp: 2026/10/10 14:05:31]

**ai**: Namesto vrstice »p q p« je v [[izjave in izjavni vezniki]] zdaj konstrukcijsko drevo za izraz $p \implies q \implies p$, narisano kot Mermaid diagram (Obsidian ga izriše sam, brez vtičnika). Izrisa v Obsidianu nisem mogel preveriti, zato poglej, ali so listi lepo v zgornji vrsti.

```mermaid
graph TD
    p1["p"] --> a["p ⇒ q"]
    q["q"] --> a
    a --> r["p ⇒ q ⇒ p"]
    p2["p"] --> r
```

- **Zgradba:** zgoraj so listi $p$, $q$, $p$; prva dva se združita v $p \implies q$, ta pa z drugim $p$ v končni izraz. To se ujema s tvojo vrstico spodaj, da $q \implies p$ v izrazu ne nastopa.
- **Dolžina in globina:** drevo ima 5 vozlišč (3 spremenljivke + 2 veznika) in globino 2. Tega v zapisek nisem dopisal.
- **Znak:** v diagramu je `⇒` vpisan kot navaden znak, ker Mermaid ne izriše LaTeXa (`$\implies$`).
[Timestamp: 2026/10/10 14:05:34]

**user**: naredi resničnostno tabelo za ta izraz ker meni se je neda prepisat iz zvezka
[Timestamp: 2026/10/10 14:10:32]

**ai**: Tvojo vrstico s stolpci sem v [[izjave in izjavni vezniki]] zamenjal z resničnostno tabelo za $q \land (p \implies (\neg r))$. Vrednosti sem izračunal sam, zato jih lahko primerjaš z zvezkom:

| $p$ | $q$ | $r$ | $\neg r$ | $p \implies \neg r$ | $q \land (p \implies (\neg r))$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |

Vrstice so urejene od 000 do 111; če ste jih na predavanju pisali v obratnem vrstnem redu (od 111 navzdol), povej in jih obrnem.
[Timestamp: 2026/10/10 14:10:34]

**user**: ali lahko kamor sem dal | narediš malo bolj močno črto
[Timestamp: 2026/10/10 14:11:05]

**ai**: Tabelo v [[izjave in izjavni vezniki]] sem prepisal v LaTeX, tako da sta navpični črti samo tam, kjer si imel `|`: za stolpcem $r$ in pred končnim izrazom. Izrisa v Obsidianu nisem mogel preveriti.

Navadna Markdown tabela ne zna poudariti posamezne črte, zato sem uporabil okolje `array`. Črte določa vrstica `{ccc|cc|c}`: vsak `c` je en stolpec, `|` pa črta med njima. Vrednosti so enake kot prej.

$$
\begin{array}{ccc|cc|c}
p & q & r & \neg r & p \implies \neg r & q \land (p \implies (\neg r)) \\
\hline
0 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 & 1 \\
1 & 0 & 0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 \\
1 & 1 & 0 & 1 & 1 & 1 \\
1 & 1 & 1 & 0 & 0 & 0
\end{array}
$$

Slabost je, da tabele ne moreš več urejati s klikanjem po celicah, ampak samo v kodi. Če želiš dvojno črto, zamenjaj `|` z `||`.
[Timestamp: 2026/10/10 14:11:10]

**user**: kako se naredi tisto vijugo za enakovredna izraza
[Timestamp: 2026/10/10 14:18:59]

**ai**: Vijuga za enakovredna izraza je `\sim`, v Latex Suite pa jo dobiš z bližnjico `simm` (znotraj formule):

| Vpiši | Koda | Videz |
|-|-|-|
| `simm` | `A \sim B` | $A \sim B$ |

Če ste na predavanju pisali kak drug znak, so to najpogostejše različice:

| Vpiši | Koda | Videz |
|-|-|-|
| `sim=` | `A \simeq B` | $A \simeq B$ |
| `\approx` | `A \approx B` | $A \approx B$ |
| `===` | `A \equiv B` | $A \equiv B$ |

Bližnjice `simm`, `sim=` in `===` so že zapisane v [[05 Latex Suite - simboli]]; `\approx` nima bližnjice, zato jo vtipkaš v celoti.
[Timestamp: 2026/10/10 14:19:03]

**user**: olepšaj še sedaj malo te zapiske.  ampak ne preveč kakor lako vidiš sem od prej ko si ustavil tiste tabele jih izbrisal na primer.   

še za dva izraza moraš narediti pravilnostno tabelo, saj jih boš videl.
[Timestamp: 2026/10/10 14:24:04]

**ai**: Zapisek [[izjave in izjavni vezniki]] je urejen in obe manjkajoči pravilnostni tabeli sta dodani; novih razlag ali dodatnih tabel nisem dodajal. Izrisa v Obsidianu nisem mogel preveriti.

**Novi tabeli** (vrednosti sem izračunal sam, v enaki obliki s črto kot prejšnja):
- $(p \implies q) \lor (\neg q \implies p)$: v vseh štirih vrsticah je 1, torej je tavtologija. Obdržal sem tvojo postavitev `p q | izraz`, brez vmesnih stolpcev.
- $\neg p \lor q$ in $p \implies q$: stolpca sta enaka (1, 1, 0, 1), zato sta izraza enakovredna.

**Kaj sem olepšal:**
- **Zakoni izjavnega računa:** prilepljeno besedilo je imelo pokvarjene znake (`^`, `_`, `,`, `⇠`). Prepisal sem jih v $\land$, $\lor$, $\iff$, $\sim$ in razdelil v oštevilčen seznam.
- **Pravopis in oblika:** tipkarske napake, vejice, velike začetnice v naslovih, vse tabele veznikov v enaki obliki, branja implikacije in ekvivalence kot alineje.
- **Naslovi:** dodal sem tri podnaslove (»Resničnostna tabela«, »Tavtologija, protislovje, nevtralni izrazi«, »Enakovredni izrazi«), da spodnji del ni en sam blok.

**Vsebinski popravki, ki jih preveri:**
- »neresnične(1)« sem popravil v (0), »tavtografija« v tavtologija, »nevrtalni« v nevtralni, »protislovje je vedno negativen« v »vedno neresničen«.
- Pri izjavnih izrazih je pisalo »potem so tudi vsi iz njih izjavni izrazi«; izpisal sem jih: $A \land B$, $A \lor B$, $A \veebar B$, $A \implies B$, $A \iff B$.
- Pri globini je pisalo »je dolžina drevesa«; zapisal sem »višina drevesa«.

**Kar je ostalo nedokončano, ker v zapisku ni bilo podatka:**
- Pri ekskluzivni disjunkciji manjka, kako se bere (za »beremo« je prazno).
- Pri dvomestnih in tromestnih veznikih ni primerov.
[Timestamp: 2026/10/10 14:24:05]

**user**: tukaj dokončaj
[Timestamp: 2026/10/10 14:26:17]

**ai**: Stavek pri ekskluzivni disjunkciji v [[izjave in izjavni vezniki]] je dokončan: »… označimo z $A \veebar B$ in beremo »ali A ali B«.«

To je običajno branje za ekskluzivno disjunkcijo (resnična je, ko je resnična natanko ena od izjav); če ste na predavanju rekli drugače, ga zamenjaj.
[Timestamp: 2026/10/10 14:26:20]

**user**: še to napiši še pri ostalih
[Timestamp: 2026/10/10 14:26:59]

**ai**: V [[izjave in izjavni vezniki]] ima zdaj vsak veznik pred tabelo stavek o tem, kdaj je resničen, tako kot negacija:

- **Konjunkcija:** $A \land B$ je resnična natanko takrat, ko sta $A$ in $B$ obe resnični.
- **Disjunkcija:** $A \lor B$ je resnična natanko takrat, ko je resnična vsaj ena od izjav $A$ in $B$.
- **Ekskluzivna disjunkcija:** $A \veebar B$ je resnična natanko takrat, ko je resnična natanko ena od izjav $A$ in $B$.
- **Implikacija:** $A \implies B$ je neresnična natanko takrat, ko je $A$ resnična in $B$ neresnična.
- **Ekvivalenca:** $A \iff B$ je resnična natanko takrat, ko imata $A$ in $B$ isto logično vrednost.

Pri implikaciji sem stavek namenoma obrnil na »neresnična«, ker je tako krajše in se ujema s tvojim opisom zgoraj v seznamu veznikov.
[Timestamp: 2026/10/10 14:27:02]

**user**: dobro sedaj pri zakonih izjavnega računa  vsak zakon malo razloži,  profesor je delal neke primerjave ki so mi bile ušeč a si jih nisem zapomnil mapak je bilo nekaj takega:   komunitativnost:  konjukcija in disjunkcija sta kot množenje ker .... ali kaj takega.
[Timestamp: 2026/10/10 14:29:10]

**ai**: V razdelku »Zakoni izjavnega računa« v [[izjave in izjavni vezniki]] ima zdaj vsak zakon pod formulami kratko razlago s primerjavo z računanjem. Primerjave so moje, ne profesorjeve, ker njegovih ne poznam; če se katere spomniš drugače, jo popravim.

Osnovna ideja, zapisana na vrhu razdelka: $\land$ se obnaša kot množenje, $\lor$ kot seštevanje, $\neg$ pa kot predznak minus.

- **Dvojna negacija:** dva minusa se izničita, $-(-x) = x$.
- **Idempotenca:** ponovitev iste izjave ne pove nič novega; pri številih to velja le za 0 in 1 pri množenju ($1 \cdot 1 = 1$).
- **Komutativnost:** vrstni red ni pomemben, kot pri $a \cdot b = b \cdot a$ in $a + b = b + a$. Implikacija ni komutativna, podobno kot odštevanje.
- **Asociativnost:** vseeno je, kje so oklepaji, kot pri $(a \cdot b) \cdot c = a \cdot (b \cdot c)$. Implikacija ni asociativna, podobno kot odštevanje.
- **Absorpcija:** $B$ je odveč, o vsem odloča $A$. Pri navadnem računanju tega zakona ni, zato je razložen z vrednostma 0 in 1.
- **Distributivnost:** prvi zakon je odpravljanje oklepajev, $(a + b) \cdot c = a \cdot c + b \cdot c$. Drugi pri številih ne velja, v logiki pa velja v obe smeri.
- **De Morgan:** negacija gre k vsakemu členu in veznik se obrne, podobno kot $-(a + b) = -a - b$. Primer: »ni res, da dežuje ali sneži« pomeni »ne dežuje in ne sneži«.
[Timestamp: 2026/10/10 14:29:12]

**user**: to datoteko slovnično uredi
[Timestamp: 2026/10/15 14:40:34]

**ai**: [[nastanek računalništva 2]] je slovnično urejen: tipkarske napake, vejice, velike začetnice in pike na koncu alinej. Popravil sem tudi »von ojman« v »von Neumann«, »zaimslil« v »zamislil« in »naslovljviva« v »naslovljiva«.

Popravil sem še tabelo, kar presega slovnico. »word 0« je bil v glavi tabele, zato se je vse zamaknilo za eno vrstico (word 1 je imel naslov 0). Zdaj ima glava stolpce »Beseda«, »Naslov« in »Naslov (*ni treba, da se začne z 0*)«, vrstice pa se ujemajo: word 0 ima naslov 0 oziroma k+0. Prazne vrstice okoli »...« sem odstranil.

Zadnji stavek »Najmanjša količina informacije v sodobnih računalniških sistemih« je ostal nedokončan, ker v zapisku ni nadaljevanja.
[Timestamp: 2026/10/15 14:40:34]

**user**: dobro sme dodal še nekaj. tako da še enkrat
[Timestamp: 2026/10/15 14:52:18]

**ai**: Novi del v [[nastanek računalništva 2]] je urejen; zgornji del, ki sem ga popravil že prej, je ostal enak.

- **Naslova:** »Najmanjša količina informacije …« in »Pomnilniška beseda« sta zdaj podnaslova (`##`).
- **Formula:** prazno formulo `${}{}$` in `${}\sim{}$` sem zamenjal z »približno«, zapis bita pa z $b \in \{0, 1\}$.
- **Tabela bitov:** oznake so zdaj z indeksi ($b_{M-1}$ … $b_0$), poravnane na sredino. Odstranil sem tudi zaskrit znak `¸` pred »M-bitna beseda«.
- **LSB in MSB:** opisa sta alineji z angleškima izrazoma in kraticama.
- **Pravopis:** »najivšjo« → »največjo«, »vrendost« → »vrednost«, vejice, presledki pred oklepaji in pri enotah (0 V, 1,1 V).

Pri 0 V je v tvojem zapisku pisalo »(ni **0**)«; spremenil sem v »(je **0**)«, ker sem sklepal, da je to tipkarska napaka. Preveri, ali si res tako mislil.
[Timestamp: 2026/10/15 14:52:18]

**user**: še nekaj sem dodal
[Timestamp: 2026/10/15 15:29:51]

**ai**: Novi del v [[nastanek računalništva 2]] je urejen; vse nad stavkom o $M = 8$ je ostalo, kot je bilo.

- **Bajt:** »zato so ij dali ime BYTE« je zdaj »Zato so ji dali ime **bajt** (angl. *byte*).«
- **Nov podnaslov:** pomnilnik, informacija in operandi so pod naslovom »Pomnilnik in informacija«, kot alineje z odebeljenimi ključnimi pojmi. Vprašanje »kako so operandi in ukazi predstavljeni z biti« je podalineja pri informaciji.
- **Pravopis:** »oporandi« → »operandi«, »ukaiz« → »ukazi«, »nizt« → »nizi«, »predstavjeno« → »predstavljeno«, »nemoremo« → »ne moremo«.
- **Primer z biti:** `10010110` je zapisan kot koda, da se ločí od besedila. Sklep, da iz bitnega zapisa ne moremo prepoznati tipa informacije, je v calloutu `[!important]`, kot v prvem zapisku.
[Timestamp: 2026/10/15 15:29:51]

**user**: uporabi nekaj drugega kot tisti \inromation ali kar je ker tisto je preveč
[Timestamp: 2026/10/15 15:34:09]

**ai**: Namesto okvirja `[!important]` je ključni stavek zdaj samo odebeljen, s puščico spredaj:

→ **Iz bitnega zapisa ne moremo prepoznati tipa informacije.** Mi kot programerji se odločimo, kako bomo interpretirali vsebino neke pomnilniške besede.

Uredil sem tudi vrstice, ki si jih dodal na koncu:
- »besedeomejimo« sem razdelil v dve vrstici: konec stavka in »Omejimo se na:«.
- Naslov »CELA NEPREDZNAČENA ŠTEVILA« je zdaj z malimi črkami.
- »kaok« sem popravil v »kako« in obe vprašanji pod naslovom združil v en odstavek.

Zapomnil sem si, da so ti okvirji preveč, zato bom v zapiskih ključne stvari raje samo odebelil.
[Timestamp: 2026/10/15 15:34:09]

**user**: daj to v md
[Timestamp: 2026/10/15 15:36:51]

**ai**: Primer s številom 347 v [[nastanek računalništva 2]] je zdaj zapisan v Markdownu z LaTeXom:

- vsaka števka je alineja s svojo potenco: $3 \to 3 \cdot 10^2 = 300$, $4 \to 4 \cdot 10^1 = 40$, $7 \to 7 \cdot 10^0 = 7$
- pod alinejami je celotna vsota v bloku: $347 = 3 \cdot 10^2 + 4 \cdot 10^1 + 7 \cdot 10^0$

V tvojem zapisu je pri trojki pisalo $3 \cdot 10^0$. Popravil sem v $10^2$, ker je 3 na mestu stotic.

Zadnjemu stavku sem dodal »in njihovega mesta v zapisu«, ker vrednost ni odvisna samo od števk, ampak tudi od tega, kje stojijo. Če tega dodatka nočeš, ga izbriši.
[Timestamp: 2026/10/15 15:36:51]

**user**: napiši v md
[Timestamp: 2026/10/15 15:42:38]

**ai**: Formula v [[nastanek računalništva 2]] je zdaj zapisana v LaTeXu:

$$
\text{vrednost} = \sum_{i=0}^{n-1} x_i \cdot B^i
$$

Spodnji dve vrstici sta zdaj alineji: desetiški sistem z $B = 10$, $x_i \in \{0, 1, \dots, 9\}$ in računalnik z $B = 2$, $x_i \in \{0, 1\}$.

Pri računalniku je v tvojem zapisku pisalo enako kot pri desetiškem sistemu ($B = 10$, števke 0–9). Spremenil sem v $B = 2$, ker računalnik dela z biti; če si vrstico samo skopiral in jo nameraval dopolniti sam, preveri, ali se ujema s predavanjem.
[Timestamp: 2026/10/15 15:42:38]

**user**: samo to ščaraj
[Timestamp: 2026/10/15 15:57:49]

**ai**: V [[nastanek računalništva 2]] sem uredil samo razdelek o celih predznačenih številih:

- **Naslov:** »CELA PREDZNAČENA ŠTEVILA« je zdaj naslov, z malimi črkami, kot »Cela nepredznačena števila« nad njim.
- **Vprašanje:** »kako bitnemu zapisu dodati predznak« je uvodni stavek z vprašajem.
- **Primera:** `0011` → $+3$ in `1011` → $-3$ sta podalineji pod točko 1, bitni zapisi so kot koda.
- **Pravopis:** »poziciskega« sem popravil v »pozicijskega«.

»Seštejemo $+3$ in $-3$:« sem pustil nedokončano, ker v zapisku ni nadaljevanja.
[Timestamp: 2026/10/15 15:57:49]

**user**: sedja še seštej
[Timestamp: 2026/10/15 15:58:09]

**ai**: Seštevanje je dodano v [[nastanek računalništva 2]] pod točko 1:

```
  0011   (+3)
+ 1011   (-3)
------
  1110   (-6)
```

Bite sem seštel kot navadno nepredznačeno število ($3 + 11 = 14$ = `1110`). Rezultat `1110` se v zapisu s predznakom in velikostjo prebere kot $-6$, pravilno pa bi bilo $0$ (`0000`).

Iz tega sem dopisal sklep: **pri zapisu s predznakom in velikostjo navadno seštevanje bitov ne da pravilnega rezultata.** To je tudi običajen razlog, zakaj se na predavanjih nato preide na drug zapis predznačenih števil.
[Timestamp: 2026/10/15 15:58:09]

**user**: nariši premico
[Timestamp: 2026/10/15 16:21:07]

**ai**: V [[nastanek računalništva 2]] je pod točko 2 zdaj premica z vsemi 3-bitnimi zapisi:

```
 000   001   010   011   100   101   110   111
──┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──▶
  0     1     2     3     4     5     6     7
```

Narisal sem jo v bloku kode, ker se tako znaki poravnajo v stolpce; LaTeX in vtičniki za risanje bi bili za to preveč. Pod vsakim bitnim zapisom je njegova nepredznačena vrednost od 0 do 7, saj v zapisku ni pisalo, katere vrednosti naj bodo na premici.

Uvodno vrstico sem slovnično uredil: »Recimo, da je $n = 3$, da nam bo lažje. Zapišemo ta števila na premico:«. Če ste na predavanju nato desno polovico (`100`–`111`) prestavili na levo stran kot negativna števila, mi povej, pa dodam še drugo premico.
[Timestamp: 2026/10/15 16:21:07]

**user**: poglej šeenkrat
[Timestamp: 2026/10/15 16:22:26]

**ai**: Pod premico si zamenjal vrednosti z $-4$ do $3$, a so bile zamaknjene, tako da $0$ ni stal pod `100`. Poravnal sem jih, zdaj vsaka vrednost stoji pod svojim zapisom:

```
 000   001   010   011   100   101   110   111
──┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──▶
 -4    -3    -2    -1     0     1     2     3
```

Pri tem pripisu je vrednost vedno za 4 manjša od nepredznačene (`000` = $0 - 4 = -4$, `111` = $7 - 4 = 3$). Takemu zapisu se običajno reče zapis z odmikom (tukaj odmik 4). V zapisek tega nisem dopisal, ker ne vem, ali ste ga na predavanju poimenovali tako.
[Timestamp: 2026/10/15 16:22:26]

**user**: uredi sedaj to
[Timestamp: 2026/10/15 16:27:42]

**ai**: Del o zapisu z odmikom v [[nastanek računalništva 2]] je urejen:

- **Postavitev:** vse je zamaknjeno pod točko 2, da sodi skupaj s premico.
- **Pravopis:** »doloimo«, »poziciskega/pozisciske«, »primieri« in »primir« so popravljeni; »OFFSET« je zdaj **odmik** (angl. *offset*).
- **Primera:** $v(110) = 6 - 4 = 2$ in $v(011) = 3 - 4 = -1$ sta v LaTeXu.
- **Splošna formula:** namesto »E...« sem jo dopisal sam:

$$
v = \sum_{i=0}^{n-1} x_i \cdot 2^i - 2^{n-1}
$$

Prvi del je navadna pozicijska vrednost (kot zgoraj pri nepredznačenih številih), $2^{n-1}$ pa je sredina. Za $n = 3$ je to $2^2 = 4$, kar se ujema s tvojim primerom. Primerjaj jo s tablo, ker sem jo izpeljal sam.

Pravilo »0 = −, 1 = +« sem pustil, ker je pravilno: tukaj je obratno kot pri predznaku in velikosti.
[Timestamp: 2026/10/15 16:27:42]

**user**: uredi to
[Timestamp: 2026/10/15 16:32:54]

**ai**: Primer seštevanja v zapisu z odmikom je zdaj urejen enako kot prejšnji pri predznaku in velikosti:

```
  100   (0)
+ 001   (-3)
-----
  101   (1)
```

Pod njim piše: dobimo `101` → $5 - 4 = 1$, pravilno pa bi bilo $-3$ (`001`). Na koncu je odebeljen sklep, da tudi pri zapisu z odmikom navadno seštevanje bitov ne da pravilnega rezultata. Vse je zamaknjeno pod točko 2.

Uredil sem še vrstico pod tem, čeprav je nisi označil: »LEKSIFOGRAFSKO« je zdaj »**leksikografsko**«, »Ampak dobro« pa je odebeljeno.
[Timestamp: 2026/10/15 16:32:54]