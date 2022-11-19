#Questão05 (exerc01_5)

ladoA = int(input("Digite o valor A : "))
ladoB = int(input("Digite o valor B : "))
ladoC = int(input("Digite o valor C : "))

somaAB = ladoA + ladoB
somaAC = ladoA + ladoC
somaBC = ladoB + ladoC

if somaAB <= ladoC :
    print("Os valores informados não podem ser os lados de um triângulo")
elif somaAC <= ladoB :
    print("Os valores informados não podem ser os lados de um triângulo")
elif somaBC <= ladoA :
    print("Os valores informados não podem ser os lados de um triângulo")
else :
    print("Os valores informados podem ser lados de um triângulo")
    

# Daiane

lado1 = int(input("Digite um valor: "))
lado2 = int(input("Digite um valor: "))
lado3 = int(input("Digite um valor: "))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
        print('Nao é um triangulo')
elif (lado1 == lado2) and (lado1 == lado3) :
        print('Equilatero')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('Isósceles')
else:
        print('Escaleno')
#