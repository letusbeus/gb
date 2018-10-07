# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
####
def lucky_ticket(ticket_number):
    pass

    tn_str = str(ticket_number)
    tn_int_list = list(map(int, tn_str))
    if sum(tn_int_list[:3]) == sum(tn_int_list[3:]):
        return "Билет счастливый"
    else:
        return "Билет несчастливый"

print(lucky_ticket(114006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1,fib2 = 1,1
    result = []
    for i in range(0, m):
        fib = fib1 + fib2
        result.append(fib2)
        fib1 = fib2
        fib2 = fib
    print(result[n:m])
    return
fibonacci(55, 59)
fibonacci(17, 21)
fibonacci(7, 12)
fibonacci(0, 5)


