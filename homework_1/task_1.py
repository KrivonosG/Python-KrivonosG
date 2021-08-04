duration = int(input('Введите продолжительность временного итервала в секундах: '))
day = (duration // 86400) % 7
hour = (duration // 3600) % 24
minute = (duration // 60) % 60
seconds = duration % 60
if hour < 10:
    hour = str('0{0}'.format(str(hour)))
else:
    hour = str(hour)
if minute < 10:
    minute = str('0{0}'.format(str(minute)))
else:
    minute = str(minute)
if seconds < 10:
    seconds = str('0{0}'.format(str(seconds)))
else:
    seconds = str(seconds)
print(str(day), 'дн', str(hour), 'час', str(minute), 'мин', str(seconds), 'сек')