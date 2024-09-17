
tamanho=int(input(''))
vetor=[None]*tamanho
maior_valor=-1000
menor_valor=1000
i_menor=0
i_maior=0
for indice in range(tamanho):
    vetor[indice]=int(input('')) 
    if vetor[indice]>maior_valor:
        maior_valor=vetor[indice]
        i_maior=indice
    if vetor[indice]<menor_valor:
        menor_valor=vetor[indice]
        i_menor=indice
print(f"o maior valor {maior_valor} esta na posição {i_maior}")
print(f"o menor valor {menor_valor} esta na posição {i_menor}")