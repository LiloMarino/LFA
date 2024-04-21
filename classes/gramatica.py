from classes.alfabeto import Alfabeto
from classes.sintaxe import Sintaxe
from classes.vocabulario import Vocabulario


class Gramatica:
    def __init__(
        self,
        vocabulario: Vocabulario,
        alfabeto: Alfabeto,
        sintaxe: Sintaxe,
        simbolo_inicial: str,
    ) -> None:
        assert isinstance(
            vocabulario, Vocabulario
        ), "'vocabulario' deve ser uma instância de Vocabulario"
        assert isinstance(
            alfabeto, Alfabeto
        ), "'alfabeto' deve ser uma instância de Alfabeto"
        assert isinstance(
            sintaxe, Sintaxe
        ), "'sintaxe' deve ser uma instância de Sintaxe"
        assert (
            isinstance(simbolo_inicial, str) and len(simbolo_inicial) == 1
        ), "'simbolo_inicial' deve ser uma string com um único caractere"
        assert alfabeto.issubset(
            vocabulario
        ), "O alfabeto deve ser um subconjunto do vocabulário"
        assert (
            simbolo_inicial in vocabulario
        ), f"'{simbolo_inicial}' não pertence ao vocabulário"
        self.alfabeto = alfabeto
        self.vocabulario = vocabulario
        self.sintaxe = sintaxe
        self.simbolo_inicial = simbolo_inicial

    # Métodos Mágicos
    def __or__(self, value: "Gramatica") -> "Gramatica":
        alfabeto = self.alfabeto | value.alfabeto
        vocabulario = self.vocabulario | value.vocabulario
        return Gramatica(vocabulario, alfabeto, self.sintaxe, self.simbolo_inicial)

    def __str__(self) -> str:
        return f"G = ({self.vocabulario}, {self.alfabeto}, {self.sintaxe}, S = {self.simbolo_inicial} )"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(vocabulario={repr(self.vocabulario)}, "
            f"alfabeto={repr(self.alfabeto)}, "
            f"sintaxe={repr(self.sintaxe)}, "
            f'simbolo_inicial="{repr(self.simbolo_inicial)}")'
        )
