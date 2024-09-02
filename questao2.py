# Função para calcular a média das notas
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Solicita ao usuário as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = calcular_media(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média final do aluno é: {media:.2f}")
