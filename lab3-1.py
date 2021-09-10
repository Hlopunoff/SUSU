# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).

# Python поддерживает умножение строк на числа.

hello = "Hello "

world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных
hello_world = hello + world
print(hello_world)

# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками

print('Hello'*10)

# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками
print('Hello, World! ' + 'World '*2 + 'Hello Hello!')


# Вы можете получить доступ к символу строки, если знаете его позицию. Например, str[index] даст символ в позиции
# index в строке str.

# Запомните! Строки всегда индексируются с 0.

python = "Python"
python = python.replace('o', '')
python = python.replace('y', '')

# p_letter = ??? # Используйте переменную python для получения строки "pthn".
p_letter = python
print(p_letter)


# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки. Обратите
# внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1. Таким образом, вы можете
# использовать отрицательные числа в операторе индексирования для подсчета символов с конца строки.

long_string = "This is a very long string!"

# Используйте отрицательный индекс для получения символа '!' из строки
print(long_string[-1])
