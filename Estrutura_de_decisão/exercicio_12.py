'''
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3%
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

h = float(input("Insira quantas horas você trabalha por mês: "))
d = float(input("Insira quanto você recebe por hora: "))
s = h*d
IR = s * 0 / 100
INSS = s * 10 / 100
FGTS = s*11/100
if s <= 900:
   print(f"Salário Bruto: R${s}")
   print(f"IR: Isento:{IR}")
   print(f"INSS: R${INSS}")
   print(f"FGTS: R${FGTS}")
   print(f"Salário líquido: RS{s - INSS}")
elif s <= 1500:
   IR = s * 5 / 100
   print(f"Salário Bruto: R${s}")
   print(f"IR: R$:{IR}")
   print(f"INSS: R${INSS}")
   print(f"FGTS: R${FGTS}")
   print(f"Total de descontos: R${INSS + IR}")
   print(f"Salário líquido: RS{s - INSS - IR}")
elif s <= 2500:
   IR = s * 10 / 100
   print(f"Salário Bruto: R${s}")
   print(f"IR: R$:{IR}")
   print(f"INSS: R${INSS}")
   print(f"FGTS: R${FGTS}")
   print(f"Total de descontos: R${INSS + IR}")
   print(f"Salário líquido: RS{s - INSS - IR}")
elif s > 2500:
   IR = s * 20 / 100
   print(f"Salário Bruto: R${s}")
   print(f"IR: R$:{IR}")
   print(f"INSS: R${INSS}")
   print(f"FGTS: R${FGTS}")
   print(f"Total de descontos: R${INSS + IR}")
   print(f"Salário líquido: RS{s - INSS - IR}")


