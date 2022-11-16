#Questão03 (exerc01_3)


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
else:
    print ("Obeso")
