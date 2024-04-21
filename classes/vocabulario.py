from typing import Iterable

from multipledispatch import dispatch

from classes.alfabeto import Alfabeto


class Vocabulario(set):
    @dispatch(set)
    def __init__(self, vocabulario: set) -> None:
        """
        Inicia um Vocabulário a partir de um conjunto

        Args:
            vocabulario (set): Conjunto
        """
        super().__init__(vocabulario)

    @dispatch(object, Alfabeto)
    def __init__(self, simbolos_n_terminais: Iterable, alfabeto: Alfabeto) -> None:
        """
        Inicia um Vocabulário

        Args:
            simbolos_n_terminais (Iterable): Símbolos não terminais
            alfabeto (Alfabeto): Alfabeto

        Raises:
            ValueError: Caso exista alguma intersecção entre o alfabeto e os símbolos não terminais
        """
        assert isinstance(
            alfabeto, Alfabeto
        ), "O parâmetro 'alfabeto' deve ser do tipo Alfabeto"
        super().__init__(simbolos_n_terminais)
        if not self.isdisjoint(alfabeto):
            raise ValueError(
                f"Os símbolos não terminais e os símbolos terminais têm intersecção: {self & alfabeto}"
            )
        self |= alfabeto

    # Métodos Mágicos

    def __str__(self) -> str:
        return f"V = {sorted(self)}"

    def __or__(self, value: "Vocabulario") -> "Vocabulario":
        return Vocabulario(super().__or__(value))
