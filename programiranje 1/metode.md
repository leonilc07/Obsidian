**Metode nizov ne morejo spremeniti niza**, ker so nizi nespremenljivi. Vedno naredijo in vrnejo **nov niz** (ali število/seznam), original ostane enak. Če hočeš spremembo obdržati, rezultat shrani: `niz = niz.lower()`

## Trik: štetje z `bool`

```python
ovire = 0
for znak in vrstica:
	ovire += znak == "#"
return ovire
```

- `znak == "#"` vrne `True` ali `False`
- `bool` je podvrsta `int`: **`True == 1`, `False == 0`**
- prištevanje `True` poveča števec za 1, `False` ga ne spremeni → štetje brez `if`
- krajše: `sum(znak == "#" for znak in vrstica)` ali `vrstica.count("#")`

## Metode nizov

- `niz.lower()` / `niz.upper()`: vse v male / velike črke
	- `"PyThOn".lower()` → `"python"`
- `niz.count(pod)`: kolikokrat se `pod` pojavi (brez prekrivanja)
	- `"banana".count("a")` → `3`, `"banana".count("ana")` → `1`
- `niz.index(pod)`: indeks **prve** pojavitve, če je ni → **`ValueError`**
- `niz.find(pod)`: kot `index`, a če ne najde → **`-1`**
	- `"banana".find("n")` → `2`, `"banana".find("x")` → `-1`
	- **pazi:** `-1` je veljaven indeks (zadnji znak), zato preveri `if i != -1`
- `niz.rfind(pod)`: išče z desne → **zadnja** pojavitev, sicer `-1`
	- `"banana".rfind("a")` → `5`
- *(redko)* *`niz.center(širina, znak=" ")`: postavi niz na sredino polja dane širine*
	- *`"ab".center(6, "*")` → `"**ab**"`*
- *(redko)* *`niz.ljust(širina, znak)` / `niz.rjust(širina, znak)`: poravnava levo / desno, polnilo na drugo stran*
	- *`"ab".ljust(5, ".")` → `"ab..."`, `"ab".rjust(5, ".")` → `"...ab"`*
- `niz.strip()` / `lstrip()` / `rstrip()`: odstrani presledke, `\n`, `\t` z obeh strani / leve / desne
	- `"  hej\n".strip()` → `"hej"`
	- z argumentom odstrani **katerekoli** naštete znake, ne podniza: `"xxabyx".strip("xy")` → `"ab"`
- **`niz.split()` / `niz.split(",")`**: razbije niz v **seznam**
	- brez argumenta: deli po presledkih, prazne dele izpusti → `"  a   b ".split()` → `['a', 'b']`
	- z ločilom: deli točno po njem, prazne dele obdrži → `"a,,b".split(",")` → `['a', '', 'b']`
- `ločilo.join(seznam)`: obratno od `split`, **združi** elemente seznama v en niz, med njih vstavi ločilo
	- metodo kličeš na **ločilu**, ne na seznamu: `", ".join(["a", "b", "c"])` → `"a, b, c"`
	- **`"".join(tabela_nizov)`** → nize iz tabele zlepi skupaj brez ločila: `"".join(["a", "b", "c"])` → `"abc"`
		- uporabno, ko v zanki nabiraš dele v tabelo in jih na koncu združiš v en niz
	- `"-".join("abc")` → `"a-b-c"` (deluje na vsakem zaporedju nizov)
	- vsi elementi morajo biti **nizi**, sicer `TypeError`: `", ".join([1, 2])` ne dela → `", ".join(str(x) for x in [1, 2])` → `"1, 2"`
	- `" ".join(niz.split())` → odstrani odvečne presledke
- `niz.replace(staro, novo)`: vse pojavitve `staro` zamenja z `novo` in vrne **nov niz**, original ostane enak
	- `"banana".replace("a", "o")` → `"bonono"`
	- `s = "hej"; s.replace("h", "b")` → `s` je še vedno `"hej"`, zato shrani: `s = s.replace("h", "b")`
	- tretji argument omeji število zamenjav: `"banana".replace("a", "o", 1)` → `"bonana"`
	- brisanje znaka: `"a-b-c".replace("-", "")` → `"abc"`
	- odvečni presledki brez `split`/`join`: verižimo `replace` → `niz.replace("  ", " ").replace("  ", " ")...`
		- vsak klic dva presledka zamenja z enim, zato pri daljših nizih presledkov rabiš več klicev
		- zanesljivo: `while "  " in niz: niz = niz.replace("  ", " ")`
- `niz.endswith(konec)`: vrne **`True`/`False`**, ali se niz konča s `konec`
	- `"slika.png".endswith(".png")` → `True`, `"slika.png".endswith(".jpg")` → `False`
	- več možnosti hkrati s **terko**: `"slika.png".endswith((".png", ".jpg"))` → `True`
	- obratno za začetek: `niz.startswith(začetek)`
- metode **`is...`**: preverijo, ali niz izpolnjuje pogoj, in vrnejo **`True`/`False`**
	- npr. `niz.isnumeric()` → ali so vsi znaki števke: `"123".isnumeric()` → `True`, `"12a".isnumeric()` → `False`
	- **pazi:** `"-5"` in `"3.14"` vrneta `False` (minus in pika nista števki), prazen niz `""` tudi `False`
	- obstaja jih več (`isalpha`, `isupper`, `islower`, `isspace` ...), vse delujejo enako

