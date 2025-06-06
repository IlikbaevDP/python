# 5. Задача о числах Фибоначчи:
# Напишите программу, которая выводит первые 10 чисел
# Фибоначчи.
from functools import total_ordering
from itertools import count

from my import result

# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b
#

#6. Задача о выводе чисел в обратном порядке:
#Напишите программу, которая выводит числа от 10 до 1
#в обратном порядке.
# for i in  range(10, 0, -1):
#     print(i)


# 7. Задача о подсчете гласных букв:
# Напишите программу, которая считает количество
# гласных букв в заданной строке.

# text = input("Введите любой текст: ")
# vowels = "АОУЫИЭЕЁЮЯ"
# count = 0
# for i in text:
#     if i in vowels:
#         count += 1
# print(count)

#8. Задача о сумме цифр числа: Напишите программу, которая считает сумму цифр заданного числа.

# n =(input("Ввидите число"))
# total = 0
# for  digit in n:
#     total +=int(digit)
#     print(f"Сумма чисел:{total}")

# 9. Задача о выводе таблицы умножения: Напишите программу, которая выводит таблицу умножения от 1 до 10.

# for i in range(1 , 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#         print()

# # 10. На вход программа получает список из целых чисел.
# # Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.
#
# numbers = [3, -6, 10, 0, -3, 5, -7]
# result = []
# for i in numbers:
#     if abs(i) > 5:
#         result.append(i)
# print(result)

# сокращённый вариант:
# numbers = [3, -6, 10, 0, -3, 5, -7]
# result = [x for x in numbers if abs(x) > 5]
# print(result)

# 11. Евгению предоставили строку, состоящую из русских букв разных регистров,
# и попросили очистить ее от заглавных литер.
# Как ему показалось, он написал верный код, но результат совсем не порадовал.
# Ниже представлен пример работы «чистильщика строк», которому срочно требуется ваша помощь.

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
#
# for letter in letters:
#     if letter.upper() = letters:
#         letters.replace(letter, '')
#
# print(letters)
#
# решение задачи:
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# result = ''
# for letter in letters:
#     if letter.islower():
#         result += letter
# print(result)

# 12. Для идентификации своего круга проверенных лиц будущий тайный агент
# Максим решил пускать на свою страничку в Интернете только тех, чьи никнеймы
# есть в его секретном списке.
# Он уверен в своих людях, как и в том, что имена товарищей невозможно подобрать случайно.
#
# К слову, вот этот список: Мавпродош, Лорнектиф, Древерол, Фиригарпиг, Клодобродыч.
# По мере увеличения круга знакомых Максим, естественно, дополнит данный список.
#
# Ваша задача такова: повторите код, который будет спрашивать у пользователя его ник и
# либо пускать на сайт (выведется сообщение «Ты – свой. Приветствую, любезный {НИК_ПОСЕТИТЕЛЯ}!»),
# либо нет (в этом случае будет такой текст: «Тут ничего нет. Еще есть вопросы?».

# secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
# while True:
#     nickname = input("Для входа введите ваш никнейм: ")
#     if nickname in secret_list:
#         print(f"Ты – свой. Приветствую, любезный {nickname}!")
#         break
#     else:
#          print("Тут ничего нет. Еще есть вопросы?")