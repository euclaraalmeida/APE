N_linhas=2
N_col=2
matriz_A=[[None]*N_col for i in range(N_linhas)]
matriz_b=[[None] *N_col for i in range(N_linhas)]
c=[[None]*N_col for i in range(N_linhas)]
for i in range(N_linhas):
    for j in range(N_col):
        matriz_A[i][j]=int(input(''))
for i in range(N_linhas):
    for j in range(N_col):
         matriz_b[i][j]=int(input(''))
for i in range(N_linhas):
    for j in range(N_col):
        c[i][j]=matriz_A[i][j]+matriz_b[i][j]
        print(f'{c[i][j]:4}',end=' ')
    print()