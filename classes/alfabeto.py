from collections import abc
from typing import AbstractSet, Generator, Iterable


class Alfabeto(set):
    def __init__(self, simbolos: Iterable) -> None:
        """
        Inicia um alfabeto

        Args:
            simbolos (Iterable): Símbolos do alfabeto

        Raises:
            ValueError: Caso o alfabeto seja vazio
        """
        if not simbolos:
            raise ValueError("O alfabeto não pode ser vazio")
        super().__init__(simbolos)

    @property
    def simbolos_ordenados(self) -> list:
        """
        Retorna uma lista ordenada dos símbolos

        Returns:
            list: Retorna uma lista ordenada dos símbolos
        """
        return sorted(self)

    def frt(self, max_depth: int = -1) -> Generator:
        """
        Gera os elementos do Fechamento Recursivo e Transitivo do Alfabeto

        Args:
            max_depth (int, optional): Profundidade máxima de recursão. Se negativo, é infinito. Defaults to -1.

        Yields:
            Palavra: Retorna a próxima cadeia do fechamento
        """

        def generate_depth(n: int):
            # Gera todas as palavras de tamanho 'n'
            def generate_character(posicao: int, palavra: str = ""):
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

        def generate_depth(n: int):
            # Gera todas as palavras de tamanho 'n'
            def generate_character(posicao: int, palavra: str = ""):
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

    def __str__(self) -> str:
        return f"Σ = {self.simbolos_ordenados}"

    def __or__(self, value: "Alfabeto") -> "Alfabeto":
        return Alfabeto(super().__or__(value))
