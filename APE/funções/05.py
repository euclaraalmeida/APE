def identidade(mat):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j:
                if matriz[i][j]==1:
                    return True
                else:
                    return False
            if i!=j:
                if matriz[i][j]==0:
                    return True
                else:
                    return False
   
        # start

# escolhendo a ordem(tamanho)
ordem=int(input(''))
matriz=[[None]*ordem for i in range(ordem)]
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j]=int(input(f'{[i]}x{[j]}'))


for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz[i][j]:4}',end=' ')
    print()

if identidade(matriz):
    print('É identidade')
else:
    print('Não é identidade')

# dado a ordem
ordem=3
matriz=[[None]*ordem for i in range(ordem)]
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j]=int(input(f'{[i]}x{[j]}'))


for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz[i][j]:4}',end=' ')
    print()

if identidade(matriz):
    print('É identidade')
else:
    print('Não é')