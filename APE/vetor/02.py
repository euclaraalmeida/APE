total=3
vetor=[None]*total
cont=0
k=int(input(''))
for indice in range(total):
    vetor[indice]=int(input(''))
    if vetor[indice]==k:
        cont+=1
print(cont)