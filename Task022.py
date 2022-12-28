# Задача 22:
# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
#  2 4 6 8 10 12 10 8 6 4 2
#  3 6 9 12 15 18)

# Output: 11 6
# 6 12
import random


def EnterNumber(n):
    while True:
        try:
            if int(n) == 0:
                n = input(
                    'Давайте 0 все же вводить те будем, введите больше ноля: ')
            if int(n) < 0:
                n = input('Введите целое положительное число: ')
            if int(n) > 0:
                break

        except:
            n = input('Совсем неправильно, повторите ввод: ')
    return int(n)


def ArrayGererator(k):
    m = []
    i = 0
    for i in range(0, k):
        m.append(random.randint(0, 50))
    return m


def ArraySort(g):
    if len(g) > 1:
        l = 0
        while l < len(g):
            for i in range(0, len(g) - 1):
                if g[i] > g[i + 1]:
                    k = g.pop(i+1)
                    g.insert(i, k)
            l += 1
    return g


numFyrstLengthArray = EnterNumber(input('Введите длинну первого массива: '))
numSecondLengthArray = EnterNumber(input('Введите длинну первого массива: '))

fyrstArray = ArrayGererator(numFyrstLengthArray)
print('Первый массив: ', fyrstArray)

secondArray = ArrayGererator(numSecondLengthArray)
print('Второй массив: ', secondArray)

fyrstSet = set(fyrstArray)
secondSet = set(secondArray)
crossSet = secondSet.intersection(fyrstSet)

arrayCross = list(crossSet)

if arrayCross == []:
    print('Не получилось, ту так ты числа побольше вводи))))')
else:
    print('числа присутствующие в обоих массивах: ', ArraySort(arrayCross))
