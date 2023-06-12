'''
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n
'''



def func(valor):
    if isinstance(valor, int):
        x = 1
        while x <= valor:
            y = 1
            texto = ''
            while y <= x:                
                texto += str(y) + "\t"
                y += 1
            print(texto)
            x += 1


func(10)
