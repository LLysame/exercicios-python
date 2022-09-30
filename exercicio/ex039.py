# faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com sua idade, se ele ainda
# vai se alistar ao serviços militar, se é a hora de se
# alistar ou se ja passou fo tempo do alistamento.Seu
# programa também deverá mostrar o tempo que falta ou
# que passou do prazo.

# from datetime import date
# nasc = int(input('ano de nascimento: '))
# ano_atual = date.today().year
# idade=ano_atual-nasc
# print('quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,ano_atual))
# if idade<18:
#     saldo = 18-idade
#     ano=ano_atual+saldo
#     print('\033[33mainda faltam\033[m {} anos para o alistamento.'.format(saldo))
#     print('seu alistamento vai ser no ano de {}.'.format(ano))
# elif idade>18:
#     saldo = idade-18
#     ano=ano_atual-saldo
#     print('\033[31mESTA ATRASADO!!!\033[m, deveria se alistar há {} anos atrás'.format(saldo))
#     print('seu alistamento foi em {}'.format(ano))
# else:
#     print('você deve se alistar \033[31mIMEDIATAMENTE!!!\033[m')
