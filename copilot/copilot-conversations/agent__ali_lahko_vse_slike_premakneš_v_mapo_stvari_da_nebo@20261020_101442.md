---
epoch: 1792484082162
mode: agent
backendId: claude
sessionId: "67aab41d-d976-4058-ae1f-851528bf45f3"
agentLabel: "ali lahko vse slike premakneš v mapo stvari da nebo vse v en…"
usage: '{"usedTokens":179843,"contextWindow":1000000,"inputTokens":2,"outputTokens":8,"cacheReadTokens":178913,"cacheWriteTokens":920,"updatedAt":1792489927563}'
tags:
  - copilot-conversation
---

**user**: ali lahko vse slike premakneš v mapo stvari da nebo vse v eni mapi. mapa stvari že obsatja
[Timestamp: 2026/10/20 10:14:42]

**ai**: 
[Timestamp: 2026/10/20 10:14:42]

**user**: sedaj si na wifi-ju prej nisi bil. nadaljuj
[Timestamp: 2026/10/20 10:17:28]

**ai**: Wikilinks delujejo po imenu, edino markdown povezavo v UML noti moram popraviti.Vse slike so zdaj v mapi `stvari`. Premaknil sem 9 slik:

- **7 slik iz Copilot pogovorov** (`copilot/copilot-conversations/attachments/`). Prazno mapo `attachments` sem izbrisal.
- **`sinx_vecje_pol.svg`** iz mape `matematika`.
- **`diagram-primerov-uporabe.svg`** iz mape `uvod v računalništvo`.

Povezave delujejo naprej:

- Povezave oblike `![[ime.png]]` Obsidian najde po imenu datoteke, zato jih ni bilo treba spreminjati.
- Edino povezavo s potjo, v [[02 UML - pregled]], sem popravil na `../stvari/diagram-primerov-uporabe.svg`. Te nove poti v Obsidianu nisem preveril, zato preglej, ali se diagram v tej noti prikaže.

Nove priponke Obsidian že shranjuje v `stvari`. **Copilot pa bo slike iz novih pogovorov verjetno spet shranjeval v svojo mapo `attachments`.** To lahko spremeniš v nastavitvah Copilota, če ima nastavitev za mapo slik.
[Timestamp: 2026/10/20 10:17:28]

**user**: ne slike iz najinega pogovora daj nazaj kamor so bile.
[Timestamp: 2026/10/20 10:19:16]

**ai**: Vrnil sem vseh 7 slik iz Copilot pogovorov nazaj v `copilot/copilot-conversations/attachments/`.

Sliki `sinx_vecje_pol.svg` in `diagram-primerov-uporabe.svg` sem pustil v mapi `stvari`. Če želiš, da gresta tudi onidve nazaj na prejšnje mesto, mi povej.
[Timestamp: 2026/10/20 10:19:16]

**user**: v tej datoteki naredi en mijhen uvod. nič nalsovov samo na kratko, tisto x in y os samo da je realna števila in imaginarna, kaj os imaginarna kaj je dvodimenzionalno število kako je sestavljeno kompleksno število  nekaj reči in kako jih jaz pišem: Z - kompleksno Z = a + bi, Re(z)= a, Im(z)=b, a + ib + c + id = (a+c)+i(b+d) potem kaj je -1 * 1 na navadnem X Y seznamu in da je 180 stopinj potem da je i ubistvu 90 in ne 180 in je i*i -1 in potem i=koren-1 .  lahko uporabiš utičnike ki jih imam nameščene, po smisl kakor se ti zdi
[Timestamp: 2026/10/20 10:26:43]

**ai**: Pišem uvod v [[kompleksna števila]]. Graf naredim z Desmos vtičnikom, ki ga imaš nameščenega.V [[kompleksna števila]] sem napisal kratek uvod brez naslovov. Datoteka je bila prej prazna. Uvod pokriva:

- **Realno os in imaginarno os**: $x$ os je realna, $y$ os je imaginarna, zato je kompleksno število dvodimenzionalno, točka v ravnini.
- **Zapis**, kot ga pišeš ti: $z = a + bi$, $\text{Re}(z) = a$, $\text{Im}(z) = b$.
- **Seštevanje**: $(a + ib) + (c + id) = (a + c) + i(b + d)$.
- **Zasuke**: $1 \cdot (-1) = -1$ je zasuk za $180^\circ$, $i$ je zasuk samo za $90^\circ$. Dva zasuka z $i$ dasta $180^\circ$, zato je $i \cdot i = -1$ in $i = \sqrt{-1}$.

Za konec sem dodal **Desmos graf**. Na njem so točke $1$, $i$, $-1$, $-i$ in črtkana enotska krožnica, osi pa sta označeni z Re in Im, tako da se zasuk po $90^\circ$ vidi na sliki. Ime osi in oznake točk sem preveril v kodi vtičnika, v Obsidianu pa grafa nisem odprl. Če se ne prikaže pravilno, mi povej.
[Timestamp: 2026/10/20 10:26:43]

**user**: sedaj pokaži ča če zmnožiš dve kompleksni števili se imginarni del pokrajša
[Timestamp: 2026/10/20 10:32:49]

**ai**: V [[kompleksna števila]] sem pod graf dodal množenje dveh kompleksnih števil:

- **Splošno**: $(a + bi)(c + di) = (ac - bd) + i(ad + bc)$. Ker je $i^2 = -1$, člen $bd\,i^2$ ni več imaginaren in se premakne v realni del kot $-bd$.
- **Primer**: $(2 + 3i)(1 + 4i) = -10 + 11i$.
- **S konjugiranim številom** $\bar{z} = a - bi$ se imaginarna dela odštejeta, $-abi + abi = 0$, in ostane samo realno število $a^2 + b^2$. Primer: $(3 + 2i)(3 - 2i) = 13$.

Ne vem čisto, kaj si mislil s "pokrajša", zato sem dal oboje. Pri navadnem množenju se imaginarni del ne izgubi v celoti, ampak se samo del $bd\,i^2$ premakne v realni del. Do konca se imaginarni del pokrajša šele pri množenju s konjugiranim številom. Če si mislil samo enega od teh dveh primerov, drugega lahko odstranim.
[Timestamp: 2026/10/20 10:32:49]

