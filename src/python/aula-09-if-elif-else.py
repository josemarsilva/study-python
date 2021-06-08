# aula9-if-elif-else.py

if True:
    print("Verdadeiro")  # observe a hierarquia deslocamento de 4 espacos
    num_1 = 2
    num_2 = 4
    print( "resultado da soma é ", num_1 + num_2 )
else:
    print("Falso")


dia_da_semana = "seg"
if dia_da_semana == "seg":
    print(f"{dia_da_semana}: Segunda-feira")
elif dia_da_semana == "ter":
    print(f"{dia_da_semana}: Terça-feira")
elif dia_da_semana == "qua":
    print(f"{dia_da_semana}: Quarta-feira")
elif dia_da_semana == "qui":
    print(f"{dia_da_semana}: Quinta-feira")
elif dia_da_semana == "sex":
    print(f"{dia_da_semana}: Terça feira")
elif dia_da_semana == "sab":
    print(f"{dia_da_semana}: Sábado")
elif dia_da_semana == "dom":
    print(f"{dia_da_semana}: Domingo")
else:
    print(f"{dia_da_semana}: dia da semana não definido")
