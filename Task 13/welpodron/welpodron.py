# Сравнение не только чисел 

stroka_1 = 'Строка'
stroka_2 = stroka_1

number_1 = 60

if stroka_1 == stroka_2:
    print('Эти строки одинаковы! Магия!')

spisok_1 = [12, 30]
spisok_2 = spisok_1

if spisok_1 == spisok_2:
    print('Эти списки одинаковы!')

if spisok_1[0] > number_1:
    print('number_1 меньше чем первый элемент списка')
else:
    print('number_1 больше элемента списка')

slovarb_1 = {
    10 : '10',
    34 : spisok_1
}

if spisok_1 == slovarb_1:
    print(':c')
else:
    print('Хорошо, что это разные типы данных')

if spisok_1 == slovarb_1[34]:
    print('А вот теперь всё в порядке')

spisok_3 = ['Строка', 10]

if spisok_3[0] == 'строка':
    print('Большие буквы играют важную роль')
elif spisok_3[1] < 0:
    print('Число меньше нуля')
elif spisok_3[1] * 0 != 0:
    print('Интересный случай')
else:
    print('Все перечисленные выше каскадные elif не сработали')