**user**: dobro sedaj dajej že naslove MNOŽENJE in nato bo DELJENJE a ne točno tisto množenje sem mislil za konjugetivno da se pokrajša, sedaj si ta označen del napisal "zanimivo" napiši drugače kakor ti misliš ker sedaj ne zastopim
[Timestamp: 2026/10/20 10:37:20]

**ai**: V [[kompleksna števila]] sem dodal naslova **Množenje** in **Deljenje**. Uvod nad njima je ostal brez naslova.

**Množenje** je zdaj razloženo bolj preprosto, brez besede "pokrajša":
- Množiš kot pri navadnih oklepajih, vsak člen z vsakim.
- Kjer dobiš $i^2$, napišeš $-1$.
- Na koncu zložiš skupaj realne člene in skupaj člene z $i$.
- Primer ostane isti: $(2 + 3i)(1 + 4i) = -10 + 11i$.

"Pokrajša" je zdaj samo pri **konjugiranem številu**, kjer res drži. Najprej piše, da je $\bar{z}$ isto število z obrnjenim predznakom pred $i$. Potem se pri $z \cdot \bar{z}$ člena $-abi + abi$ pokrajšata in ostane $a^2 + b^2$.

Pod **Deljenje** sem napisal tudi vsebino, ne samo naslova: ulomek razširiš s konjugiranim imenovalcem, $i$ v imenovalcu se pokrajša in ostane realno število. Primer: $\frac{5 + 5i}{1 + 2i} = 3 - i$. Če si hotel deljenje napisati sam, ga lahko odstranim.
[Timestamp: 2026/10/20 10:37:20]

**user**: aja daj v uvod še znak za mnžico kompleksnih števil
[Timestamp: 2026/10/20 10:39:54]

**ai**: V uvod [[kompleksna števila]] sem dodal znak za množico kompleksnih števil, $\mathbb{C}$. Stoji takoj za prvim odstavkom.

- Zraven je verižica množic $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, da se vidi, da $\mathbb{C}$ vsebuje vsa realna števila.
- Zapis $z = a + bi$ sem dopolnil z $\in \mathbb{C}$ in $a, b \in \mathbb{R}$, ker sta $a$ in $b$ realni števili.
[Timestamp: 2026/10/20 10:39:54]

**user**: ok sedaj od tukaj naprej so zapiski zanimivi in nebom vedel točno kaj smo hoteli povedati.  začeli smo z semizdi da definicijo kompleksnih števil{a+ ib| a,b so realna} in nato pokazali da je obsolutna od Z ubistvu pitagora in to pokazali na grafu(svoj nalsov)
[Timestamp: 2026/10/20 10:43:32]

**ai**: Oznaka `|z|` bi zmotila Desmos, ker ta vtičnik loči nastavitve z `|`. Popravljam jo:Na konec [[kompleksna števila]] sem dodal nov razdelek **Absolutna vrednost**, za Deljenjem. V njem je:

- **Definicija z množico**: $\mathbb{C} = \{\, a + bi \mid a, b \in \mathbb{R} \,\}$.
- **Pitagora**: $|z|$ je razdalja točke $z$ od izhodišča. $a$ in $b$ sta kateti pravokotnega trikotnika, $|z|$ je hipotenuza, zato $|z| = \sqrt{a^2 + b^2}$.
- **Primer**: $z = 3 + 4i$, $|z| = 5$.
- **Desmos graf** s tem trikotnikom: točka $z$, kateti $a = 3$ in $b = 4$ ter hipotenuza.
- **Povezava z množenjem**: $z \cdot \bar{z} = a^2 + b^2 = |z|^2$. To smo že dobili pri konjugiranem številu.

Na grafu hipotenuza nima oznake "|z| = 5", ampak "razdalja = 5". Desmos vtičnik znak `|` bere kot ločilo med nastavitvami, zato bi se oznaka pokvarila. Graf je napisan po pravilih vtičnika, ki sem jih pogledal v njegovi kodi, v Obsidianu pa ga nisem odprl, zato preveri, ali se trikotnik prikaže pravilno.
[Timestamp: 2026/10/20 10:43:32]

**user**: nah to daj v uvod
[Timestamp: 2026/10/20 10:45:50]

**ai**: Definicijo $\mathbb{C} = \{\, a + bi \mid a, b \in \mathbb{R} \,\}$ sem prestavil v uvod [[kompleksna števila]]. Zdaj je takoj pod vrstico z znakom $\mathbb{C}$ in verižico množic, iz razdelka Absolutna vrednost pa sem jo odstranil.
[Timestamp: 2026/10/20 10:45:50]

**user**: in zakaj je samo obsolutna vrednost od Z hipotenuza? kaj pa samo z ali pa samo negativni z? saj z saom posebi je hipotenuza, ne vidim zakaj bi rabil dati aboslutno okoli? ali je to zato da če je -z se pretvori v in zaradi nič drugega?
[Timestamp: 2026/10/20 10:48:58]

**ai**: Ne, ni samo zaradi minusa. Bistvo je, da **$z$ ni dolžina, ampak točka** (ali puščica od izhodišča do te točke). $|z|$ pa je **dolžina te puščice**, torej navadno realno število.

**Primer z $z = 3 + 4i$:**
- $z = 3 + 4i$ je točka v ravnini, 3 desno in 4 gor. Pove, *kje* je in v *kateri smeri*.
- $|z| = 5$ je samo dolžina hipotenuze, brez smeri.
- $z \neq 5$. Število $5$ je čisto druga točka, leži na realni osi. Zato ne moreš reči, da je $z$ hipotenuza. $z$ je oglišče trikotnika (oziroma cela puščica), dolžina hipotenuze pa je $|z|$.

