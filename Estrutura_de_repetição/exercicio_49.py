'''
Faça um programa que mostre os n termos da Série a seguir:

      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

    Imprima no final a soma da série.
'''

n = int(input("Insira a quantidade de termos: "))
m = 1
soma_dos_termos = 0

print("S = ", end="")
for i in range(1, n+1):
    print(f"{i}/{m} + ", end="")
    if i < n and n > i:
        print(" + ", end="")
    else:
        print(".")
    
    soma_dos_termos += i/m
    m+=2
    
print("\nSoma dos termos: %.2f" % soma_dos_termos)