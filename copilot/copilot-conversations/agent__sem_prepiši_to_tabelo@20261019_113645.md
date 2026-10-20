---
epoch: 1792402605133
mode: agent
backendId: claude
sessionId: "b79c4aa0-ba58-41d7-b90d-a159161c6ecf"
agentLabel: "sem prepiši to tabelo"
usage: '{"usedTokens":54927,"contextWindow":1000000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":51735,"cacheWriteTokens":3187,"updatedAt":1792420811482}'
tags:
  - copilot-conversation
---

**user**: sem prepiši to tabelo

<!-- copilot-image:328b40601f538e586638d05670218830330c1d2f528e6be72be9691c1d366076 -->
![[copilot-image-328b40601f538e586638d05670218830330c1d2f528e6be72be9691c1d366076.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/19 11:36:45]

**ai**: Tabela s slike je zdaj v [[Strojni ukazi]] pod naslovom „5. strojni ukazi“. Ima vseh 16 ukazov (od 0000 do 1111) s stolpci Binary Op Code, Operation in Meaning. Tri pogoje pri COMPARE X sem v isti celici ločil z `<br>`, da so vsak v svoji vrstici kot na sliki.
[Timestamp: 2026/10/19 11:36:45]

**user**: ta dokument sedja slogovno uredi
[Timestamp: 2026/10/19 11:46:24]

**ai**: Slogovno sem uredil [[Strojni ukazi]]:

- **Pravopis:** popravil sem tipkarske napake, npr. „krmilno enotot“ → „krmilno enoto“, „namesnske“ → „namenske“, „proggramađ“ → „programa“, „tipiččno“ → „tipično“.
- **Krajšave:** „pom loc“, „pom lok“ in „reg“ sem povsod izpisal kot „pomnilniška lokacija“ in „register“.
- **Naslovi** se zdaj začnejo z veliko začetnico. Ključne pojme (ALE, vezja, registri, podatkovna pot, pogojne kode) sem poudaril s krepkim tiskom.
- **Ukazi** (`LOAD X`, `ADD X, Y` …) so zapisani kot koda, njihov opis pa je ločen s pomišljajem. Zamaknjene vrstice pri vejitvah so zdaj običajne alineje.
- **Tabela:** glavo sem prevedel v slovenščino (Binarna koda, Operacija, Pomen), opisi v stolpcu Pomen pa so ostali v angleščini kot na sliki.

Vsebinsko sem spremenil dve stvari:

- **`JUMPGE X`:** prej je pisalo „GT **in** EQ“, zdaj „GT **ali** EQ“. GE pomeni „večje ali enako“, GT in EQ pa ne moreta biti hkrati 1. Preveri, ali se to ujema z zapiski s predavanj.
- **„pop“:** na koncu datoteke je bila osamljena beseda „pop“, ki sem jo odstranil, ker je bila videti kot pomotoma natipkana. Če je bil to začetek novega razdelka, mi povej.
[Timestamp: 2026/10/19 11:46:24]

**user**: okrajšaj ta izraz kar tukaj v chat in ga izbriši iz te datoteke.
[Timestamp: 2026/10/19 15:06:11]

**ai**: Izraz se poenostavi v $p \lor \neg q$ oziroma $q \implies p$. Iz datoteke sem ga izbrisal.

**Postopek:**

1. Prva dva člena imata skupen $\neg q$:
$(\neg p \land \neg q) \lor (p \land \neg q) \sim (\neg p \lor p) \land \neg q \sim 1 \land \neg q \sim \neg q$
2. Ostane:
$\neg q \lor (p \land q)$
3. Uporabimo distributivnost:
$(\neg q \lor p) \land (\neg q \lor q) \sim (\neg q \lor p) \land 1$
4. Rezultat:
$$\neg q \lor p \sim p \lor \neg q \sim q \implies p$$

**Preverba:** izraz je neresničen samo, ko je $p = 0$ in $q = 1$. Ta kombinacija edina manjka med tremi členi.
[Timestamp: 2026/10/19 15:06:11]

**user**: ne te naloge mapak tisti na katero se naloga skliciju ki smo jo delali v šoli imam samo rešeno in ne napisanega besedila. Baza je n1 kar je smo A1 in je lih člen in je resnična. nato smo n2 A1 in a2 na za kar velja isto.  nato smo da indukcisko predsotavili da za vse člene manjše od n to velja in smo naredili A1 .. A1 A1+1 .. An razdelili na B in C. mato smo uzeli najprej da je vseh členov liho mnogo in noter da je B liho in C sodo ali obratno kar je A res. nato pa še da je sodo mnogo vseh in potem oba liha ali oba soda kar pa A potem ni res. tako da pride ravno prav na koncu.

<!-- copilot-image:14a95bab7c3dc6d4583d1d89b0a676bf2079327e1954f42e20c55d0b7ce5c805 -->
![[copilot-image-14a95bab7c3dc6d4583d1d89b0a676bf2079327e1954f42e20c55d0b7ce5c805.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/19 16:11:17]

**ai**: Na konec [[2 predavanje]] sem dodal razdelek **Ekskluzivna disjunkcija več členov**, v katerem je zapisana trditev, na katero se sklicuje naloga, in tvoj dokaz.

**Trditev:** $A_1 \veebar A_2 \veebar \dots \veebar A_n$ je pri poljubni postavitvi oklepajev resničen natanko tedaj, ko je liho mnogo členov resničnih. Iz tega sledi, da je $\veebar$ asociativen.

**Dokaz** je zapisan tako, kot ste ga delali v šoli:
- **Baza:** $n = 1$ in $n = 2$.
- **Indukcijska predpostavka:** trditev velja za vse izraze z manj kot $n$ členi.
- **Korak:** izraz razdelimo na $B \veebar C$.
  - Liho mnogo resničnih se razdeli na liho + sodo, zato je $A$ resničen.
  - Sodo mnogo se razdeli na liho + liho ali sodo + sodo, zato je $A$ neresničen.

Dodal sem eno pojasnilo: $B$ in $C$ dobimo tako, da izraz razdelimo pri zadnjem (zunanjem) vezniku $\veebar$. Zato dokaz velja pri katerikoli postavitvi oklepajev.
[Timestamp: 2026/10/19 16:11:17]

**user**: reši še to pod to

<!-- copilot-image:d77c90db9193e23296d0eb92c42f4421f001de505e39d544f4742362381ba685 -->
![[copilot-image-d77c90db9193e23296d0eb92c42f4421f001de505e39d544f4742362381ba685.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/19 16:39:53]

**ai**: Odgovor, ki si ga izbral, je pravilen: izraz $A_1 \iff A_2 \iff \dots \iff A_n$ je resničen natanko tedaj, ko je **sodo mnogo členov lažnih**.

Rešitev sem dodal v [[2 predavanje]] kot nov razdelek **Ekvivalenca več členov**, takoj pod dokazom za ekskluzivno disjunkcijo. Dokaz gre po istem postopku kot tisti za $\veebar$:

- **Baza:**
  - Pri $n = 1$ je izraz resničen, ko je lažnih 0 členov.
  - Pri $n = 2$ je resničen, ko sta lažna 0 ali 2 člena.
- **Korak:** izraz razdelimo na $B \iff C$.
  - Sodo mnogo lažnih se razdeli na sodo + sodo ali liho + liho. $B$ in $C$ imata zato enako vrednost in $A$ je resničen.
  - Liho mnogo lažnih se razdeli na sodo + liho. $B$ in $C$ imata različni vrednosti in $A$ je lažen.

Dodal sem še kratko opombo z bližnjico, ki deluje brez nove indukcije: $A \iff B \sim \neg A \veebar B$. Ko negiramo člene, postanejo lažni členi resnični, zato lahko uporabimo trditev za $\veebar$.
[Timestamp: 2026/10/19 16:39:53]