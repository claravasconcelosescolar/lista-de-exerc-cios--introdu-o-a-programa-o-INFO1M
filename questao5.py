# Função para calcular o troco
def calcular_troco(preco_total, valor_pago):
    return valor_pago - preco_total

# Solicita ao usuário o preço total da compra e o valor pago
preco_total = float(input("Digite o preço total da compra: R$ "))
valor_pago = float(input("Digite o valor dado para o pagamento: R$ "))

# Calcula o troco
troco = calcular_troco(preco_total, valor_pago)

# Verifica se o valor pago é suficiente
if troco < 0:
    print("O valor dado para o pagamento é insuficiente.")
else:
    # Exibe o resultado
    print(f"O troco a ser pago é: R$ {troco:.2f}")
