total=3
vetor=[None]*total
for i in range(total):
    vetor[i]=int(input(''))
for y in vetor:
    if vetor.count(y)==1:
        print(f" {y} é distinto")
   

