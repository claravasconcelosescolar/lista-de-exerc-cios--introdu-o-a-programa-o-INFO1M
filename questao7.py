# Função para calcular o valor do abono salarial
def calcular_abono_salarial(salario):
    percentual = 0.30
    valor_fixo = 150.00
    abono = (percentual * salario) + valor_fixo
    return abono

# Solicita ao usuário o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Calcula o valor do abono salarial
abono = calcular_abono_salarial(salario)

# Exibe o resultado
print(f"O valor do abono salarial é: R$ {abono:.2f}")
