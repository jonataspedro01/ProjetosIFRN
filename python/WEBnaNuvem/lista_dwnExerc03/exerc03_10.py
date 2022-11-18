def main():

    n = int(input("Digite o valor de n: "))
    soma = 0
  
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor

    if n == soma:
        print(n,"É perfeito")
    else: 
        print(n,"Não é perfeito" )

main()