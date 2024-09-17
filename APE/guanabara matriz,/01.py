linha=4
coluna=4
matriz=[[None]*coluna for i in range(linha)]
for i in range(linha):
    for j in range(coluna):
        matriz[i][j]=int(input(''))
for i in range(linha):
    for j in range(coluna):
        print(f'{matriz[i][j]:4}',end='')
    print()

for i in range(linha):
    sp=0
    for j in range(coluna):
        if matriz[i][j]%2==0:
            sp+=matriz[i][j]

for j in range(coluna):
    sc=0
    for i in range(linha):
        if j==3:
            sc+=matriz[i][j]
maior=-1000
for i in range(linha):
    for j in range(coluna):
        if i==2:
            if matriz[i][j]>maior:
                maior=matriz[i][j]
print(f'soma par {sp}')
print(f'soma 3 coluna {sc}')
print(f'o maior da 2 linha {maior}')




