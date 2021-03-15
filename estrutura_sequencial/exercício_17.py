'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados, 
e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
area = float(input("Insira em metros quadrados a medida da área a ser pintada: "))
litros = area/6

# Cálculo de quantidade para latas
latas = litros/18
valor = latas*80

# Cálculo de quantidade para galões
galoes = litros/3.6
valor_g = galoes*25

# Cálculo de quantidade para latas misturada com galões
conjunto = litros/21.6
valor_c = conjunto*105



print(
    f"Temos aqui 3 opções para te auxiliar em sua compra:",
    "\n" 
    f"Comprar apenas latas de 18 litros: Preço: R${valor}, Latas:{latas}",
    "\n"
    f"Comprar apenas galões de 3,6 litros: Preco: R${valor_g }, Galões: {galoes}"
    "\n"
    f"Comprar latas e galões de forma a minimizar o desperdício:" +
    "Preço: R${:.2f}, Latas:{:.2f}, Galões{:.2f}".format(valor_c, latas, galoes)
    )