---
epoch: 1792138884390
mode: agent
backendId: claude
sessionId: "e7ae8ea3-6dbc-4b3d-b804-3d0c35ac32fb"
agentLabel: "daj še ostale sem noter"
usage: '{"usedTokens":66072,"contextWindow":1000000,"inputTokens":2,"outputTokens":328,"cacheReadTokens":65403,"cacheWriteTokens":339,"updatedAt":1792152979525}'
tags:
  - copilot-conversation
---

**user**: daj še ostale sem noter

<!-- copilot-image:48a420f0be13782b79ce444d3d57c58bdd85adf0d57e11851f0f368e9f90ad0d -->
![[copilot-image-48a420f0be13782b79ce444d3d57c58bdd85adf0d57e11851f0f368e9f90ad0d.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/16 10:21:24]

**ai**: V [[izjave in izjavni vezniki]] sem pod razdelek »Zakoni izjavnega računa«, takoj za De Morganovima zakonoma, dodal zakone 8–12:

- **8. Kontrapozicija**
- **9. Lastnosti 0 in 1**
- **10. Še lastnosti 0 in 1**
- **11. Lastnosti implikacije**
- **12. Lastnosti ekvivalence**

Formule sem prepisal s slike. Vsak zakon ima tako kot zakoni 1–7 kratko razlago in primerjavo z računanjem, kjer se ujema. Pri 12. zakonu sem v razlago dodal še, da je $\neg(A \iff B)$ enako $A \veebar B$. Tega na sliki ni.
[Timestamp: 2026/10/16 10:21:24]

**user**: napiši to rešitev v tabeli, 1 vrstica = 1 enka
[Timestamp: 2026/10/16 14:04:50]

**ai**: V [[2 predavanje]] sem pod tvoj stavek o rešitvi 1 dodal tabelo. Vsaka vrstica je ena enka iz pravilnostne tabele, skupaj jih je 5:

- spremenljivka z vrednostjo 1 je v konjunkciji zapisana kot $p$
- spremenljivka z vrednostjo 0 je zapisana kot $\neg p$

Pod tabelo je še celoten $A_{DNO}$, kjer so vse konjunkcije združene z disjunkcijo.
[Timestamp: 2026/10/16 14:04:50]

**user**: dobro in še slovnino popravi
[Timestamp: 2026/10/16 14:05:21]

**ai**: Popravil sem slovnico v [[2 predavanje]]:

- **Tipkarske napake:** enakovredns → enakovredna, pravilnistna → pravilnostna, primir → Primer, konjukcija → konjunkcija.
- **Vejice:** dodal sem jih pred »da« in »kjer«.
- **Predlogi:** »z konjunkcijami« → »s konjunkcijami«, »tabelo« → »s pravilnostno tabelo«.
- **Velike začetnice:** v naslovu in na začetku stavkov.
- **Dopolnitve:** v vprašanje sem dodal manjkajočo besedo »izraza«. »Adno« je zdaj zapisan kot $A_{DNO}$, »DNO« pa z malimi črkami in še vedno krepko.

Spremenil sem tudi vsebino enega stavka. Prej je pisalo »kjer je rešitev 1«, zdaj »kjer je vrednost 1«.

**Naslov »Reševanje ukazov« sem pustil**, ker nisem prepričan, kaj je bilo mišljeno. Če je to »Reševanje nalog«, mi povej in ga popravim.
[Timestamp: 2026/10/16 14:05:21]

**user**: naredi še za rešitev dva kjer uzameš 0 in narediš konjuktivno normalno obliko
[Timestamp: 2026/10/16 14:06:38]

**ai**: V [[2 predavanje]] sem pod DNO dodal še rešitev 2, konjunktivno normalno obliko (KNO). Tabela ima 3 vrstice, ena za vsako ničlo (000, 010, 110):

- spremenljivka z vrednostjo 0 je v disjunkciji zapisana kot $p$
- spremenljivka z vrednostjo 1 je negirana ($\neg p$)

Tako je disjunkcija v svoji vrstici enaka 0. Na koncu so vse disjunkcije združene s konjunkcijo:

$A_{KNO} = (p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor r)$
[Timestamp: 2026/10/16 14:06:38]

**user**: dobro in sedaj odspodaj okrajšaj kno da dobiš 

ta retultat.  in povej da če okrajšaš dno dobiš isto. nato ta rezultat okrajšaj v p implements q implements r
[Timestamp: 2026/10/16 14:09:28]

**ai**: V [[2 predavanje]] sem pod KNO dodal poenostavitev v dveh delih.

1. **Okrajšava KNO:** prvi dve disjunkciji se razlikujeta samo v $q$ in $\neg q$, zato se združita v $p \lor r$. Z distributivnostjo nato dobimo $p \land \neg q \lor r$. Ob vsakem koraku je napisan zakon, ki se uporabi. Tvoj zapis $\neg g$ sem popravil v $\neg q$.
2. **Pretvorba v implikacije:** $p \land \neg q \lor r \sim \neg(p \implies q) \lor r \sim (p \implies q) \implies r \sim p \implies q \implies r$. Oklepaje na koncu lahko izpustimo, ker se implikacije berejo od leve proti desni.

Med obe izpeljavi sem dodal še stavek, da poenostavitev DNO da isti rezultat. Te poenostavitve DNO nisem izpeljal po korakih, ampak sem rezultat preveril na pravilnostni tabeli: $p \land \neg q \lor r$ je 0 natanko v vrsticah 000, 010 in 110, tako kot $A$.
[Timestamp: 2026/10/16 14:09:28]

**user**: to reši
[Timestamp: 2026/10/16 14:13:13]

**ai**: V [[2 predavanje]] sem dopisal dokaz, da je $\{\neg, \lor\}$ poln nabor:

$$A \land B \sim \neg\neg(A \land B) \sim \neg(\neg A \lor \neg B)$$

Prvi korak uporabi dvojno negacijo, drugi De Morganov zakon. Vsak $\land$ lahko torej zapišemo samo z $\neg$ in $\lor$. Ker je $\{\neg, \lor, \land\}$ poln nabor (vsak izraz lahko zapišemo v DNO), je poln tudi $\{\neg, \lor\}$.

Pri tem sem popravil še ta del zapiska:

- **Dokončan stavek:** stavek, ki se je končal s »kar pomeni,...«, zdaj pravi, da lahko vsak izraz zapišemo samo z vezniki iz nabora.
- **Tipkarske napake:** povni → poln, nabo → nabor, spremenjimo → izrazimo.
- **Naslov:** »nabori znakov« sem preimenoval v »Nabori veznikov«. Če ga želiš imeti po starem, ga lahko vrnem.
[Timestamp: 2026/10/16 14:13:13]

**user**: naredi za nabor 0, implikacija in za dokazat izberi 1, implikacija
[Timestamp: 2026/10/16 14:14:55]

**ai**: 
[Timestamp: 2026/10/16 14:14:55]

**user**: ne samo dokaži drugače da je 0, implikacija polni nabor in povej zakaj ni 1, implikacija polni nabor
[Timestamp: 2026/10/16 14:15:59]

**ai**: V [[2 predavanje]] sem pod dokaz za $\{\neg, \lor\}$ dodal dva nova razdelka.

**$\{0, \implies\}$ je poln nabor.** Za izhodišče vzamemo poln nabor $\{\neg, \lor\}$ in oba veznika zapišemo samo z $0$ in $\implies$:
- $\neg A \sim A \implies 0$
- $A \lor B \sim \neg A \implies B \sim (A \implies 0) \implies B$

**$\{1, \implies\}$ ni poln nabor, ker ohranja enico.** Vsak izraz, sestavljen samo iz $1$, $\implies$ in spremenljivk, je 1, ko so vse spremenljivke enake 1, saj velja $1 \implies 1 = 1$. Zato s tem naborom ne moremo zapisati na primer $\neg p$, ki je pri $p = 1$ enak 0.
[Timestamp: 2026/10/16 14:15:59]