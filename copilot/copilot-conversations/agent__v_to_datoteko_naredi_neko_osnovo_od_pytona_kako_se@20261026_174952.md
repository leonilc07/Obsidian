---
epoch: 1793033392088
mode: agent
backendId: claude
sessionId: "12004afc-0361-44d5-a244-75aab0e3f43c"
agentLabel: "v to datoteko naredi neko osnovo od pytona kako se kaj obnaš…"
usage: '{"usedTokens":73041,"contextWindow":1000000,"inputTokens":2,"outputTokens":116,"cacheReadTokens":70725,"cacheWriteTokens":2198,"updatedAt":1793034224719}'
tags:
  - copilot-conversation
---

**user**: v to datoteko naredi neko osnovo od pytona kako se kaj obnaša in kar misliš da je potrebno, kako se ga naloži in ohranja različne dokumente z condo kaj so knjižnice, malo o odzadju kako se razlikuje od drugih jezikov in nato malo bolj tehnično na temu kaj kako dela kakšne tabele recimo ali kaj takega
[Timestamp: 2026/10/26 17:49:52]

**ai**: Zapisal sem zapiske v [[pyton osnove]] (prej je bila datoteka prazna). Vsebina po poglavjih:

1. **Ozadje**: zgodovina Pythona in primerjalna tabela s C/C++ in Javo (interpretiran ali prevajan jezik, dinamični tipi, upravljanje pomnilnika, zamiki, hitrost).
2. **Namestitev in Conda**: Miniconda ali Anaconda, zakaj potrebuješ ločena okolja in vsi osnovni `conda` ukazi (ustvarjanje, aktivacija, nameščanje, izvoz v `environment.yml`).
3. **Knjižnice**: razlika med modulom in paketom, standardna knjižnica, različni načini `import` in najbolj uporabne zunanje knjižnice (numpy, pandas, matplotlib, scipy …).
4. **Osnove jezika**: tipi, operatorji, pogoji, zanke, funkcije, `input` in `print` ter f-stringi.
5. **Podatkovne strukture**: tabela, ki primerja list, tuple, set, dict in str, primeri za vsako strukturo in pravilen način za 2D tabelo (s pastjo, ki se ji je treba izogniti).
6. **Tehnični del**:
   - spremenljivke so v resnici imena, ki kažejo na objekte (`is` ali `==`, kopije)
   - spremenljivi in nespremenljivi tipi
   - časovna zahtevnost osnovnih operacij
   - list je v ozadju dinamična tabela, dict pa zgoščevalna (hash) tabela
   - bytecode, kako se sprošča pomnilnik in GIL
   - numpy tabele v primerjavi z navadnimi seznami
7. **Dodatno**: izjeme, delo z datotekami in kratek uvod v razrede.

Če želiš, lahko kakšen del razširim, na primer numpy in pandas ali rekurzijo.
[Timestamp: 2026/10/26 17:49:52]

**user**: poglej to datoteko "C:\Users\leoni\Downloads\03b indeksi in rezine.ipynb" in v to datoteko povej samo glavno od indeksiranja ker ot že vse ven samo nevem kje se kaj loti z 0 ali z 1 in podobne stvari. potem bolj povej o rezanju in dveh funkcijah, enumeration ki ti oštevilči stvari v listu ali tabeli in zipu ki ti združi liste. in še malo če imajo kakšn dober "sinegri"
[Timestamp: 2026/10/26 17:58:26]

**ai**: 
[Timestamp: 2026/10/26 17:58:26]

**user**: in ne tako na dolgo kakor je v tej datoteki ki sem  ti jo poslal
[Timestamp: 2026/10/26 17:58:54]

**ai**: V [[pyton indeksi in rezine]] sem zapisal kratke zapiske, veliko krajše od originala, brez dolgih razlag:

- **Indeksiranje**: kaj se začne z 0, kako delajo negativni indeksi in pravilo za `range` in rezine (začetek je vključen, konec ni).
- **Rezanje**: oblika `s[začetek:konec:korak]` s primeri, ki jih največ uporabljaš (prvih ali zadnjih n znakov, odbijanje, obračanje, vrivanje). Zraven je še, kako z rezinami spreminjaš sezname.
- **`enumerate`**: oštevilči elemente, s parametrom `1` začne šteti pri 1.
- **`zip`**: združi sezname in se ustavi pri najkrajšem.
- **Sinergije**:
  - `zip(s, s[1:])` da pare zaporednih elementov, npr. za razlike ali preverjanje, ali seznam narašča
  - `enumerate(zip(...))` da indeks in več seznamov hkrati
  - `enumerate` pomaga pri iskanju indeksov
  - z `zip` primerjaš dva niza po znakih

