'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,..
Faça um programa que gere a série até que o valor seja maior que 500.
'''

x = 1
y = 1
z = 1
while True:
    print(z)
    z = x+y
    x=y
    y=z
    if z>500:
        print(z)
        break