dia,mes,ano=(input().split('/'))
nome=input('').split()
m=nome[0].capitalize()
m_2=nome[-1].capitalize()
tudo_m=m+m_2
print(tudo_m)
junto=ano+mes+dia+'_'+tudo_m
print(junto)