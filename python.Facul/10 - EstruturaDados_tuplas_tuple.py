#Manipulando tuplas - tuple
# Aqui consingo enviar as Tuplas e adicionar valores
cores = ("vermelha", "azul", "amarelo", "verde", "azul")
print(f"Meu carro é {cores[2]}")

# Aqui consigo contar quantas cores
qtd = len(cores) #No tuplas e tuple se usa aspas.
print(f"Tenho {qtd} de opções de cores")

cor = input ("Digite uma cor: ")
qtd_cor = cores.count(cor)
print(f"Temos {qtd_cor} tipo de {cor}")

# Aqui fala se tem ou não a cor.
cor = input("Digite uma cor: ")
if cor in cores:
    print(f"A cor {cor} exixte na loja")
else:
    print(f"a cor {cor} não existe na loja")

aluno = ("Gustavo", 10, 5)
#nome = aluno[0]
#nota1 = aluno[1]
#nota2 = aluno[2]

# aqui é um método chamado desempacotamento.
nome, nota1, nota2 = aluno
media = (nota1 + nota2) / 2

print(f"O aluno {nome} com as nota {nota1} e {nota2} esta com média {media}")
