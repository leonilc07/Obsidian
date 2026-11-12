# Množice
## relacija pripadnosti
**Relacija pripadnosti** $x \in A$ beremo „$x$ pripada $A$“ ($x$ je element množice $A$).
- $x \notin A$ pomeni $\neg(x \in A)$, torej $x$ ni element $A$

## podajanje množic
Množice lahko podamo na dva načina:
- z **naštevanjem elementov**: $A = \{0, 1, 2\}$
- z neko **izjavno formulo**: $A = \{x \,;\, \varphi(x)\}$

Pri podajanju s formulo velja:
$$x \in A \iff \varphi(x)$$
Element je v množici natanko takrat, ko je zanj formula $\varphi$ resnična. $\varphi(x)$ je torej enomestni predikat, ki pove, katere elemente vzamemo.

Zgledi:
- $A = \{x \,;\, x \neq x\} = \emptyset$, **prazna množica**: noben $x$ ni različen od samega sebe, formula je vedno 0, zato množica nima elementov
- $B = \{x \,;\, x = 0 \lor x = 1 \lor x = 2\} = \{0, 1, 2\}$: isto množico lahko podamo z naštevanjem ali s formulo
- $C = \{x \,;\, x^2 + 1 \geq 5\}$: če so to realna števila, je $C$ množica vseh $x$, za katere velja $x \leq -2$ ali $x \geq 2$. Te množice ne moremo podati z naštevanjem, ker je neskončna.

## Russellov paradoks
**Ni vsaka izjavna formula dobra!** Vzemimo
$$R = \{x \,;\, x \notin x\}$$
torej množico vseh množic, ki niso element same sebe. Ali velja $R \in R$?
- če $R \in R$, potem $R$ izpolnjuje pogoj $x \notin x$, torej $R \notin R$, **protislovje**
- če $R \notin R$, potem $R$ izpolnjuje pogoj $x \notin x$, torej mora biti $R \in R$, **protislovje**

Obe možnosti vodita v protislovje, zato $R$ ni množica. Pri podajanju s formulo ne smemo vzeti kar katerekoli formule.

**Primer s knjižnico:** v knjižnici so katalogi, ki naštevajo knjige in druge kataloge. Nekateri katalogi navajajo tudi sami sebe, drugi ne. Knjižničar bi rad naredil katalog $K$, ki našteva **natanko vse kataloge, ki ne navajajo sami sebe**.

**Predpostavimo**, da tak katalog $K$ obstaja. Potem mora $K$ bodisi navajati samega sebe bodisi ne:
- $K$ navaja sebe: potem je $K$ katalog, ki navaja sam sebe, takih pa $K$ ne sme navajati. $K$ torej sebe ne navaja, **protislovje**
- $K$ ne navaja sebe: potem je $K$ katalog, ki ne navaja sam sebe, vse take pa mora $K$ navajati. $K$ torej sebe navaja, **protislovje**

V obeh primerih pridemo v protislovje, torej je bila predpostavka napačna: **takega kataloga ni mogoče narediti**. Enako je z $R$: ko vprašamo, ali je $R \in R$, smo že predpostavili, da $R$ obstaja kot množica, in ta predpostavka vodi v protislovje.

## enakost in vsebovanost
Množici $A$ in $B$ sta **enaki**:
$$A = B \iff \forall x\, (x \in A \Leftrightarrow x \in B)$$
- množici sta enaki, ko imata **iste elemente**, vrstni red in ponavljanje nista pomembna: $\{0, 1, 2\} = \{2, 0, 1\}$

Množica $A$ je **podmnožica** množice $B$ (relacija **inkluzije**):
$$A \subseteq B \iff \forall x\, (x \in A \Rightarrow x \in B)$$
- vsak element $A$ je tudi element $B$

Množica $A$ je **prava podmnožica** množice $B$ (relacija **stroge inkluzije**):
$$A \subset B \iff A \subseteq B \land A \neq B$$
- $A$ je vsebovana v $B$, $B$ pa ima vsaj en element, ki ga $A$ nima

