
def somar(vet):
    soma=0
    for i in range(len(vetor)):
        soma+=vetor[i]
    return soma


''' inserindo os numeros no vetor '''
tam=int(input(''))
vetor=[None]*tam
for i in range(tam):
    vetor[i]=int(input(''))   
somar(vetor)
mais=somar(vetor) 
print(mais)


''' Dado o vetor '''
vetor=[6,3,8,7, 2,5]
somar(vetor)
conta=somar(vetor)
print(conta)