## Metode seznamov

**Seznami so spremenljivi** → za razliko od nizov metode, kot sta `append` in `extend`, spremenijo **original** in vrnejo `None`. Zato **ne** piši `sez = sez.append(x)`, ker bo `sez` potem `None`.

- `sez.append(x)`: doda **en** element na konec seznama
	- `sez = [1, 2]; sez.append(3)` → `sez` je `[1, 2, 3]`
	- če dodaš seznam, se doda kot en element: `[1, 2].append([3, 4])` → `[1, 2, [3, 4]]`
- `len(sez)`: število elementov (to je **funkcija**, ne metoda, zato `len(sez)` in ne `sez.len()`)
	- `len([1, 2, 3])` → `3`, deluje tudi na nizih: `len("hej")` → `3`
- `sez.extend(seznam)`: dobi seznam stvari in **vsako** doda na konec seznama
	- `sez = [1, 2]; sez.extend([3, 4])` → `sez` je `[1, 2, 3, 4]`
	- enako kot `sez += [3, 4]`
- `sez.count(x)`: kolikokrat se `x` pojavi v seznamu
	- `[1, 2, 1, 1].count(1)` → `3`
- *(redko)* *`sez.index(x)`: indeks prve pojavitve `x`, če ga ni → `ValueError`*
	- *`[5, 7, 9].index(7)` → `1`*
	- seznami **nimajo `find`**, obstaja samo `index`
	- `index` se skoraj **nikoli ne uporablja**, ker se mu skoraj vedno lahko izogneš, npr. z **`enumerate`**, ki da indeks in element hkrati:
		- `for i, x in enumerate(sez):` → `i` je indeks, `x` element
- `sez.remove(x)`: odstrani **prvo** pojavitev vrednosti `x`, če je ni → `ValueError`
	- `sez = [3, 5, 3]; sez.remove(3)` → `sez` je `[5, 3]`
	- uporabi ga **samo, kadar ne veš, kje se stvar nahaja**, saj mora seznam preiskati od začetka; če indeks poznaš, uporabi `pop(i)`
- `sez.pop()`: odstrani **zadnji** element in ga **vrne**
	- `sez = [1, 2, 3]; x = sez.pop()` → `x` je `3`, `sez` je `[1, 2]`
	- lahko ga kličemo z **argumentom** (indeksom): `sez.pop(i)` odstrani in vrne element na mestu `i`
		- `sez = ["a", "b", "c"]; sez.pop(0)` → vrne `"a"`, `sez` je `["b", "c"]`
- `del tab[i]`: izbriše element na mestu `i` (to je **ukaz**, ne metoda, in **ne vrne** ničesar, za razliko od `pop`)
	- `tab = ["a", "b", "c", "d"]; del tab[1]` → `tab` je `["a", "c", "d"]`
	- **kaj se zgodi v tabeli:** element izgine, vsi elementi **za njim se premaknejo za eno mesto levo** in dobijo indeks manjši za 1, dolžina se zmanjša za 1
		- prej: `"c"` na indeksu `2`, `"d"` na `3` → potem: `"c"` na `1`, `"d"` na `2`
		- zato brisanje blizu začetka dolge tabele traja dlje (premakniti mora vse za njim)
		- **pazi** pri brisanju v zanki po indeksih: po `del` se indeksi zamaknejo, zato lahko kakšen element preskočiš
- `tab.reverse()`: obrne vrstni red elementov **v originalu**, vrne `None`
	- `tab = [1, 2, 3]; tab.reverse()` → `tab` je `[3, 2, 1]`
	- **razlika s `tab[::-1]`:**
		- `tab.reverse()` spremeni **originalno** tabelo, nič ne vrne
		- `tab[::-1]` naredi **novo** obrnjeno tabelo, original ostane enak → `obrnjena = tab[::-1]`
		- `[::-1]` deluje tudi na nizih (`"hej"[::-1]` → `"jeh"`), `reverse()` pa samo na seznamih, ker nizov ni mogoče spreminjati
- **`tab.sort()`**: uredi tabelo **v originalu** od najmanjšega do največjega, vrne `None` → to se bo uporabljalo **največ**
	- `tab = [3, 1, 2]; tab.sort()` → `tab` je `[1, 2, 3]`
	- nize uredi po abecedi: `["c", "a", "b"]` → `["a", "b", "c"]`
	- obratno (od največjega): `tab.sort(reverse=True)` → `[3, 2, 1]`
	- **pazi:** `tab = tab.sort()` → `tab` je `None`
- `sorted(tab)`: naredi **novo** urejeno tabelo, original ostane enak
	- to je **funkcija**, ne metoda (kot `len`), zato `sorted(tab)` in **ne** `tab.sorted()`, ki ne obstaja
	- `tab = [3, 1, 2]; urejena = sorted(tab)` → `urejena` je `[1, 2, 3]`, `tab` je še vedno `[3, 1, 2]`
	- tudi tu obratno: `sorted(tab, reverse=True)` → `[3, 2, 1]`
	- deluje na **vsem**, čez kar lahko greš z zanko, tudi na nizih, a vedno vrne **seznam**: `sorted("cab")` → `['a', 'b', 'c']`
		- nazaj v niz: `"".join(sorted("cab"))` → `"abc"`
	- razlika s `sort` je enaka kot med `[::-1]` in `reverse()`: `sorted` → nova tabela, `sort` → spremeni original
