import math, random
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list = [1, 2, 4, 0]
list1 = [pow(item, 2) for item in list]
print("Original list: ", list)
print("Changed list: ", list1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list1 = ["mango", "melon", "orange", "watermelon", "apple", "banana", "grapefruit"]
list2 = ["apple", "mango", "watermelon", "apricot"]
list3 = [fruit for fruit in list1 if fruit in list2]
print(list3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print("Enter a: ")
a = int(input())
print("Enter b: ")
b = int(input())
print("Enter c: ")
c = int(input())
rand_list = [random.randint(a, b) for _ in range(c)]
checked_list = [num for num in rand_list if (num > 0) and (num % 3 == 0) and (num / 4 != 0)]
print(rand_list)
print(checked_list)
