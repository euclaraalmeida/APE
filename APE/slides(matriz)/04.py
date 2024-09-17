import random
linhas=3
colunas=5
matriz=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j]=random.randint(1,10)
        print(f'{matriz[i][j]:4}', end=' ')
    print()
    
for i in range(linhas):
    soma=0
    for j in range(colunas):
        soma+=matriz[i][j]
    print(F'soma de cada linha{soma:3}')
for j in range(colunas):
    soma=0
    for i in range(linhas):
        soma+=matriz[i][j]
    print(F'soma de cada coluna{soma:5}')

