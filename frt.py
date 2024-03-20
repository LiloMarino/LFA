from classes.alfabeto import Alfabeto

ITER = 3
binario = Alfabeto("01")
generator = binario.frt(ITER)
for palavra in generator:
    print(palavra, end=" ")
print()
generator = binario.fr(ITER - 1)
for palavra in generator:
    print(palavra, end=" ")
