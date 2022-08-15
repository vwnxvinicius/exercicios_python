'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
for i in list(range(50)):
    if i % 2 == 0:
        i+=1
        print(i)

#or

for i in range(1,50,2):
    pass
    #print(i)
