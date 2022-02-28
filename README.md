Задание 1. 
Здравствуйте, были вопросы по поводу решения, у меня был вариант: 


duration = input(int('Введите число в секундах'))

if duration < 604800:
     print('{} дн'.format(duration))
elif duration < 86400 :
     print('{} час'.format(duration))
elif duration < 3600:
     print('{} мин'.format(duration))
elif duration < 60:
     print('{} сек'.format(duration))

result = duration
print(result)


Но я так и не понял почему у меня не получилось реализовать правильно.
