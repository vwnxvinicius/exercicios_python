'''

Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

'''

menor_altura = 500
maior_altura = 0
numero_mais_baixo = 0
numero_mais_alto = 0

for i in range(3):
    numero_do_aluno = int(input("Insira o número do aluno: "))
    altura = int(input("Insira a altura do aluno em centímetros: "))

    if altura > maior_altura:
        maior_altura = altura
        numero_mais_alto = numero_do_aluno
    
    if altura < menor_altura:
        menor_altura = altura
        numero_mais_baixo = numero_do_aluno

print(f"O aluno mais baixo tem {menor_altura}cm de altura e seu número é {numero_mais_baixo}")
print(f"O aluno mais alto tem {maior_altura}cm de altura e seu número é {numero_mais_alto}")