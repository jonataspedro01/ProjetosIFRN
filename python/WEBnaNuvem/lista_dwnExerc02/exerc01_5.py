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