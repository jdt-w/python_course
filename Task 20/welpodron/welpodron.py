print('Уже знакомая функция print()')

def function_1():
    print('Меня вызвала функция print(), внутри функции function_1()')

function_1()

def function_2():
    list_1 = [90, 40, 'Строка']

function_2()

print(function_2())

list_1 = function_2()

print(list_1)

new_type = None

if list_1 == new_type:
    print('Значения list_1 и new_type совпадают')

def function_3():
    dict_1 = {
        30: [13],
        'Строка': ['Строка']
    }
    return dict_1

function_3()

print(function_3())

dict_1 = function_3()

print(dict_1)