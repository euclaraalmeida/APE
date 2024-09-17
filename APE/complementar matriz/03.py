ord=3
coluna=ord
matriz=[[None]*coluna for i in range(ord)]
for i in range(ord):
    for j in range(coluna):
        matriz[i][j]=int(input(''))
for i in range(ord):
    for j in range(coluna):
        print(f'{matriz[i][j]:4}', end=' ')
    print()
    mt=0
for i in range(ord):
    for j in range(coluna):
        mt+=matriz[i][j]
for i in range(ord):
    sl=0
    for j in range(coluna):
        sl+=matriz[i][j]
    print(f'linha{sl:3}')
    
for j in range(coluna):
    sc=0
    for i in range(ord):
        sc+=matriz[i][j]
    print(f'coluna{sc:3}')
    sd=0
for i in range(ord):
    for j in range(coluna):
        if i==j:
            sd+=matriz[i][j]
    ss=0
for i in range(ord):
    for j in range(coluna):
        if i+j==ord-1:
            ss+=matriz[i][j]
print(f'diag{sd}')
print(f'diag secund{ss}')
print(f'matriz toda{mt}')
