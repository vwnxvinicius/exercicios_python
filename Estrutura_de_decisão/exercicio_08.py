# Produto que recebe o preço de três produtos e informa qual deverá ser comprado sabendo
# Que a compra deverá ser feita com base no menor preço

leite = float(input("Informe o preço do leite: "))
ovo = float(input("Informe o preço do ovo: "))
carne = float(input("Informe o preço da carne: "))

if leite < ovo and leite < carne:
    print("Com base no preço o produto que deve ser comprado é o leite.")
elif ovo < leite and ovo < carne:
    print("Com base no preço o produto que deve ser comprado é o ovo.")
else:
    print("Com base no preço o produto que deve ser comprado é a carne.")