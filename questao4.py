import math

# Função para calcular o perímetro (ou circunferência) do círculo
def calcular_perimetro(raio):
    return 2 * math.pi * raio

# Função para calcular a área do círculo
def calcular_area(raio):
    return math.pi * raio ** 2

# Solicita ao usuário o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula o perímetro e a área
perimetro = calcular_perimetro(raio)
area = calcular_area(raio)

# Exibe os resultados
print(f"O perímetro do círculo é: {perimetro:.2f}")
print(f"A área do círculo é: {area:.2f}")
