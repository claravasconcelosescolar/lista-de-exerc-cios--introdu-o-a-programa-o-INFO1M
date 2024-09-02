# Função para calcular o Índice de Massa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicita ao usuário o peso e a altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
