tam=int(input(''))
vetor_A=[None]*tam
for i in range(tam):
    vetor_A[i]=int(input(''))
vetor_B=[]
for i in range(tam): #OK
    if vetor_A[i]%2==0:
        vetor_B.append(0)
    if vetor_A[i]%2!=0:
        vetor_B.append(1)
print(f'A={vetor_A}, B={vetor_B}')