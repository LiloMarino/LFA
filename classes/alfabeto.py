from collections import abc
from typing import Generator


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

    @property
    def simbolos_ordenados(self) -> list:
        """
        Retorna uma lista ordenada dos símbolos

        Returns:
            list: Retorna uma lista ordenada dos símbolos
        """
        return sorted(self.simbolos)

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

    def frt(self, max_depth: int = -1) -> Generator:
        """
        Gera os elementos do Fechamento Recursivo e Transitivo do Alfabeto

        Args:
            max_depth (int, optional): Profundidade máxima de recursão. Se negativo, é infinito. Defaults to -1.

        Yields:
            Palavra: Retorna a próxima cadeia do fechamento
        """
        from classes.palavra import Palavra

        def generate_depth(n: int):
            # Gera todas as palavras de tamanho 'n'
            def generate_character(posicao: int, palavra: Palavra = Palavra(self)):
                # Gera o caractere na posição da cadeia
                if posicao == 0:
                    yield palavra
                else:
                    for simbolo in self.simbolos_ordenados:
                        # Para cada símbolo na posição
                        yield from generate_character(posicao - 1, palavra + simbolo)

            yield from generate_character(n)

        if max_depth > -1:
            # Se max_depth for especificado, gere até o tamanho max_depth
            for i in range(max_depth):
                yield from generate_depth(i)
        else:
            # Caso contrário, gere infinitamente
            i = 0
            while True:
                yield from generate_depth(i)
                i += 1

    def fr(self, max_depth: int = -1) -> Generator:
        """
        Gera os elementos do Fechamento Recursivo do Alfabeto

        Args:
            max_depth (int, optional): Profundidade máxima de recursão. Se negativo, é infinito. Defaults to -1.

        Yields:
            Palavra: Retorna a próxima cadeia do fechamento
        """
        from classes.palavra import Palavra

        def generate_depth(n: int):
            # Gera todas as palavras de tamanho 'n'
            def generate_character(posicao: int, palavra: Palavra = Palavra(self)):
                # Gera o caractere na posição da cadeia
                if posicao == 0:
                    yield palavra
                else:
                    for simbolo in self.simbolos_ordenados:
                        # Para cada símbolo na posição
                        yield from generate_character(posicao - 1, palavra + simbolo)

            yield from generate_character(n)

        if max_depth > -1:
            # Se max_depth for especificado, gere até o tamanho max_depth
            for i in range(max_depth):
                yield from generate_depth(i + 1)
        else:
            # Caso contrário, gere infinitamente
            i = 0
            while True:
                yield from generate_depth(i)
                i += 1

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
        return f"Σ = {self.simbolos_ordenados}"

    def __repr__(self) -> str:
        return f"Alfabeto(simbolos = {self.simbolos_ordenados})"
