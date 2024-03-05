def fact(x):
    pr = 1
    while x > 0:
        pr = pr * x
        x = x - 1
    return pr

print('Введите число, факториал которого нужно найти:')
i = int(input())
print('Факториал числа ', i, '=', fact(i))