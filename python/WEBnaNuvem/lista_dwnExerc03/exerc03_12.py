#Questão12 (exerc03_12)   

aplicacao = float(input("Digite o valor da aplicação: "))
quantidadeMes = int(input("Digite quantos meses de investimento: "))
rendimento = 5/100

vf = aplicacao * (1+rendimento) ** quantidadeMes

if vf > 200: 
 print('Valor apos ',quantidadeMes,' meses: R$ ',vf)

# 

aplicado = 100.00
rendimento = 0

while aplicado <= 200:
    aplicado = aplicado + (aplicado * (5 / 100.00))
    rendimento = rendimento + 1

print("Capital investido será de: ",rendimento, aplicado)