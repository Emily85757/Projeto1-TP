class Fibonacci:
    def __init__(self, numero: int):
        self._N = numero

    def fibonacci(self) -> list[int]:
        lista = [1, 1] if self._N > 1 else [1]
        primeiro, segundo = 1, 1
        for _ in range(2, self._N):
            proximo = primeiro + segundo
            lista = lista + [proximo]   # concatenação em vez de append
            primeiro, segundo = segundo, proximo
        return lista



