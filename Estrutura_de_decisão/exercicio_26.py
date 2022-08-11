'''

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: 
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é
R$ 2,50 o preço do litro do álcool é R$ 1,90.

'''

litros_vendidos = float(input("Quantos litros você deseja colocar: "))
combustivel = input("Escolha o combustível:\n A - álcool\n G - gasolina\n ---------  ")

if combustivel == "A":
    if litros_vendidos <= 20:
        desconto = (1.90 * 3) / 100
        valor_final = (litros_vendidos * 1.90) - desconto
    else:
        desconto =  (1.90 * 5) / 100
        valor_final = (litros_vendidos * 1.90) - desconto
elif combustivel == "B":
    if litros_vendidos <= 20:
        desconto = (1.90 * 4) / 100
        valor_final = (litros_vendidos * 1.90) - desconto
    else:
        desconto =  (1.90 * 6) / 100
        valor_final = (litros_vendidos * 1.90) - desconto

print(valor_final)