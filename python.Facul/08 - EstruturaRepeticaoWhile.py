senha = input ("Digite sua senha: ")
senha_correta = "123"

while senha != senha_correta: #while repeti quando o usuario inseri um valor direfente da variavel.
    print ("Senha incorreta! Tente novamente")
    senha = input ("Digite sua senha: ")

print ("Acesso permitido!")