from random import randint

name = input('Ваше имя?')
surname = input('Ваша фамилия?')
group = input('Ваша группа?')
print(f'Привет, {surname} {name} из группы {group}!')
email = input('Введите свою электронную почту?')
print(surname[:5].lower() + name[:5].lower() * 2 + email[:5].lower() * 3)

random_num = 2

print(random_num * '   _~_    ')
print(random_num * '  (o o)   ')
print(random_num * ' /  V  \  ')
print(random_num * '/(  _  )\ ')
print(random_num * '  ^^ ^^   ')

