anos_experiencia = int(input("Digite os anos de experiencia: ")) # Dev Junior.

if anos_experiencia == 0: #quando atende a condição.
    nivel = "Estagiario"
elif anos_experiencia <= 3: #caso seja verdadeiro, ele para de ser chamado e não irá para o próximo ELIF.
    nivel = "Júnior"
elif anos_experiencia <= 8: #caso seja verdadeiro, ele para de ser chamado e não irá para o próximo ELIF.
    nivel = "Pleno"
else: #quando não atende a condição.
    nivel = "Sênior"

print(f"Você é um desenvolvedor do nivel: {nivel}")