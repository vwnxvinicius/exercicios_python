# Programa que recebe quanto o usuário ganha por hora;
# Quantas horas ele trabalha no mês e;
# Retorna o salário dele por mês

s = float(input("Quanto você recebe por hora?  ")) # Sálario por hora
h = int(input("Quantas horas você trabalha por mês?  ")) # Horas trabalhadas
t = s*h # Total recebido em um mês
print(f"Trabalhando {h} horas por mês e recebendo {s} por hora ",
    f"você receberá {t} no final do mês"
    )
