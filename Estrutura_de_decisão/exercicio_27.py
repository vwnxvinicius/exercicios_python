'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de 
carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total 
da compra. 
Escreva um programa que peça o TIPO e a QUANTIDADE de carne comprada pelo usuário e 
gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print(
    "São permitidos apenas dois tipos de carne por cliente" + 
    "\nFILÉ DUPLO - - R$ 4,90Kg \nALCATRA - - R$ 5,90Kg  \nPICANHA - - R$ 6,90Kg"
    )

tipo_de_carne = int(input(
    "Insira um dos tipos de carne que você deseja: " +
    "\nFILÉ DUPLO - - 1 \nALCATRA - - 2  \nPICANHA - - 3\n" +
    "------------------------------------------------------------>"
))
tipo_de_carne2 = int(input(
    "Insira um dos tipos de carne que você deseja: " +
    "\nFILÉ DUPLO - - 1 \nALCATRA - - 2  \nPICANHA - - 3\n" +
    "------------------------------------------------------------>"
))

qtd_1 = float(input("Insira a quantidade de carne para o primerito tipo escolhido (Kg) : "))
qtd_2 = float(input("Insira a quantidade de carne para o segundo tipo escolhido (Kg) : "))

pagamento = input("Pagamento utilizando cartão tabajara? (S) ou (N)")

if tipo_de_carne == 1 and tipo_de_carne2 == 2:
    preco1 = qtd_1 * 4.90
    preco2 = qtd_2 * 5.90
    total = preco1 + preco2
    if pagamento == 'S':
        preco_a_pagar = (total*5) / 100
    print(
        f"TIPO DE CARNE E QNTD: {tipo_de_carne}:{qtd_1}kg e {tipo_de_carne2}:{qtd_2}kg\n",
        f"PREÇO TOTAL: {total}\n",
        f"PAGAMENTO NO CARTÃO TABAJARA: 5% DESCONTO\n",
        f"PREÇO A PAGAR: R${preco_a_pagar}"
    )