n_apostadores=4
n_apostas=2
matriz=[[None]*n_apostas for i in range(n_apostadores)]
for i in range(n_apostadores):
    for j in range(n_apostas):
        matriz[i][j]=int(input('digite a aposta'))
        cont=0
        if matriz[i][j]>=1 and matriz[i][j]<=80:
            matriz.append(matriz[j])
            
            if (6,7) in matriz[j]:
                cont+=1
print(cont)




