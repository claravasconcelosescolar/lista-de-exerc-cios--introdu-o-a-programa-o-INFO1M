# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (9 * celsius + 160) / 5

# Solicita ao usuário a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte para Fahrenheit
fahrenheit = celsius_para_fahrenheit(celsius)

# Exibe o resultado
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")
