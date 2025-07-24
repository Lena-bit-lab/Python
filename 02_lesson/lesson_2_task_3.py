def square(x):
    s = x**2
    return s


from math import ceil


x = float(input('Длина стороны квадрата: '))
result = square(x)
rounded_result = ceil(result)


print(f'Округленное в большую стороноу произведение - {ceil(result)}')
