spisok_1 = [[28, 70, 36], ['Строка 1', "Строка 2"]]
number_1 = 13
number_2 = number_1 + 5
stroka_1 = 'Строчка'

slovarb_1 = {
    number_1: [
        spisok_1,
        30
    ],
    stroka_1: {
        number_2: [
            90,
            40,
            'Строка в списке'
        ],
        stroka_1: 'Строчка-строчечка'
    }
}

print('Посмотрим что хранит в себе словарь slovarb_1 на первоначальном уровне:', '\n')
print('Ключ: ', number_1)
print('Значение ключа: ', slovarb_1[number_1], '\n')
print('Ключ: ', stroka_1)
print('Значение ключа: ', slovarb_1[stroka_1], '\n')

print('Увеличим уровень вложенности', '\n')
print('Ключ: ', number_1)
print('Значение ключа: ', slovarb_1[number_1])
print('Получим первый элемент значения ключа: ', slovarb_1[number_1][0], '\n')
print('Ключ: ', number_1)
print('Значение ключа: ', slovarb_1[number_1])
print('Получим второй элемент значения ключа: ', slovarb_1[number_1][1], '\n')

print('Увеличим уровень вложенности', '\n')
print('Ключ: ', stroka_1)
print('Значение ключа: ', slovarb_1[stroka_1])
print('Получим первый элемент значения ключа: ', slovarb_1[stroka_1][number_2], '\n')
print('Ключ: ', stroka_1)
print('Значение ключа: ', slovarb_1[stroka_1])
print('Получим второй элемент значения ключа: ', slovarb_1[stroka_1][stroka_1], '\n')