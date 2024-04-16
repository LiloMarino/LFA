from classes.alfabeto import Alfabeto


class Palavra:
    def __init__(self, alfabeto: Alfabeto, palavra: str = "") -> None:
        """
        Inicia uma Palavra

        Args:
            alfabeto (Alfabeto): Alfabeto usado na construção da palavra
            palavra (str, optional): Palavra. Defaults to "".

        Raises:
            ValueError: Caso o símbolo da palavra não esteja no alfabeto
        """
        for simbolo in palavra:
            if simbolo not in alfabeto:
                raise ValueError(f"O símbolo '{simbolo}' não está no alfabeto.")
        self.palavra = palavra
        self.alfabeto = alfabeto

    # Métodos Mágicos

    def __len__(self) -> int:
        return self.palavra.__len__()

    def __add__(self, other: object) -> "Palavra":
        if isinstance(other, Palavra):
            if other.alfabeto == self.alfabeto:
                return Palavra(self.alfabeto, self.palavra + other.palavra)
            else:
                raise ValueError(
                    "Os alfabetos das palavras devem ser iguais para a adição."
                )
        elif not isinstance(other, Palavra) and isinstance(other, str):
            return Palavra(self.alfabeto, self.palavra + other)
        else:
            raise TypeError("Só é permitido a concatenação entre palavras e símbolos!")

    def __radd__(self, other: object) -> "Palavra":
        if isinstance(other, str):
            return Palavra(self.alfabeto, self.palavra + other)
        else:
            raise TypeError("Só é permitido a concatenação entre palavras e símbolos!")

    def __pow__(self, value: int) -> "Palavra":
        if len(self.palavra) > 0 or value > 0:
            return Palavra(self.alfabeto, self.palavra * value)
        else:
            raise ZeroDivisionError("Não é possível elevar uma palavra vazia ao zero.")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Palavra):
            return self.palavra == other.palavra
        elif isinstance(other, str):
            return self.palavra == other
        else:
            return False

    def __str__(self) -> str:
        if len(self.palavra) == 0:
            return "'λ'"
        else:
            return f"'{self.palavra}'"

    def __repr__(self) -> str:
        return (
            f"Palavra(palavra = '{self.palavra}', alfabeto = {self.alfabeto.simbolos})"
        )
