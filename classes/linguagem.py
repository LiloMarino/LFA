from classes.alfabeto import Alfabeto
from classes.sintaxe import Sintaxe
from classes.vocabulario import Vocabulario


class Linguagem:
    def __init__(
        self,
        vocabulario: Vocabulario,
        alfabeto: Alfabeto,
        sintaxe: Sintaxe,
        simbolo_inicial: str,
    ) -> None:
        assert isinstance(
            vocabulario, Vocabulario
        ), "vocabulario deve ser uma instância de Vocabulario"
        assert isinstance(
            alfabeto, Alfabeto
        ), "alfabeto deve ser uma instância de Alfabeto"
        assert isinstance(sintaxe, Sintaxe), "sintaxe deve ser uma instância de Sintaxe"
        assert (
            isinstance(simbolo_inicial, str) and len(simbolo_inicial) == 1
        ), "simbolo_inicial deve ser uma string com um único caractere"