**Dokaz, da je $A = B$:** ekvivalenco $x \in A \Leftrightarrow x \in B$ razdelimo na dve implikaciji, zato pokažemo:
- $A \subseteq B$: vsak element $A$ je v $B$
- $B \subseteq A$: vsak element $B$ je v $A$

$$A = B \iff A \subseteq B \land B \subseteq A$$

**Trditev:** za poljubne množice $A$, $B$ in $C$ velja
- $\emptyset \subseteq A$: izjava $x \in \emptyset$ je vedno 0, implikacija z neresnično predpostavko pa je vedno 1
- $A \subseteq A$: $x \in A \Rightarrow x \in A$ je tavtologija
- če $A \subseteq B$ in $B \subseteq C$, potem $A \subseteq C$: iz $x \in A \Rightarrow x \in B$ in $x \in B \Rightarrow x \in C$ sledi $x \in A \Rightarrow x \in C$

# Operacije z množicami
Vsaka operacija je definirana z izjavnim veznikom med $x \in A$ in $x \in B$:
- **unija** $A \cup B = \{x \,;\, x \in A \lor x \in B\}$: elementi, ki so v $A$ **ali** v $B$
- **presek** $A \cap B = \{x \,;\, x \in A \land x \in B\}$: elementi, ki so v $A$ **in** v $B$
- **razlika** $A \setminus B = \{x \,;\, x \in A \land x \notin B\}$: elementi $A$, ki niso v $B$
- **simetrična razlika** $A + B = \{x \,;\, x \in A \veebar x \in B\}$: elementi, ki so v **natanko eni** od množic

![[Operacije z množicami.excalidraw]]

## lastnosti operacij
$\Rightarrow$ beremo „če …, potem …“ (velja samo v eno smer), $\iff$ pa „natanko takrat, ko“ (velja v obe smeri). $A \subseteq B$ beremo „$A$ je podmnožica $B$“.

**1.** $A = B \iff A \subseteq B \land B \subseteq A$
- beremo: $A$ je enaka $B$ natanko takrat, ko je $A$ podmnožica $B$ in $B$ podmnožica $A$
- zakaj: to smo pokazali pri enakosti
- primer: $A = \{1, 2\}$, $B = \{2, 1\}$: vsak element $A$ je v $B$ in obratno, zato $A = B$
- primer: $A = \{1, 2\}$, $B = \{1, 2, 3\}$: $A \subseteq B$, ampak $B \not\subseteq A$ (zaradi 3), zato $A \neq B$

**2.** $A \subseteq B \Rightarrow A \cup C \subseteq B \cup C$
- beremo: če je $A$ podmnožica $B$, potem je unija $A$ in $C$ podmnožica unije $B$ in $C$
- zakaj: če je $x \in A \cup C$, je $x \in A$ (in zato $x \in B$) ali $x \in C$, v obeh primerih je $x \in B \cup C$
- primer: $A = \{1, 2\}$, $B = \{1, 2, 3\}$, $C = \{2, 3, 4\}$: $A \cup C = \{1, 2, 3, 4\} \subseteq \{1, 2, 3, 4\} = B \cup C$

**3.** $A \subseteq B \Rightarrow A \cap C \subseteq B \cap C$
- beremo: če je $A$ podmnožica $B$, potem je presek $A$ in $C$ podmnožica preseka $B$ in $C$
- zakaj: če je $x \in A$ in $x \in C$, je tudi $x \in B$ in $x \in C$
- primer: $A = \{1, 2\}$, $B = \{1, 2, 3\}$, $C = \{2, 3, 4\}$: $A \cap C = \{2\} \subseteq \{2, 3\} = B \cap C$

**4.** $A \cap B \subseteq A \subseteq A \cup B$
- beremo: presek $A$ in $B$ je podmnožica $A$, $A$ pa je podmnožica unije $A$ in $B$
- zakaj: sledi iz $p \land q \Rightarrow p$ in $p \Rightarrow p \lor q$
- primer: $A = \{1, 2\}$, $B = \{2, 3\}$: $A \cap B = \{2\} \subseteq \{1, 2\} \subseteq \{1, 2, 3\} = A \cup B$

