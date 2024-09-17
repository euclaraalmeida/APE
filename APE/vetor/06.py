total=int(input(''))
vetor=[None]*total
for y in range(total):
    vetor[y]=int(input(''))
print(vetor)
for y in range(total):
    vetor.sort(reverse=True)
print(vetor)