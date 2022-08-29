'''

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


'''

maior_indice_acidentes = 0
menor_indice_acidentes = 10000000
cidade_maior_indice_acidentes = 0
cidade_menor_indice_acidentes = 0
acidentes_cidades_pequenas = 0
cidades_pequenas = []
veiculos = 0


for i in range(5):
    codigo_cidade = int(input("Insira o código da cidade: "))
    quantidade_veiculos = int(input("Insira a quantidade de veículos em passeio: "))
    quantidade_acidentes_com_vitimas = int(input("Insira a quantidade de acidentes com vítimas: "))

    veiculos += quantidade_veiculos

    if quantidade_veiculos <= 2000:
        cidades_pequenas.append(quantidade_acidentes_com_vitimas)

    if quantidade_acidentes_com_vitimas > maior_indice_acidentes:
        maior_indice_acidentes = quantidade_acidentes_com_vitimas
        cidade_maior_indice_acidentes = codigo_cidade
    
    if quantidade_acidentes_com_vitimas < menor_indice_acidentes:
        menor_indice_acidentes = quantidade_acidentes_com_vitimas
        cidade_menor_indice_acidentes = codigo_cidade


for i in range(len(cidades_pequenas)):
    acidentes_cidades_pequenas += cidades_pequenas[i]

media_veiculos = veiculos/5
media_acidentes_cidades_pequenas = acidentes_cidades_pequenas/len(cidades_pequenas)

print(
    f"O maior índice de acidentes é {maior_indice_acidentes} e pertence a cidade com código:",
    f"{cidade_maior_indice_acidentes}"
    )

print(
    f"O menor índice de acidentes é {menor_indice_acidentes} e pertence a cidade com código:",
    f"{cidade_menor_indice_acidentes}"
    )

print(f"A média de veículos em todas as cidades é de {media_veiculos}")
print(f"A média de acidentes em cidades com menos de 2.000 veículos é de: {media_acidentes_cidades_pequenas}")