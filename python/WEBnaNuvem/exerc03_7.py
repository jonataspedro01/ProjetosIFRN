#Questão7 (exerc07_2)  

numero = int(input("Digite um número inteiro de no máximo 4 dígitos. "))

if  999 <= abs(numero) <= 9999 :
   numero = str(numero)
   print (numero[::-1])
else:
    print("Você digitou mais de 4 digitos")
    
    
  