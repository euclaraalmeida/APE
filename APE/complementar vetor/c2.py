n=int(input(''))
vetor_A=[None]*n
vetor_B=[None]*n
for i in range(n):
    vetor_A[i]=int(input(''))
for i in range(n):
    vetor_B[i]=int(input(''))
c=[]
for i in range(n):
    c.append(vetor_A[i])
    c.append(vetor_B[i])
    print(f"{c}")