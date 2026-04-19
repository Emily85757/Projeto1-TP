class Fibonacci:
    
    def __init__(self, numero : int):
        self._N = numero
      
      
    #16/04/26 - relatar fibonacci, horarios  
    def fibonacci(self) -> list[int]:
        listaString = ['1']
        primeiro = 1
        segundo = 1
        proximo = 1
        for contagem in range (1, self._N, 1):
            listaString += f", {proximo}"
            primeiro = segundo
            segundo = proximo
            proximo = primeiro + segundo
        listaInteiro = list(map(int, listaString))
        return listaInteiro
        
