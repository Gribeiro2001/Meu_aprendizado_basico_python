# Módulos é um grupo de fuções 

import random
import Operacoes
from colorama import Fore, init
init(autoreset=True)

def exibir_menu():
    print("1. soma")
    print("2. subtracao")
    print("3. multiplicacao")
    print("4. divisao")
    print("5. Número aleatorio")
    print("0. sair")

def obter_numeros():
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))
    return[a, b]

while True:
    exibir_menu()

    funcao = input("Escolha uma função: ")
    if (funcao == "0"):
        print("Saindo do sistema")
        break
    if (funcao == "1"):
        a, b = obter_numeros()
        resultado = Operacoes.soma (a, b)
        print(Fore.BLUE + f"Resultado: {resultado}")
    elif (funcao == "2"):
        a, b = obter_numeros()
        resultado = Operacoes.subtracao (a, b)
        print(f"Resultado: {resultado}")
    elif (funcao == "3"):
        a, b = obter_numeros()
        resultado = Operacoes.multiplicacao (a, b)
        print(f"Resultado: {resultado}")
    elif (funcao == "4"):
        a, b = obter_numeros()
        if b != 0:
            resultado = Operacoes.divisao (a, b)
            print(f"Resultado: {resultado}")
        else:
            print("Não é possivel dividir por zero!")
    elif funcao == "5":
        a, b = obter_numeros()
        resultado = random.randint(a, b)
        print("Resultado: ", resultado)
    else:
        print(Fore.RED + "Opção invalida. tente novamente!")