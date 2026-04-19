import math

class Somatoria:
    def __init__(self):
        self._soma = 0.0
        self._quantos = 0
        self._soma_inversos = 0.0
        self._quantos_inversos = 0
        self._soma_ponderada = 0.0
        self._soma_pesos = 0.0

    def somar(self, valor: float):
        self._soma += valor
        self._quantos += 1

    def somar_inverso(self, valor: float):
        if valor == 0:
            raise ZeroDivisionError("Inverso de zero não pode ser calculado.")
        self._soma_inversos += 1 / valor
        self._quantos_inversos += 1

    def somar_ponderado(self, valor: float, peso: float):
        self._soma_ponderada += valor * peso
        self._soma_pesos += peso

    @property
    def media_aritmetica(self):
        return self._soma / self._quantos if self._quantos > 0 else 0

    @property
    def media_harmonica(self):
        if self._quantos_inversos == 0:
            raise ZeroDivisionError("Não há valores para calcular média harmônica.")
        return self._quantos_inversos / self._soma_inversos

    @property
    def media_ponderada(self):
        return self._soma_ponderada / self._soma_pesos if self._soma_pesos > 0 else 0

    @property
    def raiz_media_quadratica(self):
        if self._quantos == 0:
            return 0
        return math.sqrt(self._soma / self._quantos)

    @property
    def soma(self):
        return self._soma
