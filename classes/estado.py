from classes.sintaxe import Sintaxe


class Estado:
    def __init__(self, nome: str, transicoes: Sintaxe = None) -> None:
        self.nome = nome
        self.transicoes = transicoes

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return self.nome

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Estado):
            return self.nome == other.nome
        return False

    def __hash__(self) -> int:
        return hash(self.nome)
