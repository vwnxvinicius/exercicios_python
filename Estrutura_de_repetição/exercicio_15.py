'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,..
Faça um programa capaz de gerar a série até o n-ésimo termo.
'''



n = int(input("Insira a quantidade de termos da sequência de fibonnaci: "))
x = 1
y = 1
z = 1
for i in range(1, n+1,1):
    print(z)
    z = x+y
    x=y
    y=z