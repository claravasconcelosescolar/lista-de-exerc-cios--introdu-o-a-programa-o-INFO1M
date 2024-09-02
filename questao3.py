# Função para calcular a gorjeta
def calcular_gorjeta(valor_conta, percentual_gorjeta=10):
    return valor_conta * (percentual_gorjeta / 100)

# Solicita ao usuário o valor da conta
valor_conta = float(input("Digite o valor total da conta em reais: "))

# Calcula a gorjeta
gorjeta = calcular_gorjeta(valor_conta)

# Exibe o resultado
print(f"A gorjeta a ser paga é: R$ {gorjeta:.2f}")
