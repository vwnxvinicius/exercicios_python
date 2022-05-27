# Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

s = input("Insira 'F' ou 'M': ")
if s == 'F' or s == 'f':
    print("F - Feminino")
elif s == 'M' or s == 'm':
    print("M - Masculino")
else:
    print("Sexo inválido")
