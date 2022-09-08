'''

O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
    Considere que o cliente deve informar quando o pedido deve ser encerrado.


'''

print(" --- Insira 0 para encerrar o pedido --- \n",
    "Especificação   Código  Preço\n",
    "Cachorro Quente 100     R$ 1,20\n",
    "Bauru Simples   101     R$ 1,30\n"
    " Bauru com ovo   102     R$ 1,50\n"
    " Hambúrguer      103     R$ 1,20\n"
    " Cheeseburguer   104     R$ 1,30\n"
    " Refrigerante    105     R$ 1,00\n"
    )


preco_codigo_100 = 0
preco_codigo_101 = 0
preco_codigo_102 = 0
preco_codigo_103 = 0
preco_codigo_104 = 0
preco_codigo_105 = 0


preco_final = 0

while True:
    codigo = int(input("Insira o código do produto desejado: "))

    # Encerrando o loop
    if codigo == 0:
        break

    quantidade = int(input("Insira a quantidade do mesmo: "))


    if codigo == 100:
        preco_produto = 1.20 * quantidade
        preco_codigo_100 = preco_produto
    elif codigo == 101:
        preco_produto = 1.30 * quantidade
        preco_codigo_101 = preco_produto
    elif codigo == 102:
        preco_produto = 1.50 * quantidade
        preco_codigo_102 = preco_produto
    elif codigo == 103:
        preco_produto = 1.20 * quantidade
        preco_codigo_103 = preco_produto
    elif codigo == 104:
        preco_produto = 1.30 * quantidade
        preco_codigo_104 = preco_produto
    elif codigo == 105:
        preco_produto = 1.00 * quantidade
        preco_codigo_105 = preco_produto
    else:
        print("Código inválido")
    
    preco_final += preco_produto


print("CONTA")
if preco_codigo_100:
    print(f"Cachorro quente:{preco_codigo_100}")
if preco_codigo_101:
    print(f"Bauru Simples:{preco_codigo_101}")
if preco_codigo_102:
    print(f"Bauru com ovo:{preco_codigo_102}")
if preco_codigo_103:
    print(f"Hambúrguer:{preco_codigo_103}")
if preco_codigo_104:
    print(f"Cheeseburguer:{preco_codigo_104}")
if preco_codigo_105:
    print(f"Refrigerante:{preco_codigo_105}")


print(f"PREÇO TOTAL: {preco_final}")