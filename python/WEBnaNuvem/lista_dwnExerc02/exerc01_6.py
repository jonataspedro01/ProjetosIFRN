#Questão06 (exerc01_6)


vendas= float(input("Digite o valor de mercadorias vendidos : "))
valor2mil = 5/100 * vendas
valor2a8mil = 6/100 * vendas
valor8mil = 8/100 * vendas


if vendas > 0 and vendas <= 2000 :
    print("Sua comissão é no valor de: " , valor2mil)
elif vendas > 2000 and vendas < 8000:
    print("Sua comissão é no valor de: " , valor2a8mil)
else :
    print("Sua comissão é no valor de: " , valor8mil)
