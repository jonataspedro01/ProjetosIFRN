arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

print(linhas)


colunas = linhas[0].slipt(',')
print(colunas[1])