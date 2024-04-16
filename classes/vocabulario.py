from collections import abc

from classes.alfabeto import Alfabeto


class Vocabulario(abc.MutableSet):
    def __init__(
        self, simbolos_n_terminais: set[str] | str, alfabeto: Alfabeto
    ) -> None:
        """
        Instancia um Vocabulario

        Args:
            simbolos (set[str]):  Conjunto de símbolos terminais e não terminais finitos
            que formam o vocabulário

        Raises:
            ValueError: Caso o conjunto esteja vazio
            TypeError: Caso os elementos do conjunto não sejam uma string ou um conjunto
        """
        if isinstance(simbolos_n_terminais, str):
            simbolos_n_terminais = set(simbolos_n_terminais)
        if not isinstance(simbolos_n_terminais, set):
            raise TypeError("Símbolos não terminais deve ser um conjunto ou uma string")
        intersecao = simbolos_n_terminais & alfabeto.simbolos
        if intersecao:
            raise ValueError(
                f"Os símbolos não terminais e os símbolos terminais têm intersecção: {intersecao}"
            )
        self.vocabulario = simbolos_n_terminais | alfabeto.simbolos

    # Métodos Mágicos

    def __contains__(self, x: object) -> bool:
        return self.vocabulario.__contains__(x)

    def __iter__(self) -> abc.Iterator:
        return self.vocabulario.__iter__()

    def __len__(self) -> int:
        return self.vocabulario.__len__()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vocabulario):
            return self.vocabulario == other.vocabulario
        return TypeError("É possível comparar apenas entre vocabulários")

    def __str__(self) -> str:
        return f"V = {sorted(self.vocabulario)}"

    def __repr__(self) -> str:
        return f"Vocabulário(vocabulário = {sorted(self.vocabulario)})"
