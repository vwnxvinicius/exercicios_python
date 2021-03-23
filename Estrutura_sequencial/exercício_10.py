# Programa que recebe uma temperatura em graus Celsius e;
# Converte para Fahrenheit

C = float(input("Digite uma temperatura em graus Celsius: "))
F = (C * 9/5) + 32
print("A temperatura recebida em graus Celsius corresponde a {:.2f} em  Fahrenheit".format(F))