lista = [4,10,5]
lista.extend([14,2])
print(lista)

lista = [4,10,5,4]
print(lista.count(4))

lista = [4,10,5]
lista.append(7)
print(lista)

lista = [4,10,5]
lista.insert(1, 100)
print(lista)

'''
LISTA DE EXERCICIOS
''' 

#01 lista 05

lista = [1,2,3,4,5]
for num in lista:
    print(num)

#02 lista 05

lista = []
for num in range(5):
  valor =  int(input("Digite um número: "))
  lista.append(valor)

for num in lista:
    print(num)