# sem usar count
frase=input('')
cont=0
for i in frase:
    if i==' ':
        cont+=1
print(cont)

# usando count
frase=(input())
cont=frase.count(' ')
print(cont)

# criando função
def contador(frase):
    cont=0
    for i in frase:
        if i==' ':
            cont+=1
    return cont

'''start'''

string=(input(''))
cont=contador(string)
print(cont)