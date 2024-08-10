# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# Exibe o calendário todo do ano em que deseja
# print(calendar.calendar(2024))

# Mostra o calendário do mês de dezembro-
# print(calendar.month(2024, 12))
#Útimo dia do mês
# print(calendar.monthrange(2024, 12))

# Retorna o nome das semanas
# print(list(calendar.day_name))

# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 12)
# print(calendar.day_name[numero_primeiro_dia])

# data do ultimo dia do mês
# print(calendar.weekday(2022, 12, ultimo_dia))

# Mostra as semanas do mês e ano desejado
for week in calendar.monthcalendar(2024, 1):
  for day in week:
    if day == 0:
      continue
    print(day)