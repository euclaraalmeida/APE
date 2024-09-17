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
vetor_A=[] 
for i in range(linha):
    for j in range(coluna):
        if i==j:
            vetor_A.append(matriz[i][j])
print(f'{vetor_A}')
vetor_b=[]
for i in range(linha):
    for j in range(coluna):
        if i+j==linha-1:
            vetor_b.append(matriz[i][j])
print(f'{vetor_b}')      
