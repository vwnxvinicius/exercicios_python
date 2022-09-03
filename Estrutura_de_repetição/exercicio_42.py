'''

Faça um programa que leia uma quantidade indeterminada de 
números positivos e 
conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo. 


'''
print("Para encerrar o programa insira um número negativo")
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0


while True:
    numero = int(input("Insira um número positivo: "))
    if numero < 0:
        break

    if numero >= 0 and numero <=25:
        intervalo_1+=1
    elif numero >= 26 and numero <= 50:
        intervalo_2+=1
    elif numero >= 51 and numero <= 75:
        intervalo_3+=1
    else:
        intervalo_4+=1

print(f"Quantidade de números entre 0 e 25: {intervalo_1}")
print(f"Quantidade de números entre 26 e 50: {intervalo_2}")
print(f"Quantidade de números entre 51 e 75: {intervalo_3}")
print(f"Quantidade de números entre 76 e 100: {intervalo_4}")

    