Množici $A$ in $B$ sta **disjunktni**, če je $A \cap B = \emptyset$, torej nimata skupnih elementov.
- primer: $\{1, 2\}$ in $\{3, 4\}$ sta disjunktni, $\{1, 2\}$ in $\{2, 3\}$ pa ne

# Univerzalna množica in komplement
**Univerzalna množica**, označimo jo z $S$, ustreza **področju pogovora** v predikatnem računu.
- **vse** obravnavane množice so vsebovane v univerzalni množici $S$

**Komplement** množice $A$, označimo ga z $A^c$, definiramo kot
$$A^c = S \setminus A$$
To so vsi elementi iz $S$, ki niso v $A$. Ker so vsi $x$ iz $S$, velja $x \in A^c \iff x \notin A$, zato komplement ustreza **negaciji**.
- primer: $S = \{1, 2, 3, 4, 5, 6\}$, $A = \{1, 2\}$, potem je $A^c = \{3, 4, 5, 6\}$

![[Komplement množice.excalidraw]]

## lastnosti komplementa
V primerih je $S = \{1, 2, 3, 4, 5, 6\}$.

**1.** $(A^c)^c = A$
- beremo: komplement komplementa $A$ je $A$
- zakaj: $\neg \neg p \sim p$
- primer: $A = \{1, 2\}$, $A^c = \{3, 4, 5, 6\}$, $(A^c)^c = \{1, 2\} = A$

**2.** $(A \cup B)^c = A^c \cap B^c$
- beremo: komplement unije je presek komplementov
- zakaj: $\neg (p \lor q) \sim \neg p \land \neg q$ (De Morgan)
- primer: $A = \{1, 2\}$, $B = \{2, 3\}$: $(A \cup B)^c = \{1, 2, 3\}^c = \{4, 5, 6\}$ in $A^c \cap B^c = \{3, 4, 5, 6\} \cap \{1, 4, 5, 6\} = \{4, 5, 6\}$

**3.** $(A \cap B)^c = A^c \cup B^c$
- beremo: komplement preseka je unija komplementov
- zakaj: $\neg (p \land q) \sim \neg p \lor \neg q$ (De Morgan)
- primer: $A = \{1, 2\}$, $B = \{2, 3\}$: $(A \cap B)^c = \{2\}^c = \{1, 3, 4, 5, 6\}$ in $A^c \cup B^c = \{3, 4, 5, 6\} \cup \{1, 4, 5, 6\} = \{1, 3, 4, 5, 6\}$

**4.** $A \setminus B = A \cap B^c$
- beremo: razlika $A$ in $B$ je presek $A$ s komplementom $B$
- zakaj: $x \notin B$ pomeni isto kot $x \in B^c$
- primer: $A = \{1, 2\}$, $B = \{2, 3\}$: $A \setminus B = \{1\}$ in $A \cap B^c = \{1, 2\} \cap \{1, 4, 5, 6\} = \{1\}$

**5.** $A \subseteq B \Rightarrow B^c \subseteq A^c$
- beremo: če je $A$ podmnožica $B$, potem je komplement $B$ podmnožica komplementa $A$ (večja množica ima manjši komplement)
- zakaj: kontrapozicija, $x \in A \Rightarrow x \in B$ je enakovredno $x \notin B \Rightarrow x \notin A$
- primer: $A = \{1, 2\}$, $B = \{1, 2, 3\}$: $B^c = \{4, 5, 6\} \subseteq \{3, 4, 5, 6\} = A^c$

