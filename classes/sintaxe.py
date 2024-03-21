from collections import abc

from classes.producao import Producao


class Sintaxe(abc.MutableMapping):

    def __init__(self, prod: dict[str, list[str]] | list[Producao] | Producao) -> None:
        """
        Instancia uma Sintaxe

        Args:
            prod (dict[str, str] | list[Producao] | Producao): Um dicionário
            que representa as produções, produção ou
            uma lista de produções para a criação da sintaxe

        Raises:
            TypeError: Caso o argumento seja do tipo inválido
        """
        self.__producoes: dict[str, list[str]] = dict()
        if isinstance(prod, Producao):
            self.__producoes[prod.origem] = prod.produto
        elif isinstance(prod, list):
            for p in prod:
                assert isinstance(
                    prod, Producao
                ), "As produções devem  ser instâncias de Producao"
            for p in prod:
                if self.__producoes[p.origem]:
                    self.__producoes[p.origem].append(p.produto)
                else:
                    self.__producoes[p.origem] = [p.produto]
        elif isinstance(prod, dict):
            for key, value in prod.items():
                assert isinstance(key, str) and isinstance(
                    value, list
                ), f"Chaves e valores devem ser strings; '{type(key).__name__}' e '{type(value).__name__}' encontrados."
                for i in value:
                    assert isinstance(
                        i, str
                    ), "Os valores do dicionário devem ser strings."
            self.__producoes = prod
        else:
            raise TypeError(f"Tipo de argumento inválido: {prod}")

    # Métodos Mágicos
    def __str__(self) -> str:
        return str([str(producao) for producao in self.__producoes])

    def __repr__(self) -> str:
        return f"Sintaxe(produções = {self.__producoes})"

    def __iter__(self) -> abc.Iterator:
        return self.__producoes.__iter__()

    def __len__(self) -> int:
        return self.__producoes.__len__()

    def __getitem__(self, __key: str) -> list[str]:
        return self.__producoes[__key]

    def __setitem__(self, __key: str, __value: str | list[str]) -> None:
        assert isinstance(__key, str), "A chave deve ser uma string"
        if isinstance(__value, list):
            for prod in __value:
                assert isinstance(prod, str), "As produções devem ser strings"
            self.__producoes[__key] = __value
        elif isinstance(__value, str):
            self.__producoes[__key].append(__value)
        else:
            raise TypeError("Tipos de valor inválidos")

    def __delitem__(self, __key: str) -> None:
        return self.__producoes.__delitem__(__key)