**Kaj pa $-z$?**
- $-z = -3 - 4i$ je druga točka, na nasprotni strani izhodišča, zasukana za $180^\circ$.
- Dolžina je ista: $|-z| = \sqrt{(-3)^2 + (-4)^2} = 5$.
- Tudi $4 + 3i$, $5i$, $-5$ in še neskončno drugih točk ima $|z| = 5$. Vse ležijo na krožnici s polmerom 5. Absolutna vrednost "pozabi" smer in obdrži samo razdaljo.

**Povezava z realnimi števili:** tudi tam $|x|$ ni le "odstrani minus". Pomeni **razdaljo od 0** na premici: $|-3| = 3$, ker je $-3$ tri enote od nič. Pri realnih številih sta možni samo dve smeri (levo in desno), zato je videti, kot da se samo zbriše minus. V ravnini je smeri neskončno, zato je $|z|$ pravo merjenje dolžine s Pitagoro.

**Še en razlog:** kompleksnih števil ne moreš primerjati. Ne obstaja pravilo, ali je $3 + 4i$ "večje" od $5i$. Njune absolutne vrednosti pa lahko primerjaš, ker so to realna števila.

Če želiš, to razlago na kratko dodam v razdelek Absolutna vrednost v [[kompleksna števila]].
[Timestamp: 2026/10/20 10:48:58]

**user**: dodaj sem razlago kaj je ubistvu aboslutna vrednost, ker ot da ne asom obrne - sem iuvedel uzadnje komaj pri profesorju in nikoli prej. tako da mi manjka ta osnova niti kaj je to
[Timestamp: 2026/10/20 10:53:34]

**ai**: V [[enacbe procenti abslutna]] sem pod naslov *Absolutna vrednost* dodal osnovno razlago, preden pride tvoja definicija s primeri. Napisal sem tri stvari:

- **Kaj je absolutna vrednost:** $|x|$ je razdalja števila $x$ od $0$ na številski premici. Razdalja nikoli ni negativna, zato je $|3| = |-3| = 3$. Obe števili sta 3 korake od nič, samo na nasprotnih straneh.
- **Od kod pride pravilo z minusom:** pri negativnem $x$ moraš obrniti predznak, da dobiš pozitivno razdaljo. Zato je v definiciji $-x$, ki je pri negativnem $x$ pozitivno število. Primer: $-(-3) = 3$. To je torej posledica razdalje, ne neko pravilo samo zase.
- **Povezava s tvojim primerom:** $|a - b|$ je razdalja med $a$ in $b$. Zato je $|x + 1|$ razdalja $x$ od $-1$. Primera se ločita pri $x = -1$, ker tam $x + 1$ zamenja predznak.

To je ista ideja kot pri kompleksnih številih: tam je $|z|$ razdalja od izhodišča v ravnini, tukaj pa razdalja od $0$ na premici.
[Timestamp: 2026/10/20 10:53:34]

**user**: dobro sedaj tukaj daj samo da Z | |Z| naredi krog
[Timestamp: 2026/10/20 10:55:57]

**ai**: Na konec razdelka *Absolutna vrednost* v [[kompleksna števila]] sem dodal, da vsa števila z isto absolutno vrednostjo tvorijo krog:

$$\{\, z \in \mathbb{C} \mid |z| = r \,\}$$

To je **krožnica** s središčem v $0$ in polmerom $r$.

Pod tem je Desmos graf krožnice za $r = 5$. Na njej so označene točke $3 + 4i$, $-3 - 4i$, $4 + 3i$, $5i$ in $-5$. Tako se vidi, da imajo vse $|z| = 5$, čeprav so različna števila. Graf je napisan enako kot prejšnja dva, v Obsidianu ga nisem odprl.
[Timestamp: 2026/10/20 10:55:57]

**user**: dobro sedaj lastnosti kompleksnih števil. 1 je dvojni negaitven Z je Z
[Timestamp: 2026/10/20 10:57:13]

**ai**: Na konec [[kompleksna števila]] sem dodal nov razdelek **Lastnosti kompleksnih števil** s prvo lastnostjo:

$$\overline{\overline{z}} = z$$

Zraven je razlaga v enem koraku: $z = a + bi \rightarrow \bar{z} = a - bi \rightarrow \overline{\overline{z}} = a + bi = z$. Konjugiranje obrne predznak pred $i$, zato dvakratno konjugiranje vrne isto število.

"Dvojni negativni" sem razumel kot **dvojno konjugirano število** (dve črti nad $z$), ker se te lastnosti tako začnejo. Če si mislil navaden minus, $-(-z) = z$, mi povej in ga zamenjam. Naslednje lastnosti mi narekuj, pa jih dodajam kot 2., 3. ...
[Timestamp: 2026/10/20 10:57:13]

**user**: 2jaz im bom rekel konj Z (konjugiarno število) ko smo že pri tem naredi tik po uvodu samo en odsek za to stvar.  dobro 2 je da Z * konj Z je |Z|na kvadrat
[Timestamp: 2026/10/20 10:59:37]

**ai**: V [[kompleksna števila]] sem naredil dve spremembe.

**Nov razdelek Konjugirano število**, takoj za uvodom in pred Množenjem:
- Definicija: $z = a + bi \Rightarrow \bar{z} = a - bi$. Zraven piše, da ga ti imenuješ "konj $z$".
- Primer: $3 + 2i \rightarrow 3 - 2i$.
- Desmos graf, kjer se vidi, da je $\bar{z}$ zrcalna slika $z$ čez realno os.

Definicijo konjugiranega števila sem odstranil iz razdelka Množenje, ker je zdaj v svojem razdelku. Račun $z \cdot \bar{z}$ in primer sta tam ostala.

**Lastnost 2** v razdelku Lastnosti kompleksnih števil:
$$z \cdot \bar{z} = (a + bi)(a - bi) = a^2 + b^2 = |z|^2$$

Rezultat je vedno realno število.
[Timestamp: 2026/10/20 10:59:37]

**user**: 3 je da konj(x + w) = konj X in konj W
[Timestamp: 2026/10/20 11:01:17]

**ai**: Lastnost 3 sem dodal v [[kompleksna števila]]:

$$\overline{z + w} = \bar{z} + \bar{w}$$

