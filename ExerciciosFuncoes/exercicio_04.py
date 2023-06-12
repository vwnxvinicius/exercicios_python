# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
# se seu argumento for zero ou negativo. 

def p_or_n(n):
    if n > 0:
        return "P"
    else:
        return "N"


print(p_or_n(10))
print(p_or_n(-1))