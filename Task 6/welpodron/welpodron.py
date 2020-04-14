spisok_1 = ["Это строка в списке в одних кавычках, она имеет НУЛЕВОЙ индекс", 'Это строка в списке в других кавычках, она имеет индекс равный ЕДИНИЦЕ']

print(spisok_1[0], spisok_1[1])
#
stroka_1 = spisok_1[0]
stroka_2 = spisok_1[1]

print(stroka_1, stroka_2)
#одинаковый результат
number_1 = 0
stroka_3 = spisok_1[number_1]
stroka_4 = spisok_1[number_1 + 1]

print(stroka_3, stroka_4)
#