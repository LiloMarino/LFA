from collections import abc

from classes.producao import Producao


class Sintaxe(abc.Iterable):

    def __init__(self, producoes: list[Producao] | Producao) -> None:
        """
        Instancia uma Sintaxe

        Args:
            producoes (list[Producao] | Producao): Produção ou uma
            lista de produções para a criação da sintaxe

        Raises:
            TypeError: Caso o argumento seja do tipo inválido
        """
        if isinstance(producoes, Producao):
            self.producoes = list()
            self.producoes.append(producoes)
        elif isinstance(producoes, list):
            for prod in producoes:
                assert isinstance(prod, Producao)
            self.producoes = producoes
        else:
            raise TypeError(
                "Produções deve ser uma produção única ou uma lista de produções"
            )

    def append(self, object: Producao) -> None:
        """
        Adiciona a produção à sintaxe

        Args:
            object (Producao): Produção a ser adicionada
        """
        if isinstance(object, Producao):
            self.producoes.append(object)
        else:
            raise TypeError("Objetos devem ser instâncias da classe 'Producao'")

    def remove(
        self, producao: Producao = None, origem: str = None, produto: str = None
    ) -> None:
        """
        Remove uma produção da sintaxe

        Args:
            producao (Producao, optional): Produção a ser removida. Defaults to None.
            origem (str, optional): Origem da produção. Defaults to None.
            produto (str, optional): Produto da produção. Defaults to None.

        Raises:
            ValueError: Caso os argumentos estejam inválidos
            ValueError: Caso não exista nenhuma produção igual a especificada
        """

        p = producao if isinstance(producao, Producao) else None
        if origem is not None and produto is not None:
            p = Producao(origem, produto)
        if p is None:
            raise ValueError("Deve-se informar um par origem/produto ou uma produção")

        for producao in self.producoes:
            if p == producao:
                self.producoes.remove(producao)
                return
        raise ValueError(
            f"Não existe nenhuma produção com Origem '{origem}' e Produto '{produto}'"
        )

    def sort(self, key: None = None, reverse: bool = False) -> None:
        """
        Ordena a sintaxe

        Args:
            key (None, optional): Chave de ordenação. Defaults to None.
            reverse (bool, optional): Reverso. Defaults to False.
        """
        if key is None:
            self.producoes.sort(key=lambda producao: producao.origem, reverse=reverse)
        else:
            self.producoes.sort(key=key, reverse=reverse)

    # Métodos Mágicos
    def __str__(self) -> str:
        return str([str(producao) for producao in self.producoes])

    def __repr__(self) -> str:
        return f"Sintaxe(produções = {self.producoes})"

    def __iter__(self) -> abc.Iterator:
        return self.producoes.__iter__()

    def __getitem__(self, origem: str) -> list[Producao]:
        return Sintaxe([prod for prod in self.producoes if prod.origem == origem])