**6.** $A \cap B = \emptyset \iff A \subseteq B^c \iff B \subseteq A^c$
- beremo: $A$ in $B$ sta disjunktni natanko takrat, ko je $A$ vsebovana v komplementu $B$, in natanko takrat, ko je $B$ vsebovana v komplementu $A$
- zakaj: če nimata skupnih elementov, noben element $A$ ni v $B$, torej je v $B^c$ (in obratno za $B$)
- primer: $A = \{1, 2\}$, $B = \{4, 5\}$: $A \cap B = \emptyset$, $A \subseteq \{1, 2, 3, 6\} = B^c$, $B \subseteq \{3, 4, 5, 6\} = A^c$

# Enakosti z množicami
**Pokažimo, da velja** $A \cup (A \cap B) = A$.

Dokaz: označimo $a$: $x \in A$ in $b$: $x \in B$.
$$
\begin{aligned}
x \in A \cup (A \cap B) &\iff x \in A \lor x \in A \cap B && \text{definicija unije} \\
&\iff x \in A \lor (x \in A \land x \in B) && \text{definicija preseka} \\
&\iff a \lor (a \land b) \\
&\iff a && \text{absorpcija} \\
&\iff x \in A
\end{aligned}
$$

Tej lastnosti pravimo **absorpcija**. Operacije z množicami pravzaprav **podedujejo** ustrezne lastnosti izjavnih veznikov: $\cup$ se obnaša kot $\lor$, $\cap$ kot $\land$, $^c$ kot $\neg$ in $+$ kot $\veebar$.

**Pravila prednosti** (od najmočnejše do najšibkejše):
1. komplement $^c$
2. presek $\cap$, razlika $\setminus$
3. unija $\cup$, seštevanje $+$

Podobno kot pri veznikih, kjer $\neg$ veže močneje od $\land$, ta pa močneje od $\lor$. Npr. $A \cup B \cap C^c$ pomeni $A \cup (B \cap (C^c))$.

## seznam enakosti
1. **Zakon dvojnega komplementa:** $(A^c)^c = A$
2. **Idempotenca:** $A \cap A = A$, $A \cup A = A$
3. **Komutativnost:** $A \cap B = B \cap A$, $A \cup B = B \cup A$, $A + B = B + A$
4. **Asociativnost:**
   - $(A \cap B) \cap C = A \cap (B \cap C)$
   - $(A \cup B) \cup C = A \cup (B \cup C)$
   - $(A + B) + C = A + (B + C)$
5. **Absorpcija:** $A \cap (A \cup B) = A$, $A \cup (A \cap B) = A$
6. **Distributivnost:**
   - $(A \cap B) \cup C = (A \cup C) \cap (B \cup C)$
   - $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$
   - $(A + B) \cap C = (A \cap C) + (B \cap C)$
7. **De Morganova zakona:** $(A \cup B)^c = A^c \cap B^c$, $(A \cap B)^c = A^c \cup B^c$
8. **Kontrapozicija:** $A \subseteq B \sim B^c \subseteq A^c$
9. **Lastnosti prazne množice $\emptyset$ in univerzalne množice $S$:**
   - $A \cup A^c = S$, $A \cap A^c = \emptyset$
   - $A + A = \emptyset$, $A + A^c = S$
10. **Še lastnosti $\emptyset$ in $S$:**
    - $A \cap \emptyset = \emptyset$, $A \cup \emptyset = A$
    - $A \cap S = A$, $A \cup S = S$
11. **Lastnosti vsebovanosti** (**to moraš znati še v spanju**):
    - $A \subseteq B \sim A \cup B = B \sim A \cap B = A \sim A \setminus B = \emptyset$
    - če $A \subseteq B$, potem $A \cup C \subseteq B \cup C$
    - če $A \subseteq B$, potem $A \cap C \subseteq B \cap C$
    - $A \cap B \subseteq A$, $B \subseteq A \cup B$
12. **Lastnosti razlike množic:** $A \setminus B = A \cap B^c$
13. **Lastnosti simetrične razlike:**
    - $A + B = (A \setminus B) \cup (B \setminus A)$
    - $A + B = (A \cup B) \setminus (A \cap B)$

## dokazi lastnosti vsebovanosti
**$A \subseteq B \sim A \cup B = B$**

