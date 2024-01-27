numero = int(input("Digite um numero: "))

print (f"Tabuada do {numero}: ")

for i in range(1, 11): #FOR repeti o codigo varias vezes
    resultado = numero * i #range me da uma sequencia de numeros 1, 2, 3, etc..
    print(f"{numero} x {i} = {resultado}")