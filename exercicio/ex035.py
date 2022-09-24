# desenvolva um programa que leia o comprimento de três 
# retas e diga ao usuario se elas podem ou não formar 
# um triangulo.

raio1 = float(input('Primeiro numero: '))
raio2 = float(input('Segundo numero: '))
raio3 = float(input('Terceiro numero: '))
if raio1<raio2+raio3 and raio2<raio1+raio3 and raio3<raio1+raio2:
    print('Então pode fazer um tringulo!!!!!')
else:
    print('Não pode fazer um triangulo!!!!')