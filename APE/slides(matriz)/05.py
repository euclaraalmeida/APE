linhas=2
colunas=3
matriz_A=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz_A[i][j]=int(input(''))
matriz_B=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz_B[i][j]= matriz_A[i][j]*2
        print(f'{matriz_B[i][j]:4}',end='')
    print()
