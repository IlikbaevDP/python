# Ваша программа должна выполнять следующие
# действия:
# 1. Получить текст от пользователя: Программа
# должна запросить у пользователя ввод строки
# текста.
# 2. Подсчитать количество гласных и согласных букв:
# Определите, какие буквы считаются гласными
# (например, "а", "е", "и", "о", "у", "ы", "э", "ю", "я" в
# русском языке, а также их заглавные эквиваленты).
# Все остальные буквы алфавита считаются
# согласными.
# Учитывайте только буквы русского алфавита,
# игнорируйте цифры, знаки препинания и пробелы.
# 3. Найти самое длинное слово:
# Разделите текст на слова.
# Определите слово с наибольшей длиной.
# Если есть несколько слов одинаковой
# максимальной длины, выведите любое из них.
# 4. Подсчитать количество вхождений заданного
# слова:
# Программа должна запросить у пользователя слово
# для поиска.
# Подсчитайте, сколько раз это слово встречается в
# тексте (без учета регистра).
# Примеры ввода/вывода
# Ввод:
# Введите текст: Привет мир! Это тестовая строка для
# анализа.
# Введите слово для поиска: мир
# Ожидаемый вывод:
# Гласных букв: 12
# Согласных букв: 16
# Самое длинное слово: тестовая
# Слово 'мир' встречается: 1 раз

# string = input("Введите текст: ")
# search_word = input("Введите слово для поиска: ")
# text = string.upper()
#
# vowels = "АОУЫИЭЕЁЮЯ"
# vowel_count = 0
# consonant_count = 0
#
# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# #
# print("Количество гласных букв:", vowel_count)
# print("Количество согласных букв:", consonant_count)
#
# words = string.split()
# max_word = ""
# for word in words:
#     clean_word = ""
#     for char in word:
#         if char.isalpha():
#             clean_word += char
#     # # сокращенный вариант вложенного цикла:
#     # # clean_word = "".join([c for c in word if c.isalpha()])
#     # if len(clean_word) > len(max_word):
#     #     max_word = clean_word
#
# print("Самое длинное слово:", max_word)
#
#
# normalized_words = []
# for word in words:
#     clean = "".join([c for c in word if c.isalpha()])
#     normalized_words.append(clean)
#
# print("Количество вхождений слова:", normalized_words.count(search_word))
#

# ДЗ_QA415_07.06
#
# name = input("Введите ваше имя: ")
# def greet_and_count():
#  print(f"Привет, {name}! Добро пожаловать")
#
#
#
#
# string = input()
# print(string)
# count = len(string)  # кол-во символов в строке с пробелами
# print("Количество символов в строке: {0}".format(count))
# d = {}
# for char in set(string):
#  d[char] = string.count(char)
# print(d)  # Кол-во всех букв в строке
#
# print(string.replace(' ', ''))  # Строка без пробелов между словами
#
#  Задача 8
# def is_prime(n):
#    if n < 2: return False
#   for i in range(2, n):
#    if n % i == 0:
#     return True
# primes = []
# for num in range(100,1000):
#     if all(num%i!=0 for i in range(2,num)):
#         print (num)

# for num in range(100,1000):
#     if all(num%i!=0 for i in range(2,num)):
#         print (num)
