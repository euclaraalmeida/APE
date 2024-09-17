def fatorial(n):
    mult=1
    for i in range(1,valor+1):
        mult*=i
    return mult
# programa start
valor=int(input(''))
fatorial(valor)
mult=fatorial(valor)
print(mult)
