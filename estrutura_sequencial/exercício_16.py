# Programa para auxiliar uma loja de tintas, 
# O algoritmo receberá uma área em metros quadrados,
# Sabendo que a cobertura da tinta é de 1 litro para 3 metros quadrados,
# E que a lata de tinta com 18 litros custa R$80,00
# O algoritmo deverá calcular e retornar quantas latas serão utilizadas e o valor total

area = float(input("Insira em metros quadrados a medida da área a ser pintada: "))

litros = area/3
latas = litros/18
valor = latas*80

print(
    "Você preccisará de {:.2f} litros, que corresponde a {:.2f} latas, o preço total será de R${:.2f}".format(litros, latas, valor)
    )