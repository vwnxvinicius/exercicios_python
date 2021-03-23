# Programa que recebe a altura de uma pessoa e calcula seu peso ideal
# Alterando a fórmula conforme o sexo do usuário

altura = float(input("Digite sua altura: "))
pi_homem = (72.7*altura) - 58 
pi_mulher = (62.1*altura) - 44.7
print(
    "Considerando a altura, o peso ideal é de {:.2f} para homens\n".format(pi_homem),
    "e {:.2f} para mulheres".format(pi_mulher)
    )