# Função para calcular o saldo da conta bancária
def calcular_saldo(valor_depositado, valor_sacado):
    return valor_depositado - valor_sacado

# Solicita ao usuário o valor depositado e o valor sacado
valor_depositado = float(input("Digite o valor depositado: R$ "))
valor_sacado = float(input("Digite o valor sacado: R$ "))

# Calcula o saldo
saldo = calcular_saldo(valor_depositado, valor_sacado)

# Exibe o resultado
print(f"O saldo da conta bancária é: R$ {saldo:.2f}")
