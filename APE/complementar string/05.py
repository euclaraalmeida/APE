frase=(input(''))
resul=''
for i in range(len(frase)):
        resul=frase[i]*(i+1)
        print(resul) 
for i in range(len(frase)-2,-1,-1):
        resul=frase[i]*(i+1)
        print(resul) 

