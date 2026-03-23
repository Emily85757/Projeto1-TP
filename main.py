import subprocess

def principal():
    opcao = -1
    while opcao != 0:
        subprocess.run('cls' , shell= True)
        print("\nOpções Disponíveis\n")
        print("1  – Estatística de uma lista de valores.")
        print("2 - MMC entre dois valores digitados.")
        print("3 - Raiz Cúbica de um valor digitado.")
        print("4 - MDC por subtrações sucessivas.")
        print("5 - Lista de números de Fibonacci.")
        print("0 - Sair")
        opcao = int(input("Digite a opção que deseja: "))

        match opcao:
            case 1: pass
            case 2: pass
            case 3: pass
            case 4: pass
        if opcao != 0:
            input("\nTecle [Enter] para retornar ao seletor\n")

