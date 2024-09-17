def numeros(num1,num2,num3):
    menor=num1
    if num2<menor:
        menor=num2
    if num3<menor:
        menor=num3
    return menor
#programa começa
a,b,c=map(int,input('').split())
if  numeros(a,b,c):
    menor=numeros(a,b,c)
    print(menor)
