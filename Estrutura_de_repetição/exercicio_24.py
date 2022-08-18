'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas = [1, 5, 6, 8, 10]
x = 0
for i in range(len(notas)):
    x += notas[i]
media = x/len(notas)
print(media)