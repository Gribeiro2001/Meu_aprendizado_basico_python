nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequancia: "))

if nota >= 5 and frequencia >= 75:
    situacao = "Aprovado"
elif nota >= 5 or frequencia >= 75: #caso seja verdadeiro, ele para de ser chamado e não irá para o próximo ELIF.
    situacao = " de Recuperção"
else:
    situacao = "Reprovado"

print(f"Você esta {situacao}")