Pri konjugiranju je vseeno, ali najprej seštevaš in potem konjugiraš, ali najprej konjugiraš in potem seštevaš. Zraven je dokaz v eni vrstici z $z = a + bi$ in $w = c + di$.

Namesto $x$ sem napisal $z$, ker v zapiskih kompleksno število vedno označuješ z $z$. Napisal sem tudi $+$ med $\bar{z}$ in $\bar{w}$, ker si verjetno mislil to in ne "in". Če je bilo na tabli drugače, mi povej.
[Timestamp: 2026/10/20 11:01:17]

**user**: 4 je isto za množenje  in a upaš poudariti tisto enačbo tik za število?
[Timestamp: 2026/10/20 11:01:58]

**ai**: V [[kompleksna števila]] sem dodal lastnost 4:

$$\overline{z \cdot w} = \bar{z} \cdot \bar{w}$$

Zraven je dokaz s formulo za množenje, ki je že v razdelku Množenje.

Pri vseh štirih lastnostih sem odebelil formulo takoj za številko, na primer **$\overline{\overline{z}} = z$**. Tako se lastnosti hitro najdejo, razlaga za pomišljajem pa ostane navadna. Odebeljene formule nisem videl v Obsidianu. V nekaterih temah $\LaTeX$ znotraj `**` ni videti krepko, zato preveri, ali so formule res poudarjene.
[Timestamp: 2026/10/20 11:01:58]

**user**: poglej kako sem to napisal, tako popravi še 3(bolj logicno) in enačba se in odebeljila
[Timestamp: 2026/10/20 11:05:39]

**ai**: Ubežni znaki so se pri `sed` izgubili, zato popravljam ročno:V [[kompleksna števila]] sem popravil oboje.

**Lastnost 3** je zdaj zapisana tako kot tvoja 4:
$$\overline{z + w} = \overline{(a + ib) + (c + id)} = (a - ib) + (c - id) = \bar{z} + \bar{w}$$
Brez vmesnega seštevanja se takoj vidi, da se pri vsakem številu obrne predznak pred $i$.

**Odebelitev**: zvezdice `**` ne odebelijo $\LaTeX$ formule, zato sem jih zamenjal z `\boldsymbol{...}` znotraj formule. To uporabim pri vseh štirih lastnostih, na primer `$\boldsymbol{\overline{z \cdot w} = \bar{z} \cdot \bar{w}}$`. Te oblike v Obsidianu nisem videl, zato preveri, ali so formule zdaj res krepke.
[Timestamp: 2026/10/20 11:05:39]

**user**: 5 je da Z + konjZ = 2ib
[Timestamp: 2026/10/20 11:06:41]

**ai**: Lastnost 5 sem dodal v [[kompleksna števila]], vendar z minusom, ker s plusom ne drži:

$$z - \bar{z} = (a + ib) - (a - ib) = 2ib$$

- **Pri minusu** se pokrajšata realna dela in ostane $2ib$. To je tvoj rezultat.
- **Pri plusu** se pokrajšata imaginarna dela: $z + \bar{z} = 2a$. To sem dodal kot eno vrstico pod lastnostjo 5.

Če je na tabli res pisalo $z + \bar{z} = 2ib$, je verjetno napaka pri prepisu. Preveri pri sošolcu ali v profesorjevih prosojnicah.
[Timestamp: 2026/10/20 11:06:41]

**user**: ne mislil sem da ostane 2a = 2Re(Z)
[Timestamp: 2026/10/20 11:08:32]

**ai**: Lastnost 5 je zdaj taka, kot si jo mislil:

$$z + \bar{z} = (a + ib) + (a - ib) = 2a = 2\,\text{Re}(z)$$

Imaginarna dela se pokrajšata, zato je rezultat realno število.

Pod njo je ostala vrstica za odštevanje, $z - \bar{z} = 2ib = 2i\,\text{Im}(z)$, ker je to druga polovica iste ideje. Če je profesor nima posebej, jo lahko pobrišem.
[Timestamp: 2026/10/20 11:08:32]

**user**: dobro in daj pod isto samo še da ostane 2Im(z)
[Timestamp: 2026/10/20 11:09:12]

**ai**: Pod lastnost 5 sem dodal še odštevanje, zapisano enako kot vsota (odebeljena formula, pod njo pa izračun):

$$z - \bar{z} = (a + ib) - (a - ib) = 2ib = 2i\,\text{Im}(z)$$

