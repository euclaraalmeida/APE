total=int(input(''))
vetor=[None]*total
par=0
impar=0
cp=0
ci=0
cont=0
soma=0
for i in range(total):
    vetor[i]=int(input(''))
    soma=soma+vetor[i]
    cont+=1
    if vetor[i]%2==0:
        cp+=1
    if vetor[i]%2!=0:
        ci+=1
media=soma/cont
print(f"{cp}  par(es)")
print(f"{ci}  impar(es) ")
print(f"{soma} soma dos resultados")
print(f"media: {media}")
