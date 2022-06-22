import calendar
import pandas as pd

monthNumber = int(input("Insira o número do mês: "))
month = calendar.monthcalendar(2022,monthNumber)

def day_names(month):
    monthdaysdic = {'segunda':[],'terça':[],'quarta':[],'quinta':[],'sexta':[],'sabado':[],'domingo':[]}

    for week in month:
        for day in range(len(week)):

            if week[day] != 0:
                if day == 0:
                    monthdaysdic['segunda'].append(week[day])
                elif day == 1:
                    monthdaysdic['terça'].append(week[day])

                elif day == 2:
                    monthdaysdic['quarta'].append(week[day])

                elif day == 3:
                    monthdaysdic['quinta'].append(week[day])

                elif day == 4:
                    monthdaysdic['sexta'].append(week[day])

                elif day == 5:
                    monthdaysdic['sabado'].append(week[day])
                elif day == 6:
                    monthdaysdic['domingo'].append(week[day])
    return monthdaysdic

segunda_horario = input('Insira seu horário na segunda: ')
segunda_descrição = input('Insira sua descrição na segunda: ')

terça_horario = input('Insira seu horário na terça: ')
terça_descrição = input('Insira sua descrição na terça: ')

quarta_horario = input('Insira seu horário na quarta: ')
quarta_descrição = input('Insira sua descrição na quarta: ')

quinta_horario = input('Insira seu horário na quinta: ')
quinta_descrição = input('Insira sua descrição na quinta: ')

sexta_horario = input('Insira seu horário na sexta: ')
sexta_descrição = input('Insira sua descrição na sexta: ')

sabado_horario = input('Insira seu horário no sabado: ')
sabado_descrição = input('Insira sua descrição no sabado: ')

domingo_horario = input('Insira seu horário no domingo: ')
domingo_descrição = input('Insira sua descrição no domingo: ')

dn = day_names(month)
tabela = {'dia':[dia for dia in range(1,32)],'horario':[],'descrição':[]}

for i in tabela['dia']:
    if i in dn['segunda']:
        tabela['horario'].append(segunda_horario)
        tabela['descrição'].append(segunda_descrição)
    elif i in dn['terça']:
        tabela['horario'].append(terça_horario)
        tabela['descrição'].append(terça_descrição)
    elif i in dn['quarta']:
        tabela['horario'].append(quarta_horario)
        tabela['descrição'].append(quarta_descrição)
    elif i in dn['quinta']:
        tabela['horario'].append(quinta_horario)
        tabela['descrição'].append(quinta_descrição)
    elif i in dn['sexta']:
        tabela['horario'].append(sexta_horario)
        tabela['descrição'].append(sexta_descrição)
    elif i in dn['sabado']:
        tabela['horario'].append(sabado_horario)
        tabela['descrição'].append(sabado_horario)
    else:
        tabela['horario'].append(domingo_horario)
        tabela['descrição'].append(domingo_descrição)

tabela_df = pd.DataFrame(tabela)
print(tabela_df)
tabela_df.to_csv('frequencia.csv',index=False,encoding='utf-16')