import math
from math import sqrt

# Переменные булева типа могут принимать только два значения.
# С помощью оператора сравнения == выведите два возможных значения переменной is_equal.
# Обратите внимание на результат применения функции int() к булевому значению.


two = 2

three = 3

is_equal = two == three
is_greater = three >= two
print(is_greater, is_equal)

#

print(int(True))

#

print(str(False))

"""
В языке Python поддерживается множество операций сравнения( ==, >=, < и т.д.).
Все подобные операции имеют одинаковый приоритет. Результат сравнения - булева переменная.
Сравнения могут осуществляться в любом порядке.
"""

one = 1

two = 2

three = 3

print(one < two < three)  # Сравнения (one < two) и (two < three) происходят в одно и то же время.

# Создайте несколько переменных и осуществите различные сравнения между ними, выведите результаты в консоль.

print(two >= one)
print(two == two)
char_a = 'A'
char_b = 'b'
print(char_a > char_b)
print(char_a < char_b)
print(char_a == char_b)

# name = input('Имя:')
# print(f'Hello, {name}')

# equation
x = 10
y1 = 1 / sqrt(abs(1 - x ** 4 - x ** 2))
print(y1)
y2 = math.e ** sqrt(x + sqrt(x))
print(y2)
y3 = ((x ** 2 + 1) / (3 * (x ** 2 - 1))) + (x ** 2 - 1) * (1 - x)
print(y3)
y4 = sqrt(x + sqrt(x + x))
print(y4)
# geometry  №1
a = int(input("Введите длину ребра: "))
print(a*(math.sqrt(3))/2)
