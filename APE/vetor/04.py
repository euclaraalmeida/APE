n=10
vetor=[None]*n
for i in range(n):
    vetor[i]=int(input(''))
for i in range(n):
    if i%2==0:
        print(f'{vetor[i]}  e esta na posiçao{i} é par')
    if i%2!=0:
        print(f'{vetor[i]}  e esta na posiçao{i} é impar')
        

