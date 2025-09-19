# Criar um código python indique se a temperatura está agradavel ou não.
# Condições:
# Temperatura >= 30° informar que está muito quente
# Temperatura >= 20° informar que a temperatura esta agradável
# Temperatura >= 10 ° informar que está frio
# Temperatura abaixo de 10° informar que está muito frio

# Etapas para resolução:
# 1) Solicitar a temperatura para o usuário
# 2) Verificar a condicional
# 3) Imprimir a resposta segundo a temperatura

temperatura = float(input("Digite a temperatura do dia: "))

 # if condição:
    #bloco de código a ser executado
 # elif condição:
    #bloco de código a ser executado
 # else:
    #bloco de código a ser executado

if temperatura >=30:
    print(f"A temperatura do dia é {temperatura}° C e o dia está muito quente.")
elif temperatura >=20:
    print(f"A Temperatura do dia é {temperatura}° C e o dia está agradável.")
elif temperatura >=10:
    print(f"A temeperatura do dia é {temperatura}° C e o dia está frio")
else:
    print(f"A temperatura do dia é {temperatura}° C e o dia está muito fruio")

