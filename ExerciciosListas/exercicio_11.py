# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 


vetor_1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
vetor_2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor_3 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
vetor_4 = []
x = 0

for i in vetor_1:
    vetor_4.append(i)
    vetor_4.append(vetor_2[x])
    vetor_4.append(vetor_3[x])
    x+=1


print(vetor_4)