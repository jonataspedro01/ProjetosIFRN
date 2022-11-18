
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
  

      
      
