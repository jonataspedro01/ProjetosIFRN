#Questão03 (exerc03_3)    

num = int(input("Digite um número de 1 a 12 : "))

def verificadia_semana(num):
    dicionario_mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 
        'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 
        8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
        11: 'Novembro', 12: 'Dezembro' }
    while (num !=0 and num < 13 and num >0):
            print(dicionario_mes[num])
            num = int(input("Digite outro número de 1 a 12 : "))
    else:
      print("Mês inválido")

verificadia_semana(num)