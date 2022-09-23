'''

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos. 

'''

n = int(input("Insira a quantidade de termos: "))
soma_dos_termos = 1

print("H = 1 + ", end="")
for i in range(2, n+1):
    print(f"{1}/{i}", end="")
    if i < n and n > i:
        print(" + ", end="")
    else:
        print(".")
    
    soma_dos_termos += 1/i
    
print("\nSoma dos termos: %.2f" % soma_dos_termos)