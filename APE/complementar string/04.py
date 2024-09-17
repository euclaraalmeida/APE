s=input()
n=int(input())
verifica='a,e,i,o,u'
frase=''
for i in s:
    if i in verifica:
        frase+=i*n
    else:
        frase+=i
print(frase)

