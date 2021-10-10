import datetime

date_and_time = datetime.datetime(2019, 10, 10, 9, 15, 30)

#strftime crea un string a partir de un obj date_and_time
date_and_time.strftime('%Y-%m-%d')
date_and_time.strftime('%Y-%m-%d %H:%M:%S')
date_and_time.strftime('%Y/%m/%d')
date_and_time.strftime('%Y-%m-%d T%H:%M:%S')

#la funcion strptime crea un objeto datetime a partir de un string
datetime.datetime.strptime('2019-01-10', '%Y-%m-%d')

#con horas min sec
datetime.datetime.strptime('2019-01-10 11:30:25', '%Y-%m-%d %H:%M:%S')

#con caracter T agregado
datetime.datetime.strptime('2019-01-10 T11:30:25', '%Y-%m-%d T%H:%M:%S')
