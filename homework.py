# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

ls = ['1', '3', '3', '3', '4']
mi = min(ls)
ma = max(ls)
ls2 = [mi if i == ma else i for i in ls]
print(' '.join(ls2))


# 2. Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается 
# объявлять массивы и использовать циклы (даже для ввода и вывода). 
# Через рекурсию необходимо делать
# Input: 2 -> 3 4
# Output: 4 3

# def f(n):
#     if n == 0:
#         return ''
#     x = int(input())
#     return f(n - 1) + f' {x}'


# n = int(input('Введите количво чисел:  '))
# print(f(n))