# Programa que recebe as horas trabalhadas no mês e,
# Quanto  o usuário ganha por hora, calcula seu salário no mês e retorna:
# Sálario bruto;
# Valor do INSS: 11%
# Valor do sindicato: 8%
# Imposto de renda: 11%
# Sálario líquido;

# Horas trabalhadas no mês
h = int(input("Quantas horas você trabalha por mês? "))
# Salário por hora
s = float(input("Quanto você recebe por hora? "))

salario_bruto = h * s
inss = (salario_bruto * 11) / 100
imposto_renda = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 8) / 100
salario_liquido = salario_bruto - inss - imposto_renda - sindicato
print(f"Seu salário bruto é de {salario_bruto}.")
print(
    f"Você irá pagar {inss} de inss, {sindicato} de sindicato e",
    f"{imposto_renda} de imposto de renda.",
    )
print("Seu salário líquido será de {:.2f}".format(salario_liquido))