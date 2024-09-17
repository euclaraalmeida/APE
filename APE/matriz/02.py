import random
linhas=int(input(''))
colunas=linhas
matriz=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j]=random.randint(1,10)
        print(f'{matriz[i][j]:4}',end=' ')
    print()
for i in range(linhas):
    for j in range(colunas):
        if i==j:
            print(f'{matriz[i][j]}')