'''
Altere o programa anterior permitindo ao usuário informar as 
populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''



a = int(input("Insira a população do país A: "))
taxa_de_crescimento_a = int(input("Insira a taxa de crescimento do país A: ('%' ao ano)"))
b = int(input("Insira a população do país B: "))
taxa_de_crescimento_b= int(input("Insira a taxa de crescimento do país B: ('%' ao ano)"))
anos = 0

while ((taxa_de_crescimento_a > taxa_de_crescimento_b) and (a > b)) or ((taxa_de_crescimento_b > taxa_de_crescimento_a) and (b > a)):
    print(
        "A taxa de crescimento da maior população\n" +
        "não pode ser maior que a taxa de crescimento do país com menor população"
    )
    a = int(input("Insira a população do país A: "))
    taxa_de_crescimento_a = int(input("Insira a taxa de crescimento do país A: ('%' ao ano)"))
    b = int(input("Insira a população do país B: "))
    taxa_de_crescimento_b= int(input("Insira a taxa de crescimento do país B: ('%' ao ano)"))

while a <= b:
    a += (a * taxa_de_crescimento_a) / 100
    b += (b * taxa_de_crescimento_b) / 100
    anos += 1
print(f"Anos necessários para a população do país A superar o país B: {anos}")

operacao = int(input("Deseja repetir a operação? SIM-1 NÃO-2:  "))
while operacao == 1:
    a = int(input("Insira a população do país A: "))
    taxa_de_crescimento_a = int(input("Insira a taxa de crescimento do país A: ('%' ao ano)"))
    b = int(input("Insira a população do país B: "))
    taxa_de_crescimento_b= int(input("Insira a taxa de crescimento do país B: ('%' ao ano)"))
    anos = 0
    while a <= b:
        a += (a * taxa_de_crescimento_a) / 100
        b += (b * taxa_de_crescimento_b) / 100
        anos += 1
    print(f"Anos necessários para a população do país A superar o país B: {anos}")
    operacao = int(input("Deseja repetir a operação? SIM-1 NÃO-2:  "))