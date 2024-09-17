LINHAS=5
COLUNAS=4
matriz=[[None]*COLUNAS for i in range(LINHAS)]
for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j]=int(input(''))
    media=0
for i in range(LINHAS):
    for j in range(COLUNAS):
        media+=matriz[i][j]/3
        if j==4:
            matriz[i][j].append(media)
        print(f'{matriz[i][j]:4}', end =' ')
    print()

