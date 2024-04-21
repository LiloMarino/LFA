class Producao:
    def __init__(self, origem: str, produto: str) -> None:
        """
        Inicia uma Produção

        Args:
            origem (str): Origem da produção.
            produto (str): Resultado da produção

        Raises:
            TypeError: Caso os argumentos não sejam do tipo correto.
        """
        if isinstance(origem, str) and isinstance(produto, str):
            self.origem = origem
            self.produto = produto
        else:
            raise TypeError("Origem e Produto devem ser strings")

    # Métodos Mágicos

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Producao):
            return self.origem == other.origem and self.produto == other.produto
        return False

    def __str__(self) -> str:
        return f"{self.origem} -> {self.produto}"

    def __repr__(self) -> str:
        return str(self)
