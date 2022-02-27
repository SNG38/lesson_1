
duration = (int)(input('Введите число в секундах: '))

day = duration // 86400
hours = duration % 86400 // 3600
minute = duration % 86400 % 3600 // 60
sec = duration % 86400 % 3600 % 60 % 60
print(day, 'дн', hours, 'час', minute, 'мин', sec, 'сек')




