import random
# Домашнее задание Cеминар 6,2.

#                           Задание  1 из сем 1 Принимаем цифру, отвечаем явялеется ли днем недели

# print(__import__("calendar").day_name[int(input("Введите день недели: "))])


#                          Задание 3 из сем 2  Принимаем x и y  и выдает номер плоскости

# x, y = map(float, input("Введите x, y через пробел = ").split())
# print(x, y)
# if x*y > 0:
#     if x > 0:
#         n = 1
#     else:
#         n = 3
# else:
#     if x > 0:
#         n = 4
#     else:
#         n = 2
# print(n, 'четверть')


# Задача 1 из сем 2 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print(sum(map(int, list(input("Введите вещественное число: ")))))



# Задача 2 из семинара 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.

# n = int(input('Введите N: '))
# my_list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'Последовательность: {my_list}\nСумма: {round(sum(my_list), 2)}')


# задача 3 из семинара 2 перемешат список
# n = int(input("Введите N: "))
# my_list = [random.randint(0,9) for i in range(n)]
# leng = len(my_list)
# print(f'Изначальная последовательность: {my_list}')
# for i in range(leng):
#     i_random = random.randint(0, leng-1)
#     temp = my_list[i]
#     my_list[i] = my_list[i_random]
#     my_list[i_random] = temp
# print(f'Перемешалось: {my_list}') 


# 1 из семинара 3 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# my_list = list(map(int, input("Введите значения черех пробел = ").split()))
# print(sum(x for i, x in enumerate(my_list) if i % 2 != 0))


# 2 из семинара 3 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# my_list = list(map(int, input("Введите числа через пробел:\n").split()))
# l = len(my_list)//2 + 1 if len(my_list) % 2 != 0 else len(my_list)//2
# new_lst = [my_list[i]*my_list[len(my_list)-i-1] for i in range(l)]
# print(new_lst)

# 3 из семминара 3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# my_list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(new_lst)
# print(max(new_lst) - min(new_lst))










