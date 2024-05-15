n1=int(input('Digite o N1:'))
n2=int(input('Digite o N2:'))
a=n1+n2
s=n1-n2
m=n1*n2
d=n1/n2
pot=n1**n2
di=n1//n2
re=n1%n2
print('A soma dos números vale:{}'.format(a))
print('A subtração \n     ente eles  vale:{}'.format(s))
print('A multiplicação    vale:{}'.format(m), end=', ')
print('A divisão          vale:{:.3f}'.format(d))
print('A potenciação      vale:{}'.format(pot))
print('A divisão inteira  vale:{}'.format(di))
print('O resto da divisão vale:{:.2f}'.format(re))



