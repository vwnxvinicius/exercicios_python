'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

while True:
    n = int(input("Insira um número para calcular o fatorial: "))
    if n > 16:
        n = int(input("O número precisa ser menor que 16 para calcular o fatorial: "))
    x=1
    for i in range(n):
        x = x*(i+1)
    print(x)
    operacao = int(input("Deseja realizar a operação novamente: 1-SIM 2-NÃO:  "))
    if operacao == 2:
        break