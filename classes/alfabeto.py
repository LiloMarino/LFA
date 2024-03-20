from collections import abc


class Alfabeto(abc.Set):
    def __init__(self, simbolos: set[str]) -> None:
        """
        Instancia um Alfabeto

        Args:
            simbolos (set[str]):  Conjunto de símbolos finitos que formam o alfabeto

        Raises:
            ValueError: Caso o conjunto esteja vazio
            TypeError: Caso os elementos do conjunto não sejam uma string ou um conjunto
        """
        if not simbolos:
            raise ValueError("O alfabeto não pode ser vazio")
        if isinstance(simbolos, set):
            self.simbolos = simbolos
        elif isinstance(simbolos, str):
            self.simbolos = set(simbolos)
        else:
            raise TypeError("Símbolos deve ser um conjunto ou uma string")

    def add_simbolo(self, simbolo: str) -> None:
        """
        Adiciona um símbolo ao alfabeto

        Args:
            simbolo (str): Símbolo a ser adicionado

        Raises:
            TypeError: Caso o símbolo não seja um caractere
        """
        if isinstance(simbolo, str):
            self.simbolos.add(simbolo)
        else:
            raise TypeError("Simbolo deve ser uma string")

    def discard_simbolo(self, simbolo: str) -> bool:
        """
        Remove um símbolo do alfabeto e retorna se foi removido com sucesso

        Args:
            simbolo (str): Símbolo a ser removido do alfabeto

        Returns:
            bool: Retorna se o símbolo foi removido com sucesso
        """
        self.simbolos.discard(simbolo)
        return True if simbolo in self.simbolos else False

    # Métodos Mágicos

    def __contains__(self, x: object) -> bool:
        return self.simbolos.__contains__(x)

    def __iter__(self) -> abc.Iterator:
        return self.simbolos.__iter__()

    def __len__(self) -> int:
        return self.simbolos.__len__()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Alfabeto):
            return self.simbolos == other.simbolos
        return TypeError("É possível comparar apenas entre alfabetos")

    def __str__(self) -> str:
        return f"Σ = {self.simbolos.__str__()}"

    def __repr__(self) -> str:
        return f"Alfabeto(simbolos = {self.simbolos})"
