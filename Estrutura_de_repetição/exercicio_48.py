'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

    Exemplo:

      12376489
      => 98467321

'''

n = input("Insira um número inteiro: ")
novo_inteiro = ''

for i in range(1, len(n)+1):
    novo_inteiro += n[-i]

print(int(novo_inteiro))