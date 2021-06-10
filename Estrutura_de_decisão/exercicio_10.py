# Programa que recebe o turno em que o usuário estuda e retorna
# "Bom dia" para M - Matutino,
# "Boa tarde" para V - Vespertino,
# "Boa noite" para N - Noturno,
# "Valor inválido" para qualquer valor diferente dos anteriores

horario = input("Digite o horário em que você estuda\n"
                "M - Matutino\n"
                "V - Vespertino\n"
                "N - Noturno\n"
                "Digite aqui: ")

if horario == "M" or horario == "m":
    print("Bom dia!!!!")
elif horario == "V" or horario == "v":
    print("Boa tarde!!!!!")
elif horario == "N" or horario == "n":
    print("Boa noite!!!!!")
else:
    print("Valor inválido")

