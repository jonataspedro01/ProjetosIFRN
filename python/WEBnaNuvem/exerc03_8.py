#Questão08 (exerc03_08)    

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'não é primo')
            break
    else:
        print(num, 'é primo')
elif num == 0:
    print(num, 'é zero')
elif num == 1:
    print(num, 'é um')
else:
    print(num, 'é negativo')