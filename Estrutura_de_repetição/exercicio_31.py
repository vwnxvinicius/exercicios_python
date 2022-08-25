'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente
uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser informado
pelo operador para indicar o final da compra. O programa deve então mostrar o total da
compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e  
mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''

print('Lojas Tabajara')
produto = float(input("Produto 1: R$ "))
x = 2
valor_total = produto
while produto != 0:
    produto = float(input(f"Produto {x}: R$ "))
    x+=1
    valor_total += produto
    if produto == 0:
        print(f"Total: R$ {valor_total}")
        pagamento = float(input("Dinheiro: R$ "))
        troco = pagamento - valor_total
        print(f"Troco: R$ {troco}")
        produto = float(input("Produto 1: R$ "))
        x = 2