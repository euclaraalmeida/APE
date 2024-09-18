# função para contar quantas vezes N aparece na matriz
def conta(n,mat):
    cont=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==n:
                cont+=1
    return cont
 
#  start 
a=int(input(''))
ordem=2
matriz=[[None]*ordem for i in range(ordem)]

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j]=int(input(''))

# chamando a função conta
contador=conta(a,matriz)
if contador:
    print(contador)

# printando a matriz
for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz[i][j]:4}', end='')
    print()