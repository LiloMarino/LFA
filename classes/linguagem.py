from classes.gramatica import Gramatica


class Linguagem:
    def __init__(self, gramatica: Gramatica) -> None:
        assert isinstance(gramatica, Gramatica), "Argumento inválido para a linguagem"
        self.gramatica = gramatica

    # Métodos Mágicos

    def __str__(self) -> str:
        return f"L = ({self.gramatica})"

    def __repr__(self) -> str:
        return f"Linguagem(gramatica={self.gramatica!r})"
