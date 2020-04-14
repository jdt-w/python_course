spisok_1 = [50, 30, 20, 10, 5]

for number_1 in spisok_1:
    if number_1 > 20:
        print('number_1 больше 20, пропустим итерацию')
        continue
        print('К сожалению до меня вряд ли дойдут :c')
    else:
        print('Мы нашли number_1, который меньше ИЛИ равен 20, завершаем цикл')
        break

slovarb_1 = {
    30: 10,
    42: {},
    'Строчка-ключ': spisok_1,
    'Другая строчка-ключ': [48]
}

for klu4 in slovarb_1:
    if klu4 == 'Простая строчка' and slovarb_1[klu4] == spisok_1:
        print('Мы нашли тот самый ключ, который искали!')
        break
else:
    print('К сожалению в результате поиска мы не нашли тот самый ключ :c')