spisok_1 = [[28, 70, 36], ['Строка 1', "Строка 2"]]
number_1 = 13
number_2 = number_1 + 5
stroka_1 = 'Строчка'

for spisok in spisok_1:
    for element in spisok:
        print(element)

number_3 = 0

while number_3 < 2:
    for element in spisok_1[number_3]:
        print(element)
    number_3+=1
