'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
'''

# Salário
s = float(input("Insira quanto você recebe por mês: "))

if s <= 280:
   print(f"Salário antes do reajuste: {s}")
   print("Percentual de aumento aplicado: 20%")
   print(f"Valor do aumento: {s*20/100}")
   print(f"Salário após reajuste: {s + s*20/100}")
elif s > 280 and s <= 700:
   print(f"Salário antes do reajuste: {s}")
   print("Percentual de aumento aplicado: 15%")
   print(f"Valor do aumento: {s*15/100}")
   print(f"Salário após reajuste: {s + s*15/100}")
elif s > 700 and s <= 1500:
   print(f"Salário antes do reajuste: {s}")
   print("Percentual de aumento aplicado: 10%")
   print(f"Valor do aumento: {s*10/100}")
   print(f"Salário após reajuste: {s + s*10/100}")
elif s > 1500:
   print(f"Salário antes do reajuste: {s}")
   print("Percentual de aumento aplicado: 5%")
   print(f"Valor do aumento: {s*5/100}")
   print(f"Salário após reajuste: {s + s*5/100}")