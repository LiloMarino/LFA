from classes.gramatica import Gramatica
from classes.palavra import Palavra


class Linguagem:
    def __init__(self, gramatica: Gramatica) -> None:
        super().__init__()
        assert isinstance(gramatica, Gramatica), "Argumento inválido para a linguagem"
        self.linguagem = set()
        self.gramatica = gramatica

    # Métodos Mágicos

    def __or__(self, value: "Linguagem") -> "Linguagem":
        gramatica = self.gramatica | value.gramatica
        return Linguagem(gramatica)

    def __pow__(self, value: int) -> "Linguagem":
        l = Linguagem(self.gramatica)
        l.linguagem.add(Palavra(self.gramatica.alfabeto))
        if value == 0:
            return l
        else:
            return l ** (value - 1) + l

    def __str__(self) -> str:
        if self.linguagem:
            return f"L = ({self.linguagem})"
        else:
            return f"L = ({self.gramatica})"

    def __repr__(self) -> str:
        return f"Linguagem(gramatica={self.gramatica})"
