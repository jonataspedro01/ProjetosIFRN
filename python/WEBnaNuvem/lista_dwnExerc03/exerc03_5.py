
soma = 0
impar = 1
result = 1

for i in range(1,31):
     if i % 2 == 0:
      result = result * i
      print("Multiplicação do números pares", result)
     else:
      soma += impar
      impar += 2
      print("Soma dos números impares",soma)
  
# Daiane

soma = 0
impar = 1
numero = int(input('Digite um número ímpar entre 1 e 30: '))
for i in range(numero):
    soma += impar
    impar += 2
print("A soma dos números ímpar são: ",soma)


multiplicação = 2
par = 2
numero = int(input('Digite um número par entre 1 e 30: '))
for i in range(numero):
    numero *= par
    par *= 2
print("A multiplicação dos números par são: ",numero)
      
      
