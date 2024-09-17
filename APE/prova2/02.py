linha=20
colunas=50
k=int(input(''))
matriz=[[None]*colunas for i in range(linha)]
for i in range(linha):
    for j in range(colunas):
        matriz[i][j]=int(input(''))
for i in range(linha):
    for j in range(colunas):
        print(f'{matriz[i][j]:4}',end='')
    print()
for i in range(linha):    #ok
    for j in range(colunas):
        if matriz[i][j]==k:
            print(f'{k} aparece na posiçao [{i}][{j}]')

