# def greeting():
#     name = input("Введите ваше имя: ")
#     print("-----")
#     print(f"Привет {name}, добро пожаловать!")
#     print("-----")
#
# greeting()

# def summa(a, b):
#     c = a + b
#     return c
#
# print(summa(2, 2))
#
# result = summa(5, 5) - summa(1, 1) - summa(3,3) * summa(2,6)
# print(result)

# def f(a):
#     global b
#     b += 3
#     print(a + b)
#
# b = 2
# f(b)

# задача 1
# def print_lines(n):
#     print("-" * n)
#     print("-" * n)
#
# n = int(input("Введите количество символов в строке: "))
# print_lines(n)

# задача 2
# def print_rectangle(n):
#     if n < 2:
#         print("Ширина должна не менее 2-х")
#     print("-" * n)
#     print("-" + " " * (n - 2) + "-")
#     print("-" * n)
#
# n = int(input("Введите ширину прямоугольника: "))
# print_rectangle(n)

# задача 3
# def print_triangle():
#     n = int(input("Введите сторону треугольника: "))
#     for i in range(1, n + 1):
#         print("*" * i)
#
# print_triangle()

# 4) Напишите функцию, которая вычисляет среднее
# арифметическое пяти целых чисел.
# Запрашиваем пять чисел
# numbers =[]
# for i in range(5):
#     num = float(input(f"Введите число {i+1}: "))
#     numbers.append(num)
#
# # Вычисляем среднее значение
# average = sum(numbers) / len(numbers)
#
# # Выводим результат
# print(f"Среднее значение введённых чисел: {average:.2f}")

# 5) Напишите функцию, которая находит количество
# цифр в десятичной записи числа.
# def count_digits(number):
#     # Приводим число к положительному значению:
#     number = abs(number)
#     # Инициализируем счётчик:
#     count = 0
#     # Пока число больше 0, выполняем цикл:
#     while number > 0:
#         count += 1
#         number //= 10
#     # Если число равно 0, возвращаем 1:
#     return count if count > 0 else 1
# num = int(input("Введите число: "))
# print("Количество цифр:", count_digits(num))
# задача 7
# Найти периметр треугольника, заданного координатами своих вершин.
# (Определить функцию для расчета длины отрезка по координатам его  вершин.)
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
#
# def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
#
# print(triangle_perimetr(1, 2, 4, 5, 6, 7))


# задача 8
# Найти все трехзначные простые числа.
# (Определить функцию, позволяющую  распознавать простые числа.)

# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# primes = [i for i in range(100, 1000) if is_prime(i)]
# primes = []
# for i in range(100, 1000):
#     if is_prime(i):
#         primes.append(i)
# print(primes)

# Задача 9
# Получить все шестизначные счастливые номера.
# Счастливым называют такое  шестизначное число, в котором сумма
# его первых трёх цифр равна сумме его  последних трёх цифр.
# (Определить функцию для расчета суммы цифр  трёхзначного числа.)

# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return summa
#
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счастливое")
#     else:
#         print("Число не счастливое")
#
# is_lucky(123456)

# Задача 10
# Даны шесть различных чисел.
# Определить максимальное из них.
# (Определить функцию, находящую максимум из двух различных чисел.)

# def max6(a, b, c, d, e, f):
#     return max(a, b, c, d, e, f)
#
# print(max6(2,4,5,6,89, 9))

# Задача 13
# a = 2
# b = 4
# h = 3
# S = (a + b) * h / 2.0
# P = a + b + 2 * (h ** 2 + (a - b) ** 2 / 4) ** 0.5
# print("Площадь равнобедренной трапеции равна =",S)
# print("Периметр равнобедренной трапеции равен =",P)

# Задача 14
#
# import math
#
#
# # Функция для вычисления площади круга
# def calculate_circle_area(radius):
#     return math.pi * radius ** 2
#
#
# # Функция для вычисления площади прямоугольника
# def calculate_rectangle_area(width, height):
#     return width * height


# # Функция для вычисления площади треугольника
# def calculate_triangle_area(base, height):
#     return 0.5 * base * height
#
#
# # Вывод меню выбора фигуры
# print("Выберите фигуру:")
# print("1. Круг")
# print("2. Прямоугольник")
# print("3. Треугольник")
#
# choice = int(input("Введите номер фигуры: "))
#
# if choice == 1:
#     radius = float(input("Введите радиус круга: "))
#     area = calculate_circle_area(radius)
#     print(f"Площадь круга: {area}")
# elif choice == 2:
#     width = float(input("Введите ширину прямоугольника: "))
#     height = float(input("Введите высоту прямоугольника: "))
#     area = calculate_rectangle_area(width, height)
#     print(f"Площадь прямоугольника: {area}")
# elif choice == 3:
#     base = float(input("Введите основание треугольника: "))
#     height = float(input("Введите высоту треугольника: "))
#     area = calculate_triangle_area(base, height)
#     print(f"Площадь треугольника: {area}")
# else:
#     print("Выбрана неверная опция")
#

# 17) Напишите процедуру, которая выводит на экран все делители числа N в одну
# строку через пробел. Используя данную процедуру, составьте программу, которая
# для всех введенных натуральных чисел (числа вводятся до 0, 0 - признак окончания
# ввода) выводит делители текущего числа

# ДЗ_QA415_14.06
#
# 11. Составить программу, в результате которой
# величина а меняется значением с величиной b, а
# величина c – с величиной d. (Определить процедуру,
# осуществляющую обмен значениями двух переменных
# # величин.)4
# a = int(input("Введите значение первой переменной: "))
# b = int(input("Введите значение второй переменной: "))
# a = a + b
# b = a - b
# a = a - b
# print("a это:", a, " b это:", b)
#
# c = int(input("Введите значение третьей переменной: "))
# c = int(input("Введите значение четвертой переменной: "))
# c = c + d
# b = c - d
# c = c - d
# print("c это:", c, " d это:",d)

#  12) Даны стороны двух треугольников. Найти сумму их периметров и сумму их
# площадей. (Определить процедуру для расчета периметра и площади
# треугольника по его сторонам.)
# a = int(input("Первая сторона: "))
# b = int(input("Вторая сторона: "))
# c = int(input("Третья сторона: "))
# print("P треугольника =", a + b + c)
# print("Введите размеры прямоугольника")
# a = float(input("Длина a = "))
# b = float(input("Ширина b = "))
# p = 2*(a + b)
# s = a * b
# print("Периметр Р = 2*(", a, "+", b, ")=", p)
# print("Площадь S = ", a, "*", b, "=", s)