def add_everything_up(str1, str2):
    try:
        return str1 + str2
    except TypeError:
        return str(str1) + str(str2)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


