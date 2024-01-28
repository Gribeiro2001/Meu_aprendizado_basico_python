# manipulando conjuntos - sets
# sets não permite itens duplicado.

usuarios = {"ana", "maria"} #No sets cria entre chaves.
usuarios.add("Felipe") #Aqui consigo adicionar mais usuarios.
print (usuarios) 

usuario_digitado = input("Digite seu usuario: ")
if usuario_digitado in usuarios:
    print(f"Usuario cadastrado!")
else:
    print(f"usuario não cadastrado")

novos_usuarios = {"felipe", "gustavo", "ana"}

print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios)
print(f"união : {todos_usuarios}") #Aqui eu faço a união de todos nomes

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"interseção: {usuarios_comuns}") #Ele nos da os usuarios que estão em todas lista

usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"Difernça: {usuarios_diferentes}") #Ele mostra os usuarios que não tem em todas lista