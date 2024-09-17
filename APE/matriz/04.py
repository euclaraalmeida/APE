N_linhas=2
N_col=3
m=[[None]*N_col for i in range(N_linhas)]
n=[[None]*N_linhas for i in range(N_col)]
for i in range(N_linhas):
    for j in range(N_col):
        m[i][j]=int(input(''))
for i in range(N_linhas):
    for j in range(N_col):
        print(f'{m[i][j]:4}',end=' ')
    print()
for i in range(N_linhas):
    for j in range(N_col):
        n[j][i]=m[i][j]
for j in range(N_col):
    for i in range(N_linhas):
        print(f'{n[j][i]:4}',end='  ')
    print()