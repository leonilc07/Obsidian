---
epoch: 1792329280306
mode: agent
backendId: claude
sessionId: "1cec5fc1-c0a3-46c4-a1e3-63c81aca4188"
agentLabel: "uredi kar še ni urejeno v tej datoteki do tukaj"
usage: '{"usedTokens":47272,"contextWindow":1000000,"inputTokens":2,"outputTokens":738,"cacheReadTokens":44501,"cacheWriteTokens":2031,"updatedAt":1792330164929}'
tags:
  - copilot-conversation
---

**user**: uredi kar še ni urejeno v tej datoteki do tukaj
[Timestamp: 2026/10/18 15:14:40]

**ai**: Uredil sem razdelek pred obema primeroma, torej vse do vrstice s `10011100`:

- **Dvojiški sistem** je zdaj alineja, tako kot desetiški nad njim.
- Popravil sem stavek: »števk« → »števil«, »POZICIISKI« → **pozicijski zapis**.
- **Primera** sta zapisana z izračunom: `1011` = 11 in `10011100` = 156.

Vsebina od »Cela predznačena števila« naprej (dvojiški komplement) je ostala neurejena. Če želiš, uredim še ta del.
[Timestamp: 2026/10/18 15:14:40]

**user**: ok sedaj pa poglej to poglavje cela predznačena števila in ga popravi
[Timestamp: 2026/10/18 15:20:58]

**ai**: 
[Timestamp: 2026/10/18 15:20:58]

**user**: in daj še to noter

<!-- copilot-image:86f9d083fd333c18d452fc5712614c172ebe1106a8f34a25bfdeac7e2c2b43c3 -->
![[copilot-image-86f9d083fd333c18d452fc5712614c172ebe1106a8f34a25bfdeac7e2c2b43c3.png]]
<!-- /copilot-image -->

<!-- copilot-image:f094aa9547f83aac513d2bd36f1688ffff3603c2971ffa142a84731ce2a51ac1 -->
![[copilot-image-f094aa9547f83aac513d2bd36f1688ffff3603c2971ffa142a84731ce2a51ac1.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/18 15:28:06]

**ai**: Prvi popravek je uspel, drugi ne (verjetno zaradi presledkov). Zamenjam ta del drugače:Uredil sem poglavje **Cela predznačena števila** in dodal snov z obeh slik:

- **Zapis z odmikom** ima zdaj naslov v enakem slogu kot »Predznak in velikost«. Stavek o leksikografski razvrstitvi sem preoblikoval v celo poved.
- **Enični komplement (nova točka 3, s prve slike):**
  - krožnica za $n = 3$ (`000` = $+0$ … `111` = $-0$);
  - negativno število dobiš z obratom vseh bitov;
  - oba zgleda seštevanja: $+3 + (-3) = -0$ pokaže težavo z **dvema ničlama**, $+2 + (-3) = -1$ pa je pravilno;
  - na koncu »rešitev«: negativna števila zamaknemo za eno mesto in dobimo dvojiški komplement.
- **Dvojiški komplement (zdaj točka 4):** krožnica z druge slike, izračun vrednosti (pozicijski zapis $- 2^n$ za negativna) in splošna formula. Tvoje grobe zapiske sem uredil v tri zglede seštevanja s prenosom in prelivom ter v sklepno ugotovitev. »Rumeno mejo« sem opisal kot mejo med `011` in `100`.

Krožnici sta narisani z besedilom, saj so slike le v začasni mapi in niso v vaultu. Če želiš originalne skice, jih shrani v vault in jih vstavim z ![[...]].

**Dve stvari sem dodal sam**, ker ju na slikah ni:
- **Splošna formula za dvojiški komplement:** $v = -x_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} x_i \cdot 2^i$ (v tvojih zapiskih je bilo le »vrednost = E...«).
- **Pravilo za enični komplement**, da negativno število dobiš z obratom vseh bitov. Na slikah tega ni, je pa standardna definicija.

Preveri, ali se ujemata s tem, kar je bilo na predavanju.
[Timestamp: 2026/10/18 15:28:06]