""" Функции - это удобный способ разделить ваш код на полезные блоки, сделать его более читабельным и помочь
в его повторном использовании.

Функции определяются с помощью ключевого слова def, за которым следует имя функции. """


def hello_world():  # Функция с именем "hello_world"
    print("Hello, World!")  # Обратите внимание на отступ!


# Определите функцию с именем fun, печатающую при своем вызове любой афоризм
def fun(aphorism):
    print(aphorism)


some_text = input()
fun(some_text)

# Это основная программа (Напишите эту заметку при написании основной программы)

for i in range(3):
    hello_world()  # вызов функции, определенной выше


# замените дубликаты строк в файле (реализуйте подпрограмму, которая печатает сообщение на экран)

def print_something(text):
    for i in range(3):
        print(text)


print_something('I want to be a function')
# -----------------------------------------------------------------------------------------#


""" Параметры функции определены в скобках (), следующих после имени функции.  

Параметры ведут себя как переменные, видимые исключительно внутри тела функции """


def foo(x):  # x - параметр функции
    print("x = " + str(x))


foo(5)  # Здесь мы вызываем функцию foo, передавая 5 в качестве аргумента.


# Определите функцию с именем square, печатающую квадрат передаваемого ей значения.
def square(n):
    print(n ** 2)


square(4)
square(8)
square(15)
square(23)
square(42)

# -----------------------------------------------------------------------------------------#


""" Функции могут возвращать значения, использую ключевое слово return.  

Вы можете использовать возвращаемое значение, чтобы присвоить его переменной или просто вывести его на экран. """


def sum_two_numbers(a, b):
    return a + b  # возвращаем результат


c = sum_two_numbers(3, 12)  # присвоить результат переменной 'c'


# В последовательности Фибоначчи первые два числа равны 1 и 1, и каждое следующее число равно сумме двух предыдущих.
# Напишите функцию, возвращающую список из чисел Фибоначчи до n.

def fib(n):
    """Эта строка документации для данной функции. Она будет доступна по fib.__doc__()
        Возвращает список, содержащий числа Фибоначчи до n
    """

    result = [1]
    a = 1
    b = 1
    for __ in range(n):
        a, b = b, a + b
        result.append(a)

    return result


print(fib(10))
