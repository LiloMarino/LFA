class Producao:
    def __init__(self, origem: str, produto: str) -> None:
        if isinstance(origem, str) and isinstance(produto, str):
            self.origem = origem
            self.produto = produto
        else:
            raise ValueError("Origem e Produto devem ser strings")

    # Métodos Mágicos

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Producao):
            return self.origem == other.origem and self.produto == other.produto
        return False

    def __str__(self) -> str:
        return f"{self.origem} -> {self.produto}"

    def __repr__(self) -> str:
        return f"Producao(origem = {self.origem},  produto={self.produto})"
