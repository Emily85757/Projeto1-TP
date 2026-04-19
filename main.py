import subprocess
import math
from som import Somatoria
from prod import Produtorio
from fibo import Fibonacci

def principal():
    opcao = -1
    while opcao != 0:
        subprocess.run('cls', shell=True)
        print("\nOpções Disponíveis\n")
        print("1  – Estatística de uma lista de valores lidos de um arquivo texto.")
        print("2  - MMC entre dois valores digitados.")
        print("3  - Raiz Cúbica de um valor digitado.")
        print("4  - MDC por subtrações sucessivas.")
        print("5  - Lista de números de Fibonacci.")
        print("0  - Sair")

        try:
            opcao = int(input("\nDigite a opção que deseja: "))
        except ValueError:
            print("Opção inválida: digite um número inteiro.")
            input("\nTecle [Enter] para retornar ao seletor\n")
            continue

        match opcao:
            case 1: estatistica_arquivo()
            case 2: tratar_mmc()
            case 3: raiz_cubica()
            case 4: mdc_subtracoes()
            case 5: listarFibonacci()

def estatistica_arquivo():
    nome = input("Digite o nome do arquivo texto: ")
    som = Somatoria()
    prod = Produtorio()
    try:
        with open(nome, "r") as arq:
            for linha in arq:
                if ";" in linha:
                    v, p = map(float, linha.strip().split(";"))
                    som.somar(v)
                    som.somar_inverso(v)
                    som.somar_ponderado(v, p)
                    prod.multiplicar(v)

        print("\n OPERAÇÕES")
        print("Soma:", som.soma)
        print("Média aritmética:", som.media_aritmetica)
        print("Média harmônica:", som.media_harmonica)
        print("Média ponderada:", som.media_ponderada)
        print("Raiz média quadrática:", som.raiz_media_quadratica)
        print("Média geométrica:", prod.media_geometrica)

    except Exception as e:
        print("Erro ao processar arquivo:", e)

    input("\nTecle [Enter] para retornar ao seletor\n")


def mmc(a: int, b: int) -> int:
    divisor = 2
    resultado = 1
    while a > 1 or b > 1:
        if a % divisor == 0 or b % divisor == 0:
            resultado *= divisor
            if a % divisor == 0:
                a //= divisor
            if b % divisor == 0:
                b //= divisor
        else:
            divisor += 1
    return resultado


def tratar_mmc():
    while True:
        try:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
            print(f"MMC({a}, {b}) = {mmc(a, b)}")
        except ValueError:
            print("Digite apenas números inteiros.")
        resp = input("Deseja calcular outro MMC? (s/n): ").lower()
        if resp != "s":
            break


def raiz_cubica():
    try:
        x = float(input("Digite o valor: "))
        erro = float(input("Digite o erro máximo permitido: "))
        y = 1.0
        while True:
            novo = (x / (y * y) + 2 * y) / 3
            print(f"Palpite: {y:.6f} -> Novo valor: {novo:.6f}")
            if abs(novo - y) < erro:
                print(f"Raiz cúbica aproximada: {novo:.6f}")
                break
            y = novo
    except ValueError:
        print("Entrada inválida.")
    input("\nTecle [Enter] para retornar ao seletor\n")


def mdc_subtracoes():
    try:
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        if a <= 0 or b <= 0:
            print("Digite apenas naturais positivos.")
            return
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
            print(f"A={a}, B={b}")
        print(f"MDC = {a}")
    except ValueError:
        print("Entrada inválida.")
    input("\nTecle [Enter] para retornar ao seletor\n")


def listarFibonacci():
    try:
        n = int(input("Quantos números da sequência de Fibonacci deseja listar? "))
        fib = Fibonacci(n)
        print(f"Sequência: {fib.fibonacci()}")
    except ValueError:
        print("Entrada inválida.")
    input("\nTecle [Enter] para retornar ao seletor\n")


if __name__ == '__main__':
    principal()
