year = int(input('Введите год: '))


def is_year_leap(n):
    if n % 4 == 0:
        return True
    if n % 4 > 0:
        return False


is_leap = is_year_leap(year)

print(f"Год: {year} {is_leap}")
