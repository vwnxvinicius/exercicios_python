# Código que identifica se um número é decimal

x = float(input("Insira um número:  "))
y = round(x)
if x == y:
	print("Não é um número decimal")
else:
	print("É um número decimal")