horas_trabalhadas = float(input("Digite a quantidade de horas: "))
valor_hora = float(input("Digite o valor/hora: "))

if (horas_trabalhadas >= 100): #quando atende a condição.
    bonus = 500.00
else: #quando não atende a condição.
    bonus = 0

salario = horas_trabalhadas * valor_hora + bonus
print(f"Seu salario é de R$:  {salario}")
