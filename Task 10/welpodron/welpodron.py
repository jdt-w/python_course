number_1 = 30
stroka_1 = 'Я строка'
spisok_1 = ['Я строка в списке']

slovarb_1 = {
    number_1 : 290,
    'Я строка-ключ в словаре' : stroka_1,
    number_1 + 50 : number_1,
    stroka_1[0] : spisok_1,
    stroka_1 : spisok_1[0],
    95 : 70
}

number_2 = slovarb_1[30]

print(number_2)

number_3 = slovarb_1[number_1] #number_1 - это не ключ number_1 словаря, а значение переменной number_1, которое равно 30

print(number_3)

print(slovarb_1['Я строка-ключ в словаре']) # результат: Я строка
print(slovarb_1[95]) # 70

number_1 += 70

#  print(slovarb_1[number_1]) - ошибка ключ не найден

print(slovarb_1[80])

slovarb_1[95] = 95 

print(slovarb_1[95])