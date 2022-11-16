#Questão04 (exerc01_4)

sexo = str(input("insira o seu sexo: (feminino ou masculino): "))
peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura: "))
IMC = (peso/altura**2)
print(IMC)


if sexo == 'feminino':
   if IMC < 19.1 :
    print("Mulher, Abaixo do peso") 
   elif IMC <= 25.8:
    print ("Mulher no Peso normal")
   elif  IMC <= 27.3:
    print ("Mulher marginalmente acima do peso")
   elif IMC   <= 32.3 :
    print ("Mulher Acima do peso ideal")
   elif  IMC >32.3 :
    print("Mulher Obesa")
    
elif sexo == 'masculino' : 
  if IMC <= 20.7 :
    print("Abaixo do peso")
  elif IMC <= 26.4: 
    print ("Peso normal")
  elif IMC  <= 27.8: 
    print ("marginalmente acima do peso")
  elif IMC  <= 31.1 : 
    print ("Acima do peso ideal")
  else:
    print ("Obeso") 

