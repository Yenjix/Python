from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual=datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H/%M/%S'))
    #print(data_atual.strftime('%H/%M/%S')) #Hora
    print(data_atual.strftime('%c'))
    print(data_atual.day) #.hour .year .minute .second .date ...
    print(data_atual.weekday()) #.month
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()]) # traduzindo o dia da semana
    data_criada=datetime(2018,6,20,15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string='01/01/2019 12:20:22'
    #como converter a data q ta em STRING em DATETIME
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    print(type(data_convertida))
    nova_data=data_convertida - timedelta(days=365, hours=2, minutes=15) #subtração de dias
    print(nova_data)

def trabalhando_com_date():
    data_atual=date.today()
    print(data_atual)
    print(type(data_atual))
    print(data_atual.strftime('%d/%m/%y'))#escrevendo a data no formato do brasil
    #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    print(data_atual.strftime('%A %B %Y'))
    data_atual_str=data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

#criar em formato de horario
def trabalhando_com_time():
    horario(hour=15,minute=18,second=30)
    print(horario)
    print(type(horario))
    print(horario.strftime('%H:%M:%S'))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()