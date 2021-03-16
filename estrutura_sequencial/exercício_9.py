# Programa que recebe uma temperatura em Fahrenheit e converte para graus Celsius


F = float(input("Insira uma temperatura em Fahrenheit: "))
C = 5 * ((F-32) / 9 )
print("O valor recebido em Fahrenheit corresponde a {:.2f} em graus Celsius!".format(C))
