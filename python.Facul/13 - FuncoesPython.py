# São pedaços de codigo que agrupam instruçoes e podem ser chamadas
# varias vezes, melhorando a organização, legibilidade e reutilização.

# VANTAGENS : dividir o codigo em partes menores.
# não repetir codigo, modularização.
# Sintaxe    
# PREÇO É CHAMADO DE PARAMETRO QUE A VARIAVEL QUE EU CRIO NA FUNÇÃO QUE VAI RECEBER UM VALOR.           
    #preco_final = preco * 0.8
    #return preco_final
    #RETURN NÃO É OBRIGATORIO
    # calcular_desconto(100) 
#Boas praticas
#use nomes semanticos
#use o padrao snake case
#responsabilidade unica
#funcoes puras

valores = [100, 50, 80]

def mensagem():
    print("olá mundo")
def calcular_desconto(preco):
    preco_final = preco * 0.8
    return preco_final

def soma (a, b):
    return a + b

mensagem()
valor_pagar = calcular_desconto(100)
print(f"{valor_pagar:.2f}")

total = soma(4,90)
print(total)

print("### Valores com desconto ###")
for valor in valores:
    valor_desconto = calcular_desconto(valor)
    print(f"{valor_desconto:.2f}")
