import random
linhas=int(input(''))
colunas=linhas
matriz_a=[[None]*colunas for i in range(linhas)]
matriz_b=[[None]*colunas for i in range(linhas)]
print('¨¨¨¨¨¨¨¨¨¨¨¨matriz a¨¨¨¨¨¨¨¨¨¨¨')
for i in range(linhas):
    for j in range(colunas):
        matriz_a[i][j]=random.randint(1,10)
        print(f'{matriz_a[i][j]:4}',end=' ')
    print()
print('¨¨¨¨¨¨¨¨¨¨¨¨¨matriz B¨¨¨¨¨¨¨¨¨¨¨¨')
for i in range(linhas):
    for j in range(colunas):
        matriz_b[i][j]=i+j
        matriz_b[i][j]=matriz_b[i][j]+matriz_a[i][j]
for i in range(linhas):
    for j in range(colunas):
        if i==j or i+j==linhas-1:
            matriz_b[i][j]=0
for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz_b[i][j]:4}', end=' ')
    print()
    
