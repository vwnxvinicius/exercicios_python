# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão 
# ser compostos pelos elementos intercalados dos dois outros vetores. 

vetor_1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
vetor_2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor_3 = []
x = 0

for i in vetor_1:
    vetor_3.append(i)
    vetor_3.append(vetor_2[x])
    x+=1


print(vetor_3)