Denimo, da je $A \subseteq B$:
$$B \subseteq A \cup B \subseteq B \cup B = B$$
- prvi $\subseteq$: $B$ je vedno vsebovana v uniji z $B$
- drugi $\subseteq$: iz $A \subseteq B$ sledi $A \cup B \subseteq B \cup B$ (lastnost operacij 2, $C = B$)
- $B \cup B = B$ (idempotenca)

$B$ je torej hkrati podmnožica in nadmnožica $A \cup B$, zato $A \cup B = B$. To je ena smer.

Denimo, da je $A \cup B = B$:
$$A \subseteq A \cup B = B$$
torej $A \subseteq B$. To je druga smer.

**$A \subseteq B \sim A \cap B = A$**

Denimo, da je $A \subseteq B$: $A = A \cap A \subseteq A \cap B \subseteq A$ (idempotenca in lastnost operacij 3, $C = A$), zato $A \cap B = A$.

Denimo, da je $A \cap B = A$: $A = A \cap B \subseteq B$, torej $A \subseteq B$.

**$A \subseteq B \sim A \setminus B = \emptyset$**

Denimo, da je $A \subseteq B$:
$$A \setminus B = A \cap B^c \subseteq B \cap B^c = \emptyset$$
- $A \setminus B = A \cap B^c$ (lastnost 12)
- $A \cap B^c \subseteq B \cap B^c$, ker je $A \subseteq B$ (lastnost operacij 3, $C = B^c$)
- $B \cap B^c = \emptyset$ (lastnost 9)

Edina podmnožica $\emptyset$ je $\emptyset$, zato $A \setminus B = \emptyset$.

Denimo, da je $A \setminus B = \emptyset$:
$$
\begin{aligned}
B &= \emptyset \cup B = (A \setminus B) \cup B && \text{predpostavka} \\
&= (A \cap B^c) \cup B && \text{lastnost 12} \\
&= (A \cup B) \cap (B^c \cup B) && \text{distributivnost} \\
&= (A \cup B) \cap S = A \cup B && B^c \cup B = S
\end{aligned}
$$
Dobili smo $A \cup B = B$, iz prvega dokaza pa sledi $A \subseteq B$.

# Potenčna množica
**Potenčna množica** množice $A$, $\mathcal{P}A$, je množica **vseh podmnožic** množice $A$.
$$\mathcal{P}A = \{B \,;\, B \subseteq A\}$$
Tako $\emptyset$ kot $A$ pripadata potenčni množici $\mathcal{P}A$, ker je $\emptyset \subseteq A$ in $A \subseteq A$.

Elementi $\mathcal{P}A$ so **množice**, ne elementi $A$: $\{1\} \in \mathcal{P}\{1, 2\}$, ampak $1 \notin \mathcal{P}\{1, 2\}$.

## primer
$$\mathcal{P}\{1, 2, 3\} = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$$
- podmnožici z enim elementom (npr. $\{1\}$) pravimo **singleton** (enojec)
- podmnožici z dvema elementoma (npr. $\{1, 2\}$) pravimo **par**

Vse podmnožice dobimo sistematično s tabelo: za vsak element povemo, ali je v podmnožici (1) ali ne (0). To je kot pravilnostna tabela s tremi spremenljivkami.

| 1   | 2   | 3   | podmnožica      |
| --- | --- | --- | --------------- |
| 0   | 0   | 0   | $\emptyset$     |
| 0   | 0   | 1   | $\{3\}$         |
| 0   | 1   | 0   | $\{2\}$         |
| 0   | 1   | 1   | $\{2, 3\}$      |
| 1   | 0   | 0   | $\{1\}$         |
| 1   | 0   | 1   | $\{1, 3\}$      |
| 1   | 1   | 0   | $\{1, 2\}$      |
| 1   | 1   | 1   | $\{1, 2, 3\}$   |

Če ima $A$ $n$ elementov, potem ima $\mathcal{P}A$ $2^n$ elementov (torej ima $A$ $2^n$ podmnožic). Za vsak element sta dve možnosti (je ali ni v podmnožici), tabela ima zato $2^n$ vrstic.

