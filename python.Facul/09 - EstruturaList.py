# Manipulando listas - list

#Criando uma lista.
nomes = ["Ana", "Pedro"] #Cochetes se usa nas listas
print (f"lista original: {nomes}")
#Adicionando 2 novos nomes com FOR.
for cont in range(2): #Pedindo para repitir 3 vezes.
    novo_nome = input("Digite um nome: ")
    nomes.append(novo_nome) 
print (f"Lista adicionando 2 nomes: {nomes}") #Lista adicionando nomes.

#método 2.
for cont in range(1,4): # pedindo do 1,4 para que o range não começe do 0.
    novo_nome = input(f"Digite um nome{cont}: ")#f,cont para pedir nome por nome exe: nome1, nome 2
    nomes.append(novo_nome) 
print (f"Lista adicionando nomes: {nomes}") 

#método 3.
#Adicionando N quantidades de nomes com WHILE.
resp = "s"
while resp == "s": #Esquanto resp for "sim" então faça.
    novo_nome = input(f"Digite um nome: ") 
    nomes.append(novo_nome) 
    resp = input("Deseja cadastrar mais um nome[s/n]: ")
    #Ele me pergunta se eu quero falar mais um nome se sim ele continua se não ele fecha o programa.
print (f"Lista adicionando n nomes: {nomes}") 

#O indice serve para acessar cada Elemento individualmente.
#Listando elementos pela posição.
print(nomes [0])

#Removendo o último elemento da lista.
nomes.pop()
print(f"Removendo o último{nomes}")

#Removendo um elemento qualquer.
nomes.remove("Pedro")
print(f"Removendo um elemento: {nomes}")

#Verificando a existencia de um elemento.
nome_pesquisado = input("Digite um nome para pesquisar: ")
if nome_pesquisado in nomes : #IF quando o nome for cadastrado.
    print("nome cadastrado")
else: #ELSE quando nome não for cadastrado.
    print("nome não cadastrado")