        .global _start

        .text
        .org 0x00000000
_start:
        ldr r1, =stev1      @ r1 = naslov STEV1
        ldr r2, =stev2      @ r2 = naslov STEV2
        ldr r3, [r1]        @ r3 = vrednost STEV1
        ldr r4, [r2]        @ r4 = vrednost STEV2
        str r4, [r1]        @ STEV1 = vrednost iz r4
        str r3, [r2]        @ STEV2 = vrednost iz r3

        .data
stev1:  .word 0xBFF80000      @ -1.9375
stev2:  .word 0x420EC000      @ 35.6875