from classes.alfabeto import Alfabeto
from classes.palavra import Palavra

# Alfabeto
alfa = Alfabeto("0123456789")
print(alfa)

# Cadeia vazia
vazia = Palavra(alfa)
print(vazia, len(vazia))

# Cadeia arbitrária
cadeia_arbitraria = Palavra(alfa, "12345")
print(cadeia_arbitraria, len(cadeia_arbitraria))

# Concatenação
concatenada = cadeia_arbitraria + "2"
print(concatenada, len(concatenada))

# Associativa
palavra1 = Palavra(alfa, "123")
palavra2 = Palavra(alfa, "456")
soma1 = palavra1 + (palavra2 + "2")
soma2 = (palavra1 + palavra2) + "2"
print(soma1, "=", soma2, soma1 == soma2)

# Elemento neutro
print(
    palavra1 + vazia,
    "=",
    vazia + palavra1,
    "=",
    palavra1,
    palavra1 + vazia == vazia + palavra1 == palavra1,
)

# Não comutativo
print(
    palavra1 + palavra2,
    "!=",
    palavra2 + palavra1,
    palavra1 + palavra2 != palavra2 + palavra1,
)

# Concatenação Sucessiva
# Caso A
print(palavra1**0)
print(palavra1**2)

# Caso B
print(vazia**2)
print(vazia**0)