## zgledi
- $\mathcal{P}\emptyset = \{\emptyset\}$: edina podmnožica prazne množice je $\emptyset$, zato ima $\mathcal{P}\emptyset$ en element ($2^0 = 1$)
- $\mathcal{P}\{\emptyset\} = \{\emptyset, \{\emptyset\}\}$: $\{\emptyset\}$ ima en element (to je $\emptyset$), zato ima dve podmnožici ($2^1 = 2$)
- $\mathcal{P}\{a\} = \{\emptyset, \{a\}\}$: enako kot prej, le da je element $a$

**Trditev:** če je $A \subseteq B$, potem je $\mathcal{P}A \subseteq \mathcal{P}B$.
- beremo: če je $A$ podmnožica $B$, potem je vsaka podmnožica $A$ tudi podmnožica $B$
- zakaj: če je $C \in \mathcal{P}A$, je $C \subseteq A \subseteq B$, torej $C \subseteq B$ in $C \in \mathcal{P}B$
- primer: $A = \{1\}$, $B = \{1, 2\}$: $\mathcal{P}A = \{\emptyset, \{1\}\} \subseteq \{\emptyset, \{1\}, \{2\}, \{1, 2\}\} = \mathcal{P}B$

# Družine množic
Naj bo
$$\mathcal{A} = \{A_1, A_2, A_3, \dots\} = \{A_i \,;\, i \in \mathcal{I}\}$$
**družina množic** (množica, katere elementi so množice). Z $\mathcal{I}$ označimo **indeksno množico**, torej množico vseh indeksov $i$.

**Unija družine** $\mathcal{A}$ je množica
$$\bigcup \mathcal{A} = \bigcup_{i \in \mathcal{I}} A_i = \{x \,;\, \exists i\, (i \in \mathcal{I} \land x \in A_i)\}$$
- $x$ je v uniji, če je v **vsaj eni** od množic $A_i$

**Presek družine** $\mathcal{A}$ je množica
$$\bigcap \mathcal{A} = \bigcap_{i \in \mathcal{I}} A_i = \{x \,;\, \forall i\, (i \in \mathcal{I} \Rightarrow x \in A_i)\}$$
- $x$ je v preseku, če je v **vseh** množicah $A_i$
- tudi tu gre $\exists$ s konjunkcijo, $\forall$ pa z implikacijo, kot pri formalizaciji

## intervali
V zgledih uporabljamo intervale realnih števil:
- $[a, b] = \{x \in \mathbb{R} \,;\, a \leq x \leq b\}$, zaprti interval (krajišči sta vključeni)
- $(a, b) = \{x \in \mathbb{R} \,;\, a < x < b\}$, odprti interval (krajišči nista vključeni)
- $(a, \infty) = \{x \in \mathbb{R} \,;\, a < x\}$

## zgledi
**$A_i = [i, i + 1]$, $i \in \mathbb{Z}$**
- $\bigcup_i A_i = \mathbb{R}$: vsako realno število leži med dvema zaporednima celima številoma
- $\bigcap_i A_i = \emptyset$: nobeno število ni v vseh intervalih hkrati (npr. $A_0 \cap A_5 = \emptyset$)

**$A_i = [i, i + 1)$, $i \in \mathbb{Z}$**
- $\bigcup_i A_i = \mathbb{R}$, $\bigcap_i A_i = \emptyset$, enako kot prej
- razlika je v tem, da se sosednja intervala ne prekrivata več: pri $[i, i+1]$ je število $i + 1$ v $A_i$ in v $A_{i+1}$, pri $[i, i+1)$ pa samo v $A_{i+1}$

![[Intervali pokritje razbitje.excalidraw]]

