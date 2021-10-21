# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))  # Вывод типа переменной number

float_number = 9.0
float_number = int(float_number)
print(float_number)

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
boolean = True
string = 'Some text'
array = list()
dictionary = dict()
print(type(float_number))
print(type(boolean))
print(type(string))
print(type(array))
print(type(dictionary))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

boolean = str(boolean)
number = bool(number)
number = float(number)
