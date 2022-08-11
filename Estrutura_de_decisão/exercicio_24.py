'''
    Código que recebe dois números do usuário, pergunta a operação desejada e retorna o valor
    valor dessa operação e algumas informações sobre o número: Se ele é par ou ímpar, decimal, positivo ou negativo.
'''


x = float(input("Insira um número: "))
y = float(input("Insira um segundo número: "))

operacao = int(input(
    "Qual operação você deseja realizar:\n"
    "1: ADIÇÃO\n"
    "2: SUBTRAÇÃO\n"
    "3: MULTIPLICAÇÃO\n"
    "4: DIVISÃO\n"
    "................................   "
    ))

if operacao == 1:
    z = x + y
    print(z)
elif operacao == 2:
    z = x - y
    print(z)
elif operacao == 3:
    z = x * y
    print(z)
elif operacao == 4:
    z = x / y
    print(z)

if z % 2 == 0:
    print("É um número par")
else:
    print("É um número ímpar")

z = round(z)
if z:
	print("Não é um número decimal")
else:
	print("É um número decimal")

if z > 0:
    print("É um número negativo")
else:
    print("Não é um número negativo")