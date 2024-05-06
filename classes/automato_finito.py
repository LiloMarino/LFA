from classes.alfabeto import Alfabeto
from classes.estado import Estado
from classes.producao import Producao
from classes.sintaxe import Sintaxe


class AutomatoFinito:
    def __init__(
        self,
        estados: set[Estado],
        alfabeto: Alfabeto,
        transicoes: Sintaxe,
        estado_inicial: Estado,
        estados_finais: set[Estado],
    ) -> None:
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
