a = b = 2  # Пример множественного оператора присваивания.
# Обратите внимание на значения переменных a и b после выполнения данной операции.

print("a = " + str(a))  # Функция str() используется для приведения типа аргумента к строковому

print("b = " + str(b))  # Убраны ковычки, чтобы операция str выполнилась верно

hello = 'Привет'  # Исправлена ошибка с ковычками (были неоднородные ковычки)

print("hello = " + str(hello))  # Изменен регистр ф-ции print

# Переопределите значение переменной hello
greeting = hello  # Переопределил значение переменной hello

print("hello = " + str(hello))

# Создайте ещё несколько переменных, а затем осуществите их вывод через пробел
first_var = 30
second_var = 'Some text'

print(first_var, second_var)