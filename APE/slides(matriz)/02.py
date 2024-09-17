linha=int(input(''))
coluna=linha
matriz=[[None]*coluna for i in range(linha)]
for i in range(linha):
    for y in range(coluna):
        matriz[i][y]=i+y
for i in range(linha):
    for y in range(coluna):
        print(f'{matriz[i][y]:4}', end=' ')
    print()
