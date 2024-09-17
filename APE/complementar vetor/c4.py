vetor=[]
while True:
    num=int(input(''))
    if vetor.count(num)<1:
        vetor.append(num)
        if len(vetor)==6:
            print(vetor)
            break
    else:
        print(f"valor repetido")
