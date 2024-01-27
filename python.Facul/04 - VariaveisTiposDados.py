# 1 variaveis e tipos de dados

# 1 - O que é uma variavel?
# E um espaço reservado na memoria, que serve para 
# armazenar qualquer tipo de dado.

# 2 - o que é uma tipagem dinamica?
#  Significa que não é necessario especificar, na
# declaração, o tipo da variavel.
# Exemplo nome de variavel (snake case):
nome_aluno = "Gustavo"
nota_aluno = 8

print (nome_aluno)
print (nota_aluno)

# 3 - quais os tipo de dados no python?
# inteiro (int), decimal (float), complexo (comples),
# srring (str), boolean (vool), list, tuple, sets e diction
# Exemplos:
ano_atual = 2024 #inteiro
desconto = 15.59 #ponto flutuante
cidade = "Jandira" #texto
filhos = False #falso verdadeiro
cores = ["branco", "azul", "vermelho"] #lista
frutas = ("banana", "uva") #dupla
notas = {5, 10, 30} #ser
clientes = { #dicionario
    "nome": "Maria",
    "altura": 1.95,
    "peso": 60.00
} 
# 4 - o que é tipagem forte?
# ele nâo vai mudar ou trocar de dado automaticamente.
# exemplo:
numero1 = 23
numero2 = 100
print(numero1 + numero2)

# 5 - como trocar o tipo de variavel?
preco_produto = 1.90 #classe float
preco_produto = str(preco_produto) #classe string
preco_produto = float(preco_produto)
print (type (preco_produto))