class Produtorio:
    def __init__(self):
        self._produto = 1.0
        self._quantos = 0

    def multiplicar(self, valor: float):
        self._produto *= valor
        self._quantos += 1

    @property
    def media_geometrica(self):
        if self._quantos == 0:
            return 0
        return self._produto ** (1 / self._quantos)