import random
linhas=int(input(''))
colunas=int(input(''))
matriz=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j]=random.randint(1,20)
        print(f'{matriz[i][j]:4}',end='')
    print()
    maior=matriz[0][0]
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j]>maior:
            maior=matriz[i][j]
print(maior)
