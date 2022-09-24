#Escreva um programa que pergunte o salario de um funcionario
#  e calcule o valor do seu aumento.
#Para salario superiores a R$1.250,00, calcule um aumento de
#  10%. Para os inferiores ou iguais o aumento e de 15%.

print('='*60)
Qual_valor = int(input('qual o seu ?: '))
print('-'*60)
if Qual_valor <= 1250:
    novo_salario = Qual_valor + (Qual_valor * 15 / 100)
    print('seu novo salario e de {} !'.format(novo_salario))
else:
    novo_salario = Qual_valor - (Qual_valor * 10 / 100)
    print('seu novo salario e de {}'.format(novo_salario))
print('='*60)