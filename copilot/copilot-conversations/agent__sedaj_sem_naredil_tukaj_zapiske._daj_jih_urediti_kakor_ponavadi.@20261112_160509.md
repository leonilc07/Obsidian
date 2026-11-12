---
epoch: 1794495909094
mode: agent
backendId: claude
sessionId: "ded8b5ab-ed7b-498a-a7b3-1a652f98e5de"
topic: "sedaj sem naredil tukaj zapiske. daj jih urediti kakor ponav…"
tags:
  - copilot-conversation
usage: '{"usedTokens":78007,"contextWindow":1000000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":77780,"cacheWriteTokens":222,"updatedAt":1794507049531}'
---

**user**: sedaj sem naredil tukaj zapiske. daj jih urediti kakor ponavadi. preimenuj datoteko, izbriši tisti hand writing in use vredu napiši in razloži
[Timestamp: 2026/11/12 16:05:09]

**ai**: Pretvarjam ročni zapis v sliko, da ga lahko preberem.Ročni zapis sem prebral (pomiki LSL, LSR, ASR, ROR in format ukaza za pomik). Zdaj pišem urejen zapisek.Ročni zapis sem prepisal v besedilo in dodal razlage. Zapisek se zdaj imenuje [[operacije pomika]] in je v mapi `računalniška arhitektura`. Ročni zapis `2026.11.12 - 14.41pm.svg` sem izbrisal. Ni bil v gitu, zato ga ni mogoče obnoviti. Izbrisal sem tudi »rere re« na koncu.

**Vsebina zapiska:**
- **Štirje pomiki (LSL, LSR, ASR, ROR):** pri vsakem je opisano, kaj se zgodi z biti, in tvoj zgled z desetiškimi vrednostmi (npr. $13 \to 6$, $-4 \to -2$). Napisal sem tudi, čemu pomik služi: LSL množi z $2^n$, LSR deli nepredznačena števila, ASR deli predznačena števila.
- **Ukaz za pomik:** razpored bitov je v enaki obliki kot v zapisku [[načini naslavljanja in CISC-RISC]]. Obe obliki spodnjih 12 bitov sta ločeni, razlikuje ju bit 4 (število mest v ukazu ali v registru $R_s$).
- **Vrsta pomika (sh):** kode `00`–`11` so kratek seznam, ne tabela.

**Kje sem odstopil od zapisa, preveri:**
- Pri LSR si napisal »biti, ki ostanejo, predstavljajo ostanek«. Ostanek dajo biti, ki **izpadejo**, zato sem to zapisal tako.
- Pod zgledom za LSR si napisal »množenje s $2^{-n}$«, kar je isto kot deljenje z $2^n$. Zapisal sem oboje.
- V drugi obliki ukaza je bil okvirček za bit 7 prazen. Vpisal sem $0$, ker je tako v ARM. Preveri, ali je enako na prosojnicah.
- Koda operacije `11010` je ista kot MOV v tabeli iz prejšnjega zapiska. To sem omenil samo s povezavo na ta zapisek.

V [[glavno RA]] zapiska nisem dodal na seznam predavanj. Če želiš, ga dodam.
[Timestamp: 2026/11/12 16:05:09]

**user**: dodaj na seznam predavanj
[Timestamp: 2026/11/12 16:19:13]

**ai**: Zapisek sem v [[glavno RA]] dodal na seznam predavanj kot »predavanje 6: [[operacije pomika]]«.

**Številko predavanja sem uganil.** Vzel sem naslednjo po vrsti, ker iz zapiskov ne vidim, katero predavanje je bilo 12.11. Na seznamu tudi manjkata [[ukazi]] in [[načini naslavljanja in CISC-RISC]]. Če je bilo vsako od njiju svoje predavanje, je tole verjetno predavanje 7.

Povezava `[[ksdf]]` pri predavanju 5 ne kaže na noben zapisek. Mogoče si mislil [[ukazi]]? Če mi poveš, kako si sledijo predavanja, popravim številke in dodam manjkajoča.
[Timestamp: 2026/11/12 16:19:13]

**user**: dobro sedaj sem jih še nekaj dodal. tako da uredi jih do konca
[Timestamp: 2026/11/12 19:08:09]

**ai**: Na koncu sta dva nova ročna zapisa in vrstica o load/store. Ju pretvarjam v sliko.Slike so pripravljene, zdaj berem ročna zapisa.Zdaj zapisek preimenujem, ker zajema tudi load/store, popravim povezavo in počistim ročna zapisa.I wrote up the rest of the note. It's now called [[operacije pomika in load-store]], since it also covers load/store, and I updated the link in [[glavno RA]].

Same as last time, I deleted both handwriting files (`16.20pm.svg` and `16.39pm.svg`) and removed them from the note. They weren't in git, so they can't be restored.

**What I added:**
- **Example of shift instructions:** the memory layout from address `0x0C` is a short block. Both instructions are decoded field by field:
  - `E1A07971`: $R_7 \leftarrow R_1$ rotated right by as many places as $R_9$ holds (ROR, the count is in a register)
  - `E1A088CD`: $R_8 \leftarrow R_{13}$ arithmetically shifted right by $17$ places (ASR, the count is in the instruction)
- **Load/store instructions:** your sentence about moving data is now an intro with two bullets. Then come the three operands and an explanation of base addressing with offset ($\text{naslov} = \text{bazni register} + \text{odmik}$). Last is the instruction format with fields L, B, Rn, Rt and Imm12.

**Things to check:**
- **Assembler form:** I added the instruction names `ROR R7, R1, R9` and `ASR R8, R13, #17` to the example myself. You only had the fields decoded. Check that the lectures write them the same way.
- **Three operands:** you only had two numbered points. The address in point 2 is made of two operands (register + offset), so I explained that this adds up to three.
- **Bits 24 and 23:** in the load/store format I copied them as `1 1`, the same as in your handwriting.
[Timestamp: 2026/11/12 19:08:09]