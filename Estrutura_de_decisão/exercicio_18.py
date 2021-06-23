"""
Programa que recebe uma data no formato dd/mm/aaaa e determina se a mesma é válida
"""
d = int(input("Insira o dia de uma data: "))
m = int(input("Insira o mês dessa mesma data: "))
a = int(input("Insira o ano dessa mesma data:"))

if d > 31:
    print(f"A data {d}/{m}/{a} é inválida")
elif m > 12:
    print(f"A data {d}/{m}/{a} é inválida")
elif a > 2021:
    print(f"A data {d}/{m}/{a} é inválida")
else:
    print(f"A data {d}/{m}/{a} é válida")
