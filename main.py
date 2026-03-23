import subprocess
import mmc
import fibonacci


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
            case 1 : pass
            case 2 : pass
            case 3 : pass
            case 4 : pass
            case 5 : pass
            


if __name__ == '__main__':
    principal()

