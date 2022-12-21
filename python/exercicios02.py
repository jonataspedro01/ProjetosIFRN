""" 

#01

numero= int(input("Digite um número inteiro: "))
if numero <0 :
    print('Número negativo')

#02

numero = int(input('Digite um inteiro: '))
if (numero%2) == 0:
    print("Par")

#03

numero = int(input('Digite um inteiro: '))
if (numero%2) == 1:
    print("Impar")
  
#04 

numero = int(input('Digite um inteiro entre 1 e 10: '))
if numero >0 and numero <11 :
    print("Correto")
    
#05

numero = int(input('Digite um inteiro entre 1 e 10: '))
if numero <0 or numero >10 :
    print("Errado")

#06
senhaof = 4531
senha = int(input('Digite sua senha que deve ser igual à 4531: '))
if senha == senhaof :
    print("Senha correta")
else:
    print('Senha incorreta')


#07

valorA = int(input('Digite o valor A: '))
valorB = int(input('Digite o valor B: '))
valorC = int(input('Digite o valor C: '))
if valorA + valorB < valorC:
    print("A soma de A + B é menor que C.")
 
#08

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2 :
    print("O primeiro número é maior que o segundo")
else:
     print("O segundo número é maior que o primeiro")

  
#09

Nascimento = int(input('Digite o seu ano de nascimento: '))
Ano = int(input('Digite o ano atual: '))
idade = Ano - Nascimento
if Nascimento < Ano : 
    print(idade)

 

#10

numero = float(input('Digite um número: '))
resto = numero % 2

if resto == 0: 
   print('Número é par')
else:
    print('Número é ímpar')


#11

primeiroB= int(input("Digite a nota do Primeiro Bimestre : "))
segundoB= int(input("Digite a nota do Segundo Bimestre : "))

media = (primeiroB + segundoB) / 2

if media >= 6: 
   print('Aprovado!')
else:
    print('Reprovado!')




#12

numero= int(input("Digite um número entre 1 e 10 : "))

if numero >=1 and numero <=10 : 
   print('Correto')
else:
    print('Errado')


#13

senhaof = 4531
senha = int(input('Digite sua senha que deve ser igual à 4531: '))
if senha == senhaof :
    print("Senha correta")
else:
    print('Senha incorreta')

#14

primeiro= int(input("Digite o primeiro número : "))
segundo= int(input("Digite o segundo número : "))

if primeiro > segundo : 
   print(f"O primeiro número digitado:   {primeiro} é maior que o segundo:  {segundo}!")
else:
    print(f"O segundo número digitado:  {segundo} é maior que o primeiro:  {primeiro} !")


#15


idade = int(input("Digite sua idade : "))

if idade >= 5 and idade <= 7 :
    print("Categoria infantil")
elif idade >= 8 and idade <= 10 :
     print("Categoria juvenil")
elif idade >= 11 and idade <= 15 :
    print("Categoria adolescente")
elif idade >= 16 and idade <= 30 :
    print("Categoria adulto")
else :
    print("Categoria sênior")
     


#16


idade = int(input("Digite sua idade : "))
    
if idade >= 0 and idade <= 12 :
   print("Faixa etária: Criança") 
elif idade >= 13 and idade <= 17 :
   print("Faixa etária: Adolescente") 
elif idade >= 18 and idade <= 60 :
   print("Faixa etária: Adulto") 
else:
   print ("Idoso")
  

 
#17

peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura: "))
IMC = (peso/altura**2)
print(IMC)
    
if IMC <= 18.5 :
    print("Abaixo do peso") 
elif IMC <= 25:
    print ("Peso normal")
elif IMC  <= 30 :
    print ("Acima do peso")
elif IMC  <= 35 :
    print ("Obesidade grau I")
elif IMC  <= 40 :
    print ("Obesidade grau II")
else:
    print ("Obeso")


 #18
 
salario = int(input("Digite seu salário: "))
quinze = 15/100
dez = 10/100
cinco = 5/100
 
salq = salario * quinze
sald = salario * dez
salc = salario * cinco
 
if salario > 0 and salario <= 300 :
    print("Salário com ajuste: " , salq + salario ) 
elif salario > 300 and salario <= 600:
    print ("Salário com ajuste: " , sald + salario )
elif salario > 600 and salario <= 900:
    print ("Salário com ajuste: " , salc + salario )
else:
    print ("Seu salário não tem ajustes! Salário digitado: " , salario)

"""
#19

    
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digiteo segundo número: "))
num3 = int(input("Digite o terceiro número: "))

Lsta=[num1,num2, num3]

print(sorted(Lsta))