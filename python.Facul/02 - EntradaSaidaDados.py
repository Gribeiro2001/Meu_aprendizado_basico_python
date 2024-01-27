# - Entrada e saida de dados.

# print é a saida de dados.
# input é a entrada de dados 
#Exemplo:
nome = "gustavo"
idade = 23
print("Olá, seu nome é", nome, "e você tem", idade, "anos.")

nome = "Gustavo"
idade = "23"
mensagem = "Olá, seu nome é " + nome +  " e você tem " + idade + " anos."
print(mensagem)

mensagem = f"Olá, seu nome é {nome} e você tem {idade} anos. "
print(mensagem)

nome = input("Digite seu nome: ")
idade = input("Digite sua Idade: ")
mensagem = f"Olá, seu nome é {nome} e você tem {idade} anos. "
print(mensagem)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua Idade: "))
ano = 2024 - idade
mensagem = f"Olá, seu nome é {nome} e você nasceu no ano de {ano}. "
print(mensagem)

