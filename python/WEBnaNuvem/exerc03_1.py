#Questão01 (exerc03_1)
"""
dia = int(input("Digite um dia da semana de 1 a 7 : "))

if dia == 1 :
    print("Segunda-feira " )
elif dia == 2 :
    print("Terça-feira " )
elif dia == 3 :
    print("Quarta-feira " )
elif dia == 4 :
    print("Quinta-feira " )
elif dia == 5 :
    print("Sexta-feira " )
elif dia == 6 :
    print("Sábado" )
elif dia == 7 :
    print("Domingo " )
elif dia < 1 or dia > 7:
    print("Valor não correspondente")
    
# Outra forma, porém usando valores de 0 a 6:


dia = int(input("Digite um dia da semana de 0 a 6 : "))
sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

if dia > -1 and dia <= 4:
    print(f"Tenha uma boa {sem[dia]}-feira =D")
elif dia > 4 and dia <=6:
    print(f"Tenha um bom {sem[dia]} =D")
elif dia < 0 or dia > 6:
    print("Valor não correspondente")

"""

# Outra forma

dia_semana = int(input('Digite um número de (1 a 7): '))

def verificadia_semana(dia_semana):
    dicionario_dia_semana = {1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sabado', 7: 'Domingo'}
    for dia in dicionario_dia_semana:
        if dia_semana == dia:
            print(dicionario_dia_semana[dia])
            break
    else:
        print('Dia não encontrando')

verificadia_semana(dia_semana)