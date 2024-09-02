#Você foi contratado para desenvolver um programa que ajude a converter um tempo dado em segundos para horas, minutos e segundos. 
#A ideia é permitir que o usuário insira um valor em segundos e que o programa exiba esse valor convertido no formato de horas, minutos e segundos. 

#resulução abaixo 

def converter_tempo(segundos_totais):
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60
    return horas, minutos, segundos

# Solicita ao usuário a quantidade total de segundos
segundos_totais = int(input("Digite o total de segundos: "))

# Converte os segundos para horas, minutos e segundos
horas, minutos, segundos = converter_tempo(segundos_totais)

# Exibe o resultado
print(f"{horas} horas, {minutos} minutos e {segundos} segundos")


