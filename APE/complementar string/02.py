frase=input('')
verifica='a,e,i,o,u, '
frase_cript=''
for i in frase:
    if i in verifica:
        if i=='a':
            frase_cript+=' '
        elif i=='e':
            frase_cript+='u'
        elif i=='i':
            frase_cript+='o' 
        elif i=='o':
            frase_cript+='i'
        elif i=='u':
            frase_cript+='e'
        elif i==' ':
            frase_cript+='a'
    else: 
        frase_cript+=i
print(frase_cript)
            

        