$i$ sem pustil v formuli. Brez njega ne drži, ker $\text{Im}(z) = b$ ne vsebuje $i$. Ko se realna dela pokrajšata, ostane $2ib$, torej $2i$ krat imaginarni del. Če želiš dobiti točno $2\,\text{Im}(z)$, moraš razliko še deliti z $i$: $\frac{z - \bar{z}}{i} = 2\,\text{Im}(z)`.
[Timestamp: 2026/10/20 11:09:12]

**user**: in sedaj teritori ki ga ne razumem več 6 je Z - konj Z = 2ln(Z)

 ampak to sem pomoje samo falil in je ubistvu to drugi del 5
[Timestamp: 2026/10/20 11:11:01]

**ai**: Prav sumiš. To je drugi del lastnosti 5, ki je že v zapiskih:

$$z - \bar{z} = 2i\,\text{Im}(z)$$

"ln" je skoraj gotovo **$i\,\text{Im}$**, ki si ga hitro prepisal. Ročno napisan $i$ in takoj za njim "Im" sta videti kot "ln": pika na $i$ se izgubi, "I" postane "l", "m" pa "n". Logaritem tukaj ne bi imel smisla. Ko odšteješ $z$ in $\bar{z}$, se pokrajšata realna dela in ostane $2ib$, kar je točno $2i\,\text{Im}(z)$.

V [[kompleksna števila]] zato nisem nič spremenil. Profesor je verjetno to vzel kot svojo, 6. lastnost. Če želiš, da imaš številke enake kot on, odštevanje premaknem iz 5 v svojo točko 6.
[Timestamp: 2026/10/20 11:11:01]

**user**: 6 je potem |Z + W| <= |Z| + |W|
[Timestamp: 2026/10/20 11:12:04]

**ai**: V [[kompleksna števila]] sem dodal lastnost 6, **trikotniško neenakost**:

$$|z + w| \leq |z| + |w|$$

**Razlaga, ki sem jo napisal:**
- $z$, $w$ in $z + w$ tvorijo trikotnik. Od $0$ greš do $z$, potem še za $w$ naprej in prideš do $z + w$.
- Stranica naravnost od $0$ do $z + w$ ne more biti daljša od ovinka čez $z$. Zato je $|z + w| \leq |z| + |w|$.
- Enako ($=$) velja samo takrat, ko $z$ in $w$ kažeta v isto smer in se trikotnik splošči v daljico.

Pod njo je **Desmos graf** s točkama $z$ in $z + w$. Na njem sta polni stranici $|z|$ in $|w|$, črtkana stranica pa je $|z + w|$. Graf je napisan enako kot prejšnji, v Obsidianu ga nisem odprl.
[Timestamp: 2026/10/20 11:12:04]

**user**: kje v zapiskih je tudi ta trkotniška neenakot? ker nejke bi morala biri
[Timestamp: 2026/10/20 11:12:56]

**ai**: Trikotniška neenakost je v vaultu samo v [[kompleksna števila]], kot lastnost 6, ki sem jo pravkar dodal.

Preiskal sem vse zapiske. Iskal sem besedi "trikotniška" in "neenakost" ter zapise, kot sta $|x + y| \leq |x| + |y|$ in $|a| + |b|$. Pogledal sem tudi:

- [[enacbe procenti abslutna]]: razdelek *Absolutna vrednost* ima samo definicijo in primer enačbe, neenakosti ni.
- [[množice števil]]: ima lastnosti naravnih števil, intervale in ulomke, absolutne vrednosti in neenakosti pa ne.

PDF-jev in slik v vaultu nisem pregledal. Če si jo kdaj zapisal v kakšen PDF ali na sliko table, je to iskanje ne najde.

Verjetno jo je profesor prej pokazal za realna števila, $|x + y| \leq |x| + |y|$, ti pa je takrat nisi zapisal. Lahko jo dodam v razdelek *Absolutna vrednost* v [[enacbe procenti abslutna]], s primerom na številski premici in povezavo na lastnost 6 pri kompleksnih številih.
[Timestamp: 2026/10/20 11:12:56]

**user**: ta graf je malo prevelik
[Timestamp: 2026/10/20 11:14:51]

**ai**: Graf trikotniške neenakosti v [[kompleksna števila]] sem pomanjšal na **360 × 300** pikslov. Desmos vtičnik privzeto riše grafe velike 600 × 400. Razmerje 360 × 300 se ujema z obsegom osi, zato trikotnik ne bo raztegnjen.

Če je še vedno prevelik ali pa zdaj premajhen, mi povej, pa velikost spremenim. Na enak način lahko pomanjšam tudi ostale grafe v zapisku.
[Timestamp: 2026/10/20 11:14:51]

**user**: dobro to razumem ampak jaz sem islil da je absolutna od Z + W samo razdalja med Z in W in ne še od nič do Z
[Timestamp: 2026/10/20 11:16:44]

**ai**: Malo si zamešal: razdalja med $z$ in $w$ je **$|z - w|$**, z minusom. **$|z + w|$** pa je razdalja točke $z + w$ od $0$.

**Pri realnih številih**, kot v [[enacbe procenti abslutna]]:
- $|5 - 3| = 2$ je razdalja med $3$ in $5$ na premici.
- $|5 + 3| = 8$ ni razdalja med $3$ in $5$. To je samo razdalja števila $8$ od $0$.

**Pri kompleksnih številih je enako.** Vzemimo $z = 3 + i$ in $w = 1 + 2i$:
- $z + w = 4 + 3i$ je nova točka, zato je $|z + w| = \sqrt{4^2 + 3^2} = 5$. To je razdalja od $0$ do točke $4 + 3i$.
- $z - w = 2 - i$, zato je $|z - w| = \sqrt{2^2 + 1^2} = \sqrt{5}$. To je razdalja med točkama $z$ in $w$.

**Na grafu** se zato vidi tako:
- Črtkana črta od $0$ do $z + w$ je $|z + w|$.
- Črta od $z$ do $z + w$ je dolga $|w|$. To je $w$, ki ga premakneš tako, da se začne v $z$. Ni razdalja med $z$ in $w$, ker točka $w$ na tem grafu sploh ni narisana.

Če želiš, v [[kompleksna števila]] pod absolutno vrednost dodam kratko vrstico: "$|z - w|$ je razdalja med $z$ in $w$, $|z + w|$ je razdalja od $0$ do $z + w$". Zraven bi dodal še primer z mini grafom, da se ti to drugič ne zamenja.
[Timestamp: 2026/10/20 11:16:44]

**user**: sedaj imam to samo napisane neke enačbe: 2z + 6i = 8  == z = 4 -3i  a to naj bi kaj pomenilo ali je samo z nekega računa sestavil kompleksno število?
[Timestamp: 2026/10/20 11:19:47]

**ai**: To ni sestavljeno kar tako, to je **navadna linearna enačba**, samo da je neznanka $z$ kompleksno število. Rešiš jo popolnoma enako kot $2x + 6 = 8$, pri čemer se $i$ obnaša kot navadna črka:

$$2z + 6i = 8 \quad\Big|\; -6i$$
$$2z = 8 - 6i \quad\Big|\; :2$$
$$z = 4 - 3i$$

**Preizkus:** $2(4 - 3i) + 6i = 8 - 6i + 6i = 8$ ✓

**Kaj je profesor s tem verjetno hotel pokazati:**
- Z računskimi pravili, ki smo jih zapisali, lahko kompleksna števila uporabljaš v enačbah kot vsa druga števila: odštevaš na obeh straneh, deliš itd.
- Rešitev je lahko kompleksno število, čeprav je na desni strani realno število $8$.
- Mimogrede, $|z| = \sqrt{4^2 + 3^2} = 5$. To je spet trikotnik 3-4-5 z grafa absolutne vrednosti, zato ga lahko vzameš tudi kot primer za razdaljo od $0$.

Če želiš, v [[kompleksna števila]] dodam razdelek **Enačbe** s tem primerom, postopkom in preizkusom.
[Timestamp: 2026/10/20 11:19:47]

**user**: da
[Timestamp: 2026/10/20 11:21:01]

**ai**: Na konec [[kompleksna števila]], za Lastnosti, sem dodal razdelek **Enačbe**. V njem je:

- kratka razlaga, da kompleksno enačbo rešuješ enako kot navadno, $i$ pa je kot navadna črka;
- tvoj primer $2z + 6i = 8$, po korakih $-6i$ in $:2$, do rešitve $z = 4 - 3i$;
- preizkus $2(4 - 3i) + 6i = 8$ ✓.
[Timestamp: 2026/10/20 11:21:01]

**user**: potem je še { Z je kompleksno | z + konjz = 5} in nato ven dobiš a = 3/2 ali nekaj takega
[Timestamp: 2026/10/20 11:22:39]

**ai**: V [[kompleksna števila]] sem pod razdelek Enačbe dodal ta primer. Rezultat je $a = \frac{5}{2}$, ne $\frac{3}{2}$:

$$\{\, z \in \mathbb{C} \mid z + \bar{z} = 5 \,\}$$

**Kako pridemo do tega:**
- Po lastnosti 5 je $z + \bar{z} = 2a$, zato velja $2a = 5$ in $a = \frac{5}{2}$.
- Enačba o $b$ ne pove ničesar, zato je $b$ lahko karkoli.
- Rešitev torej ni eno število, ampak **množica** vseh $z = \frac{5}{2} + bi$, $b \in \mathbb{R}$.
- Na grafu je to **navpična premica** pri $\text{Re}(z) = \frac{5}{2}$.

Dodal sem tudi manjši Desmos graf (360 × 300) s to premico. Na njej so označene tri točke kot primeri rešitev: $\frac{5}{2}$, $\frac{5}{2} + 1{,}5i$ in $\frac{5}{2} - i$.

Če si si zapisal $\frac{3}{2}$, je bilo na desni strani verjetno $3$ namesto $5$. Takrat bi bilo $a = \frac{3}{2}$, vse drugo pa enako.
[Timestamp: 2026/10/20 11:22:39]

**user**: to označi kot primir 2
[Timestamp: 2026/10/20 11:24:11]

**ai**: V razdelku Enačbe v [[kompleksna števila]] sem primera označil s številkama:

- **Primer 1:** $2z + 6i = 8$.
- **Primer 2:** rešitev je lahko tudi množica števil, $\{\, z \in \mathbb{C} \mid z + \bar{z} = 5 \,\}$.

Obe oznaki sta odebeljeni.
[Timestamp: 2026/10/20 11:24:11]

**user**: in zakaj je po lastnosti 5 lahko kar tisti 2a ne zastopim
[Timestamp: 2026/10/20 11:25:06]

**ai**: Lastnost 5 je samo bližnjica. Lahko jo tudi izpustiš in izračunaš direktno, pa dobiš isto.

**Korak za korakom:**
1. Vsako kompleksno število lahko zapišeš kot $z = a + bi$, kjer je $a$ realni in $b$ imaginarni del.
2. Konjugirano število ima obrnjen predznak pred $i$: $\bar{z} = a - bi$.
3. Ti dve števili seštej:
$$z + \bar{z} = (a + bi) + (a - bi) = a + a + bi - bi = 2a$$
   Člena $+bi$ in $-bi$ se pokrajšata, ostane samo $a + a = 2a$.
4. Enačba pravi $z + \bar{z} = 5$. Levo stran zamenjaš z $2a$, ker smo pravkar izračunali, da je to isto:
$$2a = 5 \quad \Rightarrow \quad a = \frac{5}{2}$$

**Lastnost 5** je ta račun iz tretjega koraka, ki smo ga zapisali enkrat za vselej: $z + \bar{z} = 2a$ velja za **vsako** kompleksno število. Zato ga ni treba vsakič znova računati, ampak samo napišeš "po lastnosti 5 je to $2a$".

Ker se $b$ pokrajša, ga v enačbi sploh ni več. Zato je $b$ lahko karkoli in rešitev je cela navpična premica.

Če želiš, v Primeru 2 v [[kompleksna števila]] vrstico "Po lastnosti 5 ..." zamenjam s tem računom, da bo vse zapisano.
[Timestamp: 2026/10/20 11:25:06]

**user**: naredi ta zadnji graf manjši
[Timestamp: 2026/10/20 11:25:57]

**ai**: Zadnji graf v [[kompleksna števila]], tisti z navpično premico pri Primeru 2, sem pomanjšal s 360 × 300 na **240 × 200** pikslov. Razmerje stranic je ostalo enako, zato premica ne bo raztegnjena. Če so oznake točk zdaj pregoste, ga malo povečam nazaj.
[Timestamp: 2026/10/20 11:25:57]

**user**: in nato je še |Z - 1 - i| na kvadrat = 2
[Timestamp: 2026/10/20 11:26:36]

**ai**: V [[kompleksna števila]] sem pod Enačbe dodal **Primer 3**:

$$\{\, z \in \mathbb{C} \mid |z - 1 - i|^2 = 2 \,\}$$

**Postopek:**
- Vstaviš $z = a + bi$ in dobiš $z - 1 - i = (a - 1) + i(b - 1)$.
- Po Pitagori je $|z - 1 - i|^2 = (a - 1)^2 + (b - 1)^2 = 2$.
- To je enačba **krožnice** s središčem v $1 + i$ in polmerom $\sqrt{2}$.

Zraven sem napisal še krajšo pot brez računanja: $|z - (1 + i)|$ je razdalja med $z$ in $1 + i$, ki mora biti $\sqrt{2}$.

Dodal sem tudi majhen Desmos graf (240 × 240) s to krožnico. Na njem so označeni središče $1 + i$ ter točki $0$ in $2 + 2i$, ki ležita na krožnici. Graf je napisan enako kot prejšnji, v Obsidianu ga nisem odprl.
[Timestamp: 2026/10/20 11:26:36]

**user**: perfektno sedaj pa še ena zanimiva zadeva.  profesor je začel taok da je spet narisal hipotenuto in označil kot med Z in realnimi števili kot fi.  nato povedal |Z|cosfi + i|Z|sinfi = |Z| * e na fi
[Timestamp: 2026/10/20 11:33:51]

**ai**: Na konec [[kompleksna števila]] sem dodal nov razdelek **Polarni zapis**. Formulo sem zapisal kot $e^{i\varphi}$, ne $e^{\varphi}$. Brez $i$ v eksponentu bi bilo $e^{\varphi}$ navadno realno število in formula ne bi držala, zato je profesor verjetno napisal $e^{i\varphi}$, ti pa si $i$ pri prepisu izpustil.

**Kaj je v razdelku:**
- **Graf** s trikotnikom za $z = 3 + 4i$. Kot $\varphi$ med realno osjo in $z$ je označen z lokom.
- **Izpeljava s kotnima funkcijama:** iz $\cos\varphi = \frac{a}{|z|}$ dobiš $a = |z|\cos\varphi$, iz $\sin\varphi = \frac{b}{|z|}$ pa $b = |z|\sin\varphi$.
- Ko to vstaviš v $z = a + bi$, dobiš $z = |z|(\cos\varphi + i\sin\varphi)$.
- **Eulerjeva formula** $\cos\varphi + i\sin\varphi = e^{i\varphi}$, iz katere sledi odebeljena formula $\boldsymbol{z = |z|\,e^{i\varphi}}$.
- **Pomen:** število opišeš z dolžino in kotom (kako daleč in v katero smer), namesto z $a$ in $b$.
- **Primer:** $1 + i = \sqrt{2}\,e^{i\pi/4}$.
- **Povezava z uvodom:** $i = e^{i\pi/2}$, zato je množenje z $i$ res zasuk za $90^\circ$.

Eulerjevo formulo sem zapisal samo kot dejstvo, brez dokaza. Dokaz potrebuje vrste, ki jih verjetno še niste imeli.

Lok za kot sem narisal z omejitvami krožnice, kar vtičnik podpira, vendar tega v Obsidianu nisem preveril. Če se lok ne prikaže, mi povej.
[Timestamp: 2026/10/20 11:33:51]

**user**: in nato smo pokazali da če daš konj čez vse skupaj se samo i -ju zamenja predzank na -
[Timestamp: 2026/10/20 11:41:03]

**ai**: V razdelek Polarni zapis v [[kompleksna števila]] sem dodal konjugirano število v polarnem zapisu.

**Postopek:**
- Ko konjugiraš $z = |z|(\cos\varphi + i\sin\varphi)$, se zamenja samo predznak pred $i$. Dobiš $\bar{z} = |z|(\cos\varphi - i\sin\varphi)$.
- Ker je $\cos(-\varphi) = \cos\varphi$ in $\sin(-\varphi) = -\sin\varphi$, je to enako kot kot $-\varphi$.
- Rezultat je odebeljena formula $\boldsymbol{\bar{z} = |z|\,e^{-i\varphi}}$.

Zraven je razlaga, zakaj je to smiselno. Dolžina ostane enaka, kot pa zamenja predznak. To se ujema z grafom iz razdelka Konjugirano število, kjer je $\bar{z}$ zrcalna slika $z$ čez realno os, torej pod osjo namesto nad njo.
[Timestamp: 2026/10/20 11:41:03]

**user**: in to me samo zanima ampak kdo si je izmislil tisto kačo cos in sin spremeniti samo v čeok e in zakaj?
[Timestamp: 2026/10/20 11:43:01]

**ai**: Formule si ni nihče "izmislil", ampak jo je **odkril**. To je **Leonhard Euler**, švicarski matematik, ki jo je objavil leta 1748. Nekaj podobnega je približno 30 let pred njim zapisal že Anglež Roger Cotes, ampak v manj jasni obliki, zato se formula imenuje po Eulerju.

**Od kod pride**

Funkcije $e^x$, $\cos x$ in $\sin x$ lahko zapišeš kot neskončne vsote (vrste):
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots$$
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots \qquad \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$$

Euler je v vsoto za $e^x$ vstavil $x = i\varphi$. Potence $i$ se ponavljajo v krogu: $i, -1, -i, 1, i, -1, \dots$. Tako se predznaki sami od sebe razporedijo:
$$e^{i\varphi} = \underbrace{\Big(1 - \frac{\varphi^2}{2!} + \frac{\varphi^4}{4!} - \dots\Big)}_{\cos\varphi} + i\underbrace{\Big(\varphi - \frac{\varphi^3}{3!} + \dots\Big)}_{\sin\varphi}$$

Realni členi dajo točno $\cos$, imaginarni pa točno $\sin$. Gre torej za naključje, ki ga račun pokaže, ne za dogovor. Te vrste boste verjetno delali pri analizi.

**Zakaj se to splača**

Glavni razlog je, da se **množenje spremeni v seštevanje kotov**, ker veljajo pravila za potence:
$$e^{i\alpha} \cdot e^{i\beta} = e^{i(\alpha + \beta)}$$

Če bi isto množil v obliki s $\cos$ in $\sin$, bi dobil dolg račun s formulami za $\cos(\alpha + \beta)$ in $\sin(\alpha + \beta)$. Z $e$ je to ena vrstica.

Zato velja:
- Ko množiš kompleksni števili, **pomnožiš dolžini in sešteješ kota**. Zato je množenje z $i$ zasuk za $90^\circ$.
- Potence so lahke: $z^n = |z|^n e^{in\varphi}$. Kot samo pomnožiš z $n$.

**Za zanimivost:** če vstaviš $\varphi = \pi$, dobiš
$$e^{i\pi} + 1 = 0$$

Ta enačba v eni vrstici poveže pet najpomembnejših števil v matematiki: $0$, $1$, $e$, $i$ in $\pi$. Mnogi matematiki jo imajo za najlepšo formulo sploh.

Če želiš, v razdelek Polarni zapis dodam vrstico o množenju, $e^{i\alpha} \cdot e^{i\beta} = e^{i(\alpha + \beta)}$, ker jo boste verjetno kmalu potrebovali.
[Timestamp: 2026/10/20 11:43:01]

**user**: saj to je ubistvu naslednja enačba in sicer konj(X *W) in to spremeni v polarni zapis in nato zmnoži
[Timestamp: 2026/10/20 11:47:32]

**ai**: Na konec razdelka Polarni zapis v [[kompleksna števila]] sem dodal dve stvari.

**Množenje v polarnem zapisu** (odebeljena formula):
$$z \cdot w = |z||w|\,e^{i(\varphi + \psi)}$$
Dolžini se zmnožita, kota pa seštejeta, ker velja $e^x \cdot e^y = e^{x+y}$. Za kot števila $w$ sem uporabil $\psi$, da se ne zamenja s $\varphi$. Če je profesor pisal drugače, na primer $\varphi_1$ in $\varphi_2$, mi povej in zamenjam.

**Konjugirano število produkta $\overline{z \cdot w}$**, po korakih, kot si opisal:
1. Produkt zapišeš v polarnem zapisu: $|z||w|\,e^{i(\varphi + \psi)}$.
2. Konjugiraš, torej obrneš predznak kota: $|z||w|\,e^{-i(\varphi + \psi)}$.
3. Razbiješ nazaj na dva faktorja: $|z|\,e^{-i\varphi} \cdot |w|\,e^{-i\psi} = \bar{z} \cdot \bar{w}$.

Tako dobiš isto kot lastnost 4, le z drugim dokazom. V polarnem zapisu je račun krajši kot z $a$, $b$, $c$, $d$.
[Timestamp: 2026/10/20 11:47:32]

**user**: |𝑧| 𝑒−𝑖𝜑 ⋅|𝑤| 𝑒−𝑖𝜓 =
¯
𝑧
 ⋅
¯
𝑤
.  razloži ta korak
[Timestamp: 2026/10/20 11:50:45]

**ai**: V tem koraku se nič ne računa. Samo **prepoznaš**, kaj je vsak od obeh faktorjev.

Malo višje v razdelku Polarni zapis smo izpeljali:
$$\bar{z} = |z|\,e^{-i\varphi}$$
Konjugirano število ima isto dolžino, kot pa z minusom.

Za $w = |w|\,e^{i\psi}$ velja popolnoma enako, samo s $\psi$ namesto $\varphi$:
$$\bar{w} = |w|\,e^{-i\psi}$$

Zdaj pogledaš levo stran koraka in vsak del zamenjaš z njegovim imenom:
$$\underbrace{|z|\,e^{-i\varphi}}_{=\,\bar{z}} \cdot \underbrace{|w|\,e^{-i\psi}}_{=\,\bar{w}} = \bar{z} \cdot \bar{w}$$

Podobno je, kot če bi imel $x = 2 \cdot 3$ in $2 = a$, $3 = b$, pa napisal $x = a \cdot b$.

**Korak pred tem** je verjetno težji. Tam se $e^{-i(\varphi + \psi)}$ razbije na $e^{-i\varphi} \cdot e^{-i\psi}$. To je pravilo za potence $e^{x + y} = e^x \cdot e^y$, uporabljeno v obratni smeri: $-i(\varphi + \psi) = -i\varphi + (-i\psi)$. Dolžini $|z||w|$ pa samo razporediš, vsako k svojemu $e$.

Če želiš, v zapisek pod ta korak dodam vrstico "ker je $\bar{z} = |z|\,e^{-i\varphi}$ in $\bar{w} = |w|\,e^{-i\psi}$".
[Timestamp: 2026/10/20 11:50:45]

**user**: a točno. in nekje sem videl da če tisti ena ifi pokažeš kot funkcijo ali nekaj takega in jo pogledaš z ene smeri bo izgledala kot sin in z druge kot cos
[Timestamp: 2026/10/20 11:51:55]

**ai**: Ja, to drži. Gre za graf funkcije $e^{i\varphi}$ v 3D.

**Kako to narišeš**

Za vsak kot $\varphi$ dobiš točko $e^{i\varphi} = \cos\varphi + i\sin\varphi$. Ta točka leži na enotski krožnici. Zdaj dodaš še tretjo os, po kateri teče $\varphi$:
- os 1: $\varphi$ (kot, ki raste),
- os 2: realni del, $\cos\varphi$,
- os 3: imaginarni del, $\sin\varphi$.

Ko $\varphi$ raste, se točka vrti po krogu in se hkrati premika naprej po osi $\varphi$. Nastane **vijačnica** (spirala), podobna vzmeti ali zavitemu kablu za telefon.

**Kaj vidiš iz različnih smeri**
- **Od spredaj** (gledaš vzdolž osi $\varphi$): vidiš samo **krog**, enotsko krožnico iz grafa v uvodu.
- **Od strani**, tako da vidiš os $\varphi$ in realno os: vidiš **$\cos\varphi$**. To je senca vijačnice na tej ravnini.
- **Od zgoraj**, tako da vidiš os $\varphi$ in imaginarno os: vidiš **$\sin\varphi$**.

Kosinus in sinus sta torej dve "senci" istega vrtenja po krogu. Zato je Eulerjeva formula $e^{i\varphi} = \cos\varphi + i\sin\varphi$ tako naravna: $e^{i\varphi}$ je vrtenje, $\cos$ in $\sin$ pa sta njegova pogleda s strani.

Desmos vtičnik v Obsidianu zna risati samo 2D. Vijačnice zato ne morem narisati v zapisek, lahko pa v Polarni zapis dodam kratek opis in 2D graf, kjer sta $\cos\varphi$ in $\sin\varphi$ narisana skupaj. Če hočeš videti vijačnico, v brskalniku odpri Desmos 3D (desmos.com/3d) in vpiši krivuljo $(t, \cos t, \sin t)$.
[Timestamp: 2026/10/20 11:51:55]