Dodal sem tudi nekaj primerov, ki jih v tvoji datoteki ni: `dict(zip(...))`, primerjavo nizov po znakih, preverjanje naraščanja z `all` in iskanje indeksov z `enumerate`.
[Timestamp: 2026/10/26 17:58:54]

**user**: poglej si druge glavne datoeke v posamezni mapi in to od matematike dopolni z temi stvarmi Vrste domačih nalog in ocenjevanje
Uspešno opravljeno sprotno delo v obliki tedenskih domačih nalog je obvezni predpogoj za izpit.

Domače naloge so dveh vrst. Tri naloge bodo večje, ostale (približno deset nalog) pa manjše.

Manjše naloge: za uspešno opravljeno manjšo nalogo je potrebno pravilno rešiti ogrevalni (če obstaja) in obvezni del. Dodatna naloga ni obvezna. Za uspešno opravljeno sprotno delo vam smeta manjkati največ dve manjši nalogi.

Pri večjih nalogah je določeno, kaj je potrebno sprogramirati za oceno 6, 7, 8, 9 in 10. Za določeno oceno je potrebno sprogramirati tudi vse, kar je zahtevano za nižje ocene. Vse večje naloge so obvezne za pristop k izpitu. Ocena služi motivaciji, meni pa tudi kot pomoč pri zaokrožanju ocene izpita.

Ločeno objavljene dodatne izzive, uganke... utegnejo zahtevati stvari, ki se jih (še?) nismo učili. Te delate, ker bi se radi naučili še kaj več, ali ker vas obvezne in dodatne naloge dolgočasijo.

Domače naloge je potrebno v danem roku; po tem oddaja ni več mogoča. Oddati jih morate prek učilnice, ne po elektronski pošti ali kako drugače. Če ni drugače določeno, jih je potrebno oddati kot eno samo datoteko s končnico .py (ne kot .zip ali kaj podobnega).

Če za nalogo obstajajo testi, oddajte svoj izdelek skupaj s testi. Tako se izognemo temu, da bi poleg testov ponesreči pobrisali še kaj, česar ne smete.

Napake v rešitvah
Naloga mora prestati priložene testne primere, sicer se šteje rešitev za napačno, kar je enako, kot da je niste oddali. Tudi če prestane teste, lahko še vedno dobi 0 točk, če je napačna na kak očiten način, ki ga testi ne preverjajo, če je posebej prirejena za teste in podobno.

Nekatere naloge ne bodo imele priloženih testov. V tem primeru bomo pri popravljanju spregledali manjše napake, če bomo presodili, da je študent napake spregledal, čeprav se je trudil pravilno rešiti nalogo. Če vsebuje program napake, ki jih reševalec ni mogel spregledati in je po naši oceni zavestno oddal nedelujoč program, naloga ni bila uspešno rešena in se šteje, kot da ni bila oddana. To velja še posebej, če program vsebuje sintaktične napake, kar pomeni, da ga študent ni niti pognal.

Uporaba pripomočkov
Študent, ki za reševanje nalog pri Programiranju 1 uporablja chatGPT in podobne programe, ravna enako modro kot tretješolček, ki pri učenju poštevanke uporablja kalkulator. Oni tretješolček ne bo znal poštevanke, študent pa ne bo znal programirati.

Argument "ampak saj v praksi bomo uporabljali ta orodja, torej se jih moramo naučiti uporabljati" je enako smiseln kot argument tretješolčka, da mu ni treba znati poštevanke, ker bo za množenje uporabljal kalkulator. Tretješolčku lahko, če ne drugega, odgovorimo, da bomo v tem primeru preskočili poštevanko in začeli s trigonometrijo in verjetnostnim računom, kjer mu kalkulator ne bo pomagal.

Četudi bo rutinske programe namesto vas nekoč res pisala umetna inteligenca, gre za stopnico, na katero morate vsaj enkrat stopiti tudi peš. Če se ne strinjate, pa vam lahko z veseljem predavam funkcije višjih redov, currying in thunking. Je tudi meni bolj zabavno kot zanke in pogojni stavki. ::)

Prepisovanje in ukrepi
TL;DR: prepisovanja ne trpimo. Ta, ki da prepisovati, je enako kriv kot oni, ki prepisuje.

Če odkrijemo, da sta dve rešitvi ali celo več rešitev enaki do takšne mere, da gre za očiten plagiat, bodo kaznovani vsi udeleženi, ne glede na to, kdo je resnični avtor. Možni kazni sta dve. V primeru, da presodimo, da je prepisan manjši del naloge ali pa je kršitev milejša iz kakega drugega razloga, se šteje, da niste oddali dveh domačih nalog (kazen mora biti hujša od tega, kar ste s prekrškom pridobili!). Če gre za čisto in očitno prepisovanje, pa se razveljavi celotno sprotno delo in v tem letu ne boste mogli opravljati izpita. Posebej drzne kršitve bomo prijavili disciplinski komisiji.

Ne objavljajte svojih rešitev na forumih ali na raznih "padih", kjer jih lahko vidijo tudi drugi. Če kdo - četudi neznanec - prepiše vašo rešitev od tam, je to enako, kot da ste mu jo dali prepisati.

Izpit
Izpit je pisni. V posebnih primerih mu lahko sledi tudi ustni. Naloge boste reševali na računalnikih, priloženi bodo podobni testi kot pri domačih nalogah (z izjemo prvih).

Na izpitu je dovoljena vsa literatura v poljubni obliki. Omogočen bo dostop do Učilnice, ostali dostop do interneta pa bo zaprt. Izpit boste pisali na fakultetnih računalnikih.

Zasilnih vhodov ni
Vsako leto se najdejo študenti brez domačih nalog ali s prepisanimi domačimi nalogami, ki bi radi vseeno opravljali izpit in imajo v zvezi s tem različne predloge. Pogosta fraza je "smo mislili, da se bo dalo kaj zmeniti." Nekateri bi radi dobili dodatne domače naloge, s katerimi bodo tik pred izpitom "odslužili sprotno delo". To je očitno nekoristno - da o dodatnem delu s sestavljanjem nalog za tiste, ki med semestrom "niso imeli časa", ne govorimo. Drugi bi naknadno rešili obstoječe naloge - katerih rešitve so seveda že objavljene na Učilnici. Bistro. Tretji menijo, da bi bilo primerno, da bi bili tisti, ki niso delali sproti, kaznovani tako, da bi lahko prišli na izpit šele septembra. S tem dosežemo - kaj že?

Ne računajte na katerokoli od teh možnosti.

Homeworks and grading
Homeworks are published every week after the lectures. The usual deadline is next Tuesday at 23:55.

Three homeworks are larger and graded; others are smaller.

Smaller homeworks have three levels. You must correctly solve the warm-up task and the mandatory task. To qualify to attend the exam, you may skip (or submit incorrect solutions of) at most two homeworks. Extra homeworks are not mandatory.

Larger homeworks consist of tasks that need to be done for grades 6, 7, 8, 9 and 10. To qualify for the exam, you have to submit solutions for grade at least 6 for all larger homeworks. You can't skip those.

Homeworks must be submitted within the deadline using Ucilnica, not email or another way. When not specified otherwise, you must submit the solution in a single .py file.

Mistakes in submitted solutions
Your solution must pass the tests accompanying the homework, otherwise it is considered as incorrect. Even if it passes the test, it may be incosidered incorrect if wrong in an obvious way not tested by the tests, or it the student cheats by fitting the solution to the tests. (Don't worry about this; consider this a legal speak. If you don't try to cheat your way through the homeworks, you'll be fine.)

Some homeworks won't have the tests. In this case, we'll ignore smaller mistakes for which we believe that the students overlookoed them. If the solution includes large mistakes that are impossible to overlook or that we warned about, the solution will be considered incorrect.

Plagiarism
We have zero tolerance for plagiarism. Consequences of cheating range from annulling the bonus of two missing homeworks to reporting the incident to the faculty.  samo glavno niti približno ne usega
[Timestamp: 2026/10/26 18:02:34]

**ai**: V [[glavno programiranje]] sem dodal razdelek **stvari** z najpomembnejšimi pravili. Zgradba je enaka kot v [[DS glavno]] in [[glavno RA]]: najprej kontakt, nato stvari, potem predavanja.

Pod **stvari** je zdaj na kratko:
- **Domače naloge**: oddaš jih v učilnico kot eno `.py` datoteko, rok je običajno torek ob 23:55.
- **Manjše naloge**: rešiti moraš ogrevalni in obvezni del, manjkata ti lahko največ dve.
- **Večje naloge**: vse tri so obvezne, pri vsaki potrebuješ vsaj oceno 6.
- **Testi**: rešitev mora prestati priložene teste.
- **Prepisovanje**: ni dovoljeno, kaznovan je tudi tisti, ki da prepisati.
- **Izpit**: pisni, na računalnikih, dovoljena je vsa literatura, internet pa je omejen samo na učilnico. Brez opravljenih domačih nalog ne moreš na izpit.

Razdelek **kontakt** je ostal prazen, ker v besedilu ni bilo profesorjevega maila. Če mi ga pošlješ, ga dodam.
[Timestamp: 2026/10/26 18:02:34]

**user**: prof je janez demšar
[Timestamp: 2026/10/26 18:03:38]

**ai**: Pod kontakt v [[glavno programiranje]] sem dodal profesorja Janeza Demšarja in mail **janez.demsar@fri.uni-lj.si**. Mail sem sestavil po običajni obliki naslovov na FRI, nisem ga preveril, zato ga primerjaj z naslovom na učilnici.
[Timestamp: 2026/10/26 18:03:38]