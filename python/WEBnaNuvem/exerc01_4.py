#Questão04 (exerc01_4)

sexo = input("insira o seu sexo: m ou feminino: ")
peso = int(input("Digite seu peso : "))
altura = float(input("Digite sua altura: "))
IMC = (peso/altura**2)
print(IMC)
   

if (sexo == "m"):  
  if IMC <= 20.7 :
    print("Abaixo do peso") 
elif IMC <= 26.4: 
    print ("Peso normal")
if IMC  <= 27.8: 
    print ("marginalmente acima do peso")
elif IMC  <= 31.1 : 
    print ("Acima do peso ideal")
else:
    print ("Obeso")
    
""" 
    
else (sexo == "feminino"):
      if IMC < 19.1 :
        print("Abaixo do peso") 
elif IMC >= 19.1 or IMC < 25.8:
    print ("Peso normal")
elif IMC >= 25.8 or IMC < 27.3:
    print ("marginalmente acima do peso")
elif IMC >=27.3 or IMC < 32.3 :
    print ("Acima do peso ideal")
else  :
    print("Obesa")
    
    
"""
