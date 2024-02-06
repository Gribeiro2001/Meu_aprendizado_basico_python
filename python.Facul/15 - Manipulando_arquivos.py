def ler_arquivo(nome_arquivo): 
    arquivo = open(nome_arquivo, "r")
    conteudo = arquivo.read()
    arquivo.close()
    print(f"lendo o arquivo: {nome_arquivo}")
    print(conteudo)
    #return conteudo
ler_arquivo("cidades.txt")

