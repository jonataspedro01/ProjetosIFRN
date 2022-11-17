#Questão09 (exerc03_09)   

salarioTotal = float(input("Digite o valor do seu salário integral: "))
diasTrabalhados = int(input("Digite quantos dias você trabalhou no último mês: "))
salarioDia = salarioTotal / 22
recebido = salarioDia * diasTrabalhados


if diasTrabalhados > 22 or diasTrabalhados < 0:
    print('Valor incorreto.')
else:
    print('Salário a receber R$:  ', recebido)

