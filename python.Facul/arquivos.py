# Escrevendo em um arquivo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um exemplo de escrita em arquivo.\n")

# Lendo um arquivo
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Acrescentando conteúdo a um arquivo
with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Aqui estamos acrescentando mais algumas linhas.\n")

# Lendo o arquivo novamente após acrescentar conteúdo
with open("exemplo.txt", "r") as arquivo:
    conteudo_atualizado = arquivo.read()
    print(conteudo_atualizado)
