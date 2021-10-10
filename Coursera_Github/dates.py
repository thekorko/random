# _*_ coding utf-8 _*_

import datetime #Lib para trabajar con fechas

#date objects
#objetio de tipo date
date = datetime.date(2019, 4, 30)

#le podemos pedir los atributos
#año
print(date.year)
#mes
date.month
#dia
date.day

#funcion que devuelve el dia de la semana de esa fecha
date.weekday()
#la funcion isoweekday devuelve lo mismo pero el lunes es el dia uno y el domingo el dia 7
date.isoweekday()

#la funcion isocalendar devuelve una tupla con 3 elementos: año, numero de la semana y dia de la semana
date.isocalendar()
#(2019, 18, 2)

#devuelve una string "YYYY-MM-DD"
date.isoformat()
#2019-04-30

#fecha minima
date_min = datetime.date.min
#(1, 1, 1)

#fecha max
date_min = datetime.date.min
#(9999, 12, 31)

#dia de hoy
today = datetime.date.today()

#el dia de ayer
yesterday = today - datetime.timedelta(days=1)

#resta de dos fechas
delta = today - yesterday

#datetime objects
#fecha y hora
date_and_time = datetime.datetime(2019, 10, 10, 9, 15, 30)
#año, mes, dia, hora, minutos, segundos


#pedirle datos
date_and_time.year
date_and_time.month
date_and_time.day
date_and_time.hour
date_and_time.minute
date_and_time.second
date_and_time.microsecond


#objetos de tipo hora
#Hora minima
time_min = datetime.time.min

#Hora maxima
time_max = datetime.time.max

#solo la hora
date_and_time.date()

#fecha y hora actual
now = datetime.datetime.now()

#La fecha y hora actual en UTC
now = datetime.datetime.utcnow()
