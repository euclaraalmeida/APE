# função criptografia
def cripto(string):
    criptografia=''
    for i in string:
        if i=='A' or i=='a':
            criptografia+='@'
        elif i=='E' or i=='e':
            criptografia+='3'
        elif i=='I' or i=='i':
            criptografia+='!'
        else:
            criptografia+=i
    return criptografia

# start 
frase=input()
frase_cripto=cripto(frase)
print(frase_cripto)
