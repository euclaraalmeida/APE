linha=int(input(''))
coluna=int(input(''))
matriz=[[None]*coluna for i in range(linha)]
for i in range(linha):
    for j in range(coluna):
        matriz[i][j]=int(input(f'{[i]}x{[j]}='))
s=0
for i in range(linha): 
    for j in range(coluna):
        s+=matriz[i][j]
print(f'{s}',end=' ')
