## Kvadratna enačba – ponovitev
Splošna oblika: $ax^2 + bx + c = 0$
### Diskriminanta
$D = b^2 - 4ac$
$x_{1,2} = \dfrac{-b \pm \sqrt{D}}{2a}$
- $D > 0$ → 2 rešitvi
- $D = 0$ → 1 (dvojna) rešitev
- $D < 0$ → ni realnih rešitev
### Vietovo pravilo
$x_1 + x_2 = -\dfrac{b}{a}$
$x_1 \cdot x_2 = \dfrac{c}{a}$
Za $a = 1$ ($x^2 + bx + c = 0$) iščemo števili, katerih **vsota je $-b$** in **produkt $c$**:
$x^2 + bx + c = (x - x_1)(x - x_2)$
### Primer
$x^2 + 2x - 8 = 0$
**Z diskriminanto:**
$D = 2^2 - 4 \cdot 1 \cdot (-8) = 4 + 32 = 36$
$x_{1,2} = \dfrac{-2 \pm 6}{2} \Rightarrow x_1 = 2,\; x_2 = -4$
**Z Vietom:**
$x_1 + x_2 = -2$, $x_1 \cdot x_2 = -8 \Rightarrow 2$ in $-4$
$x^2 + 2x - 8 = (x - 2)(x + 4)$

### Hornerjev algoritem
Deljenje polinoma z $(x - a)$ in iskanje ničel.
- kandidati za cele ničle so delitelji prostega člena $c$
- prvi koeficient prepišemo, nato: pomnoži z $a$ → prištej naslednjemu koeficientu
- če je zadnje število (ostanek) $0$, je $a$ ničla

**Primer:** $x^3 - 6x^2 + 11x - 6 = 0$, poskusimo $a = 1$
```
   |  1   -6   11   -6
 1 |       1   -5    6
   |  1   -5    6  | 0
```
Ostanek $0$ → $x_1 = 1$
$x^3 - 6x^2 + 11x - 6 = (x - 1)(x^2 - 5x + 6) = (x-1)(x-2)(x-3)$
$x_1 = 1,\; x_2 = 2,\; x_3 = 3$

### Absolutna vrednost
$$|x| = \begin{cases} x, & x \geq 0 \\ -x, & x < 0 \end{cases}$$

$$|x+1| = \begin{cases} x+1, & x \geq -1 \\ -(x+1) = -x-1, & x < -1 \end{cases}$$

**Primer:** $2|x+1| = x+2$

**1. primer:** $x + 1 \geq 0 \Rightarrow x \geq -1$
$2(x + 1) = x + 2$
$2x + 2 = x + 2$
$x = 0$
$0 \geq -1$ ✓ → rešitev velja

**2. primer:** $x + 1 < 0 \Rightarrow x < -1$
$-2(x+1) = x + 2$
$-2x - 2 = x + 2$
$-3x = 4 \Rightarrow x = -\frac{4}{3}$
$-\frac{4}{3} < -1$ ✓ → rešitev velja

**Rešitev:** $x_1 = 0,\; x_2 = -\frac{4}{3}$
### Neenačba
**Primer:** $x > \frac{1}{x}$, $x \neq 0$
Pomnožimo z $x$ → ker ne vemo predznaka $x$, ločimo dva primera (pri $x < 0$ se znak obrne).

**1. primer:** $x > 0$
$x^2 > 1 \Rightarrow x > 1$ ali $x < -1$
skupaj z $x > 0$ → $x > 1$

**2. primer:** $x < 0$ (znak se obrne)
$x^2 < 1 \Rightarrow -1 < x < 1$
skupaj z $x < 0$ → $-1 < x < 0$

**Rešitev:** $x \in (-1, 0) \cup (1, \infty)$

> [!note] Opombe
> - unijo intervalov pišemo vedno **od negativnih proti pozitivnim** (od leve proti desni po številski premici)
> - parabola $ax^2 + bx + c$ je obrnjena glede na prvi člen $a$:
> 	- $a > 0$ → odprta navzgor (kot **U**)
> 	- $a < 0$ → odprta navzdol (obrnjen **∩**)


### Trigonometrična neenačba
**Primer:** $\sin x > \frac{1}{2}$

$\sin x = \frac{1}{2} \Rightarrow x = \frac{\pi}{6}$ ali $x = \frac{5\pi}{6}$
Na enotskem krogu iščemo točke, ki so **nad** premico $y = \frac{1}{2}$ (rdeči lok).

![[sinx_vecje_pol.svg|280]]

**Rešitev:** $x \in \left(\frac{\pi}{6} + 2k\pi,\; \frac{5\pi}{6} + 2k\pi\right),\; k \in \mathbb{Z}$

### Sistem dveh enačb
**Primer:** $\tan\alpha = 2$, $\alpha$ je ostri kot. $\sin\alpha = ?$, $\cos\alpha = ?$

$\sin^2\alpha + \cos^2\alpha = 1$
$\dfrac{\sin\alpha}{\cos\alpha} = 2 \Rightarrow \sin\alpha = 2\cos\alpha$

Vstavimo v prvo enačbo:
$(2\cos\alpha)^2 + \cos^2\alpha = 1$
$5\cos^2\alpha = 1 \Rightarrow \cos^2\alpha = \frac{1}{5}$
$\alpha$ je ostri kot → $\cos\alpha > 0$, $\sin\alpha > 0$

**Rešitev:**
$\cos\alpha = \frac{1}{\sqrt{5}} = \frac{\sqrt{5}}{5}$
$\sin\alpha = 2\cos\alpha = \frac{2\sqrt{5}}{5}$

**Predznaki po kvadrantih** (II | I zgoraj, III | IV spodaj):
```
   sin        cos        tan
 + | +      - | +      - | +
---+---    ---+---    ---+---
 - | -      - | +      + | -
```
Ostri kot = I. kvadrant → vse $+$
