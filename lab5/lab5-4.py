# Задача №1 на определения вида треугольника
def type_of_triangle():
    print('Введите 3 числа через пробел')
    a, b, c = list(map(float, input().split()))
    if a <= 0 or b <= 0 or c <= 0:
        print('Треугольник не существует')
    elif a >= (b + c) or b >= (a + c) or c >= (b + a):
        print('Треугольник не существует')
    elif a == b == c:
        print('Треугольник равносторонний')
    elif (a == b) or (b == c) or (a == c):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник общего вида')


type_of_triangle()


# Задача №2 квадратное уравнение
def toFixed(numObj, digits=5):
    return f"{numObj:.{digits}f}"  # Ф-ция, которая добавляет 5 нулей


def square(a, b, c):
    d = b ** 2 - (4 * (a * c))  # Считаем дискриминант
    if d > 0:
        # Если d > 0, то считаем 2 корня
        x1 = (-b - (d ** 0.5)) / 2 * a
        x2 = (-b + (d ** 0.5)) / 2 * a
        print(f'Уравнение\n({toFixed(a)})*X^2 + ({toFixed(b)})*X + ({toFixed(c)}) = 0')
        if x1 != x2:
            # Проверяем на совпадение корней
            print('Количество корней: 2')
            print(f'Первый корень: {toFixed(x1) if x1 < x2 else toFixed(x2)}\nИ второй корень: '
                  f'{toFixed(x1) if x1 > x2 else toFixed(x2)}')
        else:
            print(f'Количество корней: 1\n Этот корень: {toFixed(x1)}')
    elif d == 0:
        # Если d == 0, то один корень
        x1 = (-b) / 2 * a
        print(f'Уравнение\n({a})*X^2 + ({b})*X + ({c}) = 0')
        print(f'Количество корней: 1\n Этот корень: {toFixed(x1)}')
    else:
        # Если d < 0, то корней нет
        print(f'Уравнение\n({a})*X^2 + ({b})*X + ({c}) = 0')
        print('Количество корней: 0')


square(1, 4, 5)


# Задача №3 Поезд

def train(departureH, departureM, totalH, totalM):
    days = totalH // 24  # Считаем кол-во дней в пути
    arriveH = departureH + totalH  # Суммируем время
    arriveM = departureM + totalM
    if arriveH >= 24:
        arriveH %= 24
        if arriveM >= 60:
            arriveH += 1
            arriveM %= 60
    elif arriveM >= 60:
        arriveH += 1
        arriveM %= 60
        if arriveH >= 24:
            arriveH %= 24
    if arriveH < 10 and arriveM < 10:
        print(f'0{arriveH} hours : 0{arriveM} minutes {days} days')
    elif arriveH < 10 and arriveM >= 10:
        print(f'0{arriveH} hours : {arriveM} minutes {days} days')
    elif arriveH > 10 and arriveM < 10:
        print(f'{arriveH} hours : 0{arriveM} minutes {days} days')
    else:
        print(f'{arriveH} hours : {arriveM} minutes {days} days')


train(0,48,48,15)
