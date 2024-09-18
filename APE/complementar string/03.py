nome=input().upper()
divisao=nome.split( )
print(f'{divisao[-1]}',end=',')
for j in range(len(divisao)-1):
    print(f'{divisao[j][0]}',end='.')