**$B_i = (i, \infty)$, $i \in \mathbb{N}$**
- $\bigcup_i B_i = B_0 = (0, \infty)$: intervali so vedno manjši ($B_0 \supseteq B_1 \supseteq B_2 \supseteq \dots$), zato je unija kar največji, $B_0$
- $\bigcap_i B_i = \emptyset$: za vsako število $x$ obstaja $i \geq x$, in potem $x \notin B_i$

**$C_i = [2^{-i}, \infty)$, $i \in \mathbb{N}$**
- $\bigcup_i C_i = (0, \infty)$: $2^{-i}$ ($1, \frac{1}{2}, \frac{1}{4}, \dots$) se približuje 0, a je nikoli ne doseže, zato je vsako pozitivno število v nekem $C_i$, 0 pa v nobenem
- $\bigcap_i C_i = [1, \infty)$: intervali so vedno večji ($C_0 \subseteq C_1 \subseteq \dots$), zato je presek najmanjši, $C_0 = [1, \infty)$

# Pokritje in razbitje
Družina množic $\mathcal{A} = \{A_i \,;\, i \in \mathcal{I}\}$ je **pokritje** množice $B$, če je $B = \bigcup_{i \in \mathcal{I}} A_i$.
- množice skupaj pokrijejo celo $B$, lahko se tudi prekrivajo

Družina množic $\mathcal{A} = \{A_i \,;\, i \in \mathcal{I}\}$ je **razbitje** množice $B$, če:
- $\mathcal{A}$ pokrije množico $B$
- elementi $\mathcal{A}$ so **neprazni** in
- elementi $\mathcal{A}$ so **paroma disjunktni** (vsaki dve različni množici iz $\mathcal{A}$ sta disjunktni)

Pri razbitju je torej vsak element $B$ v **natanko eni** množici iz $\mathcal{A}$.

Na kratko: oboje pomeni, da $B$ razdelimo na kose (manjše množice).
- **pokritje**: vsak element je v **vsaj enem** kosu, kosi se lahko prekrivajo
- **razbitje**: vsak element je v **natanko enem** kosu, kosi se ne prekrivajo in noben ni prazen

**Primer iz življenja:** razred $B = \{\text{Ana}, \text{Bor}, \text{Cene}, \text{Dan}\}$
- **krožki** (pokritje): Ana in Bor sta pri šahu, Bor, Cene in Dan pri nogometu: $\{\{\text{Ana}, \text{Bor}\}, \{\text{Bor}, \text{Cene}, \text{Dan}\}\}$. Vsak je v vsaj enem krožku, Bor celo v dveh, kar je dovoljeno.
- **ekipe na tekmi** (razbitje): rdeča ekipa Ana in Bor, modra Cene in Dan: $\{\{\text{Ana}, \text{Bor}\}, \{\text{Cene}, \text{Dan}\}\}$. Vsak je v natanko eni ekipi, nobena ekipa ni prazna.
- **ni niti pokritje**: če so v ekipah samo Ana, Bor in Cene, Dan pa nikjer, ekipe ne pokrijejo celega razreda

Še ena primerjava: narezana pica je razbitje (vsak košček je v natanko enem kosu), prtički, ki se na mizi malo prekrivajo, pa so pokritje.

**Zakaj kos ne sme biti prazen:** $\emptyset$ ne vsebuje nobenega elementa, zato pri delitvi nič ne prispeva. Ker je disjunktna z vsemi množicami, bi jo sicer lahko dodali kolikorkrat bi hoteli.

Primeri za $B = \{1, 2, 3, 4\}$:
- $\{\{1, 2\}, \{3, 4\}\}$ je razbitje
- $\{\{1, 2\}, \{2, 3, 4\}\}$ je pokritje, ni pa razbitje, ker je 2 v obeh množicah

Primeri za $\mathbb{R}$ (iz zgledov zgoraj):
- $\{[i, i + 1] \,;\, i \in \mathbb{Z}\}$ je pokritje $\mathbb{R}$, ni pa razbitje, ker imata sosednja intervala skupno krajišče
- $\{[i, i + 1) \,;\, i \in \mathbb{Z}\}$ je razbitje $\mathbb{R}$

