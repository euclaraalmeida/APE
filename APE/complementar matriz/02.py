# import random
linhas=int(input(''))
colunas=linhas
matriz=[[None]*colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j]=int(input(''))
        print(f'{matriz[i][j]:4}', end=' ')
    print()
    sl=0
for i in range(linhas):
    for j in range(colunas):
        sl+=matriz[i][j]
        print(f'{sl}')
    sc=0
for j in range(colunas):
    for i in range(linhas):
        sc+=matriz[i][j]
        print(f'{sc}')
    sd=0
for i in range(linhas):
    for j in range(colunas):
        if i==j:
            sd+=matriz[i][j]
            print(f'{sd}')
if sl==sd and sl==sc:
    print('é um quandrado perfeito')
else:
    print('nao é um quadrado perfeito')
