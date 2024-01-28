#Manipulando dicionarios

#Opção 1 
#cliente = {"nome": "Gustavo", "cidade": "Carapicuiba"} 
# o nome é chave e o gustavo é o valor.
#print(cliente)

#Opção 2
cliente = {
    "nome": "Gustavo",
    "cidade": "Carapicuiba",
    "ano_nasc": 2001,
    "ativo": False
}
print(cliente["nome"]) #Aqui ele me mostra somente o nome do cliente.
cliente["ano_nasc"] = 2000 #Aqui eu altero o ano de nascimento.
print(cliente)

del cliente["cidade"] #Aqui eu deleto um elemento.
print(cliente)
              #O (IN) ele busca a chave não o valor
if "ano_nasc" in cliente: #Aqui verifica se tem a chave ano de nasc
    print(f"O cliente nasceu em: {cliente['ano_nasc']}")
else:
    print(f"Não existe a chave ano_nasc")

print (f"Lista de valores:")
for valor in cliente.values(): #Aqui ele me da todos os valor
    print(valor)

print(f"Lista de chaves")
for chave in cliente.items(): #Aqui ele me da todos as chaves
    print(chave)

for chave, valor in cliente.items(): #Aqui ele separa os valor e chaves
    print(chave)

# As listas são multaveis ordenados.
# As tuplas são listas ordernadas imultaveis.
# os sets são listas desordenadas ou estruturas de dados desordenadas
# e que não pode ter elementos repetitivos eles fazem operações de conjunto
# os dicionarios são estruturas mais complexas que deixa uma gama maior de possibilades de trabalhar 