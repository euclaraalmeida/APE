tamanho=int(input(''))
vetor_a=[None]*tamanho
vetor_b=[None]*tamanho
mult=int(input(''))
for indice in range(tamanho):
    vetor_a[indice]=int(input(''))
    vetor_b[indice]=vetor_a[indice]*mult
for i in vetor_a:
    print(i)
for y in vetor_b:
    print(y)