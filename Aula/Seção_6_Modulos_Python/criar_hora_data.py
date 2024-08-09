# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz


from datetime import datetime
# from pytz import timezone

# A ordem é ano, mês, dia e depois as horas
# data = datetime(2022, 4, 20, 7, 49, 23)
# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# print(data)

# data_str = '2024-04-20 07:29:43'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime.strptime(data_str, data_str_fmt)
# print(data)

# A hora exata de agora
# data = datetime.now(timezone('Asia/Tokyo'))
# data = datetime.now()
# print(data)


data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1723209185))