# Função para calcular o valor total da compra
def calcular_valor_compra(preco_unitario, quantidade):
    return preco_unitario * quantidade

# Solicita ao usuário o preço do alimento e a quantidade comprada
preco_unitario = float(input("Digite o preço do alimento por unidade: R$ "))
quantidade = float(input("Digite a quantidade comprada: "))

# Calcula o valor total da compra
valor_total = calcular_valor_compra(preco_unitario, quantidade)

# Exibe o resultado
print(f"O valor total da compra é: R$ {valor_total:.2f}")
