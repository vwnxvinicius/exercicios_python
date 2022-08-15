'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input("Insira um nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário: "))
sexo = input("Sexo: (f) ou (m): ")
estado_civil = input("Estado civil: (s),(c),(v),(d): ")

while len(nome) <= 3:
    print("O nome tem que ser maior que 3 caracteres")
    nome = input("Insira um nome: ")

while idade > 150 or idade < 0:
    print("Idade entre 0 e 150 anos")
    idade = int(input("Insira sua idade: "))

while salario <= 0:
    print("Salário tem que ser maior que 0")
    salario = float(input("Insira seu salário: "))

while sexo != 'f' and sexo != 'm':
    print("O sexo deve ser definido como m-masculino ou f-feminino")
    sexo = input("Sexo: (f) ou (m): ")

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Estado civil tem que ser definido como:v, c, d, ou s")
    estado_civil = input("Estado civil: (s),(c),(v),(d): ").lower()

print("Cadastro realizado